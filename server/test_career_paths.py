#!/usr/bin/env python3
"""
Career Path Testing Script
Tests all career paths with different timeframes to ensure consistent output.
"""

import asyncio
import json
import sys
from pathlib import Path

# Add server directory to path
sys.path.insert(0, str(Path(__file__).parent))

from services.watsonx_service import watsonx_service
from services.github_service import search_github_projects
from routes.roadmap import get_resources_for_skills, match_role_data


async def test_career_path(career_goal: str, timeframe: str):
    """Test a single career path with a specific timeframe"""
    print(f"\n{'='*80}")
    print(f"Testing: {career_goal} - {timeframe}")
    print(f"{'='*80}")
    
    try:
        # Step 1: Match role data
        role_data = match_role_data(career_goal)
        if not role_data:
            print(f"❌ No role data found for: {career_goal}")
            return False
        
        print(f"✅ Role matched: {role_data.get('title', 'Unknown')}")
        skills = role_data.get("skills", [])
        print(f"   Skills: {', '.join(skills[:5])}")
        
        # Step 2: Get resources
        resources = get_resources_for_skills(skills=skills, career_goal=career_goal)
        resource_count = len(resources.get("resources", []))
        print(f"✅ Resources found: {resource_count}")
        
        if resource_count < 5:
            print(f"⚠️  WARNING: Only {resource_count} resources (expected 5+)")
        
        # Step 3: Search GitHub projects
        # Use first skill as search term
        search_skill = skills[0] if skills else career_goal
        github_result = await search_github_projects(skill=search_skill)
        
        # Handle response (could be GitHubProjectsResponse or ErrorResponse)
        if hasattr(github_result, 'repositories'):
            github_projects = [
                {
                    "name": repo.name,
                    "description": repo.description,
                    "stars": repo.stars,
                    "url": repo.url
                }
                for repo in github_result.repositories
            ]
            print(f"✅ GitHub projects found: {len(github_projects)}")
        else:
            print(f"⚠️  GitHub search failed: {getattr(github_result, 'error', 'Unknown error')}")
            github_projects = []
        
        # Step 4: Test watsonx generation (if credentials available)
        if watsonx_service.project_id:
            print("🤖 Testing watsonx.ai generation...")
            roadmap = await watsonx_service.generate_career_roadmap(
                career_goal=career_goal,
                current_skills=[],
                timeframe=timeframe,
                local_resources=resources,
                github_projects=github_projects
            )
            
            if roadmap:
                print("✅ Watsonx generation successful")
                print(f"   Phases: {len(roadmap.get('phases', []))}")
                print(f"   Resources: {len(roadmap.get('resources', []))}")
                print(f"   GitHub Projects: {len(roadmap.get('githubProjects', []))}")
                print(f"   Portfolio Projects: {len(roadmap.get('portfolioProjects', []))}")
                print(f"   Weekly Plan: {len(roadmap.get('weeklyPlan', []))}")
                
                # Check if timeframe is preserved
                summary = roadmap.get('summary', '')
                if timeframe.lower() in summary.lower():
                    print(f"✅ Timeframe preserved in summary")
                else:
                    print(f"⚠️  WARNING: Timeframe '{timeframe}' not found in summary")
                
                return True
            else:
                print("❌ Watsonx generation failed")
                return False
        else:
            print("⚠️  Skipping watsonx test (no credentials)")
            return True
            
    except Exception as e:
        print(f"❌ Error testing {career_goal}: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Run all career path tests"""
    print("=" * 80)
    print("CAREER PATH TESTING SUITE")
    print("=" * 80)
    
    # Define test cases
    career_paths = [
        "SOC Analyst",
        "IT Help Desk",
        "Network Technician",
        "Cybersecurity Analyst",
        "Cloud Support Associate",
        "Software Developer"
    ]
    
    timeframes = [
        "4 weeks",
        "6 weeks",
        "3 months",
        "6 months"
    ]
    
    results = {}
    
    # Test each career path with different timeframes
    for career_goal in career_paths:
        results[career_goal] = {}
        for timeframe in timeframes:
            success = await test_career_path(career_goal, timeframe)
            results[career_goal][timeframe] = success
            
            # Small delay between tests
            await asyncio.sleep(2)
    
    # Print summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    
    total_tests = 0
    passed_tests = 0
    
    for career_goal, timeframe_results in results.items():
        print(f"\n{career_goal}:")
        for timeframe, success in timeframe_results.items():
            status = "✅ PASS" if success else "❌ FAIL"
            print(f"  {timeframe}: {status}")
            total_tests += 1
            if success:
                passed_tests += 1
    
    print("\n" + "=" * 80)
    print(f"Total: {passed_tests}/{total_tests} tests passed")
    print("=" * 80)
    
    # Exit with appropriate code
    sys.exit(0 if passed_tests == total_tests else 1)


if __name__ == "__main__":
    asyncio.run(main())

# Made with Bob
