"""
Response Normalizer Service
Ensures consistent response structure for frontend consumption.
"""

import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)


def normalize_roadmap_response(
    roadmap: Dict[str, Any],
    career_goal: str,
    requested_timeframe: str,
    github_projects: List[Dict[str, Any]],
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Normalize roadmap response to ensure all required fields exist.
    
    Args:
        roadmap: Raw roadmap from watsonx or fallback
        career_goal: User's career goal
        requested_timeframe: User's requested timeframe
        github_projects: GitHub projects from search
        metadata: Optional metadata dict
    
    Returns:
        Normalized roadmap with guaranteed structure
    """
    logger.info("🔧 Normalizing roadmap response...")
    
    # Ensure all array fields exist
    normalized = {
        "summary": roadmap.get("summary", f"A comprehensive pathway to become a {career_goal}"),
        "phases": roadmap.get("phases", []),
        "skills": roadmap.get("skills", []),
        "tools": roadmap.get("tools", []),
        "resources": roadmap.get("resources", []),
        "githubProjects": roadmap.get("githubProjects", []),
        "portfolioProjects": roadmap.get("portfolioProjects", []),
        "resumeBullets": roadmap.get("resumeBullets", []),
        "weeklyPlan": [],  # Will be validated below
        "nextSteps": roadmap.get("nextSteps", []),
        "certifications": roadmap.get("certifications", [])
    }
    
    # CRITICAL FIX: Preserve week.resources arrays in weeklyPlan
    # The enforcer adds resources to each week, but shallow copy loses them
    logger.info("🔧 Validating weeklyPlan and preserving week.resources...")
    validated_weekly_plan = []
    for i, week in enumerate(roadmap.get("weeklyPlan", [])):
        # Preserve all week fields including the resources array
        validated_week = {
            **week,  # Preserve all existing fields
            "resources": week.get("resources", [])  # Explicitly preserve resources array
        }
        
        # Log resource count for debugging
        resource_count = len(validated_week.get("resources", []))
        week_num = week.get("week", i + 1)
        logger.info(f"   Week {week_num}: {resource_count} resources preserved")
        
        validated_weekly_plan.append(validated_week)
    
    normalized["weeklyPlan"] = validated_weekly_plan
    logger.info(f"✅ Preserved resources in {len(validated_weekly_plan)} weeks")
    
    # Ensure githubProjects is always an array
    if not isinstance(normalized["githubProjects"], list):
        logger.warning(f"githubProjects is not a list: {type(normalized['githubProjects'])}")
        normalized["githubProjects"] = []
    
    # If githubProjects is empty but we have github_projects from search, use them
    if len(normalized["githubProjects"]) == 0 and github_projects:
        logger.info(f"Adding {len(github_projects)} GitHub projects from search")
        normalized["githubProjects"] = github_projects
    
    # Ensure each GitHub project has required fields
    validated_github_projects = []
    for i, project in enumerate(normalized["githubProjects"]):
        validated_project = {
            "name": project.get("name") or project.get("title") or f"Project {i+1}",
            "description": project.get("description") or "No description available",
            "url": project.get("url") or project.get("link") or project.get("html_url") or "#",
            "stars": project.get("stars") or project.get("stargazers_count") or 0,
            "language": project.get("language") or "Unknown",
            "topics": project.get("topics") or [],
            "source": project.get("source", "github_api")
        }
        validated_github_projects.append(validated_project)
    
    normalized["githubProjects"] = validated_github_projects
    
    # Ensure resources have required fields
    validated_resources = []
    for i, resource in enumerate(normalized["resources"]):
        validated_resource = {
            "title": resource.get("title") or f"Resource {i+1}",
            "type": resource.get("type") or "course",
            "url": resource.get("url") or "#",
            "provider": resource.get("provider") or "External",
            "verified": resource.get("verified", False),
            "urlVerified": resource.get("urlVerified", False)
        }
        validated_resources.append(validated_resource)
    
    normalized["resources"] = validated_resources
    
    # Add/update metadata
    if metadata is None:
        metadata = {}
    
    normalized["metadata"] = {
        **metadata,
        "requestedTimeframe": requested_timeframe,
        "normalizedTimeframe": requested_timeframe,  # Can be different if we normalize
        "matchedCareerPath": career_goal,
        "githubProjectCount": len(normalized["githubProjects"]),
        "resourceCount": len(normalized["resources"]),
        "portfolioProjectCount": len(normalized["portfolioProjects"]),
        "weeklyPlanCount": len(normalized["weeklyPlan"]),
        "responseNormalized": True
    }
    
    logger.info(f"✅ Normalization complete:")
    logger.info(f"   - GitHub Projects: {len(normalized['githubProjects'])}")
    logger.info(f"   - Resources: {len(normalized['resources'])}")
    logger.info(f"   - Portfolio Projects: {len(normalized['portfolioProjects'])}")
    logger.info(f"   - Weekly Plans: {len(normalized['weeklyPlan'])}")
    logger.info(f"   - Phases: {len(normalized['phases'])}")
    
    return normalized


def ensure_minimum_resources(
    resources: List[Dict[str, Any]],
    career_goal: str,
    min_count: int = 5
) -> List[Dict[str, Any]]:
    """
    Ensure minimum number of resources by adding general resources if needed.
    
    Args:
        resources: Current resources list
        career_goal: Career goal for context
        min_count: Minimum number of resources required
    
    Returns:
        Resources list with at least min_count items
    """
    if len(resources) >= min_count:
        return resources
    
    logger.warning(f"Only {len(resources)} resources, adding general resources to reach {min_count}")
    
    # General beginner resources that work for any career
    general_resources = [
        {
            "title": "freeCodeCamp - Learn to Code",
            "type": "course",
            "url": "https://www.freecodecamp.org/",
            "provider": "freeCodeCamp",
            "verified": True,
            "urlVerified": True,
            "source": "general_fallback"
        },
        {
            "title": "Khan Academy - Computer Programming",
            "type": "course",
            "url": "https://www.khanacademy.org/computing/computer-programming",
            "provider": "Khan Academy",
            "verified": True,
            "urlVerified": True,
            "source": "general_fallback"
        },
        {
            "title": "Coursera - Career Development",
            "type": "course",
            "url": "https://www.coursera.org/",
            "provider": "Coursera",
            "verified": True,
            "urlVerified": True,
            "source": "general_fallback"
        },
        {
            "title": "LinkedIn Learning - Professional Skills",
            "type": "course",
            "url": "https://www.linkedin.com/learning/",
            "provider": "LinkedIn",
            "verified": True,
            "urlVerified": True,
            "source": "general_fallback"
        },
        {
            "title": "YouTube - Educational Channels",
            "type": "video",
            "url": "https://www.youtube.com/",
            "provider": "YouTube",
            "verified": True,
            "urlVerified": True,
            "source": "general_fallback"
        }
    ]
    
    # Add general resources until we reach min_count
    needed = min_count - len(resources)
    resources.extend(general_resources[:needed])
    
    logger.info(f"✅ Added {needed} general resources, total now: {len(resources)}")
    
    return resources


# Made with Bob