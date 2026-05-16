# Career Recommendation System - Documentation

## Overview
The recommendation system connects all JSON data files (careers.json, resources.json, projects.json) to provide personalized career recommendations based on user skills and preferences.

## How It Works

### 1. Data Flow
```
User Input → Recommendation Service → JSON Data Files → Career Matching → Skill Gap Analysis → Resource/Project Matching → Response
```

### 2. Scoring Algorithm

**Match Score Calculation:**
```
Base Score = (Matched Skills / Total Required Skills) × 100
Category Bonus = +10% if preferred_area matches career category
Final Score = min(Base Score + Category Bonus, 100)
```

**Example:**
- Career requires: ["Python", "SQL", "Excel", "Networking", "Linux"] (5 skills)
- User has: ["Python", "SQL", "Excel"] (3 skills)
- Base Score: (3/5) × 100 = 60%
- If preferred_area matches category: 60% + 10% = 70%
- Final Score: 70%

### 3. JSON File Connections

**careers.json** → Provides career information and required_skills
- Used for: Career matching, skill requirements

**resources.json** → Provides learning resources by skill
- Connected by: `resource.skill` matches `missing_skill`
- Used for: Learning recommendations

**projects.json** → Provides hands-on projects by skill
- Connected by: `project.skill` matches `missing_skill`
- Used for: Project recommendations

**courses.json** (optional) → Would provide structured courses
- Not currently present, system continues without it

## API Endpoint

### POST /api/recommend

**Request Body:**
```json
{
  "preferred_area": "Cybersecurity",
  "current_skills": ["Python", "Networking", "Troubleshooting"],
  "hours_per_week": "6-10",
  "learning_style": "Hands-on"
}
```

**Parameters:**
- `preferred_area` (optional): Career category preference (e.g., "Cybersecurity", "Data & Analytics")
- `current_skills` (required, can be empty): List of skills user currently has
- `hours_per_week` (required): Available study time
- `learning_style` (required): Learning preference

**Response Structure:**
```json
{
  "career_matches": [
    {
      "id": "cybersecurity-analyst",
      "title": "Cybersecurity Analyst",
      "category": "Information Security",
      "description": "...",
      "match_percentage": 70,
      "matched_skills": ["Python", "Networking"],
      "missing_skills": ["Cybersecurity", "Security Monitoring", "Incident Response"],
      "common_tasks": [...],
      "related_roles": [...]
    }
  ],
  "skill_recommendations": [
    {
      "skill": "Cybersecurity",
      "resources": [
        {
          "title": "IBM SkillsBuild - Cybersecurity Fundamentals",
          "type": "course",
          "url": "https://skillsbuild.org/..."
        }
      ],
      "projects": [
        {
          "title": "Password Strength Checker",
          "description": "Create a tool that evaluates password strength...",
          "difficulty": "beginner"
        }
      ],
      "github_search_query": "Cybersecurity beginner project"
    }
  ],
  "total_careers_analyzed": 6,
  "message": "Found 3 career matches based on your 3 current skills."
}
```

## Testing

### Setup
1. Ensure server is running:
```bash
cd server
python main.py
```

2. Server should be available at: http://localhost:8000

### Test Cases

#### Test 1: User with Some Skills
```bash
curl -X POST http://localhost:8000/api/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "preferred_area": "Cybersecurity",
    "current_skills": ["Python", "Networking", "Troubleshooting"],
    "hours_per_week": "6-10",
    "learning_style": "Hands-on"
  }'
```

**Expected Result:**
- Top 3 career matches
- Cybersecurity Analyst should have high match percentage
- Missing skills identified
- Resources and projects for each missing skill

#### Test 2: User with No Skills
```bash
curl -X POST http://localhost:8000/api/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "preferred_area": "Data & Analytics",
    "current_skills": [],
    "hours_per_week": "10-20",
    "learning_style": "Visual"
  }'
```

**Expected Result:**
- Recommendations based on preferred_area
- Data Analyst should appear in top matches
- All required skills listed as missing
- Full learning path provided

#### Test 3: User with Many Skills
```bash
curl -X POST http://localhost:8000/api/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "preferred_area": "Software Development",
    "current_skills": ["React", "Git", "Python", "SQL"],
    "hours_per_week": "6-10",
    "learning_style": "Hands-on"
  }'
```

**Expected Result:**
- High match percentages (80%+)
- Frontend Developer should rank high
- Few missing skills
- Focused recommendations

#### Test 4: No Preferred Area
```bash
curl -X POST http://localhost:8000/api/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "current_skills": ["Linux", "Networking"],
    "hours_per_week": "6-10",
    "learning_style": "Reading"
  }'
```

**Expected Result:**
- All careers considered equally
- Network Technician, Help Desk Technician should rank high
- No category bonus applied

### Using API Documentation
Visit http://localhost:8000/docs for interactive testing:
1. Expand POST /api/recommend
2. Click "Try it out"
3. Edit the request body
4. Click "Execute"
5. View response

### Using Postman
1. Create new POST request
2. URL: `http://localhost:8000/api/recommend`
3. Headers: `Content-Type: application/json`
4. Body (raw JSON):
```json
{
  "preferred_area": "Cybersecurity",
  "current_skills": ["Python", "Networking", "Troubleshooting"],
  "hours_per_week": "6-10",
  "learning_style": "Hands-on"
}
```
5. Send

## Error Handling

### Missing Data Files
If careers.json is missing:
```json
{
  "error": "Data file missing",
  "detail": "careers.json not found. Please ensure data files are in server/data/"
}
```

### Invalid JSON
If JSON files are corrupted:
```json
{
  "error": "Invalid JSON data",
  "detail": "Failed to parse JSON file: ..."
}
```

### Empty Skills
System handles empty current_skills gracefully:
- Recommendations based on preferred_area only
- All career skills marked as missing
- Full learning path provided

## Files Modified/Created

### Created:
1. **server/models/schemas.py** (modified)
   - Added RecommendationRequest
   - Added RecommendationResponse
   - Added CareerMatch
   - Added SkillRecommendation
   - Added LearningResource
   - Added Project

2. **server/services/recommendation_service.py** (new)
   - load_json_file(): Loads JSON data files
   - calculate_career_match_score(): Implements scoring algorithm
   - get_skill_resources(): Matches resources to skills
   - get_skill_projects(): Matches projects to skills
   - generate_github_search_query(): Creates GitHub search queries
   - generate_recommendations(): Main recommendation logic

3. **server/routes/recommendations.py** (new)
   - POST /api/recommend endpoint
   - Full API documentation

4. **server/main.py** (modified)
   - Added recommendations router

### Unchanged:
- server/data/careers.json
- server/data/resources.json
- server/data/projects.json

## Example Request/Response

### Request:
```json
{
  "preferred_area": "Cybersecurity",
  "current_skills": ["Python", "Networking", "Troubleshooting"],
  "hours_per_week": "6-10",
  "learning_style": "Hands-on"
}
```

### Response (abbreviated):
```json
{
  "career_matches": [
    {
      "id": "cybersecurity-analyst",
      "title": "Cybersecurity Analyst",
      "category": "Information Security",
      "match_percentage": 70,
      "matched_skills": ["Python", "Networking"],
      "missing_skills": ["Cybersecurity", "Security Monitoring", "Incident Response"]
    },
    {
      "id": "help-desk-technician",
      "title": "Help Desk Technician",
      "category": "IT Support",
      "match_percentage": 75,
      "matched_skills": ["Troubleshooting", "Networking"],
      "missing_skills": ["Linux", "Git"]
    },
    {
      "id": "network-technician",
      "title": "Network Technician",
      "category": "Network Infrastructure",
      "match_percentage": 67,
      "matched_skills": ["Networking", "Troubleshooting"],
      "missing_skills": ["Linux"]
    }
  ],
  "skill_recommendations": [
    {
      "skill": "Cybersecurity",
      "resources": [
        {
          "title": "IBM SkillsBuild - Cybersecurity Fundamentals",
          "type": "course",
          "url": "https://skillsbuild.org/students/course-catalog/cybersecurity"
        }
      ],
      "projects": [
        {
          "title": "Password Strength Checker",
          "description": "Create a tool that evaluates password strength...",
          "difficulty": "beginner"
        }
      ],
      "github_search_query": "Cybersecurity beginner project"
    }
  ],
  "total_careers_analyzed": 6,
  "message": "Found 3 career matches based on your 3 current skills. Focused on Cybersecurity."
}
```

## Integration with Frontend

The frontend can use this endpoint to:
1. Display top career matches with match percentages
2. Show skill gaps for each career
3. Provide learning resources for missing skills
4. Link to GitHub projects via search queries
5. Create personalized learning paths

## Future Enhancements

1. **courses.json Support**: Add structured course recommendations
2. **Skill Weighting**: Weight skills by importance
3. **Learning Path Generation**: Create week-by-week learning plans
4. **Progress Tracking**: Track completed skills and update recommendations
5. **Certification Mapping**: Link certifications to career paths
6. **Time Estimation**: Calculate time to acquire missing skills

## Made with Bob