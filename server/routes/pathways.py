from fastapi import APIRouter, HTTPException
from models.schemas import PathwayRequest, PathwayResponse, AdaptPathwayRequest
from services.pathway_generator import generate_sample_pathway
from datetime import datetime
import re

router = APIRouter(prefix="/api/pathways", tags=["pathways"])


@router.post("/generate", response_model=PathwayResponse)
async def generate_pathway(request: PathwayRequest):
    """
    Generate a personalized career pathway based on user input.
    
    This endpoint accepts user preferences and returns a structured learning pathway
    with weekly plans, resources, projects, and certifications.
    
    For the MVP, this uses a sample generator. Later, it will integrate with IBM Bob AI.
    """
    try:
        # Generate the pathway using the sample generator
        pathway = generate_sample_pathway(request)
        return pathway
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate pathway: {str(e)}"
        )


@router.post("/adapt")
async def adapt_pathway(request: AdaptPathwayRequest):
    """
    Adapt an existing pathway based on user feedback.
    
    This is a simple implementation for the hackathon that adds an adaptation note
    and adjusts the pathway based on common feedback patterns.
    
    Future: Will integrate with AI for intelligent pathway adaptation.
    """
    try:
        pathway = request.pathway
        feedback = request.feedback.lower()
        
        # Create adaptation note
        adaptation_note = f"Adapted on {datetime.now().strftime('%Y-%m-%d')}: {request.feedback}"
        
        # Parse time-related feedback
        hours_per_day = None
        hours_per_week = None
        
        # Look for patterns like "1 hour per day", "2 hours per day", etc.
        day_match = re.search(r'(\d+)\s*hour[s]?\s*per\s*day', feedback)
        if day_match:
            hours_per_day = int(day_match.group(1))
        
        # Look for patterns like "3 hours per week", "5 hours per week", etc.
        week_match = re.search(r'(\d+)\s*hour[s]?\s*per\s*week', feedback)
        if week_match:
            hours_per_week = int(week_match.group(1))
        
        # Update pathway based on parsed time
        if hours_per_day is not None:
            # Update weeklyTimeCommitment
            pathway["weeklyTimeCommitment"] = f"{hours_per_day} hour{'s' if hours_per_day != 1 else ''} per day"
            
            # Update daily plan hours for each week
            if "weeks" in pathway:
                for week in pathway["weeks"]:
                    if "dailyPlan" in week:
                        for day in week["dailyPlan"]:
                            day["estimatedHours"] = hours_per_day
            
            pathway["summary"] = f"{pathway.get('summary', '')} [Adapted for {hours_per_day}h/day schedule]"
        
        elif hours_per_week is not None:
            # Update weeklyTimeCommitment
            pathway["weeklyTimeCommitment"] = f"{hours_per_week} hour{'s' if hours_per_week != 1 else ''} per week"
            
            # Distribute hours across days (simple: divide by number of days in dailyPlan)
            if "weeks" in pathway and len(pathway["weeks"]) > 0:
                first_week = pathway["weeks"][0]
                if "dailyPlan" in first_week and len(first_week["dailyPlan"]) > 0:
                    days_count = len(first_week["dailyPlan"])
                    hours_per_day_calc = max(1, hours_per_week // days_count)
                    
                    # Update all weeks
                    for week in pathway["weeks"]:
                        if "dailyPlan" in week:
                            for day in week["dailyPlan"]:
                                day["estimatedHours"] = hours_per_day_calc
            
            pathway["summary"] = f"{pathway.get('summary', '')} [Adapted for {hours_per_week}h/week schedule]"
        
        elif "hour" in feedback or "time" in feedback:
            # Generic time constraint without specific numbers
            pathway["weeklyTimeCommitment"] = "Flexible - Adjusted for your schedule"
            pathway["summary"] = f"{pathway.get('summary', '')} [Adapted for reduced time commitment]"
        
        elif "project" in feedback:
            # User wants more projects
            pathway["summary"] = f"{pathway.get('summary', '')} [Enhanced with additional project focus]"
        
        elif "struggling" in feedback or "difficult" in feedback or "hard" in feedback:
            # User is struggling
            pathway["summary"] = f"{pathway.get('summary', '')} [Adjusted with additional support resources]"
        
        else:
            # Generic adaptation
            pathway["summary"] = f"{pathway.get('summary', '')} [Customized based on your feedback]"
        
        # Add adaptation history if it doesn't exist
        if "adaptationHistory" not in pathway:
            pathway["adaptationHistory"] = []
        
        pathway["adaptationHistory"].append(adaptation_note)
        
        return pathway
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to adapt pathway: {str(e)}"
        )
