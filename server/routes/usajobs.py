"""
USAJOBS API Routes
Endpoints for searching live federal job postings.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Dict, Optional
from services.usajobs_service import usajobs_service


router = APIRouter(
    prefix="/api/usajobs",
    tags=["USAJOBS"]
)


@router.get("/search")
async def search_usajobs(
    keyword: str = Query(..., description="Search keyword for jobs", min_length=1),
    location: Optional[str] = Query(None, description="Optional location filter (city, state, or zip)")
) -> Dict:
    """
    Search USAJOBS for live federal job postings.
    
    This endpoint searches the USAJOBS database for current job openings matching
    the provided keyword and optional location. Results include job details such as
    title, organization, location, salary range, and summary.
    
    Args:
        keyword: Search term for jobs (e.g., "cybersecurity", "data analyst")
        location: Optional location filter (e.g., "Orlando", "Florida", "32801")
        
    Returns:
        Dictionary containing:
        - success: Boolean indicating if the search was successful
        - keyword: The search keyword used
        - originalLocation: The original location searched
        - searchLevel: "city", "state", or "nationwide"
        - locationUsed: Actual location used for results
        - count: Number of jobs found
        - jobs: List of matching jobs with details including:
            - title: Job title
            - organization: Hiring organization
            - location: Job location
            - url: Link to job posting
            - minimumSalary: Minimum salary (if available)
            - maximumSalary: Maximum salary (if available)
            - summary: Job summary (if available)
        - fallbackMessage: Optional message if fallback was used
        
    Examples:
        GET /api/usajobs/search?keyword=cybersecurity
        GET /api/usajobs/search?keyword=cybersecurity&location=Orlando
        GET /api/usajobs/search?keyword=data%20analyst&location=Florida
    """
    try:
        result = await usajobs_service.search_jobs(keyword, location)
        
        if not result.get("success"):
            # Return the error response from the service
            return result
        
        return result
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error while searching USAJOBS: {str(e)}"
        )

# Made with Bob
