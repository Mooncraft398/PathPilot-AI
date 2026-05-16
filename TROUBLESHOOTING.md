# PathPilot AI - Troubleshooting Guide

## Common Issues and Solutions

### Backend Issues

#### 1. Backend Won't Start

**Symptom:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
cd server
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

#### 2. WatsonX Authentication Fails

**Symptom:** `❌ Failed to get IAM token for watsonx.ai`

**Possible Causes:**
- Invalid `WATSONX_API_KEY`
- Expired API key
- Network connectivity issues

**Solution:**
1. Verify your API key in `.env`:
   ```bash
   # Check if .env exists
   ls server/.env
   
   # Verify API key format (should be long alphanumeric string)
   cat server/.env | grep WATSONX_API_KEY
   ```

2. Test authentication:
   ```bash
   cd server
   python test_watsonx_auth.py
   ```

3. Get a new API key:
   - Go to [IBM Cloud IAM](https://cloud.ibm.com/iam/apikeys)
   - Create new API key
   - Update `WATSONX_API_KEY` in `.env`

#### 3. WatsonX Generation Returns None

**Symptom:** `⚠️ FALLBACK: WATSONX.AI FAILED - USING TEMPLATE DATA`

**Possible Causes:**
- Token limit exceeded (response truncated)
- Invalid project ID
- Model unavailable
- JSON parsing failed

**Solution:**

1. Check logs for specific error:
   ```bash
   # Look for error messages in terminal output
   # Common patterns:
   # - "RESPONSE APPEARS TRUNCATED" → increase max_tokens
   # - "NO JSON OBJECT FOUND" → JSON parsing issue
   # - "HTTP 4xx" → authentication/permission issue
   # - "HTTP 5xx" → IBM service issue (retry)
   ```

2. Verify project ID:
   ```bash
   # Check WATSONX_PROJECT_ID in .env
   # Should be a UUID format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   ```

3. Test with smaller timeframe:
   - Try "1 month" instead of "6 months"
   - Smaller requests are less likely to hit token limits

#### 4. GitHub API Rate Limit

**Symptom:** `❌ GitHub search failed: rate limit exceeded`

**Solution:**
1. Add GitHub token to `.env`:
   ```env
   GITHUB_TOKEN=your_github_personal_access_token
   ```

2. Get token at: https://github.com/settings/tokens
   - No special scopes needed for public repo search
   - Increases rate limit from 60 to 5000 requests/hour

3. App will fall back to verified local projects if GitHub fails

#### 5. Port Already in Use

**Symptom:** `Error: Address already in use`

**Solution:**
```bash
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:8000 | xargs kill -9

# Or use different port:
python -m uvicorn main:app --reload --port 8001
```

### Frontend Issues

#### 1. Frontend Won't Start

**Symptom:** `npm ERR! missing script: dev`

**Solution:**
```bash
cd client
npm install
npm run dev
```

#### 2. Cannot Connect to Backend

**Symptom:** `Cannot connect to server. Make sure the backend is running`

**Solution:**
1. Verify backend is running:
   ```bash
   curl http://localhost:8000/health
   # Should return: {"status":"healthy","message":"API is operational"}
   ```

2. Check CORS configuration in `server/main.py`:
   - Frontend URL should be in `allow_origins`
   - Default: `http://localhost:5173`

3. Check API base URL in `client/src/utils/api.js`:
   ```javascript
   const API_BASE_URL = 'http://localhost:8000';
   ```

#### 3. Roadmap Generation Hangs

**Symptom:** Loading spinner never stops

**Possible Causes:**
- Backend timeout (90s default)
- WatsonX taking too long
- Network issue

**Solution:**
1. Check browser console for errors (F12)
2. Check backend terminal for error messages
3. Try with shorter timeframe
4. Increase timeout in `client/src/utils/api.js`:
   ```javascript
   timeout: 120000, // 2 minutes
   ```

#### 4. Projects/Resources Not Clickable

**Symptom:** Links show as `#` or don't work

**Possible Causes:**
- Invalid URLs in data
- Missing URL field
- Frontend not handling URL field correctly

**Solution:**
1. Run validation script:
   ```bash
   cd server
   python validate_data.py
   ```

2. Check browser console for errors
3. Verify project/resource has `url` field in response

### Data Issues

#### 1. Missing Career Path

**Symptom:** No projects/resources for specific career

**Solution:**
1. Check if career path exists in data files:
   ```bash
   cd server
   python validate_data.py
   ```

2. Add career path to `verified_projects.json` and `verified_resources.json`

3. Update career path mapping in `server/services/project_validator.py`

#### 2. Broken URLs

**Symptom:** Resources/projects have invalid URLs

**Solution:**
1. Run validation to identify broken URLs:
   ```bash
   cd server
   python validate_data.py
   ```

2. Update URLs in data files:
   - `server/data/verified_projects.json`
   - `server/data/verified_resources.json`

3. Resource validator will automatically replace invalid URLs with verified alternatives

### Environment Issues

#### 1. Missing .env File

**Symptom:** `WATSONX_API_KEY not set`

**Solution:**
```bash
cd server
cp .env.example .env
# Edit .env with your actual API keys
```

#### 2. .env Not Loading

**Symptom:** Environment variables not found despite .env existing

**Solution:**
1. Verify .env location:
   ```bash
   ls server/.env
   ```

2. Check .env format (no quotes needed):
   ```env
   WATSONX_API_KEY=your_key_here
   WATSONX_PROJECT_ID=your_project_id
   ```

3. Restart backend after changing .env

### Testing Issues

#### 1. How to Test Without Real API Keys

**Solution:**
- App has fallback mode that works without WatsonX
- Uses template-based roadmap generation
- Still shows GitHub projects (if token provided)
- Still validates and shows local resources/projects

#### 2. How to Test Specific Career Path

**Solution:**
```bash
# Use curl or Postman
curl -X POST http://localhost:8000/api/generate-roadmap \
  -H "Content-Type: application/json" \
  -d '{
    "careerGoal": "SOC Analyst",
    "currentSkills": ["Python", "networking"],
    "timeframe": "3 months"
  }'
```

#### 3. How to Test Multi-Call Strategy

**Solution:**
- Use timeframe >= 3 months (12+ weeks)
- Check logs for "MULTI-CALL ROADMAP GENERATION"
- Verify multiple WatsonX API calls in logs

## Debug Mode

### Enable Verbose Logging

**Backend:**
```python
# In server/main.py, add:
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Frontend:**
```javascript
// In client/src/utils/api.js
// Uncomment console.log statements
```

### Check Logs

**Backend logs:**
- Terminal where `uvicorn` is running
- Look for lines starting with `INFO`, `WARNING`, `ERROR`

**Frontend logs:**
- Browser console (F12 → Console tab)
- Network tab to see API requests/responses

## Performance Issues

### 1. Slow Roadmap Generation

**Causes:**
- Large timeframe (6+ months)
- Multi-call strategy
- Slow WatsonX response

**Solutions:**
- Use shorter timeframes for testing
- Single-call strategy is faster (< 3 months)
- Check IBM Cloud service status

### 2. High Memory Usage

**Causes:**
- Large data files loaded in memory
- Multiple concurrent requests

**Solutions:**
- Restart backend periodically
- Limit concurrent users during demo
- Use production WSGI server (gunicorn) instead of uvicorn

## Getting Help

### 1. Check Existing Documentation
- README.md - Setup and overview
- IMPLEMENTATION_STATUS.md - Current state
- docs/ folder - Detailed technical docs

### 2. Enable Debug Logging
- See "Debug Mode" section above

### 3. Run Validation
```bash
cd server
python validate_data.py
```

### 4. Test Components Individually
```bash
# Test WatsonX auth
python server/test_watsonx_auth.py

# Test backend imports
cd server
python -c "from main import app; print('OK')"

# Test frontend build
cd client
npm run build
```

## Quick Fixes Checklist

- [ ] Virtual environment activated?
- [ ] Dependencies installed? (`pip install -r requirements.txt`)
- [ ] .env file exists with valid keys?
- [ ] Backend running on port 8000?
- [ ] Frontend running on port 5173?
- [ ] CORS configured correctly?
- [ ] Data files validated?
- [ ] Browser console clear of errors?
- [ ] Network tab shows successful API calls?

## Still Having Issues?

1. Check IMPLEMENTATION_STATUS.md for known issues
2. Review error messages carefully
3. Search error message in docs/
4. Try with minimal configuration (1 month, basic career path)
5. Test with fallback mode (no WatsonX keys)

---

**Remember:** This is a hackathon project. Some features may be incomplete or require manual testing. The app is designed to fail gracefully and provide useful fallbacks.