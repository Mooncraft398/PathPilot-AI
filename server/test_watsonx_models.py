"""
Test script to list available watsonx.ai models
"""
import os
import httpx
import asyncio
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

async def get_iam_token():
    """Get IBM Cloud IAM token"""
    api_key = os.getenv("WATSONX_API_KEY")
    
    if not api_key:
        print("ERROR: WATSONX_API_KEY not found")
        return None
    
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": api_key
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, data=data, timeout=30.0)
        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            print(f"Failed to get IAM token: {response.status_code}")
            print(response.text)
            return None

async def list_models():
    """List available models"""
    token = await get_iam_token()
    if not token:
        return
    
    project_id = os.getenv("WATSONX_PROJECT_ID")
    url = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
    
    endpoint = f"{url}/ml/v1/foundation_model_specs?version=2023-05-29"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    print(f"\nFetching available models from {url}...")
    print(f"Project ID: {project_id}\n")
    
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint, headers=headers, timeout=30.0)
        
        if response.status_code == 200:
            data = response.json()
            models = data.get("resources", [])
            
            print(f"Found {len(models)} models:\n")
            
            # Filter for Granite models
            granite_models = [m for m in models if "granite" in m.get("model_id", "").lower()]
            
            if granite_models:
                print("=== GRANITE MODELS ===")
                for model in granite_models:
                    model_id = model.get("model_id", "unknown")
                    label = model.get("label", "")
                    print(f"  - {model_id}")
                    if label:
                        print(f"    Label: {label}")
                print()
            
            # Show all models
            print("=== ALL AVAILABLE MODELS ===")
            for model in models[:20]:  # Show first 20
                model_id = model.get("model_id", "unknown")
                print(f"  - {model_id}")
            
            if len(models) > 20:
                print(f"  ... and {len(models) - 20} more")
        else:
            print(f"Failed to list models: {response.status_code}")
            print(response.text)

if __name__ == "__main__":
    asyncio.run(list_models())

# Made with Bob
