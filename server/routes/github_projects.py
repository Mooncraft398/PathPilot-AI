from fastapi import APIRouter, Path
from models.schemas import GitHubProjectsResponse, ErrorResponse
from services.github_service import search_github_projects

router = APIRouter(prefix="/api/github-projects", tags=["github-projects"])


@router.get("/{skill}", response_model=GitHubProjectsResponse | ErrorResponse)
async def get_github_projects(
    skill: str = Path(..., description="Skill to search for (e.g., python, react, cybersecurity)")
):
    """
    Search GitHub for beginner project examples based on a skill.
    
    This endpoint searches public GitHub repositories using the query:
    "<skill> beginner project" and returns the top 5 results sorted by stars.
    
    Examples:
    - GET /api/github-projects/python
    - GET /api/github-projects/react
    - GET /api/github-projects/cybersecurity
    
    Authentication:
    - If GITHUB_TOKEN is set in environment variables, it will be used for authentication
    - Without a token, you may hit rate limits faster (60 requests/hour vs 5000/hour)
    
    Returns:
    - GitHubProjectsResponse: List of top 5 repositories with name, description, stars, language, and URL
    - ErrorResponse: If the request fails (rate limit, network error, etc.)
    """
    result = await search_github_projects(skill)
    return result

# Made with Bob