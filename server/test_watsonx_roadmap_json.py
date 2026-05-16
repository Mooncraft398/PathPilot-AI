#!/usr/bin/env python3
"""
Test script for WatsonX roadmap JSON generation and parsing.
This script tests the exact same flow used by the app to identify JSON parsing issues.
"""

import asyncio
import json
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from services.watsonx_service import watsonx_service
from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def validate_roadmap_schema(roadmap):
    """Validate that the roadmap has all required fields"""
    required_fields = {
        "summary": str,
        "phases": list,
        "skills": list,
        "tools": list,
        "resources": list,
        "portfolioProjects": list,
        "resumeBullets": list,
        "weeklyPlan": list,
        "nextSteps": list
    }
    
    issues = []
    
    for field, expected_type in required_fields.items():
        if field not in roadmap:
            issues.append(f"❌ Missing required field: {field}")
        elif not isinstance(roadmap[field], expected_type):
            issues.append(f"❌ Field '{field}' has wrong type: expected {expected_type.__name__}, got {type(roadmap[field]).__name__}")
    
    # Validate phases structure
    if "phases" in roadmap and isinstance(roadmap["phases"], list):
        for i, phase in enumerate(roadmap["phases"]):
            if not isinstance(phase, dict):
                issues.append(f"❌ Phase {i} is not a dictionary")
            else:
                phase_fields = ["phase", "title", "duration", "focus", "skills"]
                for field in phase_fields:
                    if field not in phase:
                        issues.append(f"❌ Phase {i} missing field: {field}")
    
    # Validate weeklyPlan structure
    if "weeklyPlan" in roadmap and isinstance(roadmap["weeklyPlan"], list):
        for i, week in enumerate(roadmap["weeklyPlan"]):
            if not isinstance(week, dict):
                issues.append(f"❌ Week {i} is not a dictionary")
            else:
                week_fields = ["week", "focus", "topics", "dailyTasks"]
                for field in week_fields:
                    if field not in week:
                        issues.append(f"❌ Week {i} missing field: {field}")
    
    # Validate portfolioProjects structure
    if "portfolioProjects" in roadmap and isinstance(roadmap["portfolioProjects"], list):
        for i, project in enumerate(roadmap["portfolioProjects"]):
            if not isinstance(project, dict):
                issues.append(f"❌ Portfolio project {i} is not a dictionary")
            else:
                project_fields = ["title", "description"]
                for field in project_fields:
                    if field not in project:
                        issues.append(f"❌ Portfolio project {i} missing field: {field}")
                
                # Check if skills field exists (important for frontend)
                if "skills" not in project:
                    issues.append(f"⚠️  Portfolio project {i} missing 'skills' field (will cause empty skills in UI)")
    
    return issues


async def test_roadmap_generation():
    """Test the complete roadmap generation flow"""
    
    print_section("WATSONX ROADMAP JSON PARSING TEST")
    
    # Check environment variables
    print("\n📋 Environment Variables:")
    api_key = os.getenv("WATSONX_API_KEY")
    project_id = os.getenv("WATSONX_PROJECT_ID")
    
    if api_key:
        masked_key = api_key[:8] + "..." + api_key[-4:]
        print(f"  ✅ WATSONX_API_KEY: {masked_key}")
    else:
        print("  ❌ WATSONX_API_KEY: NOT FOUND")
        return
    
    if project_id:
        print(f"  ✅ WATSONX_PROJECT_ID: {project_id}")
    else:
        print("  ❌ WATSONX_PROJECT_ID: NOT FOUND")
        return
    
    # Test parameters
    career_goal = "Data Analyst"
    current_skills = ["Excel", "SQL"]
    timeframe = "3 months"
    
    print_section("TEST PARAMETERS")
    print(f"  Career Goal: {career_goal}")
    print(f"  Current Skills: {', '.join(current_skills)}")
    print(f"  Timeframe: {timeframe}")
    
    # Mock resources and projects
    local_resources = {
        "resources": [
            {"title": "SQL Tutorial", "type": "course", "url": "https://example.com/sql"},
            {"title": "Excel Basics", "type": "course", "url": "https://example.com/excel"}
        ]
    }
    
    github_projects = [
        {"name": "data-analysis-project", "description": "Beginner data analysis", "stars": 100, "language": "Python"}
    ]
    
    print_section("CALLING WATSONX API")
    print("  Generating roadmap...")
    print(f"  Max tokens configured: 4000")
    print(f"  Model: ibm/granite-3-8b-instruct")
    
    try:
        # Call the actual service
        result = await watsonx_service.generate_career_roadmap(
            career_goal=career_goal,
            current_skills=current_skills,
            timeframe=timeframe,
            local_resources=local_resources,
            github_projects=github_projects
        )
        
        if result is None:
            print_section("❌ GENERATION FAILED")
            print("  WatsonX returned None")
            print("\n  Check the logs above for:")
            print("    - Authentication errors (check API key)")
            print("    - API call errors (check network/service)")
            print("    - JSON parsing errors (check for truncation)")
            print("    - Response truncation (check if response ends with })")
            print("\n  If you see 'RESPONSE APPEARS TRUNCATED':")
            print("    - The model hit the max_new_tokens limit")
            print("    - Current limit: 4000 tokens")
            print("    - Solution: Simplify prompt or increase token limit further")
            return
        
        print_section("✅ GENERATION SUCCESSFUL")
        
        # Validate schema
        print_section("VALIDATING ROADMAP SCHEMA")
        issues = validate_roadmap_schema(result)
        
        if issues:
            print("  ⚠️  Schema validation issues found:")
            for issue in issues:
                print(f"    {issue}")
        else:
            print("  ✅ All required fields present and valid!")
        
        # Print structure summary
        print_section("ROADMAP STRUCTURE SUMMARY")
        print(f"  Summary: {result.get('summary', 'N/A')[:100]}...")
        print(f"  Phases: {len(result.get('phases', []))}")
        print(f"  Skills: {len(result.get('skills', []))}")
        print(f"  Tools: {len(result.get('tools', []))}")
        print(f"  Resources: {len(result.get('resources', []))}")
        print(f"  Portfolio Projects: {len(result.get('portfolioProjects', []))}")
        print(f"  Resume Bullets: {len(result.get('resumeBullets', []))}")
        print(f"  Weekly Plans: {len(result.get('weeklyPlan', []))}")
        print(f"  Next Steps: {len(result.get('nextSteps', []))}")
        
        # Check metadata
        if "metadata" in result:
            print(f"\n  Metadata:")
            print(f"    Used WatsonX: {result['metadata'].get('usedWatsonx', False)}")
            print(f"    Model: {result['metadata'].get('model', 'unknown')}")
            print(f"    Tokens: {result['metadata'].get('tokens', 0)}")
        
        # Check weekly plan uniqueness
        print_section("WEEKLY PLAN UNIQUENESS CHECK")
        if "weeklyPlan" in result and isinstance(result["weeklyPlan"], list):
            focuses = [week.get("focus", "") for week in result["weeklyPlan"]]
            unique_focuses = set(focuses)
            
            print(f"  Total weeks: {len(focuses)}")
            print(f"  Unique focuses: {len(unique_focuses)}")
            
            if len(unique_focuses) < len(focuses):
                print("  ⚠️  WARNING: Some weeks have duplicate focus areas!")
                print("  This means the AI is repeating content.")
            else:
                print("  ✅ All weeks have unique focus areas!")
            
            print("\n  Week focuses:")
            for i, focus in enumerate(focuses, 1):
                print(f"    Week {i}: {focus}")
        
        # Check portfolio projects have skills
        print_section("PORTFOLIO PROJECTS SKILLS CHECK")
        if "portfolioProjects" in result and isinstance(result["portfolioProjects"], list):
            for i, project in enumerate(result["portfolioProjects"], 1):
                title = project.get("title", "Untitled")
                skills = project.get("skills", [])
                
                if skills and isinstance(skills, list) and len(skills) > 0:
                    print(f"  ✅ Project {i} ({title}): {len(skills)} skills")
                else:
                    print(f"  ❌ Project {i} ({title}): NO SKILLS (will show empty in UI)")
        
        # Save to file for inspection
        output_file = Path(__file__).parent / "test_roadmap_output.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print_section("✅ TEST COMPLETE")
        print(f"  Full roadmap saved to: {output_file}")
        print("  You can inspect the complete JSON structure in that file.")
        print("\n  This roadmap would work in the app: ", end="")
        
        if not issues or all("⚠️" in issue for issue in issues):
            print("✅ YES")
        else:
            print("❌ NO (see validation issues above)")
    
    except Exception as e:
        print_section("❌ EXCEPTION OCCURRED")
        print(f"  Error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("\n" + "🧪" * 40)
    print("  WATSONX ROADMAP JSON PARSING TEST SCRIPT")
    print("🧪" * 40)
    
    asyncio.run(test_roadmap_generation())
    
    print("\n" + "🧪" * 40)
    print("  TEST SCRIPT COMPLETE")
    print("🧪" * 40 + "\n")

# Made with Bob
