"""
O*NET Web Services Integration
Provides access to official occupation, skills, and task data from O*NET.
"""

import os
import httpx
import logging
from typing import Dict, List, Optional

# Set up logging
logger = logging.getLogger(__name__)


class OnetService:
    """Service for interacting with O*NET Web Services API"""
    
    # Use the v2 API (api-v2.onetcenter.org)
    BASE_URL = "https://api-v2.onetcenter.org"
    ABOUT_URL = "https://api-v2.onetcenter.org/about/"
    SEARCH_URL = "https://api-v2.onetcenter.org/online/search"
    
    def __init__(self):
        """Initialize O*NET service"""
        self._api_key = None
    
    @property
    def api_key(self):
        """Lazy load API key from environment variables"""
        if self._api_key is None:
            self._api_key = os.getenv("ONET_API_KEY")
            if not self._api_key:
                raise ValueError(
                    "O*NET API key not found. Please set ONET_API_KEY environment variable."
                )
        return self._api_key
    
    def _get_headers(self) -> Dict[str, str]:
        """Get required headers for O*NET API requests"""
        return {
            "X-API-Key": self.api_key,
            "Accept": "application/json"
        }
    
    async def test_connection(self) -> Dict:
        """
        Test O*NET API connection using the /about/ endpoint.
        
        Returns:
            Dictionary with connection test results (no API key exposed)
        """
        api_key_loaded = bool(self._api_key or os.getenv("ONET_API_KEY"))
        
        logger.info(f"Testing O*NET connection to: {self.ABOUT_URL}")
        logger.info(f"API key loaded: {api_key_loaded}")
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    self.ABOUT_URL,
                    headers=self._get_headers(),
                    timeout=30.0
                )
                
                logger.info(f"O*NET /about/ response status: {response.status_code}")
                
                # Try to parse JSON response
                try:
                    data = response.json()
                    logger.info(f"O*NET response preview: {str(data)[:200]}")
                except Exception as json_err:
                    logger.warning(f"Could not parse O*NET response as JSON: {json_err}")
                    data = {}
                
                return {
                    "success": response.status_code == 200,
                    "upstreamStatus": response.status_code,
                    "keyLoaded": api_key_loaded,
                    "responsePreview": {
                        "api_version": data.get("api_version", "N/A"),
                        "api_title": data.get("api_title", "N/A")
                    } if data else {"raw": response.text[:200]}
                }
                
        except httpx.HTTPStatusError as e:
            logger.error(f"O*NET HTTP error: {e.response.status_code}")
            return {
                "success": False,
                "upstreamStatus": e.response.status_code,
                "keyLoaded": api_key_loaded,
                "error": f"HTTP error: {e.response.status_code}"
            }
        except httpx.RequestError as e:
            logger.error(f"O*NET request error: {str(e)}")
            return {
                "success": False,
                "upstreamStatus": None,
                "keyLoaded": api_key_loaded,
                "error": f"Request error: {str(e)}"
            }
        except Exception as e:
            logger.error(f"O*NET unexpected error: {str(e)}")
            return {
                "success": False,
                "upstreamStatus": None,
                "keyLoaded": api_key_loaded,
                "error": f"Unexpected error: {str(e)}"
            }
    
    async def search_occupations(self, keyword: str) -> Dict:
        """
        Search O*NET occupations based on a keyword.
        
        Args:
            keyword: Search term for occupations
            
        Returns:
            Dictionary containing search results with occupation data
            
        Raises:
            ValueError: If keyword is empty
        """
        if not keyword or not keyword.strip():
            raise ValueError("Keyword cannot be empty")
        
        # O*NET search endpoint - use v2 API
        url = self.SEARCH_URL
        
        params = {
            "keyword": keyword.strip(),
            "start": 1,
            "end": 10
        }
        
        api_key_exists = bool(os.getenv("ONET_API_KEY"))
        
        logger.info("=" * 60)
        logger.info("O*NET SEARCH REQUEST")
        logger.info(f"Upstream URL: {url}")
        logger.info(f"Search params: {params}")
        logger.info(f"ONET_API_KEY exists: {api_key_exists}")
        logger.info("=" * 60)
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    url,
                    params=params,
                    headers=self._get_headers(),
                    timeout=30.0
                )
                
                logger.info(f"Upstream status code: {response.status_code}")
                
                # Log first 300 characters of response body
                try:
                    response_text = response.text[:300]
                    logger.info(f"Response body (first 300 chars): {response_text}")
                except Exception as e:
                    logger.warning(f"Could not log response body: {e}")
                
                # Log exact URL for 404 debugging
                if response.status_code == 404:
                    logger.error(f"O*NET 404 - Exact URL called: {response.url}")
                    logger.error(f"O*NET 404 - Request headers (no key): X-API-Key: [REDACTED], Accept: application/json")
                
                # Check for authentication errors
                if response.status_code in [401, 403]:
                    error_msg = "O*NET authentication failed. Please check your API key."
                    logger.error(f"{error_msg} Status: {response.status_code}")
                    return {
                        "success": False,
                        "error": error_msg,
                        "upstreamStatus": response.status_code,
                        "keyword": keyword,
                        "count": 0,
                        "occupations": []
                    }
                
                # Check for invalid/missing parameter
                if response.status_code == 422:
                    error_msg = "Invalid or missing parameter in O*NET request."
                    logger.error(f"{error_msg} Status: {response.status_code}")
                    return {
                        "success": False,
                        "error": error_msg,
                        "upstreamStatus": response.status_code,
                        "keyword": keyword,
                        "count": 0,
                        "occupations": []
                    }
                
                # Check for rate limiting
                if response.status_code == 429:
                    error_msg = "O*NET rate limit exceeded. Please retry later."
                    logger.error(f"{error_msg} Status: {response.status_code}")
                    return {
                        "success": False,
                        "error": error_msg,
                        "upstreamStatus": response.status_code,
                        "keyword": keyword,
                        "count": 0,
                        "occupations": []
                    }
                
                # Raise for other HTTP errors
                response.raise_for_status()
                
                data = response.json()
                
                # Check if results exist
                if not data or "occupation" not in data:
                    logger.info("O*NET returned no occupations")
                    return {
                        "success": True,
                        "keyword": keyword,
                        "upstreamStatus": response.status_code,
                        "rawTotal": data.get("total", 0) if data else 0,
                        "count": 0,
                        "occupations": []
                    }
                
                occupations = data.get("occupation", [])
                
                # Ensure occupations is a list
                if not isinstance(occupations, list):
                    occupations = [occupations] if occupations else []
                
                # Extract required fields from each occupation
                formatted_occupations = []
                for occ in occupations:
                    formatted_occupations.append({
                        "title": occ.get("title", ""),
                        "code": occ.get("code", ""),
                        "href": occ.get("href", ""),
                        "brightOutlook": occ.get("tags", {}).get("bright_outlook", False) if isinstance(occ.get("tags"), dict) else False
                    })
                
                logger.info(f"O*NET returned {len(formatted_occupations)} occupations")
                
                return {
                    "success": True,
                    "keyword": keyword,
                    "upstreamStatus": response.status_code,
                    "rawTotal": data.get("total", len(formatted_occupations)),
                    "count": len(formatted_occupations),
                    "occupations": formatted_occupations
                }
                
        except httpx.HTTPStatusError as e:
            logger.error(f"O*NET HTTP error: {e.response.status_code}")
            logger.error(f"O*NET error - Exact URL: {e.response.url}")
            error_msg = f"O*NET API request failed with status {e.response.status_code}"
            if e.response.status_code == 401:
                error_msg = "O*NET authentication failed. Please check your API key."
            elif e.response.status_code == 403:
                error_msg = "O*NET access forbidden. Please verify your API key."
            elif e.response.status_code == 404:
                error_msg = "O*NET API endpoint not found."
            elif e.response.status_code == 422:
                error_msg = "Invalid or missing parameter in O*NET request."
            elif e.response.status_code == 429:
                error_msg = "O*NET rate limit exceeded. Please retry later."
            
            return {
                "success": False,
                "error": error_msg,
                "upstreamStatus": e.response.status_code,
                "keyword": keyword,
                "count": 0,
                "occupations": []
            }
            
        except httpx.RequestError as e:
            logger.error(f"O*NET request error: {str(e)}")
            return {
                "success": False,
                "error": f"O*NET API request error: {str(e)}",
                "keyword": keyword,
                "count": 0,
                "occupations": []
            }
        except Exception as e:
            logger.error(f"O*NET unexpected error: {str(e)}")
            return {
                "success": False,
                "error": f"Unexpected error: {str(e)}",
                "keyword": keyword,
                "count": 0,
                "occupations": []
            }


# Create a singleton instance
onet_service = OnetService()

# Made with Bob
