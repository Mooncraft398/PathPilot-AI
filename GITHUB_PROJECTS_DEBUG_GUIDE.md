# GitHub Projects Data Flow Debug Guide

## Problem
GitHub projects and some resources are not showing on the frontend, even though they may exist in the backend response.

## Data Flow Architecture

```
User Form → PathwayForm.jsx → generateRoadmap() API call
    ↓
Backend /api/generate-roadmap endpoint
    ↓
search_github_for_role() → GitHub API
    ↓
normalize_roadmap_response() → adds githubProjects
    ↓
Return JSON response with roadmap.githubProjects
    ↓
Frontend receives response
    ↓
transformRoadmapToPathway() → maps to pathway.githubProjects
    ↓
savePathway() → localStorage
    ↓
PathwayPage reads from localStorage
    ↓
Renders pathway.githubProjects
```

## Debug Logging Added

### Backend (server/routes/roadmap.py)

**Location:** Lines 556-595

**Logs:**
```
📤 FINAL RESPONSE TO FRONTEND
   Career Goal: SOC Analyst
   Matched Career Path: SOC Analyst
   Resources: X
   GitHub Projects: X
   Portfolio Projects: X
   Weekly Plans: X

🐙 GitHub Projects Details (X total):
   1. project-name
      URL: https://...
      Stars: X
      Language: Python

📊 Metadata:
   GitHub Raw Count: X
   GitHub Filtered Count: X
   GitHub Shown Count: X
   Matched Resource Count: X
   Requested Timeframe: 6 weeks
   Total Weeks: 6
```

### Frontend (client/src/components/PathwayForm.jsx)

**Location:** Lines 74-107

**Logs:**
```
✅ RECEIVED ROADMAP FROM BACKEND
📦 Full response: {...}
🔑 Response keys: [...]
🗺️  Roadmap keys: [...]
🐙 GitHub projects in response: X
🐙 GitHub projects: [...]
📚 Resources in response: X
📅 Weekly plans in response: X

✅ PATHWAY TRANSFORMATION COMPLETE
📦 Final pathway object: {...}
🔑 Pathway keys: [...]
🐙 GitHub projects in pathway: X
🐙 GitHub projects: [...]
📚 Total resources across weeks: X
📅 Weeks: X

💾 Saved pathway to localStorage
🔍 Verify localStorage has githubProjects: X
```

### Frontend (client/src/pages/PathwayPage.jsx)

**Location:** Lines 15-24

**Logs:**
```
🔍 PathwayPage: Loading pathway from localStorage
📦 Loaded pathway: {...}
🐙 GitHub projects count: X
🐙 GitHub projects: [...]
```

## Testing Steps

### 1. Clear Old Data
```javascript
// In browser console:
localStorage.clear();
location.reload();
```

### 2. Generate Fresh Roadmap

**Test Request:**
```json
{
  "careerGoal": "SOC Analyst",
  "currentSkills": ["Python", "basic networking", "Wireshark"],
  "timeframe": "6 weeks"
}
```

### 3. Check Backend Logs

Look for in terminal:
```
🐙 GITHUB PROJECT SEARCH
   Career Goal: SOC Analyst
   Search Query: ...
   ✅ Found X GitHub projects

📤 FINAL RESPONSE TO FRONTEND
   GitHub Projects: X
   🐙 GitHub Projects Details (X total):
      1. project-name ...
```

**Expected:** `GitHub Projects: 5` (or more)

### 4. Check Frontend Console

Look for in browser console:
```
✅ RECEIVED ROADMAP FROM BACKEND
   🐙 GitHub projects in response: 5

✅ PATHWAY TRANSFORMATION COMPLETE
   🐙 GitHub projects in pathway: 5

💾 Saved pathway to localStorage
   🔍 Verify localStorage has githubProjects: 5

🔍 PathwayPage: Loading pathway from localStorage
   🐙 GitHub projects count: 5
```

**Expected:** All counts should be 5 (or same number)

### 5. Check Response Structure

In browser console after generation:
```javascript
// Check localStorage
const pathway = JSON.parse(localStorage.getItem('pathway'));
console.log('GitHub Projects:', pathway.githubProjects);
console.log('Count:', pathway.githubProjects?.length);
```

**Expected Structure:**
```javascript
{
  title: "SOC Analyst Career Pathway",
  goal: "SOC Analyst",
  githubProjects: [
    {
      name: "project-name",
      description: "...",
      url: "https://github.com/...",
      stars: 1234,
      language: "Python",
      topics: []
    }
  ],
  weeks: [...],
  _metadata: {
    githubProjectsCount: 5,
    originalTimeframe: "6 weeks"
  }
}
```

## Common Issues & Solutions

### Issue 1: Backend Returns 0 GitHub Projects

**Symptoms:**
```
🐙 GITHUB PROJECT SEARCH
   ✅ Found 0 GitHub projects
```

**Causes:**
- GitHub API rate limit
- GitHub token not configured
- Network error
- Search query returns no results

**Solution:**
1. Check `.env` file has `GITHUB_TOKEN`
2. Check GitHub API rate limit: https://api.github.com/rate_limit
3. Check backend logs for GitHub API errors
4. Verify search query is reasonable

### Issue 2: Backend Has Projects, Frontend Doesn't

**Symptoms:**
```
Backend: GitHub Projects: 5
Frontend: 🐙 GitHub projects in response: 0
```

**Causes:**
- Response structure mismatch
- Field name inconsistency (github_projects vs githubProjects)

**Solution:**
1. Check backend response structure in logs
2. Verify `normalize_roadmap_response()` is called
3. Check response has `roadmap.githubProjects` (camelCase)

### Issue 3: Frontend Receives, But Doesn't Transform

**Symptoms:**
```
Frontend received: 🐙 GitHub projects in response: 5
Frontend transformed: 🐙 GitHub projects in pathway: 0
```

**Causes:**
- `transformRoadmapToPathway()` mapping error
- Field name mismatch in transformation

**Solution:**
1. Check `client/src/utils/api.js` lines 382-389
2. Verify mapping: `roadmap.githubProjects` → `pathway.githubProjects`
3. Check for null/undefined handling

### Issue 4: Transforms But Doesn't Save

**Symptoms:**
```
Frontend transformed: 🐙 GitHub projects in pathway: 5
localStorage: 🔍 Verify localStorage has githubProjects: 0
```

**Causes:**
- `savePathway()` not saving all fields
- localStorage quota exceeded
- Serialization error

**Solution:**
1. Check `client/src/utils/localStorage.js`
2. Verify `JSON.stringify()` doesn't fail
3. Check browser console for errors

### Issue 5: Saves But Doesn't Display

**Symptoms:**
```
localStorage: 🔍 Verify localStorage has githubProjects: 5
PathwayPage: 🐙 GitHub projects count: 0
```

**Causes:**
- Old data in localStorage
- PathwayPage reading wrong field
- Conditional rendering hiding projects

**Solution:**
1. Clear localStorage and regenerate
2. Check PathwayPage line 541: `pathway.githubProjects`
3. Check filtering logic lines 549-556

### Issue 6: Displays But Filters Out

**Symptoms:**
```
PathwayPage loaded: 🐙 GitHub projects count: 5
Rendered: 0 cards shown
```

**Causes:**
- URL validation filtering out projects
- Confidence filtering too strict
- Missing required fields

**Solution:**
1. Check filter at lines 549-556
2. Verify projects have valid URLs
3. Check confidence levels (high/medium shown, low hidden)
4. Inspect project objects in console

## Expected Behavior

### Successful Flow

1. **Backend generates 5 GitHub projects**
2. **Backend normalizes response** with `githubProjects` array
3. **Backend logs** show 5 projects with details
4. **Frontend receives** response with 5 projects
5. **Frontend transforms** to pathway with 5 projects
6. **Frontend saves** to localStorage with 5 projects
7. **PathwayPage loads** from localStorage with 5 projects
8. **PathwayPage renders** 5 project cards (or fewer if filtered)

### Fallback Behavior

If GitHub API fails:
1. Backend logs warning
2. Backend continues with 0 GitHub projects
3. Frontend receives roadmap with empty `githubProjects: []`
4. PathwayPage shows message: "No strong GitHub projects found for this path yet."

## Manual Testing Commands

### Start Backend
```bash
cd server
uvicorn main:app --reload --port 8000
```

### Start Frontend
```bash
cd client
npm run dev
```

### Test API Directly
```bash
curl -X POST http://localhost:8000/api/generate-roadmap \
  -H "Content-Type: application/json" \
  -d '{
    "careerGoal": "SOC Analyst",
    "currentSkills": ["Python"],
    "timeframe": "6 weeks"
  }'
```

### Check Response Structure
```bash
# Save response to file
curl -X POST http://localhost:8000/api/generate-roadmap \
  -H "Content-Type: application/json" \
  -d '{"careerGoal":"SOC Analyst","currentSkills":[],"timeframe":"6 weeks"}' \
  > response.json

# Check githubProjects
cat response.json | jq '.roadmap.githubProjects | length'
cat response.json | jq '.roadmap.githubProjects[0]'
```

## Browser Console Checks

### After Generation
```javascript
// Check full pathway
const pathway = JSON.parse(localStorage.getItem('pathway'));
console.table(pathway.githubProjects);

// Check specific fields
pathway.githubProjects.forEach((p, i) => {
  console.log(`Project ${i+1}:`, {
    name: p.name,
    url: p.url,
    stars: p.stars,
    hasValidUrl: p.url && p.url !== '#'
  });
});

// Check metadata
console.log('Metadata:', pathway._metadata);
```

### On PathwayPage
```javascript
// Check what PathwayPage sees
console.log('GitHub Projects:', pathway?.githubProjects);
console.log('Count:', pathway?.githubProjects?.length);

// Check filtering
const filtered = pathway?.githubProjects?.filter(p => 
  p.url && p.url !== '#' && p.url !== ''
);
console.log('After URL filter:', filtered?.length);
```

## Next Steps

1. ✅ Debug logging added to backend and frontend
2. ⏳ User tests with fresh localStorage
3. ⏳ User checks backend terminal logs
4. ⏳ User checks browser console logs
5. ⏳ User reports where data is lost (if any)
6. ⏳ Fix specific issue based on logs

## Files Modified

1. `server/routes/roadmap.py` - Enhanced final response logging
2. `client/src/components/PathwayForm.jsx` - Enhanced transformation logging
3. `client/src/pages/PathwayPage.jsx` - Already has loading logs (lines 15-24)

## Contact Points

If GitHub projects still don't show after following this guide:

1. Share backend terminal logs (from "🐙 GITHUB PROJECT SEARCH" to "📤 FINAL RESPONSE")
2. Share browser console logs (from "✅ RECEIVED ROADMAP" to "🔍 PathwayPage")
3. Share `localStorage.getItem('pathway')` content
4. Share any error messages

This will pinpoint exactly where the data is being lost.