from fastapi import APIRouter, HTTPException
from models.schemas import PathwayRequest, PathwayResponse
from services.pathway_generator import generate_sample_pathway

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

# Made with Bob
