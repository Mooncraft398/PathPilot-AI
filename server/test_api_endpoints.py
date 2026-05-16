#!/usr/bin/env python3
"""
API Endpoint Testing Script
Tests the /api/generate-roadmap endpoint with various inputs.
"""

import requests
import json
import sys
from time import sleep

# API base URL
BASE_URL = "http://localhost:5000"


def test_generate_roadmap(career_goal: str, timeframe: str, current_skills=None):
    """Test the generate-roadmap endpoint"""
    print(f"\n{'='*80}")
    print(f"Testing: {career_goal} - {timeframe}")
    print(f"{'='*80}")
    
    if current_skills is None:
        current_skills = []
    
    payload = {
        "careerGoal": career_goal,
        "currentSkills": current_skills,
        "timeframe": timeframe
    }
    
    try:
        print(f"📤 Sending request to {BASE_URL}/api/generate-roadmap")
        print(f"   Payload: {json.dumps(payload, indent=2)}")
        
        response = requests.post(
            f"{BASE_URL}/api/generate-roadmap",
            json=payload,
            timeout=120  # 2 minute timeout for AI generation
        )
        
        print(f"📥 Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            # Check response structure
            if not data.get("success"):
                print("❌ Response indicates failure")
                print(f"   Error: {data.get('error', 'Unknown error')}")
                return False
            
            roadmap = data.get("roadmap", {})
            metadata = data.get("metadata", {})
            
            print("✅ Roadmap generated successfully")
            print(f"\n📊 Response Summary:")
            print(f"   Career Goal: {data.get('careerGoal')}")
            print(f"   Summary: {roadmap.get('summary', 'N/A')[:100]}...")
            print(f"   Phases: {len(roadmap.get('phases', []))}")
            print(f"   Skills: {len(roadmap.get('skills', []))}")
            print(f"   Tools: {len(roadmap.get('tools', []))}")
            print(f"   Resources: {len(roadmap.get('resources', []))}")
            print(f"   GitHub Projects: {len(roadmap.get('githubProjects', []))}")
            print(f"   Portfolio Projects: {len(roadmap.get('portfolioProjects', []))}")
            print(f"   Resume Bullets: {len(roadmap.get('resumeBullets', []))}")
            print(f"   Weekly Plan: {len(roadmap.get('weeklyPlan', []))}")
            print(f"   Next Steps: {len(roadmap.get('nextSteps', []))}")
            
            print(f"\n🔧 Metadata:")
            print(f"   Used Watsonx: {metadata.get('usedWatsonx', False)}")
            print(f"   Used GitHub: {metadata.get('usedGitHub', False)}")
            print(f"   Matched Resources: {metadata.get('matchedLocalResources', 0)}")
            
            # Validation checks
            issues = []
            
            if len(roadmap.get('resources', [])) < 3:
                issues.append(f"Only {len(roadmap.get('resources', []))} resources (expected 3+)")
            
            if len(roadmap.get('phases', [])) == 0:
                issues.append("No phases defined")
            
            if len(roadmap.get('weeklyPlan', [])) == 0:
                issues.append("No weekly plan")
            
            # Check if timeframe is preserved in summary
            summary = roadmap.get('summary', '').lower()
            if timeframe.lower() not in summary:
                issues.append(f"Timeframe '{timeframe}' not found in summary")
            
            if issues:
                print(f"\n⚠️  Validation Issues:")
                for issue in issues:
                    print(f"   - {issue}")
            else:
                print(f"\n✅ All validation checks passed")
            
            return len(issues) == 0
            
        else:
            print(f"❌ Request failed with status {response.status_code}")
            print(f"   Response: {response.text[:500]}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Request timed out (>120s)")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - is the server running?")
        print(f"   Make sure the backend is running at {BASE_URL}")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all API tests"""
    print("=" * 80)
    print("API ENDPOINT TESTING SUITE")
    print("=" * 80)
    print(f"Target: {BASE_URL}")
    print("=" * 80)
    
    # Check if server is running
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        print("✅ Server is running")
    except:
        print("❌ Server is not running!")
        print(f"   Please start the backend server first:")
        print(f"   cd server && python main.py")
        sys.exit(1)
    
    # Define test cases
    test_cases = [
        ("SOC Analyst", "4 weeks", []),
        ("SOC Analyst", "6 weeks", ["Python", "Networking"]),
        ("IT Help Desk", "1 month", []),
        ("Network Technician", "3 months", []),
        ("Cybersecurity Analyst", "6 months", ["Linux", "Security"]),
        ("Software Developer", "12 weeks", ["JavaScript"]),
    ]
    
    results = []
    
    for career_goal, timeframe, skills in test_cases:
        success = test_generate_roadmap(career_goal, timeframe, skills)
        results.append((career_goal, timeframe, success))
        
        # Delay between tests to avoid rate limiting
        if len(results) < len(test_cases):
            print("\n⏳ Waiting 3 seconds before next test...")
            sleep(3)
    
    # Print summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    
    passed = sum(1 for _, _, success in results if success)
    total = len(results)
    
    for career_goal, timeframe, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {career_goal} ({timeframe})")
    
    print("\n" + "=" * 80)
    print(f"Total: {passed}/{total} tests passed ({passed*100//total}%)")
    print("=" * 80)
    
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()

# Made with Bob
