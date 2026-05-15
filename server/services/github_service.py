import os
import httpx
from typing import Optional
from models.schemas import GitHubRepository, GitHubProjectsResponse, ErrorResponse


async def search_github_projects(skill: str) -> GitHubProjectsResponse | ErrorResponse:
    """
    Search GitHub repositories for beginner projects based on a skill.
    
    Args:
        skill: The skill to search for (e.g., "python", "react", "cybersecurity")
    
    Returns:
        GitHubProjectsResponse with top 5 repositories or ErrorResponse on failure
    """
    # Construct search query
    query = f"{skill} beginner project"
    
    # GitHub API endpoint
    url = "https://api.github.com/search/repositories"
    
    # Query parameters
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 5
    }
    
    # Headers
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "PathPilot-AI-Hackathon"
    }
    
    # Add authentication if token is available
    github_token = os.getenv("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"
    
    try:
        # Make request to GitHub API
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, headers=headers, timeout=10.0)
            
            # Handle rate limiting
            if response.status_code == 403:
                return ErrorResponse(
                    error="Rate limit exceeded",
                    detail="GitHub API rate limit reached. Please try again later or add a GITHUB_TOKEN to your .env file for higher limits."
                )
            
            # Handle other errors
            if response.status_code != 200:
                return ErrorResponse(
                    error="GitHub API error",
                    detail=f"GitHub API returned status code {response.status_code}"
                )
            
            # Parse response
            data = response.json()
            
            # Extract repository information
            repositories = []
            for item in data.get("items", [])[:5]:  # Ensure we only get top 5
                repo = GitHubRepository(
                    name=item.get("full_name", "Unknown"),
                    description=item.get("description"),
                    stars=item.get("stargazers_count", 0),
                    language=item.get("language"),
                    url=item.get("html_url", "")
                )
                repositories.append(repo)
            
            return GitHubProjectsResponse(
                skill=skill,
                repositories=repositories,
                total_count=data.get("total_count", 0)
            )
    
    except httpx.TimeoutException:
        return ErrorResponse(
            error="Request timeout",
            detail="GitHub API request timed out. Please try again."
        )
    
    except httpx.RequestError as e:
        return ErrorResponse(
            error="Network error",
            detail=f"Failed to connect to GitHub API: {str(e)}"
        )
    
    except Exception as e:
        return ErrorResponse(
            error="Unexpected error",
            detail=f"An unexpected error occurred: {str(e)}"
        )

# Made with Bob