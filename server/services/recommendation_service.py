import json
import os
from typing import List, Dict, Any, Optional
from pathlib import Path
from models.schemas import (
    RecommendationRequest,
    RecommendationResponse,
    CareerMatch,
    SkillRecommendation,
    LearningResource,
    Project,
    ErrorResponse
)


# Path to data directory
DATA_DIR = Path(__file__).parent.parent / "data"


def load_json_file(filename: str) -> List[Dict[str, Any]]:
    """
    Load a JSON file from the data directory.
    
    Args:
        filename: Name of the JSON file (e.g., 'careers.json')
    
    Returns:
        List of dictionaries from the JSON file
    
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file is not valid JSON
    """
    file_path = DATA_DIR / filename
    
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {filename}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def calculate_career_match_score(
    career: Dict[str, Any],
    current_skills: List[str],
    preferred_area: Optional[str]
) -> tuple[int, List[str], List[str]]:
    """
    Calculate match score for a career based on user's current skills and preferences.
    
    Scoring Logic:
    1. Base score: (matched_skills / total_required_skills) * 100
    2. Category bonus: +10% if preferred_area matches career category
    3. Final score is capped at 100%
    
    Args:
        career: Career dictionary with required_skills and category
        current_skills: List of skills the user currently has
        preferred_area: User's preferred career area (optional)
    
    Returns:
        Tuple of (match_percentage, matched_skills, missing_skills)
    """
    required_skills = career.get("required_skills", [])
    
    # Handle empty required_skills
    if not required_skills:
        return (0, [], [])
    
    # Normalize skills for case-insensitive comparison
    current_skills_lower = [skill.lower() for skill in current_skills]
    required_skills_lower = [skill.lower() for skill in required_skills]
    
    # Find matched and missing skills
    matched_skills = []
    missing_skills = []
    
    for req_skill in required_skills:
        if req_skill.lower() in current_skills_lower:
            matched_skills.append(req_skill)
        else:
            missing_skills.append(req_skill)
    
    # Calculate base score: percentage of matched skills
    base_score = (len(matched_skills) / len(required_skills)) * 100
    
    # Add category bonus if preferred_area matches
    category_bonus = 0
    if preferred_area and career.get("category"):
        # Case-insensitive partial match
        if preferred_area.lower() in career["category"].lower() or \
           career["category"].lower() in preferred_area.lower():
            category_bonus = 10
    
    # Calculate final score and cap at 100%
    final_score = min(int(base_score + category_bonus), 100)
    
    return (final_score, matched_skills, missing_skills)


def get_skill_resources(skill: str, resources_data: List[Dict[str, Any]]) -> List[LearningResource]:
    """
    Get learning resources for a specific skill.
    
    Args:
        skill: The skill to find resources for
        resources_data: List of resource dictionaries from resources.json
    
    Returns:
        List of LearningResource objects
    """
    skill_lower = skill.lower()
    
    for resource_group in resources_data:
        if resource_group.get("skill", "").lower() == skill_lower:
            resources = resource_group.get("resources", [])
            return [
                LearningResource(
                    title=r.get("title", ""),
                    type=r.get("type", ""),
                    url=r.get("url", "")
                )
                for r in resources
            ]
    
    return []


def get_skill_projects(skill: str, projects_data: List[Dict[str, Any]]) -> List[Project]:
    """
    Get projects for a specific skill.
    
    Args:
        skill: The skill to find projects for
        projects_data: List of project dictionaries from projects.json
    
    Returns:
        List of Project objects
    """
    skill_lower = skill.lower()
    
    for project_group in projects_data:
        if project_group.get("skill", "").lower() == skill_lower:
            projects = project_group.get("projects", [])
            return [
                Project(
                    title=p.get("title", ""),
                    description=p.get("description", ""),
                    difficulty=p.get("difficulty", "beginner")
                )
                for p in projects
            ]
    
    return []


def generate_github_search_query(skill: str) -> str:
    """
    Generate a GitHub search query for a skill.
    
    Args:
        skill: The skill to search for
    
    Returns:
        GitHub search query string
    """
    return f"{skill} beginner project"


async def generate_recommendations(request: RecommendationRequest) -> RecommendationResponse | ErrorResponse:
    """
    Generate career recommendations based on user input.
    
    This function:
    1. Loads all JSON data files
    2. Calculates match scores for all careers
    3. Returns top 3 career matches
    4. Provides learning resources, projects, and GitHub queries for missing skills
    
    Args:
        request: RecommendationRequest with user preferences and skills
    
    Returns:
        RecommendationResponse with career matches and skill recommendations
        or ErrorResponse if something goes wrong
    """
    try:
        # Load data files
        try:
            careers_data = load_json_file("careers.json")
        except FileNotFoundError:
            return ErrorResponse(
                error="Data file missing",
                detail="careers.json not found. Please ensure data files are in server/data/"
            )
        
        try:
            resources_data = load_json_file("resources.json")
        except FileNotFoundError:
            resources_data = []  # Continue without resources
        
        try:
            projects_data = load_json_file("projects.json")
        except FileNotFoundError:
            projects_data = []  # Continue without projects
        
        # Handle empty current_skills - still recommend based on preferred_area
        current_skills = request.current_skills if request.current_skills else []
        
        # Calculate match scores for all careers
        career_scores = []
        
        for career in careers_data:
            score, matched_skills, missing_skills = calculate_career_match_score(
                career,
                current_skills,
                request.preferred_area
            )
            
            career_scores.append({
                "career": career,
                "score": score,
                "matched_skills": matched_skills,
                "missing_skills": missing_skills
            })
        
        # Sort by score (descending) and get top 3
        career_scores.sort(key=lambda x: x["score"], reverse=True)
        top_careers = career_scores[:3]
        
        # Build career matches
        career_matches = []
        all_missing_skills = set()
        
        for item in top_careers:
            career = item["career"]
            
            career_match = CareerMatch(
                id=career.get("id", ""),
                title=career.get("title", ""),
                category=career.get("category", ""),
                description=career.get("description", ""),
                match_percentage=item["score"],
                matched_skills=item["matched_skills"],
                missing_skills=item["missing_skills"],
                common_tasks=career.get("common_tasks", []),
                related_roles=career.get("related_roles", [])
            )
            
            career_matches.append(career_match)
            
            # Collect all missing skills
            all_missing_skills.update(item["missing_skills"])
        
        # Build skill recommendations for missing skills
        skill_recommendations = []
        
        for skill in sorted(all_missing_skills):
            # Get resources for this skill
            resources = get_skill_resources(skill, resources_data)
            
            # Get projects for this skill
            projects = get_skill_projects(skill, projects_data)
            
            # Generate GitHub search query
            github_query = generate_github_search_query(skill)
            
            skill_rec = SkillRecommendation(
                skill=skill,
                resources=resources,
                projects=projects,
                github_search_query=github_query
            )
            
            skill_recommendations.append(skill_rec)
        
        # Build response message
        if current_skills:
            message = f"Found {len(career_matches)} career matches based on your {len(current_skills)} current skills."
        else:
            message = f"Found {len(career_matches)} career recommendations based on your preferred area."
        
        if request.preferred_area:
            message += f" Focused on {request.preferred_area}."
        
        return RecommendationResponse(
            career_matches=career_matches,
            skill_recommendations=skill_recommendations,
            total_careers_analyzed=len(careers_data),
            message=message
        )
    
    except json.JSONDecodeError as e:
        return ErrorResponse(
            error="Invalid JSON data",
            detail=f"Failed to parse JSON file: {str(e)}"
        )
    
    except Exception as e:
        return ErrorResponse(
            error="Unexpected error",
            detail=f"An error occurred while generating recommendations: {str(e)}"
        )

# Made with Bob