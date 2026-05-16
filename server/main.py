from dotenv import load_dotenv
from pathlib import Path

# Load environment variables FIRST, before any other imports
# This ensures all modules can access environment variables when they're imported
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import HealthResponse
from routes import pathways, github_projects, recommendations, onet, usajobs, roadmap

# Create FastAPI app
app = FastAPI(
    title="PathPilot AI API",
    description="Career pathway generator API for the IBM Bob Hackathon with watsonx.ai integration",
    version="1.0.0"
)

# Configure CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite default port
        "http://localhost:3000",  # Alternative React port
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(roadmap.router)  # AI-powered roadmap generator
app.include_router(pathways.router)
app.include_router(github_projects.router)
app.include_router(recommendations.router)
app.include_router(onet.router)
app.include_router(usajobs.router)


@app.get("/", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return HealthResponse(
        status="healthy",
        message="PathPilot AI API is running! Visit /docs for API documentation."
    )


@app.get("/health", response_model=HealthResponse)
async def health():
    """
    Alternative health check endpoint.
    """
    return HealthResponse(
        status="healthy",
        message="API is operational"
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
