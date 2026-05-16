#!/usr/bin/env python3
"""
Test script for resource link validation.
Validates all resource URLs in a generated roadmap and shows replacements.
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Dict, Any

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from services.resource_validator import resource_validator


def print_section(title: str):
    """Print a formatted section header"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


async def test_resource_validation():
    """Test resource validation on a generated roadmap"""
    
    print_section("RESOURCE LINK VALIDATION TEST")
    
    # Load test roadmap
    roadmap_path = Path(__file__).parent / 'test_roadmap_output.json'
    
    if not roadmap_path.exists():
        print(f"\n❌ Test roadmap not found: {roadmap_path}")
        print("Please run test_watsonx_roadmap_json.py first to generate a roadmap.")
        return
    
    with open(roadmap_path, 'r', encoding='utf-8') as f:
        roadmap_data = json.load(f)
    
    print(f"\n✅ Loaded roadmap from: {roadmap_path}")
    
    # Extract resources
    resources = roadmap_data.get("resources", [])
    career_goal = "Data Analyst"  # From test roadmap
    topics = roadmap_data.get("skills", []) + roadmap_data.get("tools", [])
    
    print(f"\n📊 Roadmap Info:")
    print(f"   Career Goal: {career_goal}")
    print(f"   Resources to validate: {len(resources)}")
    print(f"   Topics: {', '.join(topics[:5])}...")
    
    # Test URL validation
    print_section("VALIDATING RESOURCE URLS")
    
    validation_results = []
    
    for i, resource in enumerate(resources, 1):
        url = resource.get("url", "")
        title = resource.get("title", "Untitled")
        
        print(f"\n{i}. {title}")
        print(f"   URL: {url}")
        
        # Validate URL
        validation = await resource_validator.validate_url(url)
        
        validation_results.append({
            "resource": resource,
            "validation": validation
        })
        
        # Print validation result
        if validation["valid"]:
            print(f"   ✅ VALID (HTTP {validation['status_code']})")
            print(f"   Provider: {validation['provider']}")
        else:
            print(f"   ❌ INVALID: {validation['error']}")
            print(f"   Status: {validation.get('status_code', 'N/A')}")
    
    # Count results
    valid_count = sum(1 for r in validation_results if r["validation"]["valid"])
    invalid_count = len(validation_results) - valid_count
    
    print_section("VALIDATION SUMMARY")
    print(f"\n  Total Resources: {len(validation_results)}")
    print(f"  ✅ Valid URLs: {valid_count}")
    print(f"  ❌ Invalid URLs: {invalid_count}")
    print(f"  Success Rate: {(valid_count / len(validation_results) * 100):.1f}%")
    
    # Show verified resource pool
    print_section("VERIFIED RESOURCE POOL")
    
    verified_resources = resource_validator.match_verified_resources(
        career_goal=career_goal,
        topics=topics,
        max_resources=10
    )
    
    print(f"\n  Found {len(verified_resources)} verified resources for {career_goal}:")
    for i, resource in enumerate(verified_resources, 1):
        print(f"\n  {i}. {resource['title']}")
        print(f"     Provider: {resource['provider']}")
        print(f"     URL: {resource['url']}")
        print(f"     Topics: {', '.join(resource['topics'][:3])}")
        print(f"     Difficulty: {resource['difficulty']}")
    
    # Test validation and replacement
    print_section("VALIDATION AND REPLACEMENT")
    
    validated_resources = await resource_validator.validate_and_replace_resources(
        resources=resources,
        career_goal=career_goal,
        topics=topics
    )
    
    print(f"\n  Processed {len(validated_resources)} resources:")
    
    for i, resource in enumerate(validated_resources, 1):
        source = resource.get("source", "unknown")
        title = resource.get("title", "Untitled")
        url = resource.get("url", "")
        verified = resource.get("urlVerified", False)
        
        print(f"\n  {i}. {title}")
        print(f"     Source: {source}")
        print(f"     Verified: {'✅' if verified else '❌'}")
        print(f"     URL: {url}")
        
        if source == "local_verified_replacement":
            print(f"     ⚠️  REPLACED")
            print(f"     Original URL: {resource.get('replacedUrl', 'N/A')}")
            print(f"     Reason: {resource.get('replacementReason', 'N/A')}")
        elif source == "watsonx_unverified":
            print(f"     ⚠️  UNVERIFIED (no replacement available)")
    
    # Save cleaned roadmap
    print_section("SAVING CLEANED ROADMAP")
    
    cleaned_roadmap = roadmap_data.copy()
    cleaned_roadmap["resources"] = validated_resources
    cleaned_roadmap["metadata"]["resourceValidationEnabled"] = True
    cleaned_roadmap["metadata"]["validatedResources"] = valid_count
    cleaned_roadmap["metadata"]["replacedResources"] = sum(
        1 for r in validated_resources if r.get("source") == "local_verified_replacement"
    )
    
    output_path = Path(__file__).parent / 'test_roadmap_validated.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_roadmap, f, indent=2, ensure_ascii=False)
    
    print(f"\n  ✅ Cleaned roadmap saved to: {output_path}")
    print(f"  Original resources: {len(resources)}")
    print(f"  Validated resources: {len(validated_resources)}")
    print(f"  Replaced resources: {cleaned_roadmap['metadata']['replacedResources']}")
    
    # Final recommendations
    print_section("RECOMMENDATIONS")
    
    if invalid_count > 0:
        print("\n  ⚠️  Some resources had invalid URLs:")
        print(f"     - {invalid_count} URLs failed validation")
        print(f"     - These were replaced with verified alternatives")
        print(f"     - Consider using only verified resources in production")
    else:
        print("\n  ✅ All resource URLs are valid!")
        print(f"     - No replacements needed")
        print(f"     - WatsonX generated reliable URLs")
    
    print("\n  💡 Best Practices:")
    print("     1. Always validate URLs before displaying to users")
    print("     2. Use verified resource database as primary source")
    print("     3. Let WatsonX suggest topics, match to verified resources")
    print("     4. Mark unverified resources clearly in the UI")
    
    print_section("TEST COMPLETE")
    print()


if __name__ == "__main__":
    print("\n" + "🔗" * 40)
    print("  RESOURCE LINK VALIDATION TEST SCRIPT")
    print("🔗" * 40)
    
    asyncio.run(test_resource_validation())
    
    print("🔗" * 40)
    print("  TEST SCRIPT COMPLETE")
    print("🔗" * 40 + "\n")

# Made with Bob
