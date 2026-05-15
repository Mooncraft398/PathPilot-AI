from pydantic import BaseModel, Field
from typing import List, Optional


class PathwayRequest(BaseModel):
    """Request model for generating a career pathway"""
    goal: str = Field(..., description="Career goal (e.g., 'Junior Web Developer')")
    level: str = Field(..., description="Current skill level: beginner, intermediate, advanced")
    weeks: int = Field(..., ge=1, le=52, description="Number of weeks for the pathway")
    daysPerWeek: int = Field(..., ge=1, le=7, description="Days per week available")
    hoursPerDay: int = Field(..., ge=1, le=24, description="Hours per day available")
    preferences: List[str] = Field(default=[], description="Learning preferences: projects, videos, reading, interactive")
    budget: str = Field(..., description="Budget preference: free-first, paid-ok, premium")


class Resource(BaseModel):
    """A learning resource"""
    title: str
    type: str  # video, article, course, documentation
    url: str
    duration: str
    isFree: bool


class DailyPlan(BaseModel):
    """Daily learning plan"""
    day: int
    focus: str
    tasks: List[str]
    estimatedHours: int


class GuidedProject(BaseModel):
    """A guided project for hands-on practice"""
    title: str
    description: str
    skills: List[str]
    estimatedHours: int
    difficulty: str


class Week(BaseModel):
    """Weekly learning plan"""
    weekNumber: int
    title: str
    objectives: List[str]
    dailyPlan: List[DailyPlan]
    resources: List[Resource]
    guidedProject: GuidedProject
    resumeBullet: str
    completed: bool = False


class Certification(BaseModel):
    """Recommended certification"""
    name: str
    provider: str
    cost: str
    timeToComplete: str
    priority: str  # essential, recommended, optional


class PathwayResponse(BaseModel):
    """Response model for generated pathway"""
    title: str
    goal: str
    level: str
    summary: str
    weeklyTimeCommitment: str
    weeks: List[Week]
    finalPortfolioChecklist: List[str]
    recommendedCertifications: List[Certification]


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    message: str


class GitHubRepository(BaseModel):
    """GitHub repository information"""
    name: str
    description: Optional[str]
    stars: int
    language: Optional[str]
    url: str


class GitHubProjectsResponse(BaseModel):
    """Response model for GitHub projects search"""
    skill: str
    repositories: List[GitHubRepository]
    total_count: int


class ErrorResponse(BaseModel):
    """Error response model"""
    error: str
    detail: Optional[str] = None

# Made with Bob
