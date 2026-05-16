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
        self.api_key = os.getenv("WATSONX_API_KEY")
        self.project_id = os.getenv("WATSONX_PROJECT_ID")
        self.url = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
        self.iam_token = None
        self.token_expiry = 0
        
        if not self.api_key:
            logger.warning("WATSONX_API_KEY not found in environment variables")
        if not self.project_id:
            logger.warning("WATSONX_PROJECT_ID not found in environment variables")
    
    async def get_iam_token(self) -> Optional[str]:
        """
        Get IBM Cloud IAM access token using API key.
        Tokens are cached and reused until they expire.
        """
        import time
        
        # Return cached token if still valid (with 5 min buffer)
        if self.iam_token and time.time() < (self.token_expiry - 300):
            return self.iam_token
        
        if not self.api_key:
            logger.error("Cannot get IAM token: WATSONX_API_KEY not set")
            return None
        
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
            
            async with httpx.AsyncClient() as client:
                response = await client.post(url, headers=headers, data=data, timeout=30.0)
                
                if response.status_code != 200:
                    logger.error(f"Failed to get IAM token: {response.status_code}")
                    return None
                
                token_data = response.json()
                self.iam_token = token_data.get("access_token")
                expires_in = token_data.get("expires_in", 3600)
                self.token_expiry = time.time() + expires_in
                
                return self.iam_token
        
        except Exception as e:
            logger.error(f"Error getting IAM token: {str(e)}")
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
            logger.error("Cannot generate text: WATSONX_PROJECT_ID not set")
            return None
        
        # Get IAM token
        token = await self.get_iam_token()
        if not token:
            logger.error("Failed to get IAM token for watsonx.ai")
            return None
        
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
            
            # Make request
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    endpoint,
                    headers=headers,
                    json=body,
                    timeout=60.0
                )
                
                if response.status_code != 200:
                    logger.error(f"watsonx.ai API error: {response.status_code} - {response.text}")
                    return None
                
                result = response.json()
                
                # Extract generated text
                generated_text = result.get("results", [{}])[0].get("generated_text", "")
                
                return {
                    "generated_text": generated_text,
                    "model_id": model_id,
                    "token_count": result.get("results", [{}])[0].get("generated_token_count", 0),
                    "stop_reason": result.get("results", [{}])[0].get("stop_reason", "unknown")
                }
        
        except httpx.TimeoutException:
            logger.error("watsonx.ai request timed out")
            return None
        
        except Exception as e:
            logger.error(f"Error calling watsonx.ai: {str(e)}")
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
        
        # Construct prompt
        prompt = f"""You are a career advisor helping someone break into tech. Generate a practical, beginner-friendly career roadmap.

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
9. weeklyPlan: Array of weekly activities for the timeframe
10. nextSteps: Array of immediate action items (5-7 items)

IMPORTANT:
- Only use the provided resource URLs, never invent fake links
- Be specific and practical for beginners
- Focus on free resources when possible
- Make it actionable with clear next steps
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
