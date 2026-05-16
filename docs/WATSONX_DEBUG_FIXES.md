# WatsonX.ai Integration Debug & Fixes

## Date: 2026-05-16

## Issues Found and Fixed

### 1. ❌ Environment Variable Name Mismatch (CRITICAL)

**Problem:**
- `.env` file had `WATSONX_APIKEY` (no underscore)
- Code was looking for `WATSONX_API_KEY` (with underscore)
- This caused WatsonX to fail silently and use fallback data

**Fix:**
- Changed `.env` file from `WATSONX_APIKEY` to `WATSONX_API_KEY`
- **File:** `server/.env` line 14

**Impact:** This was the root cause preventing WatsonX from working at all.

---

### 2. ❌ Repetitive Daily Plans

**Problem:**
- Frontend transformation was generating the same generic tasks for every day:
  - "Study Foundation & Setup"
  - "Practice with hands-on exercises"
  - "Work on weekly project"
- This made it look like mock data even when WatsonX was working

**Fix:**
- Enhanced `transformRoadmapToPathway()` in `client/src/utils/api.js` to:
  - Use AI-generated `dailyTasks` from WatsonX response
  - Use AI-generated `topics` for each week
  - Create varied tasks based on week focus and day number
  - Distribute resources differently across weeks
  - Generate unique project descriptions per week

**Files Changed:**
- `client/src/utils/api.js` lines 163-210

---

### 3. ❌ Weak WatsonX Prompt

**Problem:**
- Original prompt didn't emphasize unique weekly content
- Didn't request structured daily tasks or topics per week
- Could result in generic or repetitive AI responses

**Fix:**
- Enhanced prompt in `server/services/watsonx_service.py` to:
  - Explicitly request UNIQUE focus for each week
  - Request `topics` array (3-5 specific topics per week)
  - Request `dailyTasks` array (3-5 unique tasks per week)
  - Request week-specific resources
  - Emphasize progressive difficulty across weeks
  - Provide examples of good weekly progression

**Files Changed:**
- `server/services/watsonx_service.py` lines 210-260

---

### 4. ❌ Insufficient Logging

**Problem:**
- No clear indication in logs whether WatsonX or fallback data was used
- Hard to debug when AI generation failed
- No visibility into what was happening

**Fix:**
- Added prominent logging in `server/routes/roadmap.py`:
  - Clear banner when attempting WatsonX generation
  - Success banner with model info and token count
  - Warning banner when using fallback data
  - Logs career goal, timeframe, and skills
  
- Added frontend console logging in `client/src/utils/api.js`:
  - Shows whether WatsonX data was used
  - Shows model and token info if available
  - Warns if fallback data is being used

**Files Changed:**
- `server/routes/roadmap.py` lines 294-325
- `client/src/utils/api.js` lines 147-156

---

### 5. ✅ Improved Fallback Roadmap

**Problem:**
- Fallback roadmap had generic weekly plans
- All weeks looked the same
- Didn't use career-specific data

**Fix:**
- Enhanced `create_fallback_roadmap()` in `server/routes/roadmap.py`:
  - Each week now has unique focus based on career goal
  - Uses actual skills and tools from role data
  - Includes specific topics and daily tasks per week
  - Progressive difficulty from setup → practice → projects → job prep
  - Career-specific content in week titles and tasks

**Files Changed:**
- `server/routes/roadmap.py` lines 228-295

---

## Files Modified Summary

1. **server/.env** - Fixed environment variable name
2. **server/services/watsonx_service.py** - Enhanced AI prompt for unique weekly content
3. **server/routes/roadmap.py** - Added logging and improved fallback roadmap
4. **client/src/utils/api.js** - Improved transformation to use AI data and added logging

## New Files Created

1. **server/test_env.py** - Test script to verify environment variables are loaded correctly

---

## Testing Instructions

### Step 1: Verify Environment Variables

Run the test script to confirm environment variables are loaded:

```bash
cd server
python test_env.py
```

**Expected Output:**
```
✅ WATSONX_API_KEY: Aug4dxCz...1Os
✅ WATSONX_PROJECT_ID: 7b87f934-d744-4e87-bb84-cb738ecc8044
✅ WATSONX_URL: https://us-south.ml.cloud.ibm.com/
✅ WATSONX_MODEL_ID: ibm/granite-3-8b-instruct

✅ All required WatsonX variables are present!
```

If you see `❌ WATSONX_API_KEY: NOT FOUND`, the .env file is not being read correctly.

---

### Step 2: Start the Backend

```bash
cd server
uvicorn main:app --reload
```

**Watch for these logs:**
- On startup, you should NOT see "WATSONX_API_KEY not found"
- If you do, the .env file is not being loaded

---

### Step 3: Start the Frontend

```bash
cd client
npm run dev
```

---

### Step 4: Generate a Roadmap

1. Open http://localhost:5173
2. Fill out the form:
   - Career Goal: "SOC Analyst" (or any role)
   - Skill Level: Beginner
   - Weeks: 6
   - Days per week: 5
   - Hours per day: 2
3. Click "Generate My Pathway"

---

### Step 5: Check Backend Logs

**If WatsonX is working, you'll see:**
```
================================================================================
🤖 ATTEMPTING WATSONX.AI ROADMAP GENERATION
================================================================================
Career Goal: SOC Analyst
Timeframe: 2 months
Current Skills: []
================================================================================
✅ SUCCESS: WATSONX.AI GENERATED ROADMAP
================================================================================
Model: ibm/granite-3-8b-instruct
Tokens: 1234
Phases: 3
Weekly Plans: 8
================================================================================
```

**If WatsonX fails, you'll see:**
```
================================================================================
⚠️  FALLBACK: WATSONX.AI UNAVAILABLE - USING TEMPLATE DATA
================================================================================
This means the roadmap will be generic and not AI-personalized
Check WatsonX API key and credentials in .env file
================================================================================
```

---

### Step 6: Check Frontend Console

Open browser DevTools (F12) and check the Console tab.

**If WatsonX is working:**
```
✅ USING WATSONX.AI GENERATED ROADMAP
   Model: ibm/granite-3-8b-instruct
   Tokens: 1234
```

**If using fallback:**
```
⚠️  USING FALLBACK TEMPLATE DATA (WatsonX unavailable)
   Reason: watsonx.ai unavailable or failed
```

---

### Step 7: Verify Unique Weekly Content

Check the generated roadmap:

**Good Signs (WatsonX working):**
- Each week has a different focus (not "Getting started and learning fundamentals" repeated)
- Daily tasks are specific and varied
- Resources are relevant to the career goal
- Week 1 might be "Environment Setup & Security Basics"
- Week 2 might be "Network Fundamentals & Protocols"
- Week 3 might be "Threat Detection & Analysis"
- etc.

**Bad Signs (Fallback data or poor AI response):**
- All weeks say similar things
- Daily tasks are generic
- Resources are the same every week

---

## Common Issues & Solutions

### Issue: "WATSONX_API_KEY not found in environment variables"

**Solution:**
1. Verify `.env` file exists in `server/` directory
2. Verify it contains `WATSONX_API_KEY=` (with underscore)
3. Restart the backend server
4. Run `server/test_env.py` to verify

---

### Issue: Backend starts but roadmap is still generic

**Solution:**
1. Check backend logs for the WatsonX banners
2. If you see "FALLBACK" banner, WatsonX is failing
3. Possible causes:
   - Invalid API key
   - Invalid project ID
   - Network issues
   - WatsonX service down
4. Check the error logs above the fallback banner for details

---

### Issue: Frontend shows "Cannot connect to server"

**Solution:**
1. Verify backend is running on http://localhost:8000
2. Check CORS settings in `server/main.py`
3. Try accessing http://localhost:8000/docs directly

---

### Issue: Daily plans still look repetitive

**Solution:**
1. Check if WatsonX is actually being used (see logs)
2. If using WatsonX but still repetitive:
   - The AI might need a better prompt
   - Try increasing `max_tokens` in `watsonx_service.py`
   - Try different career goals to see if it's goal-specific
3. If using fallback, the improved fallback should still have unique weeks

---

## Expected Behavior After Fixes

### ✅ With WatsonX Working:
- Backend logs show "SUCCESS: WATSONX.AI GENERATED ROADMAP"
- Frontend console shows "USING WATSONX.AI GENERATED ROADMAP"
- Each week has unique focus, topics, and tasks
- Resources are relevant to the career goal
- Daily tasks are specific and varied
- Projects are career-specific

### ✅ With Fallback (WatsonX unavailable):
- Backend logs show "FALLBACK: WATSONX.AI UNAVAILABLE"
- Frontend console shows "USING FALLBACK TEMPLATE DATA"
- Each week still has unique focus (improved fallback)
- Weekly plans progress from setup → practice → projects → job prep
- Uses career-specific skills and tools from local data
- Still better than the old repetitive fallback

---

## Architecture Notes

### Environment Variable Loading Flow:
1. `server/main.py` loads `.env` BEFORE importing other modules (line 6-7)
2. `server/services/watsonx_service.py` also loads `.env` as backup (line 10-11)
3. Both use `Path(__file__).parent / '.env'` to ensure correct path
4. Variables are accessed via `os.getenv("WATSONX_API_KEY")`

### Roadmap Generation Flow:
1. Frontend calls `/api/generate-roadmap` with career goal and timeframe
2. Backend matches role data from `server/data/roles.json`
3. Backend loads resources from `server/data/resources.json`
4. Backend searches GitHub for relevant projects
5. Backend calls WatsonX with enhanced prompt
6. If WatsonX succeeds, returns AI-generated roadmap
7. If WatsonX fails, returns improved fallback roadmap
8. Frontend transforms response to match UI expectations
9. Frontend uses AI-provided topics and tasks when available

### Data Flow:
```
User Input → Backend Route → WatsonX Service → AI Response
                ↓                                    ↓
         Local Data (roles,              Transform to JSON
         resources, projects)                       ↓
                ↓                          Return to Frontend
         Fallback Roadmap ←─────────────────────────┘
                ↓
         Frontend Transform → Display in UI
```

---

## Maintenance Notes

### To Update WatsonX Prompt:
- Edit `server/services/watsonx_service.py` lines 210-260
- Test with various career goals
- Monitor token usage (shown in logs)

### To Update Fallback Roadmap:
- Edit `server/routes/roadmap.py` lines 228-295
- Ensure each week has unique focus
- Use career-specific data when available

### To Update Frontend Transformation:
- Edit `client/src/utils/api.js` lines 163-210
- Ensure it handles both WatsonX and fallback data
- Test with various timeframes and career goals

---

## Success Criteria

✅ Backend starts without "WATSONX_API_KEY not found" error
✅ Backend logs clearly show whether WatsonX or fallback is used
✅ Frontend console shows data source (WatsonX vs fallback)
✅ Each week has unique focus and tasks
✅ Daily plans are specific and varied
✅ Resources are relevant to career goal
✅ Fallback data is still useful if WatsonX fails

---

## Next Steps

1. Test with various career goals (SOC Analyst, Web Developer, Data Scientist, etc.)
2. Monitor WatsonX token usage and costs
3. Collect user feedback on roadmap quality
4. Consider adding more career-specific data to `server/data/` files
5. Consider caching WatsonX responses to reduce API calls
6. Consider adding user authentication to track roadmap history

---

## Contact

If issues persist after following this guide:
1. Check all files were modified correctly
2. Restart both backend and frontend
3. Clear browser cache and localStorage
4. Check WatsonX API key is valid and has credits
5. Review full error logs in backend terminal

---

**Made with Bob - AI Career Roadmap Generator**