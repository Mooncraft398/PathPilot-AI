from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import HealthResponse
from routes import pathways

# Create FastAPI app
app = FastAPI(
    title="PathPilot AI API",
    description="Career pathway generator API for the IBM Bob Hackathon",
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
app.include_router(pathways.router)


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

# Made with Bob
