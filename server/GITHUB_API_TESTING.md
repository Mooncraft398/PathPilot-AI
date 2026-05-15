# GitHub API Integration - Testing Guide

## Overview
The GitHub API integration allows searching for beginner project examples based on skills.

## Endpoint
```
GET /api/github-projects/{skill}
```

## Setup

### 1. Install Dependencies
```bash
cd server
pip install -r requirements.txt
```

### 2. Optional: Add GitHub Token (Recommended)
Create a `.env` file in the `server` directory:
```bash
cp .env.example .env
```

Edit `.env` and add your GitHub token:
```
GITHUB_TOKEN=your_github_personal_access_token_here
```

Get a token at: https://github.com/settings/tokens
- Select "Generate new token (classic)"
- No special scopes needed for public repository search
- This increases rate limit from 60 to 5000 requests/hour

### 3. Start the Server
```bash
cd server
python main.py
```

Or with uvicorn:
```bash
uvicorn main:app --reload
```

## Testing

### Option 1: Browser
Open your browser and visit:
- http://localhost:8000/api/github-projects/python
- http://localhost:8000/api/github-projects/react
- http://localhost:8000/api/github-projects/cybersecurity

### Option 2: API Documentation
Visit the interactive API docs:
- http://localhost:8000/docs

Click on the `/api/github-projects/{skill}` endpoint and try it out.

### Option 3: cURL
```bash
# Search for Python beginner projects
curl http://localhost:8000/api/github-projects/python

# Search for React beginner projects
curl http://localhost:8000/api/github-projects/react

# Search for Cybersecurity beginner projects
curl http://localhost:8000/api/github-projects/cybersecurity
```

### Option 4: Postman
1. Create a new GET request
2. URL: `http://localhost:8000/api/github-projects/python`
3. Send

## Expected Response

### Success Response
```json
{
  "skill": "python",
  "repositories": [
    {
      "name": "owner/repo-name",
      "description": "A beginner-friendly Python project",
      "stars": 1234,
      "language": "Python",
      "url": "https://github.com/owner/repo-name"
    }
  ],
  "total_count": 50000
}
```

### Error Response (Rate Limit)
```json
{
  "error": "Rate limit exceeded",
  "detail": "GitHub API rate limit reached. Please try again later or add a GITHUB_TOKEN to your .env file for higher limits."
}
```

## Skills to Test
Based on our data files, test with these skills:
- Networking
- Linux
- Python
- SQL
- React
- Git
- Troubleshooting
- Cybersecurity
- Cloud Basics
- Excel
- Security Monitoring
- Incident Response

## Notes
- Without authentication: 60 requests/hour
- With GitHub token: 5000 requests/hour
- Results are sorted by stars (most popular first)
- Returns top 5 repositories only
- Search query format: "{skill} beginner project"

## Troubleshooting

### Import Error for httpx
If you get an import error, install httpx:
```bash
pip install httpx==0.25.0
```

### CORS Issues
The API is configured to accept requests from:
- http://localhost:5173 (Vite)
- http://localhost:3000 (React)
- http://127.0.0.1:5173
- http://127.0.0.1:3000

### Rate Limit Issues
Add a GITHUB_TOKEN to your .env file to increase the rate limit.

## Made with Bob