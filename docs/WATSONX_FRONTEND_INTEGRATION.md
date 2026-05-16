# Watsonx.ai Frontend Integration Guide

## Overview

This document explains how the frontend now integrates with the Watsonx.ai-powered roadmap generation backend.

## Problem Identified

The frontend was calling the **old static pathway endpoint** (`/api/pathways/generate`) which returned generic weekly sections like:
- Foundations & Setup
- Core Concepts
- Building Blocks
- Intermediate Skills
- Advanced Techniques
- Real-World Projects

However, the backend had implemented a **new Watsonx.ai endpoint** (`/api/generate-roadmap`) that returns rich AI-generated content including:
- Career summary
- 3 learning phases
- Skills breakdown
- Tools list
- Curated resources
- GitHub project suggestions
- Portfolio project ideas
- Resume bullet points
- Weekly learning plan
- Next steps checklist

## Solution Implemented

### 1. Updated API Layer (`client/src/utils/api.js`)

#### Added `transformRoadmapToPathway()` Function
This function transforms the Watsonx.ai roadmap response structure into the format expected by the frontend components:

```javascript
export const transformRoadmapToPathway = (roadmapResponse, formData) => {
  // Transforms:
  // - roadmap.phases → weeks with daily plans
  // - roadmap.resources → week resources
  // - roadmap.portfolioProjects → guided projects
  // - roadmap.resumeBullets → resume bullets per week
  // - roadmap.nextSteps → final portfolio checklist
  // - roadmap.certifications → recommended certifications
}
```

**Key Transformations:**
- **Phases → Weeks**: Distributes learning phases across the requested number of weeks
- **Resources**: Maps Watsonx.ai resources to frontend resource format
- **Projects**: Creates guided projects from portfolio project suggestions
- **Daily Plans**: Generates daily learning plans based on user's time commitment

#### Enhanced Logging
Added comprehensive console logging at every step:
- `🤖` Request to Watsonx.ai
- `✅` Successful responses
- `❌` Errors with full details
- `🔄` Transformation steps
- `📦` Data structures at each stage

### 2. Updated PathwayForm Component (`client/src/components/PathwayForm.jsx`)

#### Changed from Old Endpoint to New Endpoint

**Before:**
```javascript
const pathway = await generatePathway(formData);
```

**After:**
```javascript
// 1. Calculate timeframe from weeks
const months = Math.ceil(formData.weeks / 4);
const timeframe = `${months} month${months !== 1 ? 's' : ''}`;

// 2. Prepare Watsonx.ai request
const roadmapRequest = {
  careerGoal: formData.goal,
  currentSkills: [],
  timeframe: timeframe
};

// 3. Call Watsonx.ai endpoint
const roadmapResponse = await generateRoadmap(roadmapRequest);

// 4. Transform to frontend format
const pathway = transformRoadmapToPathway(roadmapResponse, {
  ...formData,
  timeframe
});
```

#### Added Debug Logging
Every step now logs to the browser console:
- Form submission
- API request preparation
- API response
- Transformation process
- localStorage save
- Navigation

## Data Flow

```
User Form Input
    ↓
PathwayForm.handleSubmit()
    ↓
generateRoadmap() → POST /api/generate-roadmap
    ↓
Backend: Watsonx.ai generates roadmap
    ↓
transformRoadmapToPathway()
    ↓
savePathway() → localStorage
    ↓
Navigate to /pathway
    ↓
PathwayPage displays rich AI content
```

## Debugging

### Browser Console Logs

When you generate a pathway, you'll see:
1. `🚀 Starting pathway generation with Watsonx.ai...`
2. `📋 Form data:` - Shows user input
3. `📡 Calling Watsonx.ai roadmap API...`
4. `✅ Received roadmap from Watsonx.ai`
5. `📦 Raw response from backend:` - Shows Watsonx.ai response
6. `🔄 Transforming Watsonx.ai roadmap to pathway format...`
7. `✅ Transformation complete`
8. `📦 Transformed pathway:` - Shows final pathway object
9. `💾 Saved pathway to localStorage`

### Checking if Watsonx.ai is Working

Look for the `_metadata` field in the transformed pathway:
```javascript
{
  _metadata: {
    usedWatsonx: true,  // ← Should be true if Watsonx.ai worked
    generatedAt: "2026-05-16T04:20:00.000Z",
    originalRoadmap: { /* full Watsonx.ai response */ }
  }
}
```

### Common Issues

#### Issue: Still seeing generic pathway
**Cause**: Backend might be using fallback roadmap
**Check**: Look for `metadata.usedWatsonx: false` in console logs
**Solution**: Check backend logs and Watsonx.ai credentials in `.env`

#### Issue: "Cannot connect to server"
**Cause**: Backend not running or CORS issue
**Check**: Ensure backend is running on `http://localhost:8000`
**Solution**: Run `cd server && python -m uvicorn main:app --reload`

#### Issue: Transformation errors
**Cause**: Unexpected roadmap structure from backend
**Check**: Console logs showing the raw response
**Solution**: Update `transformRoadmapToPathway()` to handle the structure

## Backend Response Structure

The Watsonx.ai endpoint returns:
```json
{
  "success": true,
  "careerGoal": "SOC Analyst",
  "roadmap": {
    "summary": "Career overview...",
    "phases": [
      {
        "phase": 1,
        "title": "Foundation & Setup",
        "duration": "Weeks 1-4",
        "focus": "Learn the basics...",
        "skills": ["Skill1", "Skill2"]
      }
    ],
    "skills": ["All", "Skills", "List"],
    "tools": ["Tool1", "Tool2"],
    "resources": [
      {
        "title": "Resource Name",
        "type": "video",
        "url": "https://...",
        "duration": "2 hours",
        "isFree": true
      }
    ],
    "githubProjects": [...],
    "portfolioProjects": [...],
    "resumeBullets": [...],
    "weeklyPlan": [...],
    "nextSteps": [...],
    "certifications": [...]
  },
  "metadata": {
    "usedWatsonx": true,
    "usedGitHub": true,
    "matchedLocalResources": 10
  }
}
```

## Frontend Expected Structure

The frontend components expect:
```json
{
  "title": "SOC Analyst Career Pathway",
  "goal": "SOC Analyst",
  "level": "beginner",
  "summary": "A comprehensive pathway...",
  "weeklyTimeCommitment": "10 hours/week",
  "weeks": [
    {
      "weekNumber": 1,
      "title": "Week 1 Title",
      "objectives": ["Objective 1", "Objective 2"],
      "dailyPlan": [
        {
          "day": 1,
          "focus": "Day 1 focus",
          "tasks": ["Task 1", "Task 2"],
          "estimatedHours": 2
        }
      ],
      "resources": [...],
      "guidedProject": {...},
      "resumeBullet": "...",
      "completed": false
    }
  ],
  "finalPortfolioChecklist": [...],
  "recommendedCertifications": [...]
}
```

## Testing

### Manual Test Steps

1. **Start Backend**:
   ```bash
   cd server
   python -m uvicorn main:app --reload
   ```

2. **Start Frontend**:
   ```bash
   cd client
   npm run dev
   ```

3. **Generate Pathway**:
   - Navigate to `/generate`
   - Enter "SOC Analyst" as career goal
   - Fill in other fields
   - Click "Generate My Pathway"

4. **Check Console**:
   - Open browser DevTools (F12)
   - Look for the emoji-prefixed logs
   - Verify `usedWatsonx: true` in metadata

5. **Verify Display**:
   - Should see rich content on `/pathway` page
   - Not just generic "Foundations & Setup" sections
   - Should see AI-generated phase titles and descriptions

## Federal Jobs Section Clarification

### How It Works

The **Federal Job Opportunities** section is **completely separate** from the Watsonx.ai roadmap generation:

1. **Watsonx.ai Roadmap**: Generates the learning pathway (phases, skills, resources, projects)
2. **USAJOBS API**: Searches for federal job postings based on the career goal

### Data Sources

- **Roadmap Content**: Generated by Watsonx.ai + local JSON files (roles.json, resources.json, etc.)
- **Job Listings**: Fetched from USAJOBS.gov API + O*NET database for job matching

### "No Jobs Found" Message

This message means:
- ✅ The AI roadmap generation **succeeded**
- ❌ The USAJOBS API returned **no matching federal job postings**

**Why this happens:**
- The job search uses the career goal keyword (e.g., "SOC Analyst")
- USAJOBS may not have active postings for that specific role at that time
- The search tries: city → state → nationwide, but may still find nothing

**This is normal and expected** - federal job availability varies by:
- Time of year
- Budget cycles
- Agency hiring needs
- Specific role terminology

### Debugging Job Search

Check the console for:
```javascript
// Job search initiated
"Searching for: SOC Analyst"

// Results
{
  "count": 0,
  "jobs": [],
  "searchLevel": "nationwide",
  "fallbackMessage": "Expanded search to nationwide..."
}
```

The roadmap will still be fully functional even if no jobs are found.

## Next Steps

1. **Test thoroughly** with different career goals
2. **Monitor console logs** for any transformation errors
3. **Report issues** if certain Watsonx.ai response structures aren't handled
4. **Enhance transformation** as needed for edge cases

## Made with Bob