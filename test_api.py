import httpx
import json

url = "http://localhost:8000/api/generate-roadmap"
data = {
    "careerGoal": "SOC Analyst",
    "currentSkills": ["Python", "basic networking"],
    "timeframe": "3 months"
}

print("Testing AI Roadmap Generator...")
print(f"POST {url}")
print(f"Request: {json.dumps(data, indent=2)}")
print("\nSending request (this may take 60-90 seconds for AI generation)...\n")

try:
    response = httpx.post(url, json=data, timeout=120.0)
    print(f"Status Code: {response.status_code}")
    print(f"\nResponse:")
    result = response.json()
    print(json.dumps(result, indent=2)[:2000])  # First 2000 chars
    if len(json.dumps(result)) > 2000:
        print("\n... (response truncated, full response is longer)")
except httpx.TimeoutException:
    print("Request timed out (AI generation taking longer than expected)")
except Exception as e:
    print(f"Error: {e}")

# Made with Bob
