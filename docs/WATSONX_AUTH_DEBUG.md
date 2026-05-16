# WatsonX Authentication Debugging Guide

## Issue: IAM Token Authentication Failing

The backend is failing to get an IBM Cloud IAM token, which prevents WatsonX.ai from working.

---

## Required Environment Variables

Your `server/.env` file MUST have these exact variable names:

```env
WATSONX_API_KEY=your_ibm_cloud_api_key_here
WATSONX_PROJECT_ID=your_watsonx_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-3-8b-instruct
```

### Important Notes:

1. **WATSONX_API_KEY** - This is your IBM Cloud API key (NOT a project ID, NOT a service credential name)
   - Get it from: https://cloud.ibm.com/iam/apikeys
   - Format: Starts with letters/numbers, about 44 characters long
   - Example format: `Aug4dxCzJZyroRx6eQ-zp0p4yb-cZwGI46JGaJZl1Os`

2. **WATSONX_PROJECT_ID** - Your WatsonX.ai project ID (UUID format)
   - Get it from: https://dataplatform.cloud.ibm.com/projects
   - Format: UUID like `7b87f934-d744-4e87-bb84-cb738ecc8044`

3. **WATSONX_URL** - The WatsonX API endpoint for your region
   - US South: `https://us-south.ml.cloud.ibm.com`
   - EU: `https://eu-de.ml.cloud.ibm.com`
   - Must match your project's region

4. **WATSONX_MODEL_ID** - The model to use
   - Default: `ibm/granite-3-8b-instruct`
   - Must be available in your project

---

## Step 1: Verify Environment Variables

Run the test script to check if variables are loaded:

```bash
cd server
python test_env.py
```

**Expected Output:**
```
✅ WATSONX_API_KEY: Aug4dxCz...1Os
✅ WATSONX_PROJECT_ID: 7b87f934-d744-4e87-bb84-cb738ecc8044
✅ WATSONX_URL: https://us-south.ml.cloud.ibm.com
✅ WATSONX_MODEL_ID: ibm/granite-3-8b-instruct

✅ All required WatsonX variables are present!
```

**If you see ❌ for any variable:**
- Check that `.env` file exists in `server/` directory
- Check variable names match exactly (case-sensitive)
- Check there are no extra spaces or quotes around values
- Restart your terminal/IDE after editing `.env`

---

## Step 2: Test IAM Authentication

Run the authentication test script:

```bash
cd server
python test_watsonx_auth.py
```

This will:
1. Load environment variables
2. Request an IAM token from IBM Cloud
3. Test calling WatsonX API with the token
4. Show detailed error messages if anything fails

### Possible Outcomes:

#### ✅ Success:
```
✅ IAM Token obtained successfully!
   Token: eyJraWQiOiIyMDI0...
   Expires in: 3600 seconds (60.0 minutes)

✅ WatsonX generation successful!
   Generated 45 tokens
```

**Action:** Your credentials are correct! The app should work.

---

#### ❌ IAM Token Failed - HTTP 400:
```
❌ Failed to get IAM token: HTTP 400
   Response: {"errorCode":"BXNIM0415E","errorMessage":"Provided API key could not be found"}
```

**Cause:** Invalid API key

**Fix:**
1. Go to https://cloud.ibm.com/iam/apikeys
2. Create a new API key or copy an existing one
3. Update `WATSONX_API_KEY` in `.env`
4. Make sure you're copying the API key itself, not the name or ID

---

#### ❌ IAM Token Failed - HTTP 403:
```
❌ Failed to get IAM token: HTTP 403
   Response: {"errorCode":"BXNIM0407E","errorMessage":"Forbidden"}
```

**Cause:** API key doesn't have proper permissions

**Fix:**
1. Go to https://cloud.ibm.com/iam/apikeys
2. Check the API key has "Editor" or "Administrator" role
3. Or create a new API key with proper permissions

---

#### ❌ WatsonX API Failed - HTTP 401:
```
✅ IAM Token obtained successfully!
❌ WatsonX API error: HTTP 401
   Response: {"error":"Unauthorized"}
```

**Cause:** Token is valid but doesn't have access to WatsonX

**Fix:**
1. Verify your IBM Cloud account has WatsonX.ai enabled
2. Check you have access to the project
3. Verify the project ID is correct

---

#### ❌ WatsonX API Failed - HTTP 404:
```
✅ IAM Token obtained successfully!
❌ WatsonX API error: HTTP 404
   Response: {"error":"Project not found"}
```

**Cause:** Invalid project ID or wrong region

**Fix:**
1. Go to https://dataplatform.cloud.ibm.com/projects
2. Open your WatsonX project
3. Copy the project ID from the URL or project settings
4. Verify `WATSONX_URL` matches your project's region

---

#### ❌ WatsonX API Failed - HTTP 400 (Model):
```
✅ IAM Token obtained successfully!
❌ WatsonX API error: HTTP 400
   Response: {"error":"Model not found or not accessible"}
```

**Cause:** Model not available in your project

**Fix:**
1. Go to your WatsonX project
2. Check available models in the project
3. Update `WATSONX_MODEL_ID` to a model you have access to
4. Common models:
   - `ibm/granite-3-8b-instruct`
   - `ibm/granite-13b-chat-v2`
   - `meta-llama/llama-2-70b-chat`

---

## Step 3: Test with Backend Running

Start the backend with enhanced logging:

```bash
cd server
uvicorn main:app --reload
```

**Watch for these logs on startup:**

```
🔧 WATSONX SERVICE INITIALIZATION
================================================================================
Loading .env from: c:/path/to/server/.env
.env exists: True
✅ WATSONX_API_KEY: Aug4dxCz...1Os
✅ WATSONX_PROJECT_ID: 7b87f934-d744-4e87-bb84-cb738ecc8044
✅ WATSONX_URL: https://us-south.ml.cloud.ibm.com
✅ WATSONX_MODEL_ID: ibm/granite-3-8b-instruct
================================================================================
```

**If you see:**
- `❌ WATSONX_API_KEY: NOT FOUND` - Environment variable not loaded
- `❌ WATSONX_PROJECT_ID: NOT FOUND` - Environment variable not loaded

**Fix:** Check `.env` file location and variable names

---

## Step 4: Generate a Roadmap

1. Start frontend: `cd client && npm run dev`
2. Open http://localhost:5173
3. Fill out the form and submit
4. Watch backend terminal for detailed logs

### Expected Logs (Success):

```
================================================================================
🤖 ATTEMPTING WATSONX.AI ROADMAP GENERATION
================================================================================
Career Goal: SOC Analyst
Timeframe: 2 months
Current Skills: []

🔑 Requesting new IAM token from IBM Cloud...
IAM Token URL: https://iam.cloud.ibm.com/identity/token
IAM Response Status: 200
✅ IAM token obtained successfully: eyJraWQiOiIyMDI0...

🔐 Getting IAM token for WatsonX...
♻️  Using cached IAM token
✅ IAM token obtained, calling WatsonX API...

WatsonX Endpoint: https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29
Model: ibm/granite-3-8b-instruct
Project ID: 7b87f934-d744-4e87-bb84-cb738ecc8044
WatsonX Response Status: 200
✅ WatsonX generation successful!
Generated 1234 tokens

================================================================================
✅ SUCCESS: WATSONX.AI GENERATED ROADMAP
================================================================================
Model: ibm/granite-3-8b-instruct
Tokens: 1234
Phases: 3
Weekly Plans: 8
================================================================================
```

### Expected Logs (Failure):

```
================================================================================
🤖 ATTEMPTING WATSONX.AI ROADMAP GENERATION
================================================================================

🔑 Requesting new IAM token from IBM Cloud...
IAM Response Status: 400
❌ Failed to get IAM token: HTTP 400
Response body: {"errorCode":"BXNIM0415E","errorMessage":"Provided API key could not be found"}

❌ Failed to get IAM token for watsonx.ai

================================================================================
⚠️  FALLBACK: WATSONX.AI UNAVAILABLE - USING TEMPLATE DATA
================================================================================
This means the roadmap will be generic and not AI-personalized
Check WatsonX API key and credentials in .env file
================================================================================
```

---

## Step 5: Check Frontend Console

Open browser DevTools (F12) → Console tab

### Expected (Success):
```
✅ USING WATSONX.AI GENERATED ROADMAP
   Model: ibm/granite-3-8b-instruct
   Tokens: 1234
```

### Expected (Failure):
```
⚠️  USING FALLBACK TEMPLATE DATA (WatsonX unavailable)
   Reason: watsonx.ai unavailable or failed
```

---

## Common Issues & Solutions

### Issue: "WATSONX_API_KEY not found"

**Symptoms:**
- Backend logs show `❌ WATSONX_API_KEY: NOT FOUND`
- IAM token request never happens

**Solutions:**
1. Check `.env` file exists in `server/` directory (not root)
2. Check variable name is exactly `WATSONX_API_KEY` (with underscore)
3. Check no extra spaces: `WATSONX_API_KEY=value` not `WATSONX_API_KEY = value`
4. Restart backend after editing `.env`

---

### Issue: "Failed to get IAM token: HTTP 400"

**Symptoms:**
- IAM request returns 400
- Error message about invalid API key

**Solutions:**
1. Verify API key is correct (44 characters, alphanumeric with hyphens)
2. Create a new API key at https://cloud.ibm.com/iam/apikeys
3. Make sure you copied the key value, not the name
4. Check for extra spaces or line breaks in `.env`

---

### Issue: "Failed to get IAM token: HTTP 403"

**Symptoms:**
- IAM request returns 403
- Error about forbidden access

**Solutions:**
1. API key doesn't have proper permissions
2. Create new API key with "Editor" or "Administrator" role
3. Check your IBM Cloud account is active

---

### Issue: "WatsonX API error: HTTP 401"

**Symptoms:**
- IAM token obtained successfully
- WatsonX API returns 401

**Solutions:**
1. Token doesn't have access to WatsonX
2. Verify WatsonX.ai is enabled in your IBM Cloud account
3. Check you have access to the project
4. Try creating a new API key

---

### Issue: "WatsonX API error: HTTP 404"

**Symptoms:**
- IAM token obtained successfully
- WatsonX API returns 404

**Solutions:**
1. Invalid project ID - verify at https://dataplatform.cloud.ibm.com/projects
2. Wrong region - check `WATSONX_URL` matches your project's region
3. Project doesn't exist or was deleted

---

### Issue: "Model not found or not accessible"

**Symptoms:**
- IAM token obtained successfully
- WatsonX API returns 400 with model error

**Solutions:**
1. Model not available in your project
2. Check available models in WatsonX project settings
3. Update `WATSONX_MODEL_ID` to an available model
4. Common alternatives:
   - `ibm/granite-13b-chat-v2`
   - `meta-llama/llama-2-70b-chat`
   - `google/flan-ul2`

---

## Verification Checklist

Before asking for help, verify:

- [ ] `.env` file exists in `server/` directory
- [ ] `WATSONX_API_KEY` is set (with underscore)
- [ ] `WATSONX_PROJECT_ID` is set (UUID format)
- [ ] `WATSONX_URL` matches your project's region
- [ ] API key is an IBM Cloud API key (not project ID)
- [ ] API key has proper permissions
- [ ] WatsonX.ai is enabled in your IBM Cloud account
- [ ] You have access to the project
- [ ] Project ID is correct
- [ ] Model is available in your project
- [ ] Backend was restarted after editing `.env`
- [ ] `python test_env.py` shows all variables
- [ ] `python test_watsonx_auth.py` passes both tests

---

## Getting Help

If tests still fail after following this guide:

1. Run `python test_watsonx_auth.py` and save the full output
2. Check backend logs when generating a roadmap
3. Check frontend console logs
4. Provide:
   - Test script output
   - Backend logs (redact API keys)
   - Frontend console logs
   - Your IBM Cloud region
   - Which model you're trying to use

---

## Success Criteria

✅ `test_env.py` shows all variables present
✅ `test_watsonx_auth.py` passes both IAM and WatsonX tests
✅ Backend logs show "✅ SUCCESS: WATSONX.AI GENERATED ROADMAP"
✅ Frontend console shows "✅ USING WATSONX.AI GENERATED ROADMAP"
✅ Generated roadmap has unique weekly content
✅ Daily tasks are specific and varied
✅ Resources are relevant to career goal

---

**Made with Bob - AI Career Roadmap Generator**