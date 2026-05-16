# Frontend Data Flow Fixes

## Date: 2026-05-16

## Overview
Fixed the frontend data flow to properly display backend data from WatsonX.ai, GitHub API, and local resources. The frontend was not correctly mapping backend response fields, causing generic placeholder data to be displayed instead of real AI-generated content.

---

## Issues Fixed

### 1. ✅ Resource Cards Showing Generic "Learning Resource" Text

**Problem:**
- Resource cards displayed "Learning Resource" instead of actual resource titles
- Missing URLs, durations, and other metadata
- Backend returned resources with `title`, `type`, `url` but frontend wasn't handling missing fields

**Fix:**
- Enhanced resource mapping in `client/src/utils/api.js` (lines 239-265)
- Added fallback values for missing fields:
  - `title`: Falls back to `name` or `Learning Resource ${idx + 1}`
  - `url`: Falls back to `link`, `href`, or `#`
  - `duration`: Falls back to `estimatedTime` or `1-2 hours`
  - `isFree`: Checks multiple fields (`isFree`, `cost === 'free'`)
- Updated `ResourceCard.jsx` to handle missing URLs gracefully
- Resources without valid URLs now display as non-clickable cards with "No link" badge

### 2. ✅ GitHub Projects Not Displaying

**Problem:**
- Backend returned GitHub projects but frontend didn't include them in pathway object
- No UI component to display GitHub projects

**Fix:**
- Added `githubProjects` array to pathway transformation (lines 308-315 in `api.js`)
- Maps GitHub project fields: `name`, `description`, `url`, `stars`, `language`, `topics`
- Added GitHub Projects section to `PathwayPage.jsx` (lines 527-580)
- Displays projects in grid layout with:
  - Project name and description
  - Star count
  - Programming language
  - Link to GitHub repository

### 3. ✅ Project Skills Mismatch

**Problem:**
- Guided project cards showed unrelated skills
- Example: "Basic Sales Data Visualization" project showing "Linux Command Line" skills
- Skills were being pulled from wrong phase/week

**Fix:**
- Enhanced project mapping logic (lines 256-265 in `api.js`)
- Now uses project-specific skills first: `projectForWeek.skills`
- Falls back to week topics, phase skills, or roadmap skills in order
- Each week gets correct project with matching skills

### 4. ✅ Insufficient Logging

**Problem:**
- Hard to debug whether frontend was using WatsonX data or fallback data
- No visibility into data transformation process

**Fix:**
- Added comprehensive console logging throughout transformation:
  - Raw backend response (JSON)
  - Data source (WatsonX vs fallback)
  - Roadmap structure (phases, weeks, resources, projects)
  - Per-week resource and project details
  - Final pathway summary with counts
- Logs clearly show:
  - ✅ USING WATSONX.AI GENERATED ROADMAP (success)
  - ⚠️ USING FALLBACK TEMPLATE DATA (failure)

---

## Files Modified

### Frontend Files

1. **`client/src/utils/api.js`**
   - Lines 140-172: Enhanced logging for data source and roadmap structure
   - Lines 239-265: Fixed resource mapping with proper fallbacks
   - Lines 256-265: Fixed project skills mapping
   - Lines 308-330: Added GitHub projects and final summary logging

2. **`client/src/components/ResourceCard.jsx`**
   - Lines 65-110: Added validation for missing URLs
   - Non-clickable cards for resources without links
   - "No link" badge for resources without URLs
   - Maintains visual consistency

3. **`client/src/pages/PathwayPage.jsx`**
   - Lines 527-580: Added GitHub Projects section
   - Grid layout with project cards
   - Shows stars, language, description
   - Links to GitHub repositories

### Backend Files (Previously Fixed)

4. **`server/.env`**
   - Fixed `WATSONX_APIKEY` → `WATSONX_API_KEY`

5. **`server/services/watsonx_service.py`**
   - Added comprehensive logging for IAM token and WatsonX API calls
   - Shows initialization status, request/response details

6. **`server/routes/roadmap.py`**
   - Added success/fallback banners in logs
   - Shows when WatsonX is used vs fallback data

---

## Data Flow

### Backend → Frontend Flow:

```
1. User submits form
   ↓
2. Frontend calls /api/generate-roadmap
   ↓
3. Backend generates roadmap (WatsonX or fallback)
   ↓
4. Backend returns JSON:
   {
     success: true,
     careerGoal: "...",
     roadmap: {
       phases: [...],
       weeklyPlan: [...],
       resources: [...],
       githubProjects: [...],
       portfolioProjects: [...],
       ...
     },
     metadata: {
       usedWatsonx: true/false,
       ...
     }
   }
   ↓
5. Frontend transforms to pathway format
   ↓
6. Frontend displays in UI
```

### Resource Mapping:

**Backend sends:**
```json
{
  "title": "Cisco Networking Basics",
  "type": "course",
  "url": "https://www.netacad.com/..."
}
```

**Frontend maps to:**
```javascript
{
  title: "Cisco Networking Basics",
  type: "course",
  url: "https://www.netacad.com/...",
  duration: "1-2 hours",  // default
  isFree: true            // default
}
```

### GitHub Project Mapping:

**Backend sends:**
```json
{
  "name": "awesome-project",
  "description": "A great learning project",
  "url": "https://github.com/...",
  "stars": 1234,
  "language": "Python"
}
```

**Frontend maps to:**
```javascript
{
  name: "awesome-project",
  description: "A great learning project",
  url: "https://github.com/...",
  stars: 1234,
  language: "Python",
  topics: []  // default
}
```

---

## Testing Instructions

### 1. Check Console Logs

Open browser DevTools (F12) → Console tab

**Expected logs when generating roadmap:**

```
================================================================================
🔄 TRANSFORMING ROADMAP TO PATHWAY FORMAT
================================================================================
📦 Raw backend response: { ... }
📋 Form data: { ... }

================================================================================
✅ USING WATSONX.AI GENERATED ROADMAP
   Model: ibm/granite-3-8b-instruct
   Tokens: 1234
   GitHub Projects: Yes
   Local Resources: 15
================================================================================

📊 Roadmap structure:
   Phases: 3
   Weekly Plans: 8
   Skills: 12
   Resources: 25
   GitHub Projects: 5
   Portfolio Projects: 3

📚 Week 1 resources (5):
   Resource 1: { title: "...", type: "course", url: "...", ... }
   Resource 2: { ... }
   ...

🎯 Week 1 project: { title: "...", skills: [...] }

================================================================================
✅ TRANSFORMATION COMPLETE
================================================================================
📦 Pathway title: SOC Analyst Career Pathway
📅 Weeks: 8
📚 Total resources across all weeks: 40
🐙 GitHub projects: 5
🎓 Certifications: 3
🤖 Used WatsonX: Yes
================================================================================
```

### 2. Verify Resource Cards

**Check that resource cards show:**
- ✅ Actual resource titles (not "Learning Resource")
- ✅ Resource type (course, video, article, etc.)
- ✅ Duration estimate
- ✅ "Free" badge if applicable
- ✅ Clickable link (or "No link" badge if unavailable)

### 3. Verify GitHub Projects

**Check that GitHub section appears with:**
- ✅ Section title: "Recommended GitHub Projects"
- ✅ Project cards in grid layout
- ✅ Project name, description, stars
- ✅ Programming language badge
- ✅ "View on GitHub" link

### 4. Verify Project Skills

**Check that guided project cards show:**
- ✅ Project title matches week focus
- ✅ Skills listed are relevant to the project
- ✅ No unrelated skills (e.g., Linux skills on a Sales project)

### 5. Verify Data Source

**In console, check:**
- ✅ "USING WATSONX.AI GENERATED ROADMAP" (if WatsonX works)
- ⚠️ "USING FALLBACK TEMPLATE DATA" (if WatsonX fails)
- ✅ Metadata shows correct counts

---

## Expected Behavior

### ✅ With WatsonX Working:

1. **Resources:**
   - Each week has different, relevant resources
   - Resource titles are specific (e.g., "Cisco Networking Basics")
   - URLs are clickable and lead to actual resources
   - Types are accurate (course, video, article, etc.)

2. **GitHub Projects:**
   - Section appears with 3-5 projects
   - Projects are relevant to career goal
   - Star counts and languages are shown
   - Links work and go to GitHub

3. **Guided Projects:**
   - Each week has a unique project
   - Project title matches week focus
   - Skills listed are relevant to the project
   - No skill mismatches

4. **Console Logs:**
   - Show "USING WATSONX.AI GENERATED ROADMAP"
   - Show actual data counts
   - Show per-week resource details

### ⚠️ With Fallback Data:

1. **Resources:**
   - Still show actual resource names from local data
   - URLs still work (from `server/data/resources.json`)
   - May be less personalized but still useful

2. **GitHub Projects:**
   - May be empty or generic
   - Console shows "GitHub Projects: 0"

3. **Guided Projects:**
   - Generic but still unique per week
   - Skills match career goal from local data

4. **Console Logs:**
   - Show "USING FALLBACK TEMPLATE DATA"
   - Show reason for fallback

---

## Common Issues & Solutions

### Issue: Resources still show "Learning Resource"

**Cause:** Backend not returning resources or transformation failing

**Debug:**
1. Check console for "📚 Week X resources" logs
2. Check if `resourcesForWeek` array is empty
3. Check backend response in "📦 Raw backend response" log
4. Verify `roadmap.resources` exists in backend response

**Solution:**
- If backend returns empty resources, check `server/data/resources.json`
- If transformation fails, check field name mismatches

### Issue: GitHub projects not showing

**Cause:** Backend not returning GitHub projects or section hidden

**Debug:**
1. Check console for "🐙 GitHub projects: X"
2. Check if `pathway.githubProjects` exists
3. Check backend response for `githubProjects` array
4. Check if section is conditionally hidden

**Solution:**
- Verify GitHub API is working in backend
- Check `metadata.usedGitHub` in backend response
- Ensure `pathway.githubProjects.length > 0`

### Issue: Project skills don't match project title

**Cause:** Skills being pulled from wrong source

**Debug:**
1. Check console for "🎯 Week X project" logs
2. Check which skills array is being used
3. Verify `projectForWeek.skills` exists

**Solution:**
- Ensure backend returns project-specific skills
- Check skill mapping priority in transformation

---

## API Response Shape

### Expected Backend Response:

```json
{
  "success": true,
  "careerGoal": "SOC Analyst",
  "roadmap": {
    "summary": "...",
    "phases": [
      {
        "phase": 1,
        "title": "Foundation & Setup",
        "duration": "Weeks 1-4",
        "focus": "...",
        "skills": ["Networking", "Linux", "Security Basics"]
      }
    ],
    "weeklyPlan": [
      {
        "week": 1,
        "focus": "Environment Setup & Security Basics",
        "topics": ["Setting up lab", "Basic concepts", "First exercises"],
        "dailyTasks": ["Install tools", "Learn basics", "Complete tutorials"],
        "resources": [...]
      }
    ],
    "skills": ["Networking", "Linux", "Security", ...],
    "tools": ["Wireshark", "Nmap", "Metasploit", ...],
    "resources": [
      {
        "title": "Cisco Networking Basics",
        "type": "course",
        "url": "https://..."
      }
    ],
    "githubProjects": [
      {
        "name": "awesome-security-tools",
        "description": "...",
        "url": "https://github.com/...",
        "stars": 1234,
        "language": "Python"
      }
    ],
    "portfolioProjects": [
      {
        "title": "Build a Network Scanner",
        "description": "...",
        "skills": ["Python", "Networking", "Security"]
      }
    ],
    "resumeBullets": [...],
    "nextSteps": [...],
    "certifications": [...]
  },
  "metadata": {
    "usedWatsonx": true,
    "usedGitHub": true,
    "matchedLocalResources": 15,
    "model": "ibm/granite-3-8b-instruct",
    "tokens": 1234
  }
}
```

---

## Success Criteria

✅ Resource cards show actual resource names
✅ Resource URLs are clickable (or show "No link" badge)
✅ GitHub projects section appears when data is available
✅ Project skills match project titles
✅ Console logs clearly show data source (WatsonX vs fallback)
✅ Each week has unique content (not repeated)
✅ Frontend displays backend data, not hardcoded placeholders

---

## Next Steps

1. **Test with real WatsonX data:**
   - Generate a roadmap
   - Check console logs
   - Verify all sections display correctly

2. **Test with fallback data:**
   - Temporarily break WatsonX (invalid API key)
   - Verify fallback data still works
   - Check console shows fallback reason

3. **Verify field mappings:**
   - Check that all backend fields are mapped
   - Ensure no data is lost in transformation
   - Verify defaults are reasonable

4. **User testing:**
   - Generate roadmaps for different career goals
   - Verify content is unique and relevant
   - Check that resources and projects match the goal

---

**Made with Bob - AI Career Roadmap Generator**