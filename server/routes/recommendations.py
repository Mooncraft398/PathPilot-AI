from fastapi import APIRouter
from models.schemas import RecommendationRequest, RecommendationResponse, ErrorResponse
from services.recommendation_service import generate_recommendations

router = APIRouter(prefix="/api", tags=["recommendations"])


@router.post("/recommend", response_model=RecommendationResponse | ErrorResponse)
async def get_recommendations(request: RecommendationRequest):
    """
    Get personalized career recommendations based on user input.
    
    This endpoint analyzes the user's current skills and preferences to:
    1. Match them with the top 3 most suitable careers
    2. Identify skill gaps for each career
    3. Provide learning resources, projects, and GitHub search queries for missing skills
    
    **Scoring Logic:**
    - Base score: (matched_skills / total_required_skills) × 100
    - Category bonus: +10% if preferred_area matches career category
    - Final score is capped at 100%
    
    **Request Body:**
    ```json
    {
      "preferred_area": "Cybersecurity",
      "current_skills": ["Python", "Networking", "Troubleshooting"],
      "hours_per_week": "6-10",
      "learning_style": "Hands-on"
    }
    ```
    
    **Response includes:**
    - Top 3 career matches with match percentages
    - Matched and missing skills for each career
    - Learning resources for each missing skill
    - Project recommendations for each missing skill
    - GitHub search queries for finding example projects
    
    **Notes:**
    - If current_skills is empty, recommendations are based on preferred_area
    - If preferred_area is not provided, all careers are considered equally
    - Resources and projects are matched by skill name (case-insensitive)
    - If no resources/projects exist for a skill, empty arrays are returned
    
    **Example Response:**
    ```json
    {
      "career_matches": [
        {
          "id": "cybersecurity-analyst",
          "title": "Cybersecurity Analyst",
          "category": "Information Security",
          "description": "...",
          "match_percentage": 70,
          "matched_skills": ["Python", "Networking"],
          "missing_skills": ["Cybersecurity", "Security Monitoring", "Incident Response"],
          "common_tasks": [...],
          "related_roles": [...]
        }
      ],
      "skill_recommendations": [
        {
          "skill": "Cybersecurity",
          "resources": [...],
          "projects": [...],
          "github_search_query": "Cybersecurity beginner project"
        }
      ],
      "total_careers_analyzed": 6,
      "message": "Found 3 career matches based on your 3 current skills."
    }
    ```
    """
    result = await generate_recommendations(request)
    return result

# Made with Bob