"""
Roadmap Enforcer Service
Enforces backend requirements: correct timeframe, resource allocation, GitHub validation
"""

import logging
import re
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)


def parse_timeframe(timeframe: str, form_weeks: Optional[int] = None) -> int:
    """
    Parse timeframe string to get total weeks.
    
    Args:
        timeframe: Timeframe string like "6 weeks", "3 months"
        form_weeks: Explicit weeks from form if provided
    
    Returns:
        Total weeks as integer
    """
    # If form explicitly provides weeks, use that
    if form_weeks and isinstance(form_weeks, int) and form_weeks > 0:
        logger.info(f"📅 Using explicit form weeks: {form_weeks}")
        return form_weeks
    
    # Parse timeframe string
    timeframe_lower = timeframe.lower().strip()
    
    # Try to extract number
    match = re.search(r'(\d+)', timeframe_lower)
    if not match:
        logger.warning(f"Could not parse timeframe '{timeframe}', defaulting to 12 weeks")
        return 12
    
    number = int(match.group(1))
    
    # Determine if it's weeks or months
    if 'month' in timeframe_lower:
        weeks = number * 4
        logger.info(f"📅 Parsed '{timeframe}' as {number} months = {weeks} weeks")
        return weeks
    elif 'week' in timeframe_lower:
        logger.info(f"📅 Parsed '{timeframe}' as {number} weeks")
        return number
    else:
        # Assume weeks if no unit specified
        logger.info(f"📅 Parsed '{timeframe}' as {number} weeks (no unit specified)")
        return number


def enforce_weekly_plan_length(
    roadmap: Dict[str, Any],
    required_weeks: int,
    career_goal: str
) -> Dict[str, Any]:
    """
    Ensure weeklyPlan has exactly required_weeks entries.
    
    Args:
        roadmap: Roadmap dict with weeklyPlan
        required_weeks: Number of weeks required
        career_goal: Career goal for context
    
    Returns:
        Roadmap with corrected weeklyPlan
    """
    weekly_plan = roadmap.get("weeklyPlan", [])
    current_weeks = len(weekly_plan)
    
    logger.info(f"📅 Enforcing weekly plan length:")
    logger.info(f"   Required: {required_weeks} weeks")
    logger.info(f"   Current: {current_weeks} weeks")
    
    if current_weeks == required_weeks:
        logger.info(f"   ✅ Weekly plan already has correct length")
        return roadmap
    
    if current_weeks > required_weeks:
        # Trim extra weeks
        logger.warning(f"   ⚠️  Trimming {current_weeks - required_weeks} extra weeks")
        roadmap["weeklyPlan"] = weekly_plan[:required_weeks]
        return roadmap
    
    # Need to add weeks
    weeks_to_add = required_weeks - current_weeks
    logger.warning(f"   ⚠️  Adding {weeks_to_add} missing weeks using fallback logic")
    
    # Get skills and tools for generating weeks
    skills = roadmap.get("skills", ["Problem Solving", "Critical Thinking"])
    tools = roadmap.get("tools", ["Industry Tools"])
    
    # Generate missing weeks
    for week_num in range(current_weeks + 1, required_weeks + 1):
        # Determine phase based on week number
        phase_index = (week_num - 1) // max(1, required_weeks // 3)
        
        if week_num <= required_weeks // 3:
            focus = f"Foundation: {skills[0] if skills else 'Core Concepts'}"
            topics = ["Fundamentals", "Basic concepts", "Getting started"]
            tasks = ["Study basics", "Complete tutorials", "Practice exercises", "Review concepts", "Build understanding"]
        elif week_num <= (required_weeks * 2) // 3:
            focus = f"Practice: {skills[min(1, len(skills)-1)] if skills else 'Hands-on Skills'}"
            topics = ["Practical application", "Projects", "Real-world scenarios"]
            tasks = ["Work on projects", "Apply concepts", "Build portfolio", "Seek feedback", "Refine skills"]
        else:
            focus = "Portfolio & Job Prep"
            topics = ["Portfolio development", "Resume", "Interview prep"]
            tasks = ["Complete projects", "Polish portfolio", "Update resume", "Practice interviews", "Apply to jobs"]
        
        weekly_plan.append({
            "week": week_num,
            "focus": focus,
            "topics": topics,
            "dailyTasks": tasks
        })
    
    roadmap["weeklyPlan"] = weekly_plan
    logger.info(f"   ✅ Weekly plan now has {len(weekly_plan)} weeks")
    
    return roadmap


def allocate_resources_to_weeks(
    roadmap: Dict[str, Any],
    total_weeks: int,
    all_resources: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Allocate resources to each week in weeklyPlan.
    
    Args:
        roadmap: Roadmap dict with weeklyPlan
        total_weeks: Total number of weeks
        all_resources: All available resources
    
    Returns:
        Roadmap with resources allocated to each week
    """
    logger.info(f"📚 Allocating resources to weeks:")
    logger.info(f"   Total weeks: {total_weeks}")
    logger.info(f"   Available resources: {len(all_resources)}")
    
    if len(all_resources) < total_weeks:
        logger.warning(f"   ⚠️  Only {len(all_resources)} resources for {total_weeks} weeks")
    
    weekly_plan = roadmap.get("weeklyPlan", [])
    
    # Target 2 resources per week when possible
    target_per_week = 2
    
    # Calculate how many resources each week should get
    if len(all_resources) >= total_weeks * target_per_week:
        # Enough for 2 per week
        resources_per_week = target_per_week
    elif len(all_resources) >= total_weeks:
        # At least 1 per week
        resources_per_week = max(1, len(all_resources) // total_weeks)
    else:
        # Not enough, will need to reuse
        resources_per_week = 1
    
    logger.info(f"   Target per week: {resources_per_week}")
    
    # Allocate resources
    for i, week in enumerate(weekly_plan):
        week_num = week.get("week", i + 1)
        
        # Calculate resource indices for this week
        start_idx = i * resources_per_week
        end_idx = min(start_idx + resources_per_week, len(all_resources))
        
        week_resources = all_resources[start_idx:end_idx]
        
        # If we ran out, reuse from beginning
        if len(week_resources) == 0 and len(all_resources) > 0:
            reuse_idx = i % len(all_resources)
            week_resources = [all_resources[reuse_idx]]
            logger.warning(f"   Week {week_num}: Reusing resource {reuse_idx + 1}")
        
        week["resources"] = week_resources
        logger.info(f"   Week {week_num}: {len(week_resources)} resources")
    
    roadmap["weeklyPlan"] = weekly_plan
    
    # Count total resources allocated
    total_allocated = sum(len(week.get("resources", [])) for week in weekly_plan)
    logger.info(f"   ✅ Total resources allocated: {total_allocated}")
    
    return roadmap


def filter_invalid_github_projects(
    github_projects: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Filter out invalid GitHub projects (placeholders, missing URLs, etc.)
    
    Args:
        github_projects: List of GitHub project dicts
    
    Returns:
        Filtered list with only valid projects
    """
    logger.info(f"🐙 Filtering GitHub projects:")
    logger.info(f"   Input count: {len(github_projects)}")
    
    valid_projects = []
    invalid_count = 0
    
    for i, project in enumerate(github_projects):
        url = project.get("url", "")
        stars = project.get("stars", 0)
        language = project.get("language", "Unknown")
        source = project.get("source", "unknown")
        
        # Check if it's a valid GitHub project
        is_valid = True
        reason = ""
        
        # Rule 1: Must have a real URL
        if not url or url == "#" or url == "":
            is_valid = False
            reason = "missing or placeholder URL"
        
        # Rule 2: If source is github_api, must have real metadata
        elif source == "github_api":
            if stars == 0 and language == "Unknown":
                is_valid = False
                reason = "github_api source but no real metadata (stars=0, language=Unknown)"
            elif not url.startswith("https://github.com/"):
                is_valid = False
                reason = "github_api source but URL doesn't start with https://github.com/"
        
        # Rule 3: URL must be a real GitHub URL if claiming to be from GitHub
        elif "github" in source.lower() and not url.startswith("https://github.com/"):
            is_valid = False
            reason = "claims GitHub source but URL is not a GitHub URL"
        
        if is_valid:
            valid_projects.append(project)
            logger.info(f"   ✅ Project {i+1}: {project.get('name', 'Unknown')} - VALID")
        else:
            invalid_count += 1
            logger.warning(f"   ❌ Project {i+1}: {project.get('name', 'Unknown')} - INVALID ({reason})")
    
    logger.info(f"   Valid projects: {len(valid_projects)}")
    logger.info(f"   Invalid projects removed: {invalid_count}")
    
    return valid_projects


def enforce_roadmap_requirements(
    roadmap: Dict[str, Any],
    career_goal: str,
    requested_timeframe: str,
    form_weeks: Optional[int],
    github_projects: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Main enforcement function - ensures all backend requirements are met.
    
    Args:
        roadmap: Raw roadmap from watsonx or fallback
        career_goal: User's career goal
        requested_timeframe: User's requested timeframe string
        form_weeks: Explicit weeks from form if provided
        github_projects: GitHub projects from search
    
    Returns:
        Enforced roadmap meeting all requirements
    """
    logger.info("=" * 80)
    logger.info("🔒 ENFORCING ROADMAP REQUIREMENTS")
    logger.info("=" * 80)
    
    # Step 1: Parse and enforce timeframe
    total_weeks = parse_timeframe(requested_timeframe, form_weeks)
    logger.info(f"✅ Total weeks determined: {total_weeks}")
    
    # Step 2: Enforce weekly plan length
    roadmap = enforce_weekly_plan_length(roadmap, total_weeks, career_goal)
    
    # Step 3: Get all resources
    all_resources = roadmap.get("resources", [])
    logger.info(f"📚 Total resources available: {len(all_resources)}")
    
    # Step 4: Allocate resources to weeks
    roadmap = allocate_resources_to_weeks(roadmap, total_weeks, all_resources)
    
    # Step 5: Filter invalid GitHub projects
    valid_github_projects = filter_invalid_github_projects(github_projects)
    
    # Update roadmap with valid GitHub projects
    roadmap["githubProjects"] = valid_github_projects
    
    # Step 6: Update phases to match timeframe
    phases = roadmap.get("phases", [])
    if phases and len(phases) >= 3:
        phase_weeks = total_weeks // 3
        phase1_end = phase_weeks
        phase2_end = phase_weeks * 2
        
        phases[0]["duration"] = f"Weeks 1-{phase1_end}"
        phases[1]["duration"] = f"Weeks {phase1_end + 1}-{phase2_end}"
        phases[2]["duration"] = f"Weeks {phase2_end + 1}-{total_weeks}"
        
        roadmap["phases"] = phases
        logger.info(f"✅ Updated phase durations to match {total_weeks} weeks")
    
    # Step 7: Add enforcement metadata
    if "metadata" not in roadmap:
        roadmap["metadata"] = {}
    
    roadmap["metadata"].update({
        "totalWeeks": total_weeks,
        "requestedTimeframe": requested_timeframe,
        "normalizedTimeframe": f"{total_weeks} weeks",
        "weeklyPlanCount": len(roadmap.get("weeklyPlan", [])),
        "resourceCount": len(all_resources),
        "githubProjectCount": len(valid_github_projects),
        "githubInvalidRemoved": len(github_projects) - len(valid_github_projects),
        "enforcementApplied": True
    })
    
    logger.info("=" * 80)
    logger.info("✅ ENFORCEMENT COMPLETE")
    logger.info("=" * 80)
    logger.info(f"   Total weeks: {total_weeks}")
    logger.info(f"   Weekly plan length: {len(roadmap.get('weeklyPlan', []))}")
    logger.info(f"   Resources: {len(all_resources)}")
    logger.info(f"   Valid GitHub projects: {len(valid_github_projects)}")
    logger.info(f"   Invalid GitHub projects removed: {len(github_projects) - len(valid_github_projects)}")
    logger.info("=" * 80)
    
    return roadmap


# Made with Bob