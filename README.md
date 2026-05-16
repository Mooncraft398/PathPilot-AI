# PathPilot AI 🚀

An AI-powered career pathway generator built for the IBM Hackathon. PathPilot AI uses **IBM watsonx.ai** to create personalized, zero-to-resume-ready career roadmaps enriched with GitHub project discovery, curated resources, and real-world job opportunities.

## 🌟 Features

- **AI-Powered Roadmap Generation**: Uses IBM watsonx.ai (Granite models) to generate intelligent, personalized career roadmaps
- **GitHub Project Discovery**: Automatically finds relevant beginner-friendly projects on GitHub
- **Curated Learning Resources**: Matches users with high-quality, free learning resources
- **Real Job Opportunities**: Integrates with USAJOBS API to show actual federal job openings
- **Structured Learning Paths**: Week-by-week plans with skills, tools, certifications, and portfolio projects
- **Resume-Ready Output**: Generates resume bullet points and portfolio project ideas
- **Secure & Private**: All API keys stored securely in environment variables, never exposed to frontend

## 🎯 Supported Career Paths

- **SOC Analyst** - Security Operations Center
- **IT Help Desk** - Technical Support
- **Network Technician** - Network Infrastructure
- **Cybersecurity Analyst** - Information Security
- **Cloud Support Associate** - Cloud Computing
- **Software Developer** - Software Development

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **IBM watsonx.ai** - AI-powered text generation (Granite models)
- **GitHub API** - Project discovery
- **USAJOBS API** - Federal job listings
- **O*NET API** - Career data

### Frontend
- **React** - UI framework
- **Vite** - Build tool
- **TailwindCSS** - Styling
- **Axios** - HTTP client

## 📋 Prerequisites

- **Python 3.8+**
- **Node.js 16+**
- **npm or yarn**
- **IBM Cloud Account** (for watsonx.ai)
- **GitHub Account** (optional, for higher API rate limits)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/PathPilot-AI.git
cd PathPilot-AI
```

### 2. Backend Setup

```bash
cd server

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from example
copy .env.example .env  # Windows
# OR
cp .env.example .env    # macOS/Linux
```

### 3. Configure Environment Variables

Edit `server/.env` and add your API credentials:

```env
# IBM watsonx.ai Configuration (REQUIRED for AI roadmap generation)
WATSONX_API_KEY=your_watsonx_api_key_here
WATSONX_PROJECT_ID=your_watsonx_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com

# GitHub API Configuration (OPTIONAL - for higher rate limits)
GITHUB_TOKEN=your_github_token_here

# O*NET Web Services API Configuration (OPTIONAL)
ONET_API_KEY=your_onet_api_key_here

# USAJOBS API Configuration (OPTIONAL)
USAJOBS_EMAIL=your_email@example.com
USAJOBS_API_KEY=your_usajobs_api_key

# Server Configuration
PORT=5000
ENVIRONMENT=development
```

#### Getting API Keys:

**IBM watsonx.ai** (Required):
1. Go to [IBM Cloud](https://cloud.ibm.com/)
2. Create a watsonx.ai project
3. Get your API key from IBM Cloud IAM
4. Copy your Project ID from watsonx.ai

**GitHub Token** (Optional but recommended):
1. Go to [GitHub Settings > Tokens](https://github.com/settings/tokens)
2. Generate a new personal access token
3. No special scopes needed for public repo search

**O*NET API** (Optional):
1. Register at [O*NET Web Services](https://services.onetcenter.org/)
2. Get your API key from the dashboard

**USAJOBS API** (Optional):
1. Register at [USAJOBS Developer](https://developer.usajobs.gov/)
2. Get your API key and use your email

### 4. Start the Backend

```bash
# Make sure you're in the server directory with venv activated
python -m uvicorn main:app --reload --port 8000
```

The backend will be available at `http://localhost:8000`

API Documentation: `http://localhost:8000/docs`

### 5. Frontend Setup

Open a new terminal:

```bash
cd client

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

## 🧪 Testing

### Automated Testing Scripts

We provide several testing scripts to validate the application:

#### 1. Data Validation
```bash
cd server
python validate_data.py
```
This validates all data files (resources, projects, certifications) for:
- Required fields
- Valid URLs
- Consistent structure
- No duplicates

#### 2. API Endpoint Testing
```bash
cd server
# Make sure backend is running first!
python test_api_endpoints.py
```
This tests the `/api/generate-roadmap` endpoint with:
- Multiple career paths
- Different timeframes (4 weeks, 6 weeks, 3 months, 6 months)
- Various skill combinations
- Response validation

#### 3. Career Path Testing
```bash
cd server
python test_career_paths.py
```
This tests all 6 career paths with different timeframes to ensure:
- Resources are matched correctly
- GitHub projects are found
- Watsonx.ai generates valid roadmaps
- Timeframes are preserved

### Manual Testing

#### Using the Frontend

1. Navigate to `http://localhost:5173`
2. Click "Generate Pathway"
3. Fill in the form:
   - **Career Goal**: "SOC Analyst" (or any supported role)
   - **Timeframe**: Select weeks (4, 6, 8, 12, etc.)
   - **Other settings**: Adjust as needed
4. Click "Generate My Pathway"
5. Verify the roadmap displays:
   - Correct timeframe in the header
   - 5+ learning resources with clickable links
   - GitHub projects (if available)
   - Portfolio project ideas
   - Weekly plan
   - Resume bullets

#### Using the API Directly

```bash
# Test the AI roadmap endpoint
curl -X POST http://localhost:5000/api/generate-roadmap \
  -H "Content-Type: application/json" \
  -d '{
    "careerGoal": "SOC Analyst",
    "currentSkills": ["Python", "basic networking", "Wireshark"],
    "timeframe": "3 months"
  }'
```

#### Test Different Timeframes
```bash
# 4 weeks
curl -X POST http://localhost:5000/api/generate-roadmap \
  -H "Content-Type: application/json" \
  -d '{"careerGoal": "IT Help Desk", "currentSkills": [], "timeframe": "4 weeks"}'

# 6 weeks
curl -X POST http://localhost:5000/api/generate-roadmap \
  -H "Content-Type: application/json" \
  -d '{"careerGoal": "Network Technician", "currentSkills": [], "timeframe": "6 weeks"}'

# 3 months
curl -X POST http://localhost:5000/api/generate-roadmap \
  -H "Content-Type: application/json" \
  -d '{"careerGoal": "Cybersecurity Analyst", "currentSkills": [], "timeframe": "3 months"}'
```

### Sample Request Body

```json
{
  "careerGoal": "SOC Analyst",
  "currentSkills": ["Python", "basic networking", "Wireshark"],
  "timeframe": "3 months"
}
```

### Expected Response Format

```json
{
  "success": true,
  "careerGoal": "SOC Analyst",
  "roadmap": {
    "summary": "A comprehensive 3-month pathway to become a SOC Analyst...",
    "phases": [
      {
        "phase": 1,
        "title": "Foundation & Setup",
        "duration": "Weeks 1-4",
        "focus": "Learn security fundamentals",
        "skills": ["Security Monitoring", "Incident Response"]
      }
    ],
    "skills": ["Security Monitoring", "SIEM Tools", "Log Analysis"],
    "tools": ["Splunk", "Wireshark", "Security Onion"],
    "resources": [
      {
        "title": "IBM SkillsBuild - Cybersecurity Fundamentals",
        "type": "course",
        "url": "https://skillsbuild.org/..."
      }
    ],
    "githubProjects": [
      {
        "name": "awesome-security",
        "description": "A collection of security resources",
        "stars": 5000,
        "url": "https://github.com/..."
      }
    ],
    "portfolioProjects": [...],
    "resumeBullets": [...],
    "weeklyPlan": [...],
    "nextSteps": [...]
  },
  "metadata": {
    "usedWatsonx": true,
    "usedGitHub": true,
    "matchedLocalResources": 5
  }
}
```

## 🔒 Security

- **API Keys**: Never commit `.env` files. All secrets are stored in environment variables.
- **Backend-Only API Calls**: Frontend never directly calls watsonx.ai or GitHub - all requests go through our secure backend.
- **Error Handling**: Error messages are sanitized to prevent credential leaks.
- **CORS**: Configured to only allow requests from the frontend origin.

## 📁 Project Structure

```
PathPilot-AI/
├── client/                 # React frontend
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page components
│   │   └── utils/         # API utilities
│   └── package.json
├── server/                # FastAPI backend
│   ├── data/             # Curated data files
│   │   ├── roles.json           # Career role definitions
│   │   ├── resources.json       # Learning resources
│   │   ├── projects.json        # Project ideas
│   │   └── certifications.json  # Certification recommendations
│   ├── models/           # Pydantic schemas
│   ├── routes/           # API endpoints
│   │   └── roadmap.py          # AI roadmap generation endpoint
│   ├── services/         # Business logic
│   │   ├── watsonx_service.py  # IBM watsonx.ai integration
│   │   └── github_service.py   # GitHub API integration
│   ├── main.py           # FastAPI app
│   ├── requirements.txt  # Python dependencies
│   └── .env.example      # Environment variables template
└── README.md
```

## 🎨 Key Endpoints

### AI Roadmap Generation
- **POST** `/api/generate-roadmap` - Generate AI-powered career roadmap

### Legacy Endpoints
- **POST** `/api/pathways/generate` - Generate sample pathway (mock data)
- **POST** `/api/pathways/adapt` - Adapt existing pathway
- **GET** `/api/github/projects/{skill}` - Search GitHub projects
- **GET** `/api/usajobs/search` - Search federal jobs
- **POST** `/api/recommendations` - Get career recommendations

## 🐛 Troubleshooting

### Backend won't start
- Ensure Python 3.8+ is installed: `python --version`
- Activate virtual environment
- Install dependencies: `pip install -r requirements.txt`
- Check `.env` file exists in `server/` directory

### Frontend won't start
- Ensure Node.js 16+ is installed: `node --version`
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Check if port 5173 is available

### AI Roadmap Generation Fails
- Verify `WATSONX_API_KEY` and `WATSONX_PROJECT_ID` are set correctly
- Check IBM Cloud IAM token is valid
- Review backend logs for detailed error messages
- The system will fall back to a template-based roadmap if watsonx.ai is unavailable

### GitHub Projects Not Showing
- **Fixed**: Response normalizer now ensures `githubProjects` array always exists
- Check backend logs for GitHub API errors
- Verify `GITHUB_TOKEN` is set for higher rate limits
- The system falls back to verified local projects if GitHub fails

### Wrong Timeframe Displayed
- **Fixed**: Frontend now preserves exact user-selected timeframe
- **Fixed**: Watsonx prompt explicitly instructs to preserve timeframe
- If issue persists, check backend logs for prompt/response details

### Insufficient Resources
- **Fixed**: Resource matching now uses career goal context and aliases
- **Fixed**: Minimum 5 resources guaranteed via fallback to verified resources
- Run `python validate_data.py` to check data files
- Add more resources to `server/data/verified_resources.json` if needed

### GitHub API Rate Limit
- Add `GITHUB_TOKEN` to `.env` for higher rate limits (5000 requests/hour vs 60)
- The system gracefully handles rate limit errors and uses local projects

### Watsonx Response Truncated
- **Fixed**: Increased `max_new_tokens` to 4000
- **Fixed**: Added retry logic with exponential backoff
- **Fixed**: Response normalizer ensures all required fields exist
- Check logs for "RESPONSE APPEARS TRUNCATED" warnings

## 📝 Development Notes

### Adding New Career Roles

1. Add role definition to `server/data/roles.json`
2. Add resources to `server/data/resources.json`
3. Add projects to `server/data/projects.json`
4. Add certifications to `server/data/certifications.json`

### Customizing AI Prompts

Edit the prompt in `server/services/watsonx_service.py` in the `generate_career_roadmap` method.

### Changing AI Model

Update the `model_id` parameter in `watsonx_service.py`:
- `ibm/granite-13b-chat-v2` (default)
- `ibm/granite-20b-multilingual`
- Other available watsonx.ai models

## 🤝 Contributing

This project was built for the IBM Hackathon. Contributions are welcome!

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- **IBM watsonx.ai** for AI-powered roadmap generation
- **GitHub** for project discovery
- **USAJOBS** for federal job listings
- **O*NET** for career data
- **IBM SkillsBuild** for learning resources

## 📧 Support

For issues or questions, please open an issue on GitHub.

---

**Made with ❤️ for the IBM Hackathon**
