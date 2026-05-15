from models.schemas import (
    PathwayRequest,
    PathwayResponse,
    Week,
    DailyPlan,
    Resource,
    GuidedProject,
    Certification
)
from typing import List


def generate_sample_pathway(request: PathwayRequest) -> PathwayResponse:
    """
    Generate a sample career pathway based on user input.
    This is a mock implementation for the hackathon MVP.
    Later, this will be replaced with IBM Bob AI integration.
    """
    
    # Calculate total hours available
    total_hours = request.weeks * request.daysPerWeek * request.hoursPerDay
    
    # Generate weeks based on the career goal
    weeks = []
    for week_num in range(1, request.weeks + 1):
        week = generate_week(
            week_num=week_num,
            goal=request.goal,
            level=request.level,
            days_per_week=request.daysPerWeek,
            hours_per_day=request.hoursPerDay,
            preferences=request.preferences,
            budget=request.budget
        )
        weeks.append(week)
    
    # Generate pathway response
    pathway = PathwayResponse(
        title=f"{request.goal} Pathway",
        goal=request.goal,
        level=request.level,
        summary=f"A comprehensive {request.weeks}-week pathway to become a {request.goal}. "
                f"This plan is designed for {request.level} learners with {request.hoursPerDay} hours/day, "
                f"{request.daysPerWeek} days/week commitment.",
        weeklyTimeCommitment=f"{request.hoursPerDay * request.daysPerWeek} hours/week",
        weeks=weeks,
        finalPortfolioChecklist=generate_portfolio_checklist(request.goal),
        recommendedCertifications=generate_certifications(request.goal, request.budget)
    )
    
    return pathway


def generate_week(
    week_num: int,
    goal: str,
    level: str,
    days_per_week: int,
    hours_per_day: int,
    preferences: List[str],
    budget: str
) -> Week:
    """Generate a single week's learning plan"""
    
    # Sample week titles based on progression
    week_titles = {
        1: "Foundations & Setup",
        2: "Core Concepts",
        3: "Building Blocks",
        4: "Intermediate Skills",
        5: "Advanced Techniques",
        6: "Real-World Projects"
    }
    
    # Get title or generate generic one
    title = week_titles.get(week_num, f"Week {week_num} - Continued Learning")
    
    # Generate daily plans
    daily_plans = []
    for day in range(1, days_per_week + 1):
        daily_plan = DailyPlan(
            day=day,
            focus=f"Day {day} Focus: Practice & Build",
            tasks=[
                f"Review concepts from previous day",
                f"Complete coding exercises ({hours_per_day - 1} hours)",
                f"Work on weekly project (1 hour)"
            ],
            estimatedHours=hours_per_day
        )
        daily_plans.append(daily_plan)
    
    # Generate resources based on preferences
    resources = generate_resources(goal, week_num, preferences, budget)
    
    # Generate guided project
    project = GuidedProject(
        title=f"Week {week_num} Project: Build a {get_project_name(goal, week_num)}",
        description=f"Apply this week's concepts by building a practical project that demonstrates your skills.",
        skills=get_week_skills(goal, week_num),
        estimatedHours=hours_per_day * 2,
        difficulty=level
    )
    
    # Generate resume bullet
    resume_bullet = f"Developed {get_project_name(goal, week_num)} using {', '.join(get_week_skills(goal, week_num)[:3])}"
    
    return Week(
        weekNumber=week_num,
        title=title,
        objectives=get_week_objectives(goal, week_num),
        dailyPlan=daily_plans,
        resources=resources,
        guidedProject=project,
        resumeBullet=resume_bullet,
        completed=False
    )


def generate_resources(goal: str, week_num: int, preferences: List[str], budget: str) -> List[Resource]:
    """Generate learning resources based on preferences and budget"""
    resources = []
    
    # Always include free resources
    if "videos" in preferences or not preferences:
        resources.append(Resource(
            title=f"Introduction to {goal} - Week {week_num}",
            type="video",
            url="https://www.youtube.com/watch?v=example",
            duration="2 hours",
            isFree=True
        ))
    
    if "reading" in preferences or not preferences:
        resources.append(Resource(
            title=f"{goal} Documentation - Week {week_num}",
            type="documentation",
            url="https://developer.mozilla.org/",
            duration="1 hour",
            isFree=True
        ))
    
    if "interactive" in preferences or not preferences:
        resources.append(Resource(
            title=f"Interactive {goal} Tutorial",
            type="interactive",
            url="https://www.freecodecamp.org/",
            duration="3 hours",
            isFree=True
        ))
    
    # Add paid resources if budget allows
    if budget in ["paid-ok", "premium"]:
        resources.append(Resource(
            title=f"Complete {goal} Course",
            type="course",
            url="https://www.udemy.com/",
            duration="10 hours",
            isFree=False
        ))
    
    return resources


def get_week_objectives(goal: str, week_num: int) -> List[str]:
    """Generate learning objectives for the week"""
    base_objectives = [
        f"Understand core concepts for week {week_num}",
        f"Complete hands-on exercises",
        f"Build a practical project",
        f"Review and reinforce learning"
    ]
    return base_objectives


def get_week_skills(goal: str, week_num: int) -> List[str]:
    """Get skills to learn this week based on goal"""
    # Sample skills for web development
    if "web" in goal.lower() or "developer" in goal.lower():
        skills_by_week = {
            1: ["HTML", "CSS", "Git Basics"],
            2: ["JavaScript Fundamentals", "DOM Manipulation", "ES6+"],
            3: ["React Basics", "Components", "Props & State"],
            4: ["React Hooks", "API Integration", "Async JavaScript"],
            5: ["State Management", "Routing", "Form Handling"],
            6: ["Full Stack Integration", "Deployment", "Best Practices"]
        }
        return skills_by_week.get(week_num, ["Programming", "Problem Solving", "Debugging"])
    
    # Generic skills for other goals
    return ["Core Concepts", "Practical Application", "Problem Solving"]


def get_project_name(goal: str, week_num: int) -> str:
    """Generate project name based on goal and week"""
    if "web" in goal.lower():
        projects = {
            1: "Personal Portfolio Page",
            2: "Interactive To-Do List",
            3: "Weather Dashboard App",
            4: "Movie Search Application",
            5: "E-commerce Product Page",
            6: "Full-Stack Blog Platform"
        }
        return projects.get(week_num, f"Week {week_num} Project")
    
    return f"{goal} Practice Project"


def generate_portfolio_checklist(goal: str) -> List[str]:
    """Generate final portfolio checklist"""
    return [
        "Complete all weekly projects",
        "Deploy at least 3 projects to production",
        "Create a professional GitHub profile",
        "Write clear README files for all projects",
        "Build a personal portfolio website",
        "Prepare a technical resume",
        "Practice explaining your projects"
    ]


def generate_certifications(goal: str, budget: str) -> List[Certification]:
    """Generate recommended certifications"""
    certifications = []
    
    # Always include free certifications
    certifications.append(Certification(
        name="freeCodeCamp Responsive Web Design",
        provider="freeCodeCamp",
        cost="Free",
        timeToComplete="300 hours",
        priority="recommended"
    ))
    
    if budget in ["paid-ok", "premium"]:
        certifications.append(Certification(
            name="AWS Certified Cloud Practitioner",
            provider="Amazon Web Services",
            cost="$100",
            timeToComplete="40 hours",
            priority="optional"
        ))
    
    return certifications

# Made with Bob
