import os
import httpx
import asyncio
import logging
from typing import Optional
from models.schemas import GitHubRepository, GitHubProjectsResponse, ErrorResponse

logger = logging.getLogger(__name__)


async def search_github_projects(
    skill: str,
    max_retries: int = 3,
    min_stars: int = 50
) -> GitHubProjectsResponse | ErrorResponse:
    """
    Search GitHub repositories for beginner projects based on a skill.
    Includes retry logic with exponential backoff and quality filtering.
    
    Args:
        skill: The skill to search for (e.g., "python", "react", "cybersecurity")
        max_retries: Maximum number of retry attempts (default: 3)
        min_stars: Minimum stars for quality filtering (default: 50)
    
    Returns:
        GitHubProjectsResponse with top 5 repositories or ErrorResponse on failure
    """
    # Construct search query with quality filters
    query = f"{skill} beginner project stars:>={min_stars}"
    
    # GitHub API endpoint
    url = "https://api.github.com/search/repositories"
    
    # Query parameters
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 10  # Get more to filter
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
    
    # Retry loop with exponential backoff
    last_error = None
    for attempt in range(max_retries + 1):
        if attempt > 0:
            wait_time = 2 ** attempt  # Exponential backoff: 2s, 4s, 8s
            logger.warning(f"🔄 GitHub API retry attempt {attempt}/{max_retries} after {wait_time}s...")
            await asyncio.sleep(wait_time)
        
        try:
            # Make request to GitHub API
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params, headers=headers, timeout=10.0)
                
                # Handle rate limiting - retry if we have attempts left
                if response.status_code == 403:
                    error_msg = "Rate limit exceeded"
                    logger.warning(f"⚠️  GitHub API: {error_msg}")
                    
                    if attempt < max_retries:
                        last_error = error_msg
                        continue
                    
                    return ErrorResponse(
                        error=error_msg,
                        detail="GitHub API rate limit reached. Please try again later or add a GITHUB_TOKEN to your .env file for higher limits."
                    )
                
                # Retry on server errors (5xx)
                if 500 <= response.status_code < 600:
                    error_msg = f"Server error: HTTP {response.status_code}"
                    logger.warning(f"⚠️  GitHub API: {error_msg}")
                    
                    if attempt < max_retries:
                        last_error = error_msg
                        continue
                    
                    return ErrorResponse(
                        error="GitHub API server error",
                        detail=f"GitHub API returned status code {response.status_code}"
                    )
                
                # Handle other errors (don't retry)
                if response.status_code != 200:
                    return ErrorResponse(
                        error="GitHub API error",
                        detail=f"GitHub API returned status code {response.status_code}"
                    )
                
                # Parse response
                data = response.json()
                
                # Extract and filter repository information
                repositories = []
                for item in data.get("items", []):
                    # Quality filters
                    stars = item.get("stargazers_count", 0)
                    has_description = bool(item.get("description"))
                    
                    # Skip low-quality repos
                    if stars < min_stars or not has_description:
                        continue
                    
                    repo = GitHubRepository(
                        name=item.get("full_name", "Unknown"),
                        description=item.get("description"),
                        stars=stars,
                        language=item.get("language"),
                        url=item.get("html_url", "")
                    )
                    repositories.append(repo)
                    
                    # Stop when we have 5 quality repos
                    if len(repositories) >= 5:
                        break
                
                logger.info(f"✅ GitHub API: Found {len(repositories)} quality repositories")
                
                return GitHubProjectsResponse(
                    skill=skill,
                    repositories=repositories,
                    total_count=data.get("total_count", 0)
                )
        
        except httpx.TimeoutException:
            error_msg = "Request timeout"
            logger.warning(f"⚠️  GitHub API: {error_msg}")
            
            if attempt < max_retries:
                last_error = error_msg
                continue
            
            return ErrorResponse(
                error=error_msg,
                detail="GitHub API request timed out. Please try again."
            )
        
        except httpx.RequestError as e:
            error_msg = f"Network error: {str(e)}"
            logger.warning(f"⚠️  GitHub API: {error_msg}")
            
            if attempt < max_retries:
                last_error = error_msg
                continue
            
            return ErrorResponse(
                error="Network error",
                detail=f"Failed to connect to GitHub API: {str(e)}"
            )
        
        except Exception as e:
            logger.error(f"❌ GitHub API unexpected error: {str(e)}")
            return ErrorResponse(
                error="Unexpected error",
                detail=f"An unexpected error occurred: {str(e)}"
            )
    
    # All retries exhausted
    logger.error(f"❌ GitHub API: All {max_retries + 1} attempts failed. Last error: {last_error}")
    return ErrorResponse(
        error="GitHub API failed",
        detail=f"Failed after {max_retries + 1} attempts: {last_error}"
    )

# Made with Bob