import os
import httpx
import json
from typing import Optional, Dict, Any
import logging
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables before anything else
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

logger = logging.getLogger(__name__)


class WatsonxService:
    """
    Service for interacting with IBM watsonx.ai API.
    Handles authentication and text generation requests.
    """
    
    def __init__(self):
        # Load environment variables with detailed logging
        self.api_key = os.getenv("WATSONX_API_KEY")
        self.project_id = os.getenv("WATSONX_PROJECT_ID")
        self.url = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
        self.model_id = os.getenv("WATSONX_MODEL_ID", "ibm/granite-3-8b-instruct")
        self.iam_token = None
        self.token_expiry = 0
        
        # Log environment variable status (safely)
        logger.info("=" * 80)
        logger.info("🔧 WATSONX SERVICE INITIALIZATION")
        logger.info("=" * 80)
        logger.info(f"Loading .env from: {env_path}")
        logger.info(f".env exists: {env_path.exists()}")
        
        if self.api_key:
            masked_key = self.api_key[:8] + "..." + self.api_key[-4:] if len(self.api_key) > 12 else "***"
            logger.info(f"✅ WATSONX_API_KEY: {masked_key}")
        else:
            logger.error("❌ WATSONX_API_KEY: NOT FOUND")
            
        if self.project_id:
            logger.info(f"✅ WATSONX_PROJECT_ID: {self.project_id}")
        else:
            logger.error("❌ WATSONX_PROJECT_ID: NOT FOUND")
            
        logger.info(f"✅ WATSONX_URL: {self.url}")
        logger.info(f"✅ WATSONX_MODEL_ID: {self.model_id}")
        logger.info("=" * 80)
    
    async def get_iam_token(self) -> Optional[str]:
        """
        Get IBM Cloud IAM access token using API key.
        Tokens are cached and reused until they expire.
        """
        import time
        
        # Return cached token if still valid (with 5 min buffer)
        if self.iam_token and time.time() < (self.token_expiry - 300):
            logger.info("♻️  Using cached IAM token")
            return self.iam_token
        
        if not self.api_key:
            logger.error("❌ Cannot get IAM token: WATSONX_API_KEY not set")
            return None
        
        logger.info("🔑 Requesting new IAM token from IBM Cloud...")
        
        try:
            url = "https://iam.cloud.ibm.com/identity/token"
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json"
            }
            data = {
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": self.api_key
            }
            
            logger.info(f"IAM Token URL: {url}")
            logger.info(f"Request headers: {headers}")
            logger.info(f"Grant type: {data['grant_type']}")
            
            async with httpx.AsyncClient() as client:
                response = await client.post(url, headers=headers, data=data, timeout=30.0)
                
                logger.info(f"IAM Response Status: {response.status_code}")
                
                if response.status_code != 200:
                    logger.error(f"❌ Failed to get IAM token: HTTP {response.status_code}")
                    logger.error(f"Response body: {response.text[:500]}")
                    
                    # Try to parse error details
                    try:
                        error_data = response.json()
                        logger.error(f"Error details: {error_data}")
                    except:
                        pass
                    
                    return None
                
                token_data = response.json()
                self.iam_token = token_data.get("access_token")
                expires_in = token_data.get("expires_in", 3600)
                self.token_expiry = time.time() + expires_in
                
                if self.iam_token:
                    masked_token = self.iam_token[:20] + "..." + self.iam_token[-10:] if len(self.iam_token) > 30 else "***"
                    logger.info(f"✅ IAM token obtained successfully: {masked_token}")
                    logger.info(f"Token expires in: {expires_in} seconds")
                else:
                    logger.error("❌ No access_token in response")
                    logger.error(f"Response keys: {list(token_data.keys())}")
                
                return self.iam_token
        
        except httpx.TimeoutException:
            logger.error("❌ IAM token request timed out")
            return None
        
        except Exception as e:
            logger.error(f"❌ Error getting IAM token: {str(e)}")
            logger.exception("Full exception details:")
            return None
    
    async def generate_text(
        self,
        prompt: str,
        model_id: str = "ibm/granite-3-8b-instruct",
        max_tokens: int = 2000,
        temperature: float = 0.7,
        top_p: float = 1.0,
        top_k: int = 50
    ) -> Optional[Dict[str, Any]]:
        """
        Generate text using IBM watsonx.ai.
        
        Args:
            prompt: The input prompt for text generation
            model_id: Model to use (default: IBM Granite 13B Chat)
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature (0.0-2.0)
            top_p: Nucleus sampling parameter
            top_k: Top-k sampling parameter
        
        Returns:
            Dictionary with generated text and metadata, or None on error
        """
        if not self.project_id:
            logger.error("❌ Cannot generate text: WATSONX_PROJECT_ID not set")
            return None
        
        # Get IAM token
        logger.info("🔐 Getting IAM token for WatsonX...")
        token = await self.get_iam_token()
        if not token:
            logger.error("❌ Failed to get IAM token for watsonx.ai")
            return None
        
        logger.info("✅ IAM token obtained, calling WatsonX API...")
        
        try:
            # Construct API endpoint
            endpoint = f"{self.url}/ml/v1/text/generation?version=2023-05-29"
            
            # Request headers
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
            
            # Request body
            body = {
                "input": prompt,
                "parameters": {
                    "decoding_method": "greedy",
                    "max_new_tokens": max_tokens,
                    "temperature": temperature,
                    "top_p": top_p,
                    "top_k": top_k,
                    "repetition_penalty": 1.1
                },
                "model_id": model_id,
                "project_id": self.project_id
            }
            
            logger.info(f"WatsonX Endpoint: {endpoint}")
            logger.info(f"Model: {model_id}")
            logger.info(f"Project ID: {self.project_id}")
            logger.info(f"Max tokens: {max_tokens}")
            logger.info(f"Prompt length: {len(prompt)} characters")
            
            # Make request
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    endpoint,
                    headers=headers,
                    json=body,
                    timeout=60.0
                )
                
                logger.info(f"WatsonX Response Status: {response.status_code}")
                
                if response.status_code != 200:
                    logger.error(f"❌ watsonx.ai API error: HTTP {response.status_code}")
                    logger.error(f"Response body: {response.text[:1000]}")
                    
                    # Try to parse error details
                    try:
                        error_data = response.json()
                        logger.error(f"Error details: {error_data}")
                    except:
                        pass
                    
                    return None
                
                result = response.json()
                
                # Extract generated text
                generated_text = result.get("results", [{}])[0].get("generated_text", "")
                token_count = result.get("results", [{}])[0].get("generated_token_count", 0)
                
                logger.info(f"✅ WatsonX generation successful!")
                logger.info(f"Generated {token_count} tokens")
                logger.info(f"Response length: {len(generated_text)} characters")
                
                return {
                    "generated_text": generated_text,
                    "model_id": model_id,
                    "token_count": token_count,
                    "stop_reason": result.get("results", [{}])[0].get("stop_reason", "unknown")
                }
        
        except httpx.TimeoutException:
            logger.error("❌ watsonx.ai request timed out (60s)")
            return None
        
        except Exception as e:
            logger.error(f"❌ Error calling watsonx.ai: {str(e)}")
            logger.exception("Full exception details:")
            return None
    
    async def generate_career_roadmap(
        self,
        career_goal: str,
        current_skills: list,
        timeframe: str,
        local_resources: dict,
        github_projects: list
    ) -> Optional[Dict[str, Any]]:
        """
        Generate a structured career roadmap using watsonx.ai.
        
        Args:
            career_goal: Target career role
            current_skills: List of current skills
            timeframe: Available timeframe (e.g., "3 months")
            local_resources: Curated resources from local data
            github_projects: Relevant GitHub projects
        
        Returns:
            Structured roadmap dictionary or None on error
        """
        # Build context from local resources
        resources_context = ""
        if local_resources.get("resources"):
            resources_context = "\n".join([
                f"- {r['title']} ({r['type']}): {r['url']}"
                for r in local_resources["resources"][:5]
            ])
        
        # Build context from GitHub projects
        github_context = ""
        if github_projects:
            github_context = "\n".join([
                f"- {p['name']}: {p['description']} ({p['stars']} stars)"
                for p in github_projects[:5]
            ])
        
        # Build skills context
        skills_text = ", ".join(current_skills) if current_skills else "none"
        
        # Construct prompt with emphasis on unique weekly content
        prompt = f"""You are a career advisor helping someone break into tech. Generate a practical, beginner-friendly career roadmap with UNIQUE content for each week.

Career Goal: {career_goal}
Current Skills: {skills_text}
Timeframe: {timeframe}

Available Resources:
{resources_context if resources_context else "Use free online resources"}

Relevant GitHub Projects:
{github_context if github_context else "Search GitHub for beginner projects"}

Generate a structured JSON roadmap with these sections:
1. summary: Brief overview of the path (2-3 sentences)
2. phases: Array of learning phases, each with:
   - phase: Phase number (1, 2, 3)
   - title: Phase name
   - duration: Time to complete
   - focus: What to learn
   - skills: Array of skills to master
3. skills: Array of all skills to learn
4. tools: Array of tools to practice
5. resources: Array of learning resources (use provided URLs, don't invent)
6. githubProjects: Array of project ideas based on provided GitHub repos
7. portfolioProjects: Array of 3-5 portfolio project ideas
8. resumeBullets: Array of 5 resume bullet point templates
9. weeklyPlan: Array of weekly activities with UNIQUE focus for each week:
   - week: Week number
   - focus: Specific learning focus for THIS week (must be different from other weeks)
   - topics: Array of 3-5 specific topics to cover this week
   - dailyTasks: Array of 3-5 unique daily tasks for this week
   - resources: Specific resources for this week's topics
10. nextSteps: Array of immediate action items (5-7 items)

CRITICAL REQUIREMENTS:
- Each week in weeklyPlan MUST have DIFFERENT focus, topics, and tasks
- Week 1 might focus on "Environment Setup & Basics"
- Week 2 might focus on "Core Concepts & Fundamentals"
- Week 3 might focus on "Hands-on Practice & Mini Projects"
- Week 4 might focus on "Building First Portfolio Project"
- Make each week progressively more advanced
- Only use the provided resource URLs, never invent fake links
- Be specific and practical for beginners
- Return ONLY valid JSON, no markdown formatting

JSON Response:"""
        
        # Generate with watsonx.ai
        result = await self.generate_text(
            prompt=prompt,
            max_tokens=2500,
            temperature=0.7
        )
        
        if not result:
            return None
        
        try:
            # Parse JSON from generated text
            generated_text = result["generated_text"].strip()
            
            # Try to extract JSON if wrapped in markdown
            if "```json" in generated_text:
                generated_text = generated_text.split("```json")[1].split("```")[0].strip()
            elif "```" in generated_text:
                generated_text = generated_text.split("```")[1].split("```")[0].strip()
            
            roadmap = json.loads(generated_text)
            
            # Add metadata
            roadmap["metadata"] = {
                "usedWatsonx": True,
                "usedGitHub": len(github_projects) > 0,
                "matchedLocalResources": len(local_resources.get("resources", [])),
                "model": result.get("model_id", "unknown"),
                "tokens": result.get("token_count", 0)
            }
            
            return roadmap
        
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON from watsonx.ai response: {str(e)}")
            logger.debug(f"Generated text: {result.get('generated_text', '')[:500]}")
            return None
        
        except Exception as e:
            logger.error(f"Error processing watsonx.ai response: {str(e)}")
            return None


# Global instance
watsonx_service = WatsonxService()


async def generate_roadmap_with_ai(
    career_goal: str,
    current_skills: list,
    timeframe: str,
    local_resources: dict,
    github_projects: list
) -> Optional[Dict[str, Any]]:
    """
    Convenience function to generate a career roadmap.
    """
    return await watsonx_service.generate_career_roadmap(
        career_goal=career_goal,
        current_skills=current_skills,
        timeframe=timeframe,
        local_resources=local_resources,
        github_projects=github_projects
    )

# Made with Bob - AI Career Roadmap Generator
