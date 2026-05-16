"""
Diagnostic script to identify exact watsonx.ai failure point
"""
import asyncio
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv
from services.watsonx_service import watsonx_service
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def diagnose_watsonx():
    """Run comprehensive watsonx diagnostics"""
    
    print("=" * 80)
    print("WATSONX.AI DIAGNOSTIC TEST")
    print("=" * 80)
    
    # Step 1: Check environment variables
    print("\n[1] CHECKING ENVIRONMENT VARIABLES")
    print("-" * 80)
    
    env_path = Path(__file__).parent / '.env'
    load_dotenv(dotenv_path=env_path)
    
    api_key = os.getenv("WATSONX_API_KEY")
    project_id = os.getenv("WATSONX_PROJECT_ID")
    url = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
    model_id = os.getenv("WATSONX_MODEL_ID", "ibm/granite-3-8b-instruct")
    
    print(f"   .env file exists: {env_path.exists()}")
    print(f"   .env file path: {env_path}")
    
    if api_key:
        masked_key = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
        print(f"   [OK] WATSONX_API_KEY: {masked_key} (length: {len(api_key)})")
    else:
        print(f"   [FAIL] WATSONX_API_KEY: NOT FOUND")
        return False
    
    if project_id:
        print(f"   [OK] WATSONX_PROJECT_ID: {project_id}")
    else:
        print(f"   [FAIL] WATSONX_PROJECT_ID: NOT FOUND")
        return False
    
    print(f"   [OK] WATSONX_URL: {url}")
    print(f"   [OK] WATSONX_MODEL_ID: {model_id}")
    
    # Step 2: Test IAM token
    print("\n[2] TESTING IAM TOKEN AUTHENTICATION")
    print("-" * 80)
    
    try:
        token = await watsonx_service.get_iam_token()
        if token:
            masked_token = token[:20] + "..." + token[-10:] if len(token) > 30 else "***"
            print(f"   [OK] IAM token obtained: {masked_token}")
            print(f"   Token length: {len(token)}")
        else:
            print(f"   [FAIL] Failed to get IAM token")
            print(f"   Check logs above for HTTP status code and error details")
            return False
    except Exception as e:
        print(f"   [FAIL] Exception getting IAM token: {e}")
        return False
    
    # Step 3: Test simple text generation
    print("\n[3] TESTING SIMPLE TEXT GENERATION")
    print("-" * 80)
    
    simple_prompt = "Generate a JSON object with one field 'test' set to 'success'. Return only valid JSON."
    
    try:
        result = await watsonx_service.generate_text(
            prompt=simple_prompt,
            model_id=model_id,
            max_tokens=100,
            temperature=0.1
        )
        
        if result:
            print(f"   [OK] Text generation successful")
            print(f"   Model: {result.get('model_id')}")
            print(f"   Tokens: {result.get('token_count')}")
            print(f"   Stop reason: {result.get('stop_reason')}")
            gen_text = result.get('generated_text', '')
            print(f"   Generated text: {gen_text[:200] if gen_text else 'NONE'}")
        else:
            print(f"   [FAIL] Text generation returned None")
            print(f"   Check logs above for:")
            print(f"      - HTTP status code (should be 200)")
            print(f"      - Error message from watsonx API")
            print(f"      - Model ID validity")
            return False
    except Exception as e:
        print(f"   [FAIL] Exception during text generation: {e}")
        return False
    
    # Step 4: Test roadmap generation
    print("\n[4] TESTING ROADMAP GENERATION")
    print("-" * 80)
    
    try:
        roadmap = await watsonx_service.generate_career_roadmap(
            career_goal="Data Analyst",
            current_skills=["Excel", "SQL"],
            timeframe="1 month",
            local_resources={"resources": []},
            github_projects=[]
        )
        
        if roadmap:
            print(f"   [OK] Roadmap generation successful")
            print(f"   Has summary: {'summary' in roadmap}")
            print(f"   Has phases: {'phases' in roadmap}")
            print(f"   Has weeklyPlan: {'weeklyPlan' in roadmap}")
            print(f"   Phases count: {len(roadmap.get('phases', []))}")
            print(f"   Weekly plans count: {len(roadmap.get('weeklyPlan', []))}")
        else:
            print(f"   [FAIL] Roadmap generation returned None")
            print(f"   Check logs above for:")
            print(f"      - JSON parsing errors")
            print(f"      - Truncation warnings")
            print(f"      - Missing closing braces")
            return False
    except Exception as e:
        print(f"   [FAIL] Exception during roadmap generation: {e}")
        return False
    
    print("\n" + "=" * 80)
    print("[SUCCESS] ALL DIAGNOSTICS PASSED - WATSONX.AI IS WORKING")
    print("=" * 80)
    return True

if __name__ == "__main__":
    success = asyncio.run(diagnose_watsonx())
    sys.exit(0 if success else 1)

# Made with Bob
