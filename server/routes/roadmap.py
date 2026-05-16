from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import json
import os
from services.watsonx_service import generate_roadmap_with_ai
from services.github_service import search_github_projects
from services.resource_validator import resource_validator
from services.project_validator import project_validator
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["roadmap"])


class RoadmapRequest(BaseModel):
    """Request model for AI-powered roadmap generation"""
    careerGoal: str = Field(..., description="Target career role (e.g., 'SOC Analyst')")
    currentSkills: List[str] = Field(default=[], description="List of current skills")
    timeframe: str = Field(..., description="Available timeframe (e.g., '3 months', '6 months')")


class RoadmapResponse(BaseModel):
    """Response model for generated roadmap"""
    success: bool
    careerGoal: str
    roadmap: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


def load_json_file(filepath: str) -> Any:
    """Load and parse a JSON file"""
    try:
        full_path = os.path.join(os.path.dirname(__file__), "..", "data", filepath)
        with open(full_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning(f"File not found: {filepath}")
        return None
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON from {filepath}: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Error loading {filepath}: {str(e)}")
        return None


def match_role_data(career_goal: str) -> Optional[Dict[str, Any]]:
    """Match career goal to role data"""
    roles = load_json_file("roles.json")
    if not roles:
        return None
    
    career_goal_lower = career_goal.lower()
    
    # Try exact match first
    for role in roles:
        if role.get("title", "").lower() == career_goal_lower:
            return role
    
    # Try partial match
    for role in roles:
        title = role.get("title", "").lower()
        if career_goal_lower in title or title in career_goal_lower:
            return role
    
    # Try matching by keywords
    for role in roles:
        keywords = role.get("beginnerKeywords", [])
        for keyword in keywords:
            if keyword.lower() in career_goal_lower:
                return role
    
    return None


def get_resources_for_skills(skills: List[str]) -> Dict[str, Any]:
    """Get learning resources for given skills"""
    all_resources = load_json_file("resources.json")
    if not all_resources:
        return {"resources": []}
    
    matched_resources = []
    
    for skill in skills:
        skill_lower = skill.lower()
        for resource_group in all_resources:
            if skill_lower in resource_group.get("skill", "").lower():
                resources = resource_group.get("resources", [])
                matched_resources.extend(resources[:3])  # Top 3 per skill
                break
    
    return {"resources": matched_resources}


def get_projects_for_skills(skills: List[str]) -> List[Dict[str, Any]]:
    """Get project ideas for given skills"""
    all_projects = load_json_file("projects.json")
    if not all_projects:
        return []
    
    matched_projects = []
    
    for skill in skills:
        skill_lower = skill.lower()
        for project_group in all_projects:
            if skill_lower in project_group.get("skill", "").lower():
                projects = project_group.get("projects", [])
                matched_projects.extend(projects[:2])  # Top 2 per skill
                break
    
    return matched_projects


def get_certifications_for_role(role_title: str) -> List[Dict[str, Any]]:
    """Get certification recommendations for a role"""
    all_certs = load_json_file("certifications.json")
    if not all_certs:
        return []
    
    role_lower = role_title.lower()
    
    for cert_group in all_certs:
        if role_lower in cert_group.get("role", "").lower():
            return cert_group.get("certifications", [])
    
    return []


async def search_github_for_role(career_goal: str, role_data: Optional[Dict[str, Any]], skills: List[str] = []) -> List[Dict[str, Any]]:
    """
    Search GitHub for relevant beginner projects and merge with verified projects
    
    Args:
        career_goal: Target career role
        role_data: Optional role data with keywords
        skills: List of skills for matching
    
    Returns:
        List of project dictionaries with URLs and metadata
    """
    logger.info("=" * 80)
    logger.info("🐙 GITHUB PROJECT SEARCH")
    logger.info("=" * 80)
    logger.info(f"Career Goal: {career_goal}")
    logger.info(f"Skills: {skills}")
    
    try:
        # Use role keywords if available
        if role_data and role_data.get("beginnerKeywords"):
            search_query = " ".join(role_data["beginnerKeywords"][:2])
        else:
            search_query = career_goal
        
        logger.info(f"Search Query: {search_query}")
        
        result = await search_github_projects(search_query)
        
        # Check if result is an error response
        from models.schemas import ErrorResponse, GitHubProjectsResponse
        
        if isinstance(result, ErrorResponse):
            logger.warning(f"❌ GitHub search failed: {result.error}")
            logger.warning(f"   Will use verified local projects instead")
            github_projects = []
        elif isinstance(result, GitHubProjectsResponse):
            github_projects = []
            for repo in result.repositories[:5]:
                github_projects.append({
                    "name": repo.name,
                    "description": repo.description or "No description",
                    "stars": repo.stars,
                    "language": repo.language or "Unknown",
                    "url": repo.url
                })
            logger.info(f"✅ Found {len(github_projects)} GitHub projects")
        else:
            logger.warning(f"⚠️  Unexpected result type from GitHub API")
            github_projects = []
        
        # Merge with verified projects to ensure minimum count
        merged_projects = project_validator.merge_github_and_verified_projects(
            github_projects=github_projects,
            career_goal=career_goal,
            skills=skills,
            min_projects=3
        )
        
        # Ensure all projects have URL field
        final_projects = [project_validator.ensure_project_has_url(p) for p in merged_projects]
        
        logger.info(f"✅ Final project count: {len(final_projects)}")
        for i, project in enumerate(final_projects, 1):
            source = project.get('source', 'unknown')
            has_url = project.get('hasUrl', False)
            logger.info(f"   {i}. {project.get('name', 'Unknown')} (source: {source}, has_url: {has_url})")
        
        logger.info("=" * 80)
        
        return final_projects
    
    except Exception as e:
        logger.error(f"Error searching GitHub: {str(e)}")
        return []


def create_fallback_roadmap(
    career_goal: str,
    current_skills: List[str],
    timeframe: str,
    role_data: Optional[Dict[str, Any]],
    local_resources: Dict[str, Any],
    github_projects: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """Create a fallback roadmap if watsonx.ai fails"""
    
    skills_to_learn = role_data.get("coreSkills", ["Problem Solving", "Communication"]) if role_data else []
    tools = role_data.get("tools", []) if role_data else []
    
    return {
        "summary": f"A practical {timeframe} roadmap to become a {career_goal}. This plan focuses on building essential skills through hands-on projects and real-world practice.",
        "phases": [
            {
                "phase": 1,
                "title": "Foundation & Setup",
                "duration": "Weeks 1-4",
                "focus": "Learn the basics and set up your learning environment",
                "skills": skills_to_learn[:2] if len(skills_to_learn) >= 2 else skills_to_learn
            },
            {
                "phase": 2,
                "title": "Core Skills Development",
                "duration": "Weeks 5-8",
                "focus": "Build practical skills through projects",
                "skills": skills_to_learn[2:4] if len(skills_to_learn) >= 4 else skills_to_learn
            },
            {
                "phase": 3,
                "title": "Portfolio & Job Prep",
                "duration": "Weeks 9-12",
                "focus": "Create portfolio projects and prepare for job applications",
                "skills": ["Portfolio Development", "Resume Writing", "Interview Prep"]
            }
        ],
        "skills": skills_to_learn,
        "tools": tools,
        "resources": local_resources.get("resources", [])[:10],
        "githubProjects": github_projects,
        "portfolioProjects": [
            {
                "title": f"Beginner {career_goal} Project",
                "description": "Build a practical project demonstrating your skills",
                "skills": skills_to_learn[:3]
            },
            {
                "title": f"Intermediate {career_goal} Project",
                "description": "Create a more complex project for your portfolio",
                "skills": skills_to_learn
            }
        ],
        "resumeBullets": [
            f"Developed hands-on skills in {', '.join(skills_to_learn[:3])}",
            f"Completed {timeframe} intensive training program in {career_goal}",
            f"Built portfolio projects demonstrating practical application of {skills_to_learn[0] if skills_to_learn else 'core skills'}",
            f"Gained experience with industry tools including {', '.join(tools[:3])}",
            "Actively learning and applying best practices in the field"
        ],
        "weeklyPlan": [
            {
                "week": 1,
                "focus": f"Environment Setup & {skills_to_learn[0] if skills_to_learn else 'Fundamentals'}",
                "topics": [f"Setting up {tools[0] if tools else 'development environment'}", "Basic concepts", "First exercises"],
                "dailyTasks": [
                    f"Install and configure {tools[0] if tools else 'required tools'}",
                    f"Learn basics of {skills_to_learn[0] if skills_to_learn else 'core concepts'}",
                    "Complete beginner tutorials",
                    "Join online communities",
                    "Set up learning schedule"
                ]
            },
            {
                "week": 2,
                "focus": f"Core {skills_to_learn[1] if len(skills_to_learn) > 1 else 'Concepts'} & Practice",
                "topics": [f"{skills_to_learn[1] if len(skills_to_learn) > 1 else 'Core concepts'}", "Hands-on exercises", "Problem solving"],
                "dailyTasks": [
                    f"Deep dive into {skills_to_learn[1] if len(skills_to_learn) > 1 else 'fundamentals'}",
                    "Complete coding challenges",
                    "Build mini-projects",
                    "Review and debug code",
                    "Document your learning"
                ]
            },
            {
                "week": 3,
                "focus": f"Advanced {skills_to_learn[2] if len(skills_to_learn) > 2 else 'Topics'} & First Project",
                "topics": [f"{skills_to_learn[2] if len(skills_to_learn) > 2 else 'Advanced concepts'}", "Project planning", "Best practices"],
                "dailyTasks": [
                    f"Learn {skills_to_learn[2] if len(skills_to_learn) > 2 else 'advanced techniques'}",
                    "Plan your first portfolio project",
                    "Start project implementation",
                    "Apply best practices",
                    "Seek feedback from community"
                ]
            },
            {
                "week": 4,
                "focus": f"Mastering {tools[1] if len(tools) > 1 else 'Tools'} & Project Development",
                "topics": [f"{tools[1] if len(tools) > 1 else 'Professional tools'}", "Version control", "Testing"],
                "dailyTasks": [
                    f"Practice with {tools[1] if len(tools) > 1 else 'industry tools'}",
                    "Continue project development",
                    "Implement testing",
                    "Refactor and optimize code",
                    "Update project documentation"
                ]
            },
            {
                "week": 5,
                "focus": "Portfolio Project Completion & Second Project",
                "topics": ["Project finalization", "Code review", "New project planning"],
                "dailyTasks": [
                    "Complete first portfolio project",
                    "Write comprehensive README",
                    "Plan second portfolio project",
                    "Start second project",
                    "Create project presentation"
                ]
            },
            {
                "week": 6,
                "focus": f"Specialization in {career_goal} & Advanced Projects",
                "topics": [f"{career_goal} specific skills", "Industry standards", "Advanced techniques"],
                "dailyTasks": [
                    f"Study {career_goal} best practices",
                    "Work on specialized project",
                    "Learn industry tools",
                    "Network with professionals",
                    "Attend virtual meetups"
                ]
            },
            {
                "week": 7,
                "focus": "Professional Branding & Portfolio Website",
                "topics": ["Resume writing", "LinkedIn optimization", "Portfolio website"],
                "dailyTasks": [
                    "Create professional resume",
                    "Optimize LinkedIn profile",
                    "Build portfolio website",
                    "Showcase your projects",
                    "Get feedback on materials"
                ]
            },
            {
                "week": 8,
                "focus": "Job Search & Interview Preparation",
                "topics": ["Interview prep", "Technical questions", "Job applications"],
                "dailyTasks": [
                    "Practice technical interviews",
                    "Research target companies",
                    "Apply to positions",
                    "Prepare for behavioral questions",
                    "Mock interviews with peers"
                ]
            }
        ],
        "nextSteps": [
            f"Start with the first recommended resource for {skills_to_learn[0] if skills_to_learn else 'your chosen skill'}",
            "Set up your development environment and tools",
            "Join relevant online communities and forums",
            "Create a GitHub account and start documenting your learning",
            "Dedicate consistent time each day to learning and practice",
            "Build your first small project within the first 2 weeks",
            "Connect with others in the field on LinkedIn"
        ]
    }


@router.post("/generate-roadmap", response_model=RoadmapResponse)
async def generate_roadmap(request: RoadmapRequest):
    """
    Generate an AI-powered career roadmap using IBM watsonx.ai.
    
    This endpoint:
    1. Loads curated resources from local JSON files
    2. Matches resources related to the career goal
    3. Searches GitHub for relevant beginner-friendly projects
    4. Builds a structured prompt for IBM watsonx.ai
    5. Calls watsonx.ai to generate a personalized roadmap
    6. Returns a structured AI-generated roadmap
    
    Security: All API keys are stored in environment variables and never exposed to the frontend.
    """
    try:
        # Validate input
        if not request.careerGoal or not request.careerGoal.strip():
            raise HTTPException(status_code=400, detail="Career goal is required")
        
        if not request.timeframe or not request.timeframe.strip():
            raise HTTPException(status_code=400, detail="Timeframe is required")
        
        logger.info(f"Generating roadmap for: {request.careerGoal}")
        
        # Step 1: Match role data
        role_data = match_role_data(request.careerGoal)
        
        # Step 2: Get skills to learn
        if role_data:
            skills_to_learn = role_data.get("coreSkills", [])
        else:
            # Use current skills as a base if no role match
            skills_to_learn = request.currentSkills if request.currentSkills else ["Problem Solving"]
        
        # Step 3: Load local resources
        local_resources = get_resources_for_skills(skills_to_learn)
        
        # Step 4: Search GitHub for projects (non-blocking, can fail gracefully)
        github_projects = await search_github_for_role(request.careerGoal, role_data, skills_to_learn)
        
        # Step 5: Get certifications
        certifications = get_certifications_for_role(request.careerGoal)
        
        # Step 6: Call watsonx.ai to generate roadmap
        logger.info("=" * 80)
        logger.info("🤖 ATTEMPTING WATSONX.AI ROADMAP GENERATION")
        logger.info("=" * 80)
        logger.info(f"Career Goal: {request.careerGoal}")
        logger.info(f"Timeframe: {request.timeframe}")
        logger.info(f"Current Skills: {request.currentSkills}")
        
        ai_roadmap = await generate_roadmap_with_ai(
            career_goal=request.careerGoal,
            current_skills=request.currentSkills,
            timeframe=request.timeframe,
            local_resources=local_resources,
            github_projects=github_projects
        )
        
        # Step 7: Handle AI response or create fallback
        if ai_roadmap:
            logger.info("=" * 80)
            logger.info("✅ SUCCESS: WATSONX.AI GENERATED ROADMAP")
            logger.info("=" * 80)
            logger.info(f"Model: {ai_roadmap.get('metadata', {}).get('model', 'unknown')}")
            logger.info(f"Tokens: {ai_roadmap.get('metadata', {}).get('tokens', 0)}")
            logger.info(f"Phases: {len(ai_roadmap.get('phases', []))}")
            logger.info(f"Weekly Plans: {len(ai_roadmap.get('weeklyPlan', []))}")
            logger.info("=" * 80)
            roadmap = ai_roadmap
            
            # Step 7a: Validate and replace resources
            logger.info("🔗 Validating resource URLs...")
            resources = roadmap.get("resources", [])
            if resources:
                topics = roadmap.get("skills", []) + roadmap.get("tools", [])
                validated_resources = await resource_validator.validate_and_replace_resources(
                    resources=resources,
                    career_goal=request.careerGoal,
                    topics=topics
                )
                roadmap["resources"] = validated_resources
                
                # Count validation results
                verified_count = sum(1 for r in validated_resources if r.get("urlVerified", False))
                replaced_count = sum(1 for r in validated_resources if r.get("source") == "local_verified_replacement")
                
                logger.info(f"✅ Resource validation complete:")
                logger.info(f"   Total resources: {len(validated_resources)}")
                logger.info(f"   Verified URLs: {verified_count}")
                logger.info(f"   Replaced URLs: {replaced_count}")
                
                # Add validation metadata
                if "metadata" not in roadmap:
                    roadmap["metadata"] = {}
                roadmap["metadata"]["resourceValidationEnabled"] = True
                roadmap["metadata"]["validatedResources"] = verified_count
                roadmap["metadata"]["replacedResources"] = replaced_count
            else:
                logger.warning("⚠️  No resources to validate")
        else:
            logger.warning("=" * 80)
            logger.warning("⚠️  FALLBACK: WATSONX.AI FAILED - USING TEMPLATE DATA")
            logger.warning("=" * 80)
            logger.warning("This means the roadmap will be generic and not AI-personalized")
            logger.warning("Possible reasons:")
            logger.warning("  1. WatsonX authentication failed (check API key)")
            logger.warning("  2. WatsonX API call failed (check network/service status)")
            logger.warning("  3. WatsonX returned invalid/incomplete JSON (check parsing errors above)")
            logger.warning("  4. WatsonX response was truncated (hit max_new_tokens limit)")
            logger.warning("")
            logger.warning("Check the detailed logs above to identify the specific issue")
            logger.warning("If you see 'RESPONSE APPEARS TRUNCATED', increase max_new_tokens")
            logger.warning("=" * 80)
            
            roadmap = create_fallback_roadmap(
                career_goal=request.careerGoal,
                current_skills=request.currentSkills,
                timeframe=request.timeframe,
                role_data=role_data,
                local_resources=local_resources,
                github_projects=github_projects
            )
            roadmap["metadata"] = {
                "usedWatsonx": False,
                "usedGitHub": len(github_projects) > 0,
                "matchedLocalResources": len(local_resources.get("resources", [])),
                "fallbackReason": "watsonx.ai failed - check logs for details"
            }
        
        # Step 8: Add certifications to roadmap
        if certifications and "certifications" not in roadmap:
            roadmap["certifications"] = certifications
        
        # Step 9: Return successful response
        return RoadmapResponse(
            success=True,
            careerGoal=request.careerGoal,
            roadmap=roadmap,
            metadata=roadmap.get("metadata")
        )
    
    except HTTPException:
        raise
    
    except Exception as e:
        logger.error(f"Error generating roadmap: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate roadmap. Please try again later."
        )

# Made with Bob
