"""
Resource validation and matching service.
Validates URLs and matches topics to verified resources.
"""

import httpx
import json
import logging
import asyncio
from pathlib import Path
from typing import List, Dict, Any, Optional
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


class ResourceValidator:
    """Validates resource URLs and matches topics to verified resources"""
    
    def __init__(self):
        self.verified_resources = self._load_verified_resources()
        self.validation_cache = {}  # Cache validation results
        
    def _load_verified_resources(self) -> Dict[str, Any]:
        """Load verified resources from JSON file"""
        try:
            resources_path = Path(__file__).parent.parent / 'data' / 'verified_resources.json'
            with open(resources_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load verified resources: {e}")
            return {}
    
    async def validate_url(self, url: str, timeout: float = 3.0) -> Dict[str, Any]:
        """
        Validate a URL by checking if it's reachable.
        
        Returns:
            {
                "valid": bool,
                "status_code": int or None,
                "error": str or None,
                "provider": str
            }
        """
        # Check cache first
        if url in self.validation_cache:
            return self.validation_cache[url]
        
        result = {
            "valid": False,
            "status_code": None,
            "error": None,
            "provider": self._extract_provider(url)
        }
        
        # Skip validation for placeholder URLs
        if url in ['#', '', 'https://example.com']:
            result["error"] = "Placeholder URL"
            self.validation_cache[url] = result
            return result
        
        try:
            async with httpx.AsyncClient(follow_redirects=True) as client:
                response = await client.head(url, timeout=timeout)
                result["status_code"] = response.status_code
                result["valid"] = 200 <= response.status_code < 400
                
                if not result["valid"]:
                    result["error"] = f"HTTP {response.status_code}"
                    
        except httpx.TimeoutException:
            result["error"] = "Timeout"
            logger.warning(f"URL validation timeout: {url}")
        except httpx.HTTPError as e:
            result["error"] = f"HTTP Error: {str(e)}"
            logger.warning(f"URL validation failed: {url} - {e}")
        except Exception as e:
            result["error"] = f"Error: {str(e)}"
            logger.error(f"URL validation error: {url} - {e}")
        
        # Cache the result
        self.validation_cache[url] = result
        return result
    
    def _extract_provider(self, url: str) -> str:
        """Extract provider name from URL"""
        try:
            parsed = urlparse(url)
            hostname = parsed.hostname or ''
            # Remove www. prefix
            hostname = hostname.replace('www.', '')
            # Get domain name
            parts = hostname.split('.')
            if len(parts) >= 2:
                provider = parts[0]
                # Capitalize first letter
                return provider.capitalize()
            return hostname.capitalize()
        except:
            return "Unknown"
    
    def match_verified_resources(
        self,
        career_goal: str,
        topics: List[str],
        max_resources: int = 6
    ) -> List[Dict[str, Any]]:
        """
        Match topics to verified resources from the database.
        
        Args:
            career_goal: Target career (e.g., "Data Analyst")
            topics: List of topics/skills to match
            max_resources: Maximum number of resources to return
            
        Returns:
            List of verified resource dictionaries
        """
        matched_resources = []
        
        # Normalize career goal for matching
        career_key = career_goal.lower().replace(' ', '_')
        
        # Try exact career match first
        if career_key in self.verified_resources:
            career_resources = self.verified_resources[career_key]["resources"]
            matched_resources.extend(career_resources[:max_resources])
            logger.info(f"Matched {len(matched_resources)} resources for career: {career_goal}")
        
        # If we need more resources, search by topics
        if len(matched_resources) < max_resources and topics:
            topic_matches = self._search_by_topics(topics, exclude=matched_resources)
            needed = max_resources - len(matched_resources)
            matched_resources.extend(topic_matches[:needed])
        
        # If still need more, add general resources
        if len(matched_resources) < max_resources:
            general_resources = self.verified_resources.get("general", {}).get("resources", [])
            needed = max_resources - len(matched_resources)
            matched_resources.extend(general_resources[:needed])
        
        # Add source metadata
        for resource in matched_resources:
            resource["source"] = "local_verified"
            resource["urlVerified"] = True
        
        return matched_resources[:max_resources]
    
    def _search_by_topics(
        self,
        topics: List[str],
        exclude: Optional[List[Dict[str, Any]]] = None
    ) -> List[Dict[str, Any]]:
        """Search for resources matching given topics"""
        if exclude is None:
            exclude = []
        
        exclude_urls = {r.get("url") for r in exclude}
        matched = []
        topics_lower = [t.lower() for t in topics]
        
        # Search across all career paths
        for career_data in self.verified_resources.values():
            for resource in career_data.get("resources", []):
                # Skip if already matched
                if resource.get("url") in exclude_urls:
                    continue
                
                # Check if any topic matches
                resource_topics = [t.lower() for t in resource.get("topics", [])]
                if any(topic in resource_topics for topic in topics_lower):
                    matched.append(resource.copy())
        
        return matched
    
    async def validate_and_replace_resources(
        self,
        resources: List[Dict[str, Any]],
        career_goal: str,
        topics: List[str],
        use_parallel: bool = True
    ) -> List[Dict[str, Any]]:
        """
        Validate resource URLs and replace invalid ones with verified alternatives.
        Uses parallel validation for better performance.
        
        Args:
            resources: List of resources to validate
            career_goal: Career goal for finding replacements
            topics: Topics for finding replacements
            use_parallel: Use parallel validation (default: True)
            
        Returns:
            List of validated/replaced resources with metadata
        """
        verified_pool = self.match_verified_resources(career_goal, topics, max_resources=20)
        verified_index = 0
        
        logger.info(f"Validating {len(resources)} resources (parallel={use_parallel})...")
        
        if use_parallel and len(resources) > 1:
            # Parallel validation for better performance
            validation_tasks = [
                self.validate_url(resource.get("url", ""))
                for resource in resources
            ]
            
            try:
                # Run all validations concurrently with timeout
                validations = await asyncio.wait_for(
                    asyncio.gather(*validation_tasks, return_exceptions=True),
                    timeout=10.0  # Max 10 seconds for all validations
                )
            except asyncio.TimeoutError:
                logger.warning("⚠️  Parallel validation timed out, falling back to sequential")
                use_parallel = False
                validations = []
        else:
            validations = []
        
        validated_resources = []
        
        for i, resource in enumerate(resources):
            url = resource.get("url", "")
            
            # Get validation result - ensure it's always a dict
            validation: Dict[str, Any]
            if use_parallel and i < len(validations):
                result = validations[i]
                # Handle exceptions from gather
                if isinstance(result, Exception):
                    logger.warning(f"Validation error for {url}: {result}")
                    validation = {"valid": False, "error": str(result), "provider": "Unknown", "status_code": None}
                elif isinstance(result, dict):
                    validation = result
                else:
                    logger.warning(f"Unexpected validation result type: {type(result)}")
                    validation = {"valid": False, "error": "Invalid result type", "provider": "Unknown", "status_code": None}
            else:
                # Sequential fallback
                validation = await self.validate_url(url)
            
            # Create resource with validation metadata
            validated_resource = resource.copy()
            validated_resource["urlVerified"] = validation.get("valid", False)
            validated_resource["validationStatus"] = validation.get("status_code")
            validated_resource["validationError"] = validation.get("error")
            
            if not validation.get("valid", False):
                # URL is invalid, replace with verified resource
                logger.warning(f"Invalid URL detected: {url} - {validation.get('error')}")
                
                if verified_index < len(verified_pool):
                    replacement = verified_pool[verified_index].copy()
                    verified_index += 1
                    
                    # Keep original title if it's descriptive
                    if resource.get("title") and resource["title"] not in ["Resource 1", "Resource 2"]:
                        replacement["originalTitle"] = resource["title"]
                    
                    replacement["source"] = "local_verified_replacement"
                    replacement["replacedUrl"] = url
                    replacement["replacementReason"] = validation.get("error", "Invalid URL")
                    
                    validated_resource = replacement
                    logger.info(f"Replaced with verified resource: {replacement['title']}")
                else:
                    # No more verified resources, mark as unverified
                    validated_resource["source"] = "watsonx_unverified"
                    logger.warning(f"No verified replacement available for: {url}")
            else:
                # URL is valid
                validated_resource["source"] = "watsonx_verified"
                validated_resource["provider"] = validation.get("provider", "Unknown")
                logger.info(f"URL validated successfully: {url}")
            
            validated_resources.append(validated_resource)
        
        logger.info(f"Validation complete: {len(validated_resources)} resources processed")
        return validated_resources


# Global instance
resource_validator = ResourceValidator()


async def validate_and_replace_resources(
    resources: List[Dict[str, Any]],
    career_goal: str,
    topics: List[str]
) -> List[Dict[str, Any]]:
    """Convenience function for resource validation"""
    return await resource_validator.validate_and_replace_resources(
        resources, career_goal, topics
    )


def get_verified_resources(
    career_goal: str,
    topics: List[str],
    max_resources: int = 6
) -> List[Dict[str, Any]]:
    """Convenience function to get verified resources"""
    return resource_validator.match_verified_resources(
        career_goal, topics, max_resources
    )

# Made with Bob
