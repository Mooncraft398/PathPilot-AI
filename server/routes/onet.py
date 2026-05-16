"""
O*NET API Routes
Endpoints for searching O*NET occupation data.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Dict
import logging
from services.onet_service import onet_service

# Set up logging
logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/api/onet",
    tags=["O*NET"]
)


@router.get("/debug")
async def debug_onet_connection() -> Dict:
    """
    Debug endpoint to test O*NET API connection.
    
    This endpoint tests the O*NET API connection without exposing sensitive credentials.
    It calls the O*NET /about/ endpoint to verify authentication is working.
    
    Returns:
        Dictionary containing:
        - success: Boolean indicating if connection test passed
        - status_code: HTTP status code from O*NET API
        - api_key_configured: Boolean indicating if API key is set (not the actual key)
        - response_preview: Small preview of API response (if successful)
        - error: Error message (if failed)
        
    Example:
        GET /api/onet/debug
    """
    try:
        result = await onet_service.test_connection()
        return result
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Debug test failed: {str(e)}"
        )


@router.get("/search")
async def search_onet_occupations(
    keyword: str = Query(..., description="Search keyword for occupations", min_length=1)
) -> Dict:
    """
    Search O*NET occupations by keyword.
    
    This endpoint searches the O*NET database for occupations matching the provided keyword.
    O*NET provides official occupation data including skills, tasks, and knowledge requirements.
    
    Args:
        keyword: Search term for occupations (e.g., "cybersecurity", "software engineer")
        
    Returns:
        Dictionary containing:
        - success: Boolean indicating if the search was successful
        - keyword: The search keyword used
        - count: Number of occupations found
        - occupations: List of matching occupations with details
        
    Example:
        GET /api/onet/search?keyword=cybersecurity
    """
    logger.info(f"Local route hit: GET /api/onet/search?keyword={keyword}")
    
    try:
        result = await onet_service.search_occupations(keyword)
        
        # If O*NET returns errors, raise appropriate HTTP exceptions
        if not result.get("success"):
            status_code = result.get("status_code")
            error_detail = result.get("error", "O*NET request failed")
            
            # Authentication errors
            if status_code in [401, 403]:
                raise HTTPException(
                    status_code=status_code,
                    detail=error_detail
                )
            # Invalid/missing parameter
            elif status_code == 422:
                raise HTTPException(
                    status_code=422,
                    detail=error_detail
                )
            # Rate limit exceeded
            elif status_code == 429:
                raise HTTPException(
                    status_code=429,
                    detail=error_detail
                )
            # Other HTTP errors from O*NET
            elif status_code:
                raise HTTPException(
                    status_code=status_code,
                    detail=error_detail
                )
            # Network or other errors (no status code)
            else:
                raise HTTPException(
                    status_code=503,
                    detail=f"O*NET service unavailable: {error_detail}"
                )
        
        return result
        
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error while searching O*NET: {str(e)}"
        )

# Made with Bob
