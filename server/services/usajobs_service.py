"""
USAJOBS API Integration
Provides access to live federal job postings from USAJOBS.
"""

import os
import httpx
import re
from typing import Dict, List, Optional, Tuple


class UsaJobsService:
    """Service for interacting with USAJOBS Search API"""
    
    BASE_URL = "https://data.usajobs.gov/api/search"
    
    def __init__(self):
        """Initialize USAJOBS service"""
        self._email = None
        self._api_key = None
    
    @property
    def email(self):
        """Lazy load email from environment variables"""
        if self._email is None:
            self._email = os.getenv("USAJOBS_EMAIL")
            if not self._email:
                raise ValueError(
                    "USAJOBS email not found. Please set USAJOBS_EMAIL environment variable."
                )
        return self._email
    
    @property
    def api_key(self):
        """Lazy load API key from environment variables"""
        if self._api_key is None:
            self._api_key = os.getenv("USAJOBS_API_KEY")
            if not self._api_key:
                raise ValueError(
                    "USAJOBS API key not found. Please set USAJOBS_API_KEY environment variable."
                )
        return self._api_key
    
    def _get_headers(self) -> Dict[str, str]:
        """Get required headers for USAJOBS API requests"""
        return {
            "Host": "data.usajobs.gov",
            "User-Agent": self.email,
            "Authorization-Key": self.api_key
        }
    
    def _parse_location(self, location: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Parse location string to extract city and state.
        
        Args:
            location: Location string (e.g., "Orlando", "Florida", "Orlando, FL")
            
        Returns:
            Tuple of (city, state) where either can be None
        """
        if not location:
            return None, None
        
        location = location.strip()
        
        # Common US state abbreviations and full names
        us_states = {
            'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
            'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
            'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
            'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
            'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY',
            'DC', 'ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
            'COLORADO', 'CONNECTICUT', 'DELAWARE', 'FLORIDA', 'GEORGIA',
            'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS',
            'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS',
            'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA',
            'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO',
            'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA',
            'OREGON', 'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA',
            'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT',
            'VIRGINIA', 'WASHINGTON', 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING',
            'DISTRICT OF COLUMBIA'
        }
        
        # Check if location contains comma (e.g., "Orlando, FL")
        if ',' in location:
            parts = [p.strip() for p in location.split(',')]
            if len(parts) == 2:
                city, state = parts
                if state.upper() in us_states:
                    return city, state
                return city, None
        
        # Check if it's just a state
        if location.upper() in us_states:
            return None, location
        
        # Otherwise, assume it's a city
        return location, None
    
    async def _perform_search(self, keyword: str, location: Optional[str] = None) -> Dict:
        """
        Perform a single USAJOBS search.
        
        Args:
            keyword: Search term for jobs
            location: Optional location filter
            
        Returns:
            Dictionary containing search results
        """
        params = {
            "Keyword": keyword.strip(),
            "ResultsPerPage": 25
        }
        
        if location and location.strip():
            params["LocationName"] = location.strip()
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.BASE_URL,
                params=params,
                headers=self._get_headers(),
                timeout=30.0
            )
            response.raise_for_status()
            
            data = response.json()
            
            # Extract search result info
            search_result = data.get("SearchResult", {})
            search_result_count = search_result.get("SearchResultCount", 0)
            search_result_items = search_result.get("SearchResultItems", [])
            
            # Clean and format job results
            jobs = []
            for item in search_result_items:
                matched_object_descriptor = item.get("MatchedObjectDescriptor", {})
                
                # Extract position details
                position_title = matched_object_descriptor.get("PositionTitle", "N/A")
                organization_name = matched_object_descriptor.get("OrganizationName", "N/A")
                
                # Extract location info
                position_location = matched_object_descriptor.get("PositionLocation", [{}])
                location_name = "N/A"
                if position_location and len(position_location) > 0:
                    first_location = position_location[0]
                    city = first_location.get("CityName", "")
                    state = first_location.get("StateCode", "")
                    location_name = f"{city}, {state}" if city and state else (city or state or "N/A")
                
                # Extract URL
                position_uri = matched_object_descriptor.get("PositionURI", "")
                
                # Extract salary info
                position_remuneration = matched_object_descriptor.get("PositionRemuneration", [{}])
                min_salary = None
                max_salary = None
                if position_remuneration and len(position_remuneration) > 0:
                    first_remuneration = position_remuneration[0]
                    min_salary = first_remuneration.get("MinimumRange")
                    max_salary = first_remuneration.get("MaximumRange")
                
                # Extract summary
                user_area = matched_object_descriptor.get("UserArea", {})
                brief_summary = user_area.get("Details", {}).get("JobSummary", "")
                
                job = {
                    "title": position_title,
                    "organization": organization_name,
                    "location": location_name,
                    "url": position_uri,
                    "minimumSalary": min_salary,
                    "maximumSalary": max_salary,
                    "summary": brief_summary[:500] if brief_summary else None
                }
                
                jobs.append(job)
            
            return {
                "count": search_result_count,
                "jobs": jobs
            }
    
    async def search_jobs(self, keyword: str, location: Optional[str] = None) -> Dict:
        """
        Search USAJOBS with fallback logic: city → state → nationwide.
        
        Args:
            keyword: Search term for jobs
            location: Optional location filter (city, state, or zip code)
            
        Returns:
            Dictionary containing:
            - success: Boolean
            - keyword: Search keyword
            - originalLocation: Original location searched
            - searchLevel: "city", "state", or "nationwide"
            - locationUsed: Actual location used for results
            - count: Number of jobs found
            - jobs: List of job postings
            - fallbackMessage: Optional message if fallback was used
        """
        if not keyword or not keyword.strip():
            raise ValueError("Keyword cannot be empty")
        
        original_location = location
        
        try:
            # Try city search first if location provided
            if location and location.strip():
                city, state = self._parse_location(location)
                
                # Level 1: Try exact location (city or full location string)
                result = await self._perform_search(keyword, location)
                
                if result["count"] > 0:
                    return {
                        "success": True,
                        "keyword": keyword,
                        "originalLocation": original_location,
                        "searchLevel": "city" if city else "state",
                        "locationUsed": location,
                        "count": result["count"],
                        "jobs": result["jobs"]
                    }
                
                # Level 2: If city search returned 0 and we have a state, try state
                if city and state:
                    result = await self._perform_search(keyword, state)
                    
                    if result["count"] > 0:
                        return {
                            "success": True,
                            "keyword": keyword,
                            "originalLocation": original_location,
                            "searchLevel": "state",
                            "locationUsed": state,
                            "count": result["count"],
                            "jobs": result["jobs"],
                            "fallbackMessage": f"No exact {city} matches found, showing {state} results instead."
                        }
                
                # Level 3: Try nationwide if both city and state returned 0
                result = await self._perform_search(keyword, None)
                
                if result["count"] > 0:
                    location_desc = city if city else location
                    return {
                        "success": True,
                        "keyword": keyword,
                        "originalLocation": original_location,
                        "searchLevel": "nationwide",
                        "locationUsed": None,
                        "count": result["count"],
                        "jobs": result["jobs"],
                        "fallbackMessage": f"No {location_desc} matches found, showing nationwide results instead."
                    }
                
                # No results at any level
                return {
                    "success": True,
                    "keyword": keyword,
                    "originalLocation": original_location,
                    "searchLevel": "nationwide",
                    "locationUsed": None,
                    "count": 0,
                    "jobs": []
                }
            
            # No location provided - search nationwide
            result = await self._perform_search(keyword, None)
            
            return {
                "success": True,
                "keyword": keyword,
                "originalLocation": None,
                "searchLevel": "nationwide",
                "locationUsed": None,
                "count": result["count"],
                "jobs": result["jobs"]
            }
                
        except httpx.HTTPStatusError as e:
            error_msg = f"USAJOBS API request failed with status {e.response.status_code}"
            if e.response.status_code == 401:
                error_msg = "USAJOBS authentication failed. Please check your API key and email."
            elif e.response.status_code == 403:
                error_msg = "USAJOBS API access forbidden. Please verify your credentials."
            elif e.response.status_code == 404:
                error_msg = "USAJOBS API endpoint not found."
            
            return {
                "success": False,
                "error": error_msg,
                "keyword": keyword,
                "location": location,
                "count": 0,
                "jobs": []
            }
            
        except httpx.RequestError as e:
            return {
                "success": False,
                "error": f"USAJOBS API request error: {str(e)}",
                "keyword": keyword,
                "location": location,
                "count": 0,
                "jobs": []
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Unexpected error: {str(e)}",
                "keyword": keyword,
                "location": location,
                "count": 0,
                "jobs": []
            }


# Create a singleton instance
usajobs_service = UsaJobsService()

# Made with Bob
