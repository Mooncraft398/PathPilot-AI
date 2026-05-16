"""
Project Validator Service
Validates GitHub project links and provides verified fallback projects.
"""

import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)


class ProjectValidator:
    """Validates and manages project links for career roadmaps"""
    
    def __init__(self):
        """Initialize with verified projects database"""
        self.verified_projects = self._load_verified_projects()
        logger.info(f"✅ Loaded {sum(len(projects) for projects in self.verified_projects.values())} verified projects")
    
    def _load_verified_projects(self) -> Dict[str, List[Dict[str, Any]]]:
        """Load verified projects from JSON file"""
        try:
            projects_path = Path(__file__).parent.parent / 'data' / 'verified_projects.json'
            with open(projects_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load verified projects: {e}")
            return {}
    
    def _normalize_career_path(self, career_goal: str) -> str:
        """Normalize career goal to match database keys"""
        career_lower = career_goal.lower().strip()
        
        # Direct mappings
        mappings = {
            'data analyst': 'data_analyst',
            'soc analyst': 'soc_analyst',
            'security analyst': 'soc_analyst',
            'cybersecurity analyst': 'soc_analyst',
            'software developer': 'software_developer',
            'software engineer': 'software_developer',
            'full stack developer': 'software_developer',
            'cloud engineer': 'cloud_engineer',
            'devops engineer': 'cloud_engineer',
            'it help desk': 'it_help_desk',
            'help desk': 'it_help_desk',
            'it support': 'it_help_desk',
            'web developer': 'web_developer',
            'frontend developer': 'web_developer',
            'backend developer': 'software_developer',
            'cybersecurity': 'cybersecurity',
            'security engineer': 'cybersecurity',
            'penetration tester': 'cybersecurity',
            'ai engineer': 'ai_ml_engineer',
            'ml engineer': 'ai_ml_engineer',
            'machine learning engineer': 'ai_ml_engineer',
            'data scientist': 'ai_ml_engineer'
        }
        
        # Check direct mappings
        if career_lower in mappings:
            return mappings[career_lower]
        
        # Check partial matches
        for key, value in mappings.items():
            if key in career_lower or career_lower in key:
                return value
        
        return 'general'
    
    def get_verified_projects(
        self,
        career_goal: str,
        skills: Optional[List[str]] = None,
        difficulty: Optional[str] = None,
        max_projects: int = 3
    ) -> List[Dict[str, Any]]:
        """
        Get verified projects for a career path
        
        Args:
            career_goal: Target career role
            skills: Optional list of skills to match
            difficulty: Optional difficulty filter (beginner, intermediate, advanced)
            max_projects: Maximum number of projects to return
        
        Returns:
            List of verified project dictionaries
        """
        career_path = self._normalize_career_path(career_goal)
        
        logger.info(f"🔍 Getting verified projects for: {career_goal} -> {career_path}")
        
        # Get projects for career path
        projects = self.verified_projects.get(career_path, [])
        
        # If no specific projects, use general projects
        if not projects:
            logger.warning(f"No projects found for {career_path}, using general projects")
            projects = self.verified_projects.get('general', [])
        
        # Filter by difficulty if specified
        if difficulty:
            projects = [p for p in projects if p.get('difficulty', '').lower() == difficulty.lower()]
        
        # Score projects by skill match if skills provided
        if skills:
            scored_projects = []
            for project in projects:
                project_skills = [s.lower() for s in project.get('skills', [])]
                user_skills = [s.lower() for s in skills]
                
                # Count matching skills
                matches = sum(1 for skill in user_skills if any(skill in ps or ps in skill for ps in project_skills))
                scored_projects.append((matches, project))
            
            # Sort by match score (descending)
            scored_projects.sort(key=lambda x: x[0], reverse=True)
            projects = [p for _, p in scored_projects]
        
        # Return top N projects
        result = projects[:max_projects]
        
        logger.info(f"✅ Returning {len(result)} verified projects for {career_goal}")
        for i, project in enumerate(result, 1):
            logger.info(f"   {i}. {project['title']} ({project['difficulty']}) - {project['url']}")
        
        return result
    
    def merge_github_and_verified_projects(
        self,
        github_projects: List[Dict[str, Any]],
        career_goal: str,
        skills: Optional[List[str]] = None,
        min_projects: int = 3
    ) -> List[Dict[str, Any]]:
        """
        Merge GitHub API projects with verified projects
        
        Args:
            github_projects: Projects from GitHub API
            career_goal: Target career role
            skills: Optional list of skills
            min_projects: Minimum number of projects to return
        
        Returns:
            Combined list of projects with source metadata
        """
        logger.info(f"🔀 Merging GitHub projects with verified projects")
        logger.info(f"   GitHub projects: {len(github_projects)}")
        
        # Add source metadata to GitHub projects
        github_with_source = []
        for project in github_projects:
            project_copy = project.copy()
            project_copy['source'] = 'github_api'
            project_copy['verified'] = False
            github_with_source.append(project_copy)
        
        # If we have enough GitHub projects, return them
        if len(github_with_source) >= min_projects:
            logger.info(f"✅ Using {len(github_with_source)} GitHub API projects")
            return github_with_source
        
        # Otherwise, supplement with verified projects
        needed = min_projects - len(github_with_source)
        logger.info(f"⚠️  Only {len(github_with_source)} GitHub projects, need {needed} more")
        
        verified = self.get_verified_projects(
            career_goal=career_goal,
            skills=skills,
            max_projects=needed
        )
        
        # Add source metadata to verified projects
        verified_with_source = []
        for project in verified:
            project_copy = project.copy()
            project_copy['source'] = 'local_verified'
            project_copy['name'] = project.get('title', 'Project')
            project_copy['description'] = project.get('description', '')
            project_copy['stars'] = project.get('stars', 0)
            project_copy['language'] = project.get('language', 'Unknown')
            verified_with_source.append(project_copy)
        
        # Combine GitHub and verified projects
        combined = github_with_source + verified_with_source
        
        logger.info(f"✅ Combined projects: {len(combined)} total")
        logger.info(f"   - GitHub API: {len(github_with_source)}")
        logger.info(f"   - Verified local: {len(verified_with_source)}")
        
        return combined
    
    def ensure_project_has_url(self, project: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ensure project has a valid URL field
        
        Args:
            project: Project dictionary
        
        Returns:
            Project with guaranteed url field
        """
        # Check various possible URL fields
        url = (
            project.get('url') or
            project.get('link') or
            project.get('html_url') or
            project.get('githubUrl') or
            project.get('github_url') or
            project.get('repoUrl') or
            project.get('repo_url') or
            ''
        )
        
        # Normalize to 'url' field
        project['url'] = url
        
        # Add metadata about URL availability
        project['hasUrl'] = bool(url and url != '#')
        
        return project


# Global instance
project_validator = ProjectValidator()

# Made with Bob
