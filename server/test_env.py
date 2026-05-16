#!/usr/bin/env python3
"""
Test script to verify environment variables are loaded correctly
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
env_path = Path(__file__).parent / '.env'
print(f"Loading .env from: {env_path}")
print(f".env file exists: {env_path.exists()}")

load_dotenv(dotenv_path=env_path)

# Check WatsonX variables
print("\n" + "=" * 80)
print("WATSONX ENVIRONMENT VARIABLES")
print("=" * 80)

watsonx_vars = {
    'WATSONX_API_KEY': os.getenv('WATSONX_API_KEY'),
    'WATSONX_PROJECT_ID': os.getenv('WATSONX_PROJECT_ID'),
    'WATSONX_URL': os.getenv('WATSONX_URL'),
    'WATSONX_MODEL_ID': os.getenv('WATSONX_MODEL_ID'),
}

for key, value in watsonx_vars.items():
    if value:
        # Mask the API key for security
        if 'KEY' in key or 'APIKEY' in key:
            masked_value = value[:8] + '...' + value[-4:] if len(value) > 12 else '***'
            print(f"✅ {key}: {masked_value}")
        else:
            print(f"✅ {key}: {value}")
    else:
        print(f"❌ {key}: NOT FOUND")

print("=" * 80)

# Check if all required variables are present
required_vars = ['WATSONX_API_KEY', 'WATSONX_PROJECT_ID']
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    print(f"\n⚠️  WARNING: Missing required variables: {', '.join(missing_vars)}")
    print("WatsonX.ai integration will NOT work without these variables.")
else:
    print("\n✅ All required WatsonX variables are present!")
    print("WatsonX.ai integration should work correctly.")

print("\n" + "=" * 80)

# Made with Bob
