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
            
            # Log full request details
            logger.info("=" * 80)
            logger.info("📤 WATSONX API REQUEST")
            logger.info("=" * 80)
            logger.info(f"Endpoint: {endpoint}")
            logger.info(f"Model: {model_id}")
            logger.info(f"Project ID: {self.project_id}")
            logger.info(f"Prompt length: {len(prompt)} characters")
            logger.info("")
            logger.info("Request Parameters:")
            logger.info(f"  decoding_method: {body['parameters']['decoding_method']}")
            logger.info(f"  max_new_tokens: {body['parameters']['max_new_tokens']}")
            logger.info(f"  temperature: {body['parameters']['temperature']}")
            logger.info(f"  top_p: {body['parameters']['top_p']}")
            logger.info(f"  top_k: {body['parameters']['top_k']}")
            logger.info(f"  repetition_penalty: {body['parameters']['repetition_penalty']}")
            logger.info("=" * 80)
            
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
                
                # Log full response structure
                logger.info("=" * 80)
                logger.info("📥 WATSONX API RESPONSE")
                logger.info("=" * 80)
                
                # Extract generated text
                results_array = result.get("results", [])
                if not results_array:
                    logger.error("❌ No results array in response")
                    logger.error(f"Response keys: {list(result.keys())}")
                    return None
                
                first_result = results_array[0]
                generated_text = first_result.get("generated_text", "")
                token_count = first_result.get("generated_token_count", 0)
                stop_reason = first_result.get("stop_reason", "unknown")
                
                # Log response metadata
                logger.info(f"Generated token count: {token_count}")
                logger.info(f"Stop reason: {stop_reason}")
                logger.info(f"Generated text length: {len(generated_text)} characters")
                logger.info(f"Generated text first 200 chars: {generated_text[:200]}")
                logger.info(f"Generated text last 200 chars: {generated_text[-200:]}")
                logger.info(f"Text ends with: '{generated_text[-50:]}'")
                logger.info(f"Ends with closing brace: {generated_text.rstrip().endswith('}')}")
                logger.info("=" * 80)
                
                logger.info(f"✅ WatsonX generation successful!")
                
                return {
                    "generated_text": generated_text,
                    "model_id": model_id,
                    "token_count": token_count,
                    "stop_reason": stop_reason
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
        
        # Construct prompt with strict JSON requirements and MINIMAL structure
        prompt = f"""Generate a career roadmap JSON for: {career_goal}

Current skills: {skills_text}
Timeframe: {timeframe}

Available verified resources:
{resources_context if resources_context else "Use well-known learning platforms"}

Return ONLY valid JSON with NO markdown, NO code fences, NO explanations.

Required structure:
{{
  "summary": "Brief 1-sentence overview",
  "phases": [
    {{"phase": 1, "title": "Foundation", "duration": "4 weeks", "focus": "Learn basics", "skills": ["skill1", "skill2"]}},
    {{"phase": 2, "title": "Practice", "duration": "4 weeks", "focus": "Build projects", "skills": ["skill3", "skill4"]}},
    {{"phase": 3, "title": "Portfolio", "duration": "4 weeks", "focus": "Create portfolio", "skills": ["skill5", "skill6"]}}
  ],
  "skills": ["skill1", "skill2", "skill3", "skill4", "skill5"],
  "tools": ["tool1", "tool2", "tool3", "tool4"],
  "resources": [
    {{"title": "Excel Fundamentals Course", "type": "course", "url": "https://www.coursera.org/learn/excel-basics", "provider": "Coursera"}},
    {{"title": "SQL Tutorial for Beginners", "type": "tutorial", "url": "https://www.w3schools.com/sql/", "provider": "W3Schools"}}
  ],
  "githubProjects": [
    {{"name": "Project 1", "description": "Beginner project", "difficulty": "beginner"}},
    {{"name": "Project 2", "description": "Intermediate project", "difficulty": "intermediate"}}
  ],
  "portfolioProjects": [
    {{"title": "Portfolio Project 1", "description": "Build something", "skills": ["skill1", "skill2"], "estimatedHours": 8, "difficulty": "beginner"}},
    {{"title": "Portfolio Project 2", "description": "Build advanced", "skills": ["skill3", "skill4"], "estimatedHours": 16, "difficulty": "intermediate"}}
  ],
  "resumeBullets": [
    "Completed {timeframe} training in {career_goal}",
    "Built 2 portfolio projects",
    "Learned 5 key skills"
  ],
  "weeklyPlan": [
    {{"week": 1, "focus": "Environment setup", "topics": ["Install tools", "Learn basics"], "dailyTasks": ["Setup workspace", "First tutorial"]}},
    {{"week": 2, "focus": "Core concepts", "topics": ["Study fundamentals", "Practice"], "dailyTasks": ["Read docs", "Do exercises"]}},
    {{"week": 3, "focus": "First project", "topics": ["Plan project", "Start coding"], "dailyTasks": ["Design", "Implement"]}},
    {{"week": 4, "focus": "Complete project", "topics": ["Finish coding", "Test"], "dailyTasks": ["Debug", "Deploy"]}}
  ],
  "nextSteps": [
    "Start with first resource",
    "Set up development environment",
    "Join online community",
    "Begin first project"
  ]
}}

IMPORTANT for resources:
- Use DESCRIPTIVE titles (not "Resource 1")
- Only use URLs from well-known platforms: Coursera, edX, Udemy, W3Schools, MDN, freeCodeCamp, Khan Academy, YouTube
- Include provider name if possible
- Use homepage URLs if specific course URLs are uncertain

CRITICAL: Return ONLY the JSON object. Start with {{ and end with }}. NO markdown. NO explanations. Complete the ENTIRE JSON."""
        
        # Generate with watsonx.ai - increased token limit for complete response
        result = await self.generate_text(
            prompt=prompt,
            max_tokens=4000,
            temperature=0.7
        )
        
        if not result:
            logger.error("❌ WatsonX returned None result")
            return None
        
        # Initialize cleaned_text for error handling
        cleaned_text = ""
        
        try:
            # Get raw generated text
            generated_text = result["generated_text"]
            
            # Log raw response for debugging
            logger.info("=" * 80)
            logger.info("📄 RAW GENERATED TEXT FROM WATSONX")
            logger.info("=" * 80)
            logger.info(f"Total length: {len(generated_text)} characters")
            logger.info(f"Token count: {result.get('token_count', 'unknown')}")
            logger.info(f"Stop reason: {result.get('stop_reason', 'unknown')}")
            logger.info("")
            logger.info(f"First 500 characters:")
            logger.info(generated_text[:500])
            logger.info("")
            logger.info(f"Last 500 characters:")
            logger.info(generated_text[-500:])
            logger.info("")
            logger.info(f"Ends with closing brace: {generated_text.rstrip().endswith('}')}")
            logger.info("=" * 80)
            
            # Clean and extract JSON
            cleaned_text = generated_text.strip()
            logger.info("🧹 Starting JSON extraction...")
            logger.info(f"Initial cleaned length: {len(cleaned_text)} characters")
            
            # Remove markdown code fences if present
            if "```json" in cleaned_text:
                logger.info("🔧 Found ```json markdown wrapper, removing...")
                parts = cleaned_text.split("```json")
                if len(parts) > 1:
                    cleaned_text = parts[1].split("```")[0].strip()
                    logger.info(f"   After removing markdown: {len(cleaned_text)} characters")
            elif "```" in cleaned_text:
                logger.info("🔧 Found ``` markdown wrapper, removing...")
                parts = cleaned_text.split("```")
                if len(parts) >= 3:
                    cleaned_text = parts[1].strip()
                    logger.info(f"   After removing markdown: {len(cleaned_text)} characters")
            
            # Remove any text before first { and after last }
            first_brace = cleaned_text.find("{")
            last_brace = cleaned_text.rfind("}")
            
            logger.info(f"🔍 Looking for JSON braces...")
            logger.info(f"   First {{ found at position: {first_brace}")
            logger.info(f"   Last }} found at position: {last_brace}")
            
            if first_brace == -1 or last_brace == -1:
                logger.error("=" * 80)
                logger.error("❌ NO JSON OBJECT FOUND IN RESPONSE")
                logger.error("=" * 80)
                logger.error(f"First {{ position: {first_brace}")
                logger.error(f"Last }} position: {last_brace}")
                logger.error(f"Full cleaned text (first 1000 chars):")
                logger.error(cleaned_text[:1000])
                logger.error("=" * 80)
                return None
            
            if first_brace > 0:
                removed_prefix = cleaned_text[:first_brace]
                logger.info(f"🔧 Removing {first_brace} characters before first {{")
                logger.info(f"   Removed text: '{removed_prefix[:100]}'...")
            
            if last_brace < len(cleaned_text) - 1:
                removed_suffix = cleaned_text[last_brace + 1:]
                logger.info(f"🔧 Removing {len(cleaned_text) - last_brace - 1} characters after last }}")
                logger.info(f"   Removed text: '...{removed_suffix[-100:]}'")
            
            cleaned_text = cleaned_text[first_brace:last_brace + 1]
            logger.info(f"✅ Extracted JSON object: {len(cleaned_text)} characters")
            
            # Check if response appears truncated
            response_ends_properly = cleaned_text.rstrip().endswith("}")
            if not response_ends_properly:
                logger.error("=" * 80)
                logger.error("❌ RESPONSE APPEARS TRUNCATED")
                logger.error("=" * 80)
                logger.error(f"Response length: {len(generated_text)} characters")
                logger.error(f"Cleaned text length: {len(cleaned_text)} characters")
                logger.error(f"Last 200 characters: {cleaned_text[-200:]}")
                logger.error(f"Response ends with: '{cleaned_text[-50:]}'")
                logger.error("=" * 80)
                logger.error("LIKELY CAUSE: WatsonX hit max_new_tokens limit before completing JSON")
                logger.error(f"Current max_new_tokens: 4000")
                logger.error("SOLUTION: Increase max_new_tokens or simplify the prompt")
                logger.error("=" * 80)
                return None
            
            # Log cleaned text
            logger.info("=" * 80)
            logger.info("🧹 CLEANED JSON TEXT")
            logger.info("=" * 80)
            logger.info(f"Length: {len(cleaned_text)} characters")
            logger.info(f"First 300 chars: {cleaned_text[:300]}")
            logger.info("=" * 80)
            
            # Attempt to parse JSON
            logger.info("🔍 Attempting to parse JSON...")
            roadmap = json.loads(cleaned_text)
            logger.info("✅ JSON parsed successfully!")
            
            # Validate required fields
            required_fields = ["summary", "phases", "skills", "weeklyPlan"]
            missing_fields = [field for field in required_fields if field not in roadmap]
            
            if missing_fields:
                logger.warning(f"⚠️  Missing required fields: {missing_fields}")
            else:
                logger.info("✅ All required fields present")
            
            # Log structure
            logger.info(f"📊 Roadmap structure:")
            logger.info(f"   - Phases: {len(roadmap.get('phases', []))}")
            logger.info(f"   - Skills: {len(roadmap.get('skills', []))}")
            logger.info(f"   - Tools: {len(roadmap.get('tools', []))}")
            logger.info(f"   - Resources: {len(roadmap.get('resources', []))}")
            logger.info(f"   - Portfolio Projects: {len(roadmap.get('portfolioProjects', []))}")
            logger.info(f"   - Weekly Plans: {len(roadmap.get('weeklyPlan', []))}")
            
            # Add metadata
            roadmap["metadata"] = {
                "usedWatsonx": True,
                "usedGitHub": len(github_projects) > 0,
                "matchedLocalResources": len(local_resources.get("resources", [])),
                "model": result.get("model_id", "unknown"),
                "tokens": result.get("token_count", 0)
            }
            
            logger.info("✅ WatsonX roadmap generation complete!")
            return roadmap
        
        except json.JSONDecodeError as e:
            logger.error("=" * 80)
            logger.error("❌ JSON PARSING FAILED")
            logger.error("=" * 80)
            logger.error(f"Error: {str(e)}")
            logger.error(f"Error at line {e.lineno}, column {e.colno}")
            logger.error(f"Error message: {e.msg}")
            logger.error("=" * 80)
            logger.error("RAW RESPONSE:")
            logger.error(result.get('generated_text', 'NO TEXT')[:1000])
            logger.error("=" * 80)
            logger.error("CLEANED TEXT:")
            logger.error(cleaned_text[:1000] if 'cleaned_text' in locals() else 'NOT AVAILABLE')
            logger.error("=" * 80)
            return None
        
        except Exception as e:
            logger.error(f"❌ Error processing watsonx.ai response: {str(e)}")
            logger.exception("Full exception:")
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
    Generate a career roadmap using watsonx.ai with intelligent strategy selection.
    
    Strategy selection:
    - 1 month (4 weeks): Single call with 3000 tokens
    - 2 months (8 weeks): Single call with 4000 tokens
    - 3+ months (12+ weeks): Multi-call strategy
    
    Args:
        career_goal: Target career role
        current_skills: List of current skills
        timeframe: Available timeframe (e.g., "3 months")
        local_resources: Curated resources from local data
        github_projects: Relevant GitHub projects
    
    Returns:
        Structured roadmap dictionary or None on error
    """
    import re
    from services.watsonx_multi_call import multi_call_generator
    
    logger.info("=" * 80)
    logger.info("🎯 INTELLIGENT ROADMAP GENERATION STRATEGY SELECTION")
    logger.info("=" * 80)
    logger.info(f"Career Goal: {career_goal}")
    logger.info(f"Timeframe: {timeframe}")
    
    # Calculate weeks from timeframe
    timeframe_lower = timeframe.lower()
    weeks_needed = 12  # default
    
    if 'month' in timeframe_lower:
        match = re.search(r'(\d+)', timeframe_lower)
        if match:
            months = int(match.group(1))
            weeks_needed = months * 4
    elif 'week' in timeframe_lower:
        match = re.search(r'(\d+)', timeframe_lower)
        if match:
            weeks_needed = int(match.group(1))
    
    logger.info(f"📅 Weeks needed: {weeks_needed}")
    
    # Strategy selection
    if weeks_needed <= 4:
        # 1 month: Single call with 3000 tokens
        logger.info("📋 Strategy: SINGLE CALL (3000 tokens)")
        logger.info("   Reason: Short timeframe (≤4 weeks)")
        logger.info("=" * 80)
        
        result = await watsonx_service.generate_career_roadmap(
            career_goal=career_goal,
            current_skills=current_skills,
            timeframe=timeframe,
            local_resources=local_resources,
            github_projects=github_projects
        )
        
        if result:
            result['metadata']['generationStrategy'] = 'single_call'
            result['metadata']['maxTokensUsed'] = 3000
        
        return result
    
    elif weeks_needed <= 8:
        # 2 months: Single call with 4000 tokens
        logger.info("📋 Strategy: SINGLE CALL (4000 tokens)")
        logger.info("   Reason: Medium timeframe (5-8 weeks)")
        logger.info("=" * 80)
        
        result = await watsonx_service.generate_career_roadmap(
            career_goal=career_goal,
            current_skills=current_skills,
            timeframe=timeframe,
            local_resources=local_resources,
            github_projects=github_projects
        )
        
        if result:
            result['metadata']['generationStrategy'] = 'single_call'
            result['metadata']['maxTokensUsed'] = 4000
        
        return result
    
    else:
        # 3+ months: Multi-call strategy
        logger.info("📋 Strategy: MULTI-CALL")
        logger.info(f"   Reason: Long timeframe ({weeks_needed} weeks)")
        logger.info("   Approach: Summary + Weekly chunks")
        logger.info("=" * 80)
        
        result = await multi_call_generator.generate_full_roadmap(
            career_goal=career_goal,
            current_skills=current_skills,
            timeframe=timeframe,
            local_resources=local_resources,
            github_projects=github_projects
        )
        
        return result

# Made with Bob - AI Career Roadmap Generator
