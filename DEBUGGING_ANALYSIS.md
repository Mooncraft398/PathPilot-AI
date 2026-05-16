# PathPilot AI - Debugging Analysis

## Issues Identified

### 1. GitHub Projects Not Showing on Frontend ❌

**Root Cause:**
- Backend returns `githubProjects` in `roadmap.githubProjects`
- Frontend transformation correctly maps it to `pathway.githubProjects`
- Frontend PathwayPage DOES render GitHub projects (lines 539-593)
- **BUT**: The condition `pathway.githubProjects && pathway.githubProjects.length > 0` might be failing

**Likely Problems:**
- GitHub API might be failing silently
- `githubProjects` array might be empty
- Backend might not be including GitHub projects in fallback mode
- Field name mismatch somewhere in the chain

**Where GitHub Data Flows:**
1. `server/routes/roadmap.py` line 419: `github_projects = await search_github_for_role(...)`
2. `server/routes/roadmap.py` line 437: Passed to `generate_roadmap_with_ai(..., github_projects=github_projects)`
3. `server/services/watsonx_service.py`: Should include in prompt/response
4. `server/routes/roadmap.py` line 450: `roadmap = ai_roadmap` (from watsonx)
5. `server/routes/roadmap.py` line 502: Fallback includes `github_projects=github_projects`
6. Backend response: `roadmap.githubProjects`
7. `client/src/utils/api.js` line 382: Maps to `pathway.githubProjects`
8. `client/src/pages/PathwayPage.jsx` line 539: Renders if exists

**Fix Required:**
- Ensure backend ALWAYS includes `githubProjects` in response (even if empty array)
- Normalize the field in backend before returning
- Add fallback rendering on frontend

### 2. Timeframe Mismatch ❌

**Root Cause:**
- User selects "6 weeks" in form
- Form calculates: `Math.ceil(6 / 4) = 2 months`
- Backend receives "2 months"
- Frontend shows "2 months" instead of "6 weeks"

**Problem Location:**
- `client/src/components/PathwayForm.jsx` lines 58-59:
  ```javascript
  const months = Math.ceil(formData.weeks / 4);
  const timeframe = `${months} month${months !== 1 ? 's' : ''}`;
  ```

**Fix Required:**
- Preserve original weeks selection
- Send both weeks and calculated timeframe to backend
- Backend should use weeks for generation
- Frontend should display user's original selection
- Add metadata to track both values

### 3. Insufficient Resources for Some Career Paths ❌

**Root Cause:**
- `get_resources_for_skills()` only returns top 3 resources per skill
- Some career paths might not have exact skill matches
- No fallback to related/general resources

**Problem Location:**
- `server/routes/roadmap.py` lines 79-96: `get_resources_for_skills()`
- Only matches exact skill names
- Limited to 3 resources per skill
- No alias matching
- No category fallback

**Fix Required:**
- Improve matching logic with aliases
- Add category-based fallback
- Increase resource count
- Use verified resources as primary source
- Add general beginner resources as last resort

### 4. Missing Verification System ❌

**Current State:**
- Data validation script exists (`validate_data.py`)
- No end-to-end API testing
- No career path verification
- No automated checks

**Fix Required:**
- Create career path validation script
- Create API test script
- Add npm scripts for validation
- Test all 6 supported career paths

### 5. WatsonX Prompt Issues ⚠️

**Current State:**
- Prompt doesn't explicitly preserve timeframe
- Prompt doesn't ground resources/projects
- No instruction to use provided data first

**Fix Required:**
- Update prompt to preserve exact timeframe
- Instruct to use provided resources
- Instruct to include GitHub projects
- Add validation instructions

## Files That Need Changes

### Backend Files:
1. `server/routes/roadmap.py` - Normalize response, improve resource matching
2. `server/services/watsonx_service.py` - Update prompt
3. `server/data/roles.json` - Add aliases for career paths
4. `server/services/resource_validator.py` - Improve matching logic

### Frontend Files:
5. `client/src/components/PathwayForm.jsx` - Preserve weeks, send both values
6. `client/src/pages/PathwayPage.jsx` - Display correct timeframe
7. `client/src/utils/api.js` - Handle metadata properly

### New Files:
8. `server/scripts/validate_career_paths.py` - Career path validator
9. `server/scripts/test_roadmap_api.py` - API tester

## Implementation Plan

### Phase 1: Backend Fixes (Priority 1)
1. Add response normalizer function
2. Improve resource matching with aliases
3. Update watsonx prompt
4. Ensure githubProjects always in response
5. Add timeframe metadata

### Phase 2: Frontend Fixes (Priority 1)
6. Preserve original weeks selection
7. Display user's selected timeframe
8. Handle empty githubProjects gracefully
9. Add debug metadata display

### Phase 3: Validation (Priority 2)
10. Create career path validator
11. Create API test script
12. Add npm scripts
13. Test all career paths

### Phase 4: Data Enhancement (Priority 2)
14. Add career path aliases to roles.json
15. Expand verified resources
16. Add more project ideas
17. Improve skill matching

## Expected Outcomes

After fixes:
- ✅ GitHub projects visible on frontend (or clear "no projects" message)
- ✅ Timeframe matches user selection exactly
- ✅ All career paths have 5+ resources minimum
- ✅ Validation scripts confirm all paths work
- ✅ API tests pass for all scenarios
- ✅ Debug metadata helps troubleshooting