#!/usr/bin/env python3
"""
Test script to verify WatsonX IAM authentication
"""
import os
import asyncio
import httpx
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
env_path = Path(__file__).parent / '.env'
print(f"Loading .env from: {env_path}")
print(f".env file exists: {env_path.exists()}")
print()

load_dotenv(dotenv_path=env_path)

# Get environment variables
api_key = os.getenv('WATSONX_API_KEY')
project_id = os.getenv('WATSONX_PROJECT_ID')
url = os.getenv('WATSONX_URL', 'https://us-south.ml.cloud.ibm.com')
model_id = os.getenv('WATSONX_MODEL_ID', 'ibm/granite-3-8b-instruct')

print("=" * 80)
print("ENVIRONMENT VARIABLES")
print("=" * 80)

if api_key:
    masked_key = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
    print(f"✅ WATSONX_API_KEY: {masked_key}")
else:
    print(f"❌ WATSONX_API_KEY: NOT FOUND")
    
if project_id:
    print(f"✅ WATSONX_PROJECT_ID: {project_id}")
else:
    print(f"❌ WATSONX_PROJECT_ID: NOT FOUND")
    
print(f"✅ WATSONX_URL: {url}")
print(f"✅ WATSONX_MODEL_ID: {model_id}")
print("=" * 80)
print()

if not api_key or not project_id:
    print("❌ Missing required environment variables. Cannot proceed.")
    exit(1)


async def test_iam_token():
    """Test getting IAM token from IBM Cloud"""
    print("=" * 80)
    print("TESTING IAM TOKEN AUTHENTICATION")
    print("=" * 80)
    
    try:
        iam_url = "https://iam.cloud.ibm.com/identity/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }
        data = {
            "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
            "apikey": api_key
        }
        
        print(f"IAM URL: {iam_url}")
        print(f"Grant type: {data['grant_type']}")
        print(f"Sending request...")
        print()
        
        async with httpx.AsyncClient() as client:
            response = await client.post(iam_url, headers=headers, data=data, timeout=30.0)
            
            print(f"Response Status: {response.status_code}")
            
            if response.status_code == 200:
                token_data = response.json()
                access_token = token_data.get("access_token")
                expires_in = token_data.get("expires_in", 0)
                
                if access_token:
                    masked_token = access_token[:20] + "..." + access_token[-10:] if len(access_token) > 30 else "***"
                    print(f"✅ IAM Token obtained successfully!")
                    print(f"   Token: {masked_token}")
                    print(f"   Expires in: {expires_in} seconds ({expires_in/60:.1f} minutes)")
                    print()
                    return access_token
                else:
                    print(f"❌ No access_token in response")
                    print(f"   Response keys: {list(token_data.keys())}")
                    return None
            else:
                print(f"❌ Failed to get IAM token: HTTP {response.status_code}")
                print(f"   Response: {response.text[:500]}")
                
                try:
                    error_data = response.json()
                    print(f"   Error details: {error_data}")
                except:
                    pass
                
                return None
                
    except httpx.TimeoutException:
        print("❌ Request timed out")
        return None
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return None


async def test_watsonx_generation(token):
    """Test calling WatsonX API with the token"""
    print("=" * 80)
    print("TESTING WATSONX TEXT GENERATION")
    print("=" * 80)
    
    try:
        endpoint = f"{url}/ml/v1/text/generation?version=2023-05-29"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        body = {
            "input": "Generate a simple JSON object with a greeting message.",
            "parameters": {
                "decoding_method": "greedy",
                "max_new_tokens": 100,
                "temperature": 0.7,
                "repetition_penalty": 1.1
            },
            "model_id": model_id,
            "project_id": project_id
        }
        
        print(f"Endpoint: {endpoint}")
        print(f"Model: {model_id}")
        print(f"Project ID: {project_id}")
        print(f"Sending request...")
        print()
        
        async with httpx.AsyncClient() as client:
            response = await client.post(endpoint, headers=headers, json=body, timeout=60.0)
            
            print(f"Response Status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                generated_text = result.get("results", [{}])[0].get("generated_text", "")
                token_count = result.get("results", [{}])[0].get("generated_token_count", 0)
                
                print(f"✅ WatsonX generation successful!")
                print(f"   Generated {token_count} tokens")
                print(f"   Response length: {len(generated_text)} characters")
                print()
                print("Generated text:")
                print("-" * 80)
                print(generated_text[:500])
                print("-" * 80)
                return True
            else:
                print(f"❌ WatsonX API error: HTTP {response.status_code}")
                print(f"   Response: {response.text[:1000]}")
                
                try:
                    error_data = response.json()
                    print(f"   Error details: {error_data}")
                except:
                    pass
                
                return False
                
    except httpx.TimeoutException:
        print("❌ Request timed out (60s)")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Run all tests"""
    print()
    print("🧪 WATSONX AUTHENTICATION TEST")
    print()
    
    # Test 1: Get IAM token
    token = await test_iam_token()
    
    if not token:
        print()
        print("=" * 80)
        print("❌ IAM TOKEN TEST FAILED")
        print("=" * 80)
        print()
        print("Possible issues:")
        print("1. Invalid WATSONX_API_KEY")
        print("2. API key doesn't have proper permissions")
        print("3. Network connectivity issues")
        print("4. IBM Cloud IAM service is down")
        print()
        print("Please verify:")
        print("- Your API key is correct in .env file")
        print("- The API key is an IBM Cloud API key (not a project ID or other credential)")
        print("- You can access https://iam.cloud.ibm.com from your network")
        return
    
    print()
    
    # Test 2: Call WatsonX API
    success = await test_watsonx_generation(token)
    
    print()
    print("=" * 80)
    if success:
        print("✅ ALL TESTS PASSED")
        print("=" * 80)
        print()
        print("WatsonX authentication is working correctly!")
        print("Your app should be able to generate AI-powered roadmaps.")
    else:
        print("❌ WATSONX API TEST FAILED")
        print("=" * 80)
        print()
        print("IAM token was obtained, but WatsonX API call failed.")
        print()
        print("Possible issues:")
        print("1. Invalid WATSONX_PROJECT_ID")
        print("2. Project doesn't have access to the model")
        print("3. Invalid WATSONX_URL (wrong region)")
        print("4. Model ID is incorrect")
        print()
        print("Please verify:")
        print("- Your project ID is correct")
        print("- The project has WatsonX.ai enabled")
        print("- The URL matches your project's region")
        print(f"- The model '{model_id}' is available in your project")
    print()


if __name__ == "__main__":
    asyncio.run(main())

# Made with Bob
