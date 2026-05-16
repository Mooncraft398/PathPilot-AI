# API Integration Notes

## Overview

PathPilot AI integrates with two external APIs to provide comprehensive career guidance:

1. **O*NET Web Services** - Official occupation, skills, and task data
2. **USAJOBS API** - Live federal job postings and market demand signals

## Why These APIs?

### O*NET Web Services
- **Purpose**: Provides authoritative data on occupations, skills, tasks, and knowledge requirements
- **Authentication**: X-API-Key header
- **Use Case**: Career exploration, skill mapping, and understanding occupation requirements
- **Data Source**: U.S. Department of Labor's Occupational Information Network
- **Benefits**: 
  - Standardized occupation codes (SOC)
  - Detailed skill and task breakdowns
  - Knowledge, abilities, and work activities data
  - Regular updates from labor market research

### USAJOBS API
- **Purpose**: Access to current federal job openings
- **Use Case**: Real-world job market examples and employer demand signals
- **Data Source**: Official U.S. government job board
- **Benefits**:
  - Live job postings with salary ranges
  - Geographic distribution of opportunities
  - Hiring organization information
  - Direct links to apply

## Data Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     PathPilot AI Backend                     │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Static JSON Files (server/data/)                            │
│  ├── careers.json      ← Fallback career data               │
│  ├── resources.json    ← Learning resources                 │
│  └── projects.json     ← Project ideas                       │
│                                                               │
│  External APIs (server/services/)                            │
│  ├── onet_service.py   ← O*NET occupation data              │
│  └── usajobs_service.py ← Live job postings                 │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Important**: Static JSON files in `server/data/` remain the primary fallback data source. External APIs supplement this data with:
- Real-time job market information
- Detailed occupation taxonomies
- Current salary ranges
- Geographic job distribution

## API Credentials Setup

### Required Environment Variables

Create a `.env` file in the `server/` directory with the following variables:

```env
# O*NET Web Services API Key
ONET_API_KEY=your_onet_api_key

# USAJOBS API Credentials
USAJOBS_EMAIL=your_email@example.com
USAJOBS_API_KEY=your_usajobs_api_key
```

### How to Obtain Credentials

#### O*NET Web Services
1. Visit: https://services.onetcenter.org/ or https://api-v2.onetcenter.org/
2. Click "Register" to create an account
3. After registration, you'll receive your API key
4. Add it to your `.env` file as `ONET_API_KEY`
5. The API key is sent via the `X-API-Key` HTTP header

#### USAJOBS API
1. Visit: https://developer.usajobs.gov/
2. Create an account or sign in
3. Request API access
4. You'll receive:
   - API Key (Authorization-Key)
   - Use your email as User-Agent
5. Add these to your `.env` file

### Security Notes

- **NEVER commit `.env` files to version control**
- `.env` is already included in `.gitignore`
- API keys are loaded server-side only
- Frontend never has access to API credentials
- Use `.env.example` as a template (without real keys)

## API Endpoints

### O*NET Debug

**Endpoint**: `GET /api/onet/debug`

**Purpose**: Test O*NET API connection without exposing credentials

**Example Request**:
```bash
curl "http://localhost:8000/api/onet/debug"
```

**Response Format**:
```json
{
  "success": true,
  "status_code": 200,
  "api_key_configured": true,
  "response_preview": {
    "api_version": "2.0",
    "api_title": "O*NET Web Services"
  }
}
```

### O*NET Search

**Endpoint**: `GET /api/onet/search`

**Parameters**:
- `keyword` (required): Search term for occupations

**Example Requests**:
```bash
# Search for cybersecurity occupations
curl "http://localhost:8000/api/onet/search?keyword=cybersecurity"

# Search for software engineering occupations
curl "http://localhost:8000/api/onet/search?keyword=software%20engineer"
```

**Response Format**:
```json
{
  "success": true,
  "keyword": "cybersecurity",
  "count": 15,
  "occupations": [
    {
      "code": "15-1212.00",
      "title": "Information Security Analysts",
      "tags": {...}
    }
  ]
}
```

### USAJOBS Search

**Endpoint**: `GET /api/usajobs/search`

**Parameters**:
- `keyword` (required): Search term for jobs
- `location` (optional): Location filter (city, state, or zip code)

**Example Requests**:
```bash
# Search for cybersecurity jobs nationwide
curl "http://localhost:8000/api/usajobs/search?keyword=cybersecurity"

# Search for cybersecurity jobs in Orlando
curl "http://localhost:8000/api/usajobs/search?keyword=cybersecurity&location=Orlando"

# Search for data analyst jobs in Florida
curl "http://localhost:8000/api/usajobs/search?keyword=data%20analyst&location=Florida"
```

**Response Format**:
```json
{
  "success": true,
  "keyword": "cybersecurity",
  "location": "Orlando",
  "count": 25,
  "jobs": [
    {
      "title": "Cybersecurity Specialist",
      "organization": "Department of Defense",
      "location": "Orlando, FL",
      "url": "https://www.usajobs.gov/job/...",
      "minimumSalary": 75000,
      "maximumSalary": 120000,
      "summary": "Job description..."
    }
  ]
}
```

## Testing the Integration

### 1. Set Up Environment

```bash
# Navigate to server directory
cd server

# Create .env file with your credentials
# (Use the format shown above)

# Install dependencies (if not already installed)
pip install -r requirements.txt
```

### 2. Start the Backend Server

```bash
# From the server directory
python main.py

# Or using uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The server will start at `http://localhost:8000`

### 3. Test the Endpoints

#### Using Browser
- O*NET: http://localhost:8000/api/onet/search?keyword=cybersecurity
- USAJOBS: http://localhost:8000/api/usajobs/search?keyword=cybersecurity
- USAJOBS with location: http://localhost:8000/api/usajobs/search?keyword=cybersecurity&location=Orlando

#### Using curl
```bash
# Test O*NET
curl "http://localhost:8000/api/onet/search?keyword=cybersecurity"

# Test USAJOBS
curl "http://localhost:8000/api/usajobs/search?keyword=cybersecurity"

# Test USAJOBS with location
curl "http://localhost:8000/api/usajobs/search?keyword=cybersecurity&location=Orlando"
```

#### Using FastAPI Docs
Visit http://localhost:8000/docs for interactive API documentation where you can test all endpoints.

### 4. Verify Error Handling

Test with missing credentials:
```bash
# Temporarily rename .env to test error handling
mv .env .env.backup

# Start server - should show credential errors
python main.py

# Restore .env
mv .env.backup .env
```

## Error Handling

Both services include comprehensive error handling:

### Missing Credentials
```json
{
  "success": false,
  "error": "O*NET API key not found. Please set ONET_API_KEY environment variable.",
  "keyword": "cybersecurity",
  "count": 0,
  "occupations": []
}
```

### API Request Failures
```json
{
  "success": false,
  "error": "O*NET API request failed with status 401",
  "keyword": "cybersecurity",
  "count": 0,
  "occupations": []
}
```

### Empty Results
```json
{
  "success": true,
  "keyword": "nonexistentjob12345",
  "count": 0,
  "jobs": []
}
```

## Integration with Frontend

The frontend can call these endpoints to:

1. **Enhance Career Exploration**
   - Show real O*NET occupation data
   - Display current job market demand
   - Provide salary expectations

2. **Validate Career Paths**
   - Check if suggested careers have active job postings
   - Show geographic availability of opportunities
   - Link to real job applications

3. **Enrich User Experience**
   - Real-time data instead of static content
   - Current market trends
   - Direct pathways to employment

### Example Frontend Integration

```javascript
// Fetch O*NET occupations
const searchOccupations = async (keyword) => {
  const response = await fetch(
    `http://localhost:8000/api/onet/search?keyword=${encodeURIComponent(keyword)}`
  );
  return await response.json();
};

// Fetch USAJOBS postings
const searchJobs = async (keyword, location = null) => {
  let url = `http://localhost:8000/api/usajobs/search?keyword=${encodeURIComponent(keyword)}`;
  if (location) {
    url += `&location=${encodeURIComponent(location)}`;
  }
  const response = await fetch(url);
  return await response.json();
};
```

## Rate Limits and Best Practices

### O*NET Web Services
- No strict rate limits documented
- Use reasonable request intervals
- Cache results when possible

### USAJOBS API
- Rate limit: Not strictly enforced but be respectful
- Recommended: Cache results for 1-24 hours
- Update job listings periodically, not on every page load

### Best Practices
1. **Cache API responses** to reduce external calls
2. **Implement retry logic** for transient failures
3. **Use fallback data** from static JSON files
4. **Monitor API usage** to stay within limits
5. **Handle errors gracefully** with user-friendly messages

## Future Enhancements

Potential improvements to the API integration:

1. **Response Caching**
   - Implement Redis or in-memory caching
   - Cache O*NET data for 24 hours
   - Cache USAJOBS data for 1-6 hours

2. **Advanced Filtering**
   - Salary range filters
   - Experience level filters
   - Education requirement filters

3. **Data Enrichment**
   - Combine O*NET and USAJOBS data
   - Cross-reference occupation codes
   - Aggregate salary data

4. **Analytics**
   - Track popular searches
   - Monitor API performance
   - Identify trending careers

## Troubleshooting

### Common Issues

**Issue**: "O*NET API key not found"
- **Solution**: Ensure `.env` file exists in `server/` directory with `ONET_API_KEY`

**Issue**: "USAJOBS authentication failed"
- **Solution**: Verify `USAJOBS_API_KEY` and `USAJOBS_EMAIL` are correct in `.env`

**Issue**: "Module not found" errors
- **Solution**: Run `pip install -r requirements.txt` from server directory

**Issue**: Empty results from APIs
- **Solution**: Try different keywords; some terms may not have matches

**Issue**: Timeout errors
- **Solution**: Check internet connection; APIs may be temporarily unavailable

## Support and Resources

- **O*NET Documentation**: https://services.onetcenter.org/reference/
- **USAJOBS API Docs**: https://developer.usajobs.gov/API-Reference/
- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **Project Repository**: Check README.md for project-specific information

---

**Last Updated**: 2026-05-16
**Maintained By**: PathPilot AI Development Team