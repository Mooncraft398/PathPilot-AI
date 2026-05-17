**User:**

<task>
Read the project files first, then update the README based on the actual current app.

Do not guess features. Only document what exists in the code.

Tasks:
1. Scan the frontend, backend, routes, API integrations, env usage, and package files.
2. Identify the real features currently implemented.
3. Identify current improvements/fixes already added.
4. Update README with:
   - Project name and short description
   - Main features
   - Tech stack
   - APIs used: O*NET, USAJOBS, GitHub REST API, Watsonx.ai
   - Setup instructions from a fresh clone
   - Required `.env` variables using placeholder values only
   - How to run frontend/backend
   - How fallback behavior works when APIs fail
   - Known limitations
   - Future improvements
   - Hackathon/submission notes if relevant
5. Make sure README does not expose API keys or private info.
6. Make it clear, professional, and concise.
7. Include any screenshots/demo notes only if the files already show them or placeholders are needed.

Return:
- Summary of what files you read
- What README sections you updated
- Any missing info I still need to add manually
- The final updated README content or directly edit the README if you have file access.
</task>
<environment_details>
# VSCode Visible Files
server\main.py

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,README.md,server/.env,server/main.py,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:14:25.031Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$0.00

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>


# Current Workspace Directory (c:/Users/ivann/Desktop/IBM Hackathon/PathPilot-AI) Files
.gitignore
DEBUGGING_ANALYSIS.md
GITHUB_PROJECTS_DEBUG_GUIDE.md
HARDENING_IMPLEMENTATION.md
HARDENING_VERIFICATION_REPORT.md
IMPLEMENTATION_COMPLETE.md
IMPLEMENTATION_STATUS.md
LICENSE
MVP_CHECKLIST.md
package-lock.json
package.json
README.md
RESOURCE_ALLOCATION_FIX.md
SETUP.md
test_api.py
test_roadmap.json
test_success.txt
TRANSFORMATION_PIPELINE_FIXES.md
TROUBLESHOOTING.md
bob_sessions/
client/
client/.gitignore
client/eslint.config.js
client/index.html
client/package-lock.json
client/package.json
client/README.md
client/vite.config.js
client/public/
client/public/favicon.svg
client/public/icons.svg
client/src/
client/src/App.css
client/src/App.jsx
client/src/index.css
client/src/main.jsx
client/src/assets/
client/src/assets/hero.png
client/src/assets/react.svg
client/src/assets/vite.svg
client/src/components/
client/src/components/JobCard.jsx
client/src/components/Navbar.jsx
client/src/components/PathwayForm.jsx
client/src/components/ProgressBar.jsx
client/src/components/ProjectCard.jsx
client/src/components/ResourceCard.jsx
client/src/components/WeekCard.jsx
client/src/pages/
client/src/pages/GeneratePage.jsx
client/src/pages/HomePage.jsx
client/src/pages/PathwayPage.jsx
client/src/utils/
client/src/utils/api.js
client/src/utils/localStorage.js
docs/
docs/api-integration-notes.md
docs/bob-architecture-notes.md
docs/FRONTEND_DATA_FLOW_FIXES.md
docs/ONET_INTEGRATION_FIX.md
docs/PROJECT_CARD_FIX.md
docs/RESOURCE_VALIDATION_SYSTEM.md
docs/WATSONX_AUTH_DEBUG.md
docs/WATSONX_DEBUG_FIXES.md
docs/WATSONX_FRONTEND_INTEGRATION.md
docs/WATSONX_JSON_PARSING_FIX.md
docs/WATSONX_TOKEN_TRUNCATION_FIX.md
requests/
server/
server/.env.example
server/GITHUB_API_TESTING.md
server/main.py
server/ONET_TESTING_GUIDE.md
server/README.md
server/RECOMMENDATION_SYSTEM.md
server/requirements.txt
server/test_api_endpoints.py
server/test_career_paths.py
server/test_env.py
server/test_hardening_validation.py
server/test_onet.py
server/test_request.json
server/test_resource_links.py
server/test_roadmap_output.json
server/test_roadmap_validated.json
server/test_watsonx_auth.py
server/test_watsonx_diagnosis.py
server/test_watsonx_models.py
server/test_watsonx_roadmap_json.py
server/validate_data.py
server/data/
server/data/careers.json
server/data/certifications.json
server/data/projects.json
server/data/resources.json
server/data/roles.json
server/data/verified_projects.json
server/data/verified_resources.json
server/models/
server/models/__init__.py
server/models/schemas.py
server/routes/
server/routes/__init__.py
server/routes/github_projects.py
server/routes/onet.py
server/routes/pathways.py
server/routes/recommendations.py
server/routes/roadmap.py
server/routes/usajobs.py
server/services/
server/services/__init__.py
server/services/github_service.py
server/services/onet_service.py
server/services/pathway_generator.py
server/services/project_validator.py
server/services/recommendation_service.py
server/services/resource_validator.py
server/services/response_normalizer.py
server/services/roadmap_enforcer.py
server/services/usajobs_service.py
server/services/watsonx_multi_call.py
server/services/watsonx_service.py
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

I'll start by reading the key project files to understand the actual implementation before updating the README.

<read_file>
<args>
<file>
<path>package.json</path>
</file>
<file>
<path>client/package.json</path>
</file>
<file>
<path>server/requirements.txt</path>
</file>
<file>
<path>server/.env.example</path>
</file>
<file>
<path>server/main.py</path>
</file>
</args>
</read_file>

---

**User:**

[read_file for 5 files] Result:
<files>
<file><path>package.json</path>
<content lines="1-5">
1 | {
2 |   "dependencies": {
3 |     "react-router-dom": "^7.15.1"
4 |   }
5 | }
</content>
</file>
<file><path>client/package.json</path>
<content lines="1-31">
 1 | {
 2 |   "name": "client",
 3 |   "private": true,
 4 |   "version": "0.0.0",
 5 |   "type": "module",
 6 |   "scripts": {
 7 |     "dev": "vite",
 8 |     "build": "vite build",
 9 |     "lint": "eslint .",
10 |     "preview": "vite preview"
11 |   },
12 |   "dependencies": {
13 |     "@tailwindcss/vite": "^4.3.0",
14 |     "axios": "^1.6.2",
15 |     "react": "^19.2.6",
16 |     "react-dom": "^19.2.6",
17 |     "react-router-dom": "^6.20.1",
18 |     "tailwindcss": "^4.3.0"
19 |   },
20 |   "devDependencies": {
21 |     "@eslint/js": "^10.0.1",
22 |     "@types/react": "^19.2.14",
23 |     "@types/react-dom": "^19.2.3",
24 |     "@vitejs/plugin-react": "^6.0.1",
25 |     "eslint": "^10.3.0",
26 |     "eslint-plugin-react-hooks": "^7.1.1",
27 |     "eslint-plugin-react-refresh": "^0.5.2",
28 |     "globals": "^17.6.0",
29 |     "vite": "^8.0.12"
30 |   }
31 | }
</content>
</file>
<file><path>server/requirements.txt</path>
<content lines="1-26">
 1 | annotated-doc==0.0.4
 2 | annotated-types==0.7.0
 3 | anyio==3.7.1
 4 | certifi==2026.4.22
 5 | click==8.3.3
 6 | colorama==0.4.6
 7 | dnspython==2.8.0
 8 | fastapi==0.104.1
 9 | h11==0.16.0
10 | httpcore==1.0.9
11 | httptools==0.7.1
12 | httpx==0.28.1
13 | idna==3.15
14 | motor==3.7.1
15 | pydantic==2.5.0
16 | pydantic_core==2.14.1
17 | pymongo==4.17.0
18 | python-dotenv==1.0.0
19 | PyYAML==6.0.3
20 | sniffio==1.3.1
21 | starlette==0.27.0
22 | typing-inspection==0.4.2
23 | typing_extensions==4.15.0
24 | uvicorn==0.24.0
25 | watchfiles==1.1.1
26 | websockets==16.0
</content>
</file>
<file><path>server/.env.example</path>
<content lines="1-33">
 1 | # FastAPI Configuration
 2 | API_HOST=0.0.0.0
 3 | API_PORT=8000
 4 | 
 5 | # CORS Origins (comma-separated)
 6 | CORS_ORIGINS=http://localhost:5173,http://localhost:3000
 7 | 
 8 | # GitHub API Configuration (optional - for higher rate limits)
 9 | # Get your token at: https://github.com/settings/tokens
10 | GITHUB_TOKEN=your_github_token_here
11 | 
12 | # O*NET Web Services API Configuration
13 | # Register at: https://services.onetcenter.org/
14 | ONET_API_KEY=your_onet_api_key_here
15 | 
16 | # USAJOBS API Configuration
17 | # Register at: https://developer.usajobs.gov/
18 | USAJOBS_EMAIL=your_email@example.com
19 | USAJOBS_API_KEY=your_usajobs_api_key
20 | 
21 | # IBM watsonx.ai Configuration
22 | # Get your credentials at: https://cloud.ibm.com/
23 | WATSONX_API_KEY=your_watsonx_api_key_here
24 | WATSONX_PROJECT_ID=your_watsonx_project_id_here
25 | WATSONX_URL=https://us-south.ml.cloud.ibm.com
26 | 
27 | # MongoDB Configuration (for future use)
28 | # MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/pathpilot?retryWrites=true&w=majority
29 | # DATABASE_NAME=pathpilot
30 | 
31 | # Environment
32 | ENVIRONMENT=development
33 | PORT=5000
</content>
</file>
<file><path>server/main.py</path>
<content lines="1-68">
 1 | from dotenv import load_dotenv
 2 | from pathlib import Path
 3 | 
 4 | # Load environment variables FIRST, before any other imports
 5 | # This ensures all modules can access environment variables when they're imported
 6 | env_path = Path(__file__).parent / '.env'
 7 | load_dotenv(dotenv_path=env_path)
 8 | 
 9 | from fastapi import FastAPI
10 | from fastapi.middleware.cors import CORSMiddleware
11 | from models.schemas import HealthResponse
12 | from routes import pathways, github_projects, recommendations, onet, usajobs, roadmap
13 | 
14 | # Create FastAPI app
15 | app = FastAPI(
16 |     title="PathPilot AI API",
17 |     description="Career pathway generator API for the IBM Bob Hackathon with watsonx.ai integration",
18 |     version="1.0.0"
19 | )
20 | 
21 | # Configure CORS for React frontend
22 | app.add_middleware(
23 |     CORSMiddleware,
24 |     allow_origins=[
25 |         "http://localhost:5173",  # Vite default port
26 |         "http://localhost:3000",  # Alternative React port
27 |         "http://127.0.0.1:5173",
28 |         "http://127.0.0.1:3000"
29 |     ],
30 |     allow_credentials=True,
31 |     allow_methods=["*"],
32 |     allow_headers=["*"],
33 | )
34 | 
35 | # Include routers
36 | app.include_router(roadmap.router)  # AI-powered roadmap generator
37 | app.include_router(pathways.router)
38 | app.include_router(github_projects.router)
39 | app.include_router(recommendations.router)
40 | app.include_router(onet.router)
41 | app.include_router(usajobs.router)
42 | 
43 | 
44 | @app.get("/", response_model=HealthResponse)
45 | async def health_check():
46 |     """
47 |     Health check endpoint to verify the API is running.
48 |     """
49 |     return HealthResponse(
50 |         status="healthy",
51 |         message="PathPilot AI API is running! Visit /docs for API documentation."
52 |     )
53 | 
54 | 
55 | @app.get("/health", response_model=HealthResponse)
56 | async def health():
57 |     """
58 |     Alternative health check endpoint.
59 |     """
60 |     return HealthResponse(
61 |         status="healthy",
62 |         message="API is operational"
63 |     )
64 | 
65 | 
66 | if __name__ == "__main__":
67 |     import uvicorn
68 |     uvicorn.run(app, host="0.0.0.0", port=8000)
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files
server\main.py

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,README.md,server/.env,server/main.py,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:14:29.067Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$0.01

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

<read_file>
<args>
<file>
<path>client/src/App.jsx</path>
</file>
<file>
<path>client/src/pages/HomePage.jsx</path>
</file>
<file>
<path>client/src/pages/GeneratePage.jsx</path>
</file>
<file>
<path>client/src/pages/PathwayPage.jsx</path>
</file>
<file>
<path>client/src/utils/api.js</path>
</file>
</args>
</read_file>

---

**User:**

[read_file for 5 files] Result:
<files>
<file><path>client/src/App.jsx</path>
<content lines="1-27">
 1 | import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
 2 | import Navbar from './components/Navbar';
 3 | import HomePage from './pages/HomePage';
 4 | import GeneratePage from './pages/GeneratePage';
 5 | import PathwayPage from './pages/PathwayPage';
 6 | 
 7 | /**
 8 |  * Main App component with routing
 9 |  */
10 | function App() {
11 |   return (
12 |     <Router>
13 |       <div className="min-h-screen bg-slate-950">
14 |         <Navbar />
15 |         <Routes>
16 |           <Route path="/" element={<HomePage />} />
17 |           <Route path="/generate" element={<GeneratePage />} />
18 |           <Route path="/pathway" element={<PathwayPage />} />
19 |         </Routes>
20 |       </div>
21 |     </Router>
22 |   );
23 | }
24 | 
25 | export default App;
26 | 
27 | // Made with Bob
</content>
</file>
<file><path>client/src/pages/HomePage.jsx</path>
<content lines="1-179">
  1 | import { Link } from 'react-router-dom';
  2 | import { hasPathway } from '../utils/localStorage';
  3 | 
  4 | /**
  5 |  * Home page - Landing page for PathPilot AI
  6 |  */
  7 | function HomePage() {
  8 |   const pathwayExists = hasPathway();
  9 | 
 10 |   return (
 11 |     <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 relative overflow-hidden">
 12 |       {/* Animated background elements */}
 13 |       <div className="absolute inset-0 overflow-hidden pointer-events-none">
 14 |         <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl animate-pulse"></div>
 15 |         <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1s' }}></div>
 16 |       </div>
 17 | 
 18 |       <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-24 relative z-10">
 19 |         {/* Hero Section */}
 20 |         <div className="text-center mb-20">
 21 |           <div className="inline-flex items-center px-4 py-2 bg-blue-500/10 border border-blue-500/20 rounded-full mb-8">
 22 |             <span className="w-2 h-2 bg-blue-500 rounded-full mr-2 animate-pulse"></span>
 23 |             <span className="text-blue-400 text-sm font-medium">AI-Powered Career Planning</span>
 24 |           </div>
 25 |           
 26 |           <h1 className="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight">
 27 |             Your Personalized
 28 |             <span className="block text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500 animate-gradient">
 29 |               Career Roadmap
 30 |             </span>
 31 |           </h1>
 32 |           
 33 |           <p className="text-xl md:text-2xl text-slate-300 mb-8 max-w-3xl mx-auto leading-relaxed">
 34 |             Transform your career goals into actionable learning paths. Get a
 35 |             <span className="text-white font-semibold"> personalized, week-by-week roadmap </span>
 36 |             tailored to your timeline and learning style.
 37 |           </p>
 38 | 
 39 |           <p className="text-base text-slate-400 mb-12 max-w-2xl mx-auto">
 40 |             From zero to resume-ready in weeks, not years. Build real projects, master in-demand skills, and land your dream job.
 41 |           </p>
 42 | 
 43 |           {/* CTA Buttons */}
 44 |           <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
 45 |             <Link
 46 |               to="/generate"
 47 |               className="group px-8 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold rounded-xl hover:from-blue-600 hover:to-purple-700 transition-all transform hover:scale-105 shadow-xl hover:shadow-2xl hover:shadow-purple-500/20"
 48 |             >
 49 |               <span className="flex items-center">
 50 |                 Generate My Pathway
 51 |                 <svg className="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
 52 |                   <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
 53 |                 </svg>
 54 |               </span>
 55 |             </Link>
 56 |             {pathwayExists && (
 57 |               <Link
 58 |                 to="/pathway"
 59 |                 className="px-8 py-4 bg-slate-800/80 backdrop-blur-sm text-white font-semibold rounded-xl hover:bg-slate-700 transition-all border border-slate-700 hover:border-slate-600 shadow-lg"
 60 |               >
 61 |                 Continue My Journey →
 62 |               </Link>
 63 |             )}
 64 |           </div>
 65 | 
 66 |           {/* Trust indicators */}
 67 |           <div className="flex flex-wrap justify-center items-center gap-6 text-sm text-slate-400">
 68 |             <div className="flex items-center">
 69 |               <svg className="w-5 h-5 text-green-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
 70 |                 <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
 71 |               </svg>
 72 |               <span>100% Free to Start</span>
 73 |             </div>
 74 |             <div className="flex items-center">
 75 |               <svg className="w-5 h-5 text-blue-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
 76 |                 <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
 77 |               </svg>
 78 |               <span>Personalized for You</span>
 79 |             </div>
 80 |             <div className="flex items-center">
 81 |               <svg className="w-5 h-5 text-purple-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
 82 |                 <path fillRule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clipRule="evenodd" />
 83 |               </svg>
 84 |               <span>Results in Weeks</span>
 85 |             </div>
 86 |           </div>
 87 |         </div>
 88 | 
 89 |         {/* Features Section */}
 90 |         <div className="grid md:grid-cols-3 gap-6 mb-24">
 91 |           <div className="group bg-slate-900/50 backdrop-blur-sm p-8 rounded-2xl border border-slate-800 hover:border-blue-500/50 transition-all hover:shadow-xl hover:shadow-blue-500/10 hover:-translate-y-1">
 92 |             <div className="w-14 h-14 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center mb-5 group-hover:scale-110 transition-transform shadow-lg shadow-blue-500/20">
 93 |               <svg className="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
 94 |                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
 95 |               </svg>
 96 |             </div>
 97 |             <h3 className="text-xl font-bold text-white mb-3">Personalized Plans</h3>
 98 |             <p className="text-slate-400 leading-relaxed">
 99 |               AI-tailored learning paths based on your career goals, skill level, and available time commitment.
100 |             </p>
101 |           </div>
102 | 
103 |           <div className="group bg-slate-900/50 backdrop-blur-sm p-8 rounded-2xl border border-slate-800 hover:border-purple-500/50 transition-all hover:shadow-xl hover:shadow-purple-500/10 hover:-translate-y-1">
104 |             <div className="w-14 h-14 bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl flex items-center justify-center mb-5 group-hover:scale-110 transition-transform shadow-lg shadow-purple-500/20">
105 |               <svg className="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
106 |                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
107 |               </svg>
108 |             </div>
109 |             <h3 className="text-xl font-bold text-white mb-3">Curated Resources</h3>
110 |             <p className="text-slate-400 leading-relaxed">
111 |               Access hand-picked learning materials, tutorials, and projects for each step of your journey.
112 |             </p>
113 |           </div>
114 | 
115 |           <div className="group bg-slate-900/50 backdrop-blur-sm p-8 rounded-2xl border border-slate-800 hover:border-green-500/50 transition-all hover:shadow-xl hover:shadow-green-500/10 hover:-translate-y-1">
116 |             <div className="w-14 h-14 bg-gradient-to-br from-green-500 to-green-600 rounded-xl flex items-center justify-center mb-5 group-hover:scale-110 transition-transform shadow-lg shadow-green-500/20">
117 |               <svg className="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
118 |                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
119 |               </svg>
120 |             </div>
121 |             <h3 className="text-xl font-bold text-white mb-3">Track Progress</h3>
122 |             <p className="text-slate-400 leading-relaxed">
123 |               Monitor your learning journey with weekly milestones and build portfolio-ready projects.
124 |             </p>
125 |           </div>
126 |         </div>
127 | 
128 |         {/* How It Works */}
129 |         <div className="bg-slate-900/30 backdrop-blur-sm rounded-3xl border border-slate-800 p-8 md:p-12">
130 |           <h2 className="text-3xl md:text-4xl font-bold text-white text-center mb-4">How It Works</h2>
131 |           <p className="text-slate-400 text-center mb-12 max-w-2xl mx-auto">
132 |             Get started in minutes with our simple 4-step process
133 |           </p>
134 |           
135 |           <div className="grid md:grid-cols-4 gap-8 relative">
136 |             {/* Connection lines for desktop */}
137 |             <div className="hidden md:block absolute top-8 left-0 right-0 h-0.5 bg-gradient-to-r from-blue-500 via-purple-500 via-green-500 to-orange-500 opacity-20"></div>
138 |             
139 |             <div className="text-center relative">
140 |               <div className="w-16 h-16 bg-gradient-to-br from-blue-500 to-blue-600 text-white rounded-2xl flex items-center justify-center text-2xl font-bold mx-auto mb-4 shadow-lg shadow-blue-500/30 relative z-10">
141 |                 1
142 |               </div>
143 |               <h3 className="text-lg font-bold text-white mb-2">Set Your Goal</h3>
144 |               <p className="text-slate-400 text-sm leading-relaxed">Tell us your career target and current skill level</p>
145 |             </div>
146 |             
147 |             <div className="text-center relative">
148 |               <div className="w-16 h-16 bg-gradient-to-br from-purple-500 to-purple-600 text-white rounded-2xl flex items-center justify-center text-2xl font-bold mx-auto mb-4 shadow-lg shadow-purple-500/30 relative z-10">
149 |                 2
150 |               </div>
151 |               <h3 className="text-lg font-bold text-white mb-2">Choose Timeline</h3>
152 |               <p className="text-slate-400 text-sm leading-relaxed">Select your available time and learning preferences</p>
153 |             </div>
154 |             
155 |             <div className="text-center relative">
156 |               <div className="w-16 h-16 bg-gradient-to-br from-green-500 to-green-600 text-white rounded-2xl flex items-center justify-center text-2xl font-bold mx-auto mb-4 shadow-lg shadow-green-500/30 relative z-10">
157 |                 3
158 |               </div>
159 |               <h3 className="text-lg font-bold text-white mb-2">Get Your Path</h3>
160 |               <p className="text-slate-400 text-sm leading-relaxed">Receive a personalized week-by-week roadmap</p>
161 |             </div>
162 |             
163 |             <div className="text-center relative">
164 |               <div className="w-16 h-16 bg-gradient-to-br from-orange-500 to-orange-600 text-white rounded-2xl flex items-center justify-center text-2xl font-bold mx-auto mb-4 shadow-lg shadow-orange-500/30 relative z-10">
165 |                 4
166 |               </div>
167 |               <h3 className="text-lg font-bold text-white mb-2">Start Learning</h3>
168 |               <p className="text-slate-400 text-sm leading-relaxed">Follow your roadmap and build your portfolio</p>
169 |             </div>
170 |           </div>
171 |         </div>
172 |       </div>
173 |     </div>
174 |   );
175 | }
176 | 
177 | export default HomePage;
178 | 
179 | // Made with Bob
</content>
</file>
<file><path>client/src/pages/GeneratePage.jsx</path>
<content lines="1-88">
 1 | import PathwayForm from '../components/PathwayForm';
 2 | 
 3 | /**
 4 |  * Generate page - Contains the pathway generation form
 5 |  */
 6 | function GeneratePage() {
 7 |   return (
 8 |     <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 relative overflow-hidden">
 9 |       {/* Animated background elements */}
10 |       <div className="absolute inset-0 overflow-hidden pointer-events-none">
11 |         <div className="absolute top-1/3 right-1/4 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl"></div>
12 |         <div className="absolute bottom-1/3 left-1/4 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl"></div>
13 |       </div>
14 | 
15 |       <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 relative z-10">
16 |         {/* Header */}
17 |         <div className="text-center mb-12">
18 |           <div className="inline-flex items-center px-4 py-2 bg-gradient-to-r from-blue-500/10 to-purple-500/10 border border-blue-500/20 rounded-full mb-6">
19 |             <svg className="w-4 h-4 text-blue-400 mr-2" fill="currentColor" viewBox="0 0 20 20">
20 |               <path fillRule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clipRule="evenodd" />
21 |             </svg>
22 |             <span className="text-blue-400 text-sm font-medium">Powered by AI</span>
23 |           </div>
24 |           
25 |           <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">
26 |             Generate Your
27 |             <span className="block text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-600">
28 |               Career Pathway
29 |             </span>
30 |           </h1>
31 |           
32 |           <p className="text-lg text-slate-300 max-w-2xl mx-auto leading-relaxed">
33 |             Tell us about your goals and preferences, and we'll create a personalized
34 |             learning roadmap tailored just for you.
35 |           </p>
36 |         </div>
37 | 
38 |         {/* Form */}
39 |         <div className="bg-slate-900/80 backdrop-blur-sm rounded-2xl border border-slate-800 p-8 md:p-10 shadow-2xl">
40 |           <PathwayForm />
41 |         </div>
42 | 
43 |         {/* Info Section */}
44 |         <div className="mt-12 grid md:grid-cols-3 gap-6">
45 |           <div className="group bg-slate-900/50 backdrop-blur-sm p-6 rounded-xl border border-slate-800 hover:border-blue-500/50 transition-all text-center">
46 |             <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform shadow-lg shadow-blue-500/20">
47 |               <svg className="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
48 |                 <path fillRule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clipRule="evenodd" />
49 |               </svg>
50 |             </div>
51 |             <div className="text-2xl font-bold text-white mb-2">AI-Powered</div>
52 |             <p className="text-slate-400 text-sm leading-relaxed">
53 |               Intelligent pathway generation based on your unique profile
54 |             </p>
55 |           </div>
56 |           
57 |           <div className="group bg-slate-900/50 backdrop-blur-sm p-6 rounded-xl border border-slate-800 hover:border-purple-500/50 transition-all text-center">
58 |             <div className="w-12 h-12 bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform shadow-lg shadow-purple-500/20">
59 |               <svg className="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
60 |                 <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
61 |               </svg>
62 |             </div>
63 |             <div className="text-2xl font-bold text-white mb-2">Personalized</div>
64 |             <p className="text-slate-400 text-sm leading-relaxed">
65 |               Tailored to your timeline, budget, and learning style
66 |             </p>
67 |           </div>
68 |           
69 |           <div className="group bg-slate-900/50 backdrop-blur-sm p-6 rounded-xl border border-slate-800 hover:border-green-500/50 transition-all text-center">
70 |             <div className="w-12 h-12 bg-gradient-to-br from-green-500 to-green-600 rounded-xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform shadow-lg shadow-green-500/20">
71 |               <svg className="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
72 |                 <path fillRule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clipRule="evenodd" />
73 |               </svg>
74 |             </div>
75 |             <div className="text-2xl font-bold text-white mb-2">Actionable</div>
76 |             <p className="text-slate-400 text-sm leading-relaxed">
77 |               Week-by-week plans with resources and projects
78 |             </p>
79 |           </div>
80 |         </div>
81 |       </div>
82 |     </div>
83 |   );
84 | }
85 | 
86 | export default GeneratePage;
87 | 
88 | // Made with Bob
</content>
</file>
<file><path>client/src/pages/PathwayPage.jsx</path>
<content lines="1-718">
  1 | import { useState, useEffect, useCallback } from 'react';
  2 | import { Link, useNavigate } from 'react-router-dom';
  3 | import { getPathway, clearPathway, updatePathway } from '../utils/localStorage';
  4 | import { adaptPathway, searchUSAJobs } from '../utils/api';
  5 | import WeekCard from '../components/WeekCard';
  6 | import ProgressBar from '../components/ProgressBar';
  7 | import JobCard from '../components/JobCard';
  8 | 
  9 | /**
 10 |  * Pathway page - Displays the generated career pathway
 11 |  */
 12 | function PathwayPage() {
 13 |   const navigate = useNavigate();
 14 |   // Initialize state directly from localStorage to avoid setState in useEffect
 15 |   const [pathway, setPathway] = useState(() => {
 16 |     const loadedPathway = getPathway();
 17 |     console.log('🔍 PathwayPage: Loading pathway from localStorage');
 18 |     console.log('📦 Loaded pathway:', loadedPathway);
 19 |     console.log('🐙 GitHub projects count:', loadedPathway?.githubProjects?.length || 0);
 20 |     if (loadedPathway?.githubProjects && loadedPathway.githubProjects.length > 0) {
 21 |       console.log('🐙 GitHub projects:', loadedPathway.githubProjects);
 22 |     }
 23 |     return loadedPathway;
 24 |   });
 25 |   const [feedback, setFeedback] = useState('');
 26 |   const [isAdapting, setIsAdapting] = useState(false);
 27 |   const [adaptError, setAdaptError] = useState(null);
 28 |   const [showAdaptSection, setShowAdaptSection] = useState(false);
 29 |   
 30 |   // USAJOBS state
 31 |   const [jobsData, setJobsData] = useState(null);
 32 |   const [jobsLoading, setJobsLoading] = useState(false);
 33 |   const [jobsError, setJobsError] = useState(null);
 34 |   const [jobLocation, setJobLocation] = useState('');
 35 | 
 36 |   const handleClearPathway = () => {
 37 |     if (window.confirm('Are you sure you want to clear your current pathway?')) {
 38 |       clearPathway();
 39 |       navigate('/');
 40 |     }
 41 |   };
 42 | 
 43 |   const handleToggleWeekComplete = (weekNumber) => {
 44 |     if (!pathway) return;
 45 | 
 46 |     // Create updated pathway with toggled week completion
 47 |     const updatedPathway = {
 48 |       ...pathway,
 49 |       weeks: pathway.weeks.map(week =>
 50 |         week.weekNumber === weekNumber
 51 |           ? { ...week, completed: !week.completed }
 52 |           : week
 53 |       )
 54 |     };
 55 | 
 56 |     // Update state and localStorage
 57 |     setPathway(updatedPathway);
 58 |     updatePathway(updatedPathway);
 59 |   };
 60 | 
 61 |   const handleAdaptPathway = async () => {
 62 |     if (!feedback.trim()) {
 63 |       setAdaptError('Please enter your feedback');
 64 |       return;
 65 |     }
 66 | 
 67 |     setIsAdapting(true);
 68 |     setAdaptError(null);
 69 | 
 70 |     try {
 71 |       console.log('🔄 Adapting pathway with feedback:', feedback);
 72 |       console.log('📋 Current pathway before adaptation:', pathway);
 73 |       
 74 |       const adaptedPathway = await adaptPathway(pathway, feedback);
 75 |       
 76 |       console.log('✅ Received adapted pathway from API:', adaptedPathway);
 77 |       console.log('⏰ New weeklyTimeCommitment:', adaptedPathway.weeklyTimeCommitment);
 78 |       
 79 |       setPathway(adaptedPathway);
 80 |       updatePathway(adaptedPathway);
 81 |       
 82 |       console.log('💾 Saved to localStorage and updated state');
 83 |       
 84 |       setFeedback('');
 85 |       setShowAdaptSection(false);
 86 |       // Show success message briefly
 87 |       alert('Pathway adapted successfully! Check the Time Commitment field.');
 88 |     } catch (error) {
 89 |       console.error('❌ Error adapting pathway:', error);
 90 |       setAdaptError(error.message || 'Failed to adapt pathway');
 91 |     } finally {
 92 |       setIsAdapting(false);
 93 |     }
 94 |   };
 95 | 
 96 |   // Memoized search function for manual button clicks
 97 |   const handleSearchJobs = useCallback(async () => {
 98 |     if (!pathway?.goal) return;
 99 |     
100 |     setJobsLoading(true);
101 |     setJobsError(null);
102 |     
103 |     try {
104 |       const result = await searchUSAJobs(pathway.goal, jobLocation || null);
105 |       setJobsData(result);
106 |     } catch (error) {
107 |       console.error('Error searching jobs:', error);
108 |       setJobsError(error.message || 'Failed to search jobs');
109 |     } finally {
110 |       setJobsLoading(false);
111 |     }
112 |   }, [pathway, jobLocation]);
113 | 
114 |   // Auto-search jobs when pathway loads (only once when goal exists and no data yet)
115 |   useEffect(() => {
116 |     // Only auto-search if we have a goal, no existing data, and not currently loading
117 |     if (pathway?.goal && !jobsData && !jobsLoading) {
118 |       const autoSearch = async () => {
119 |         setJobsLoading(true);
120 |         setJobsError(null);
121 |         
122 |         try {
123 |           const result = await searchUSAJobs(pathway.goal, null);
124 |           setJobsData(result);
125 |         } catch (error) {
126 |           console.error('Error auto-searching jobs:', error);
127 |           setJobsError(error.message || 'Failed to search jobs');
128 |         } finally {
129 |           setJobsLoading(false);
130 |         }
131 |       };
132 |       
133 |       autoSearch();
134 |     }
135 |   }, [pathway?.goal, jobsData, jobsLoading]);
136 | 
137 |   // If no pathway exists, show message
138 |   if (!pathway) {
139 |     return (
140 |       <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 flex items-center justify-center">
141 |         <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
142 |           <div className="bg-slate-900/50 backdrop-blur-sm rounded-3xl border border-slate-800 p-12">
143 |             <div className="w-24 h-24 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-xl">
144 |               <svg className="w-12 h-12 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
145 |                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
146 |               </svg>
147 |             </div>
148 |             <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">No Pathway Yet</h2>
149 |             <p className="text-lg text-slate-400 mb-8 leading-relaxed">
150 |               You haven't generated a career pathway yet. Let's create your personalized learning roadmap!
151 |             </p>
152 |             <Link
153 |               to="/generate"
154 |               className="inline-flex items-center px-8 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-bold rounded-xl hover:from-blue-600 hover:to-purple-700 transition-all transform hover:scale-105 shadow-xl hover:shadow-2xl hover:shadow-purple-500/30"
155 |             >
156 |               Generate Your Pathway
157 |               <svg className="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
158 |                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
159 |               </svg>
160 |             </Link>
161 |           </div>
162 |         </div>
163 |       </div>
164 |     );
165 |   }
166 | 
167 |   // Calculate progress
168 |   const completedWeeks = pathway.weeks.filter((week) => week.completed).length;
169 |   const totalWeeks = pathway.weeks.length;
170 | 
171 |   return (
172 |     <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 relative overflow-hidden">
173 |       {/* Animated background */}
174 |       <div className="absolute inset-0 overflow-hidden pointer-events-none">
175 |         <div className="absolute top-1/4 right-1/3 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl"></div>
176 |         <div className="absolute bottom-1/4 left-1/3 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl"></div>
177 |       </div>
178 | 
179 |       <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 relative z-10">
180 |         {/* Header */}
181 |         <div className="mb-10">
182 |           <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-4 mb-6">
183 |             <div className="flex-1">
184 |               <div className="inline-flex items-center px-3 py-1 bg-gradient-to-r from-blue-500/10 to-purple-500/10 border border-blue-500/20 rounded-full mb-4">
185 |                 <span className="w-2 h-2 bg-green-500 rounded-full mr-2 animate-pulse"></span>
186 |                 <span className="text-green-400 text-xs font-medium">Active Pathway</span>
187 |               </div>
188 |               <h1 className="text-4xl md:text-5xl font-bold text-white mb-3 leading-tight">{pathway.title}</h1>
189 |               <p className="text-lg text-slate-300 leading-relaxed">{pathway.summary}</p>
190 |             </div>
191 |             <button
192 |               onClick={handleClearPathway}
193 |               className="px-5 py-2.5 bg-slate-800/80 backdrop-blur-sm text-slate-300 rounded-xl hover:bg-slate-700 transition-all border border-slate-700 hover:border-slate-600 flex items-center space-x-2 self-start"
194 |             >
195 |               <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
196 |                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
197 |               </svg>
198 |               <span>Clear</span>
199 |             </button>
200 |           </div>
201 | 
202 |           {/* Pathway Info Cards */}
203 |           <div className="grid md:grid-cols-3 gap-4 mb-6">
204 |             <div className="group bg-slate-900/50 backdrop-blur-sm rounded-xl p-5 border border-slate-800 hover:border-blue-500/50 transition-all">
205 |               <div className="flex items-center space-x-3 mb-2">
206 |                 <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-blue-600 rounded-lg flex items-center justify-center">
207 |                   <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
208 |                     <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
209 |                   </svg>
210 |                 </div>
211 |                 <div className="text-xs font-medium text-slate-400">Career Goal</div>
212 |               </div>
213 |               <div className="text-xl font-bold text-white">{pathway.goal}</div>
214 |             </div>
215 |             
216 |             <div className="group bg-slate-900/50 backdrop-blur-sm rounded-xl p-5 border border-slate-800 hover:border-purple-500/50 transition-all">
217 |               <div className="flex items-center space-x-3 mb-2">
218 |                 <div className="w-10 h-10 bg-gradient-to-br from-purple-500 to-purple-600 rounded-lg flex items-center justify-center">
219 |                   <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
220 |                     <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
221 |                   </svg>
222 |                 </div>
223 |                 <div className="text-xs font-medium text-slate-400">Skill Level</div>
224 |               </div>
225 |               <div className="text-xl font-bold text-white capitalize">{pathway.level}</div>
226 |             </div>
227 |             
228 |             <div className="group bg-slate-900/50 backdrop-blur-sm rounded-xl p-5 border border-slate-800 hover:border-green-500/50 transition-all">
229 |               <div className="flex items-center space-x-3 mb-2">
230 |                 <div className="w-10 h-10 bg-gradient-to-br from-green-500 to-green-600 rounded-lg flex items-center justify-center">
231 |                   <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
232 |                     <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
233 |                   </svg>
234 |                 </div>
235 |                 <div className="text-xs font-medium text-slate-400">Timeframe</div>
236 |               </div>
237 |               <div className="text-xl font-bold text-white">
238 |                 {pathway._metadata?.originalTimeframe || pathway.weeks?.length ? `${pathway.weeks.length} weeks` : pathway.weeklyTimeCommitment}
239 |               </div>
240 |             </div>
241 |           </div>
242 | 
243 |           {/* Progress Section */}
244 |           <div className="bg-gradient-to-br from-slate-900/80 to-slate-900/50 backdrop-blur-sm rounded-2xl p-6 md:p-8 border border-slate-800 shadow-xl">
245 |             <div className="flex items-center justify-between mb-4">
246 |               <div>
247 |                 <h3 className="text-xl font-bold text-white mb-1">Your Progress</h3>
248 |                 <p className="text-sm text-slate-400">
249 |                   {completedWeeks} of {totalWeeks} weeks completed
250 |                 </p>
251 |               </div>
252 |               <div className="text-right">
253 |                 <div className="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-600">
254 |                   {totalWeeks > 0 ? Math.round((completedWeeks / totalWeeks) * 100) : 0}%
255 |                 </div>
256 |                 <div className="text-xs text-slate-500 mt-1">Complete</div>
257 |               </div>
258 |             </div>
259 |             <ProgressBar completed={completedWeeks} total={totalWeeks} />
260 |           </div>
261 | 
262 |           {/* Adapt My Path Section */}
263 |           <div className="mt-4 bg-gradient-to-br from-slate-900/80 to-slate-900/50 backdrop-blur-sm rounded-2xl border border-slate-800 overflow-hidden shadow-xl">
264 |             <button
265 |               onClick={() => setShowAdaptSection(!showAdaptSection)}
266 |               className="w-full p-6 md:p-8 flex items-center justify-between hover:bg-slate-800/30 transition-all group"
267 |             >
268 |               <div className="flex items-center space-x-4">
269 |                 <div className="w-12 h-12 bg-pink-500/70 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform shadow-lg shadow-pink-500/30">
270 |                   <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
271 |                     <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
272 |                   </svg>
273 |                 </div>
274 |                 <div className="text-left">
275 |                   <h3 className="text-xl font-bold text-white mb-1">Adapt My Path</h3>
276 |                   <p className="text-sm text-slate-400">Customize your learning journey based on your needs</p>
277 |                 </div>
278 |               </div>
279 |               <div className="flex items-center space-x-3">
280 |                 {showAdaptSection && (
281 |                   <span className="hidden md:inline-block px-3 py-1 bg-purple-500/10 text-purple-400 text-xs font-medium rounded-full border border-purple-500/20">
282 |                     Expanded
283 |                   </span>
284 |                 )}
285 |                 <svg
286 |                   className={`w-6 h-6 text-slate-400 transition-transform ${
287 |                     showAdaptSection ? 'rotate-180' : ''
288 |                   }`}
289 |                   fill="none"
290 |                   stroke="currentColor"
291 |                   viewBox="0 0 24 24"
292 |                 >
293 |                   <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
294 |                 </svg>
295 |               </div>
296 |             </button>
297 | 
298 |             {showAdaptSection && (
299 |               <div className="border-t border-slate-800 p-6 md:p-8 space-y-6">
300 |                 <div>
301 |                   <label className="block text-sm font-semibold text-slate-200 mb-3">
302 |                     How would you like to adjust your pathway?
303 |                   </label>
304 |                   <textarea
305 |                     value={feedback}
306 |                     onChange={(e) => setFeedback(e.target.value)}
307 |                     placeholder="Examples:&#10;• I only have 1 hour per day now&#10;• I want more project-based learning&#10;• I'm struggling with JavaScript&#10;• I need more beginner-friendly resources"
308 |                     className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent resize-none transition-all"
309 |                     rows="5"
310 |                   />
311 |                   <p className="mt-2 text-xs text-slate-500">Be specific about what you'd like to change</p>
312 |                 </div>
313 | 
314 |                 {adaptError && (
315 |                   <div className="p-4 bg-red-500/10 border border-red-500/30 rounded-xl flex items-start space-x-3">
316 |                     <svg className="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
317 |                       <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
318 |                     </svg>
319 |                     <p className="text-red-400 text-sm">{adaptError}</p>
320 |                   </div>
321 |                 )}
322 | 
323 |                 <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
324 |                   <button
325 |                     onClick={handleAdaptPathway}
326 |                     disabled={isAdapting}
327 |                     className="flex-1 sm:flex-none px-6 py-3.5 bg-pink-500/70 text-white font-bold rounded-xl hover:from-purple-600 hover:to-pink-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-lg hover:shadow-xl hover:shadow-purple-500/30 flex items-center justify-center"
328 |                   >
329 |                     {isAdapting ? (
330 |                       <>
331 |                         <svg className="animate-spin -ml-1 mr-2 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
332 |                           <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
333 |                           <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
334 |                         </svg>
335 |                         Adapting...
336 |                       </>
337 |                     ) : (
338 |                       <>
339 |                         <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
340 |                           <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
341 |                         </svg>
342 |                         Adapt Pathway
343 |                       </>
344 |                     )}
345 |                   </button>
346 |                   <button
347 |                     onClick={() => {
348 |                       setShowAdaptSection(false);
349 |                       setFeedback('');
350 |                       setAdaptError(null);
351 |                     }}
352 |                     className="px-6 py-3.5 bg-slate-800/80 backdrop-blur-sm text-slate-300 rounded-xl hover:bg-slate-700 transition-all border border-slate-700"
353 |                   >
354 |                     Cancel
355 |                   </button>
356 |                 </div>
357 | 
358 |                 {pathway.adaptationHistory && pathway.adaptationHistory.length > 0 && (
359 |                   <div className="pt-6 border-t border-slate-800">
360 |                     <h4 className="text-sm font-bold text-slate-200 mb-4 flex items-center">
361 |                       <svg className="w-4 h-4 mr-2 text-purple-400" fill="currentColor" viewBox="0 0 20 20">
362 |                         <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clipRule="evenodd" />
363 |                       </svg>
364 |                       Adaptation History
365 |                     </h4>
366 |                     <div className="space-y-3">
367 |                       {pathway.adaptationHistory.map((note, index) => (
368 |                         <div key={index} className="flex items-start space-x-3 p-3 bg-slate-800/30 rounded-lg">
369 |                           <svg className="w-5 h-5 text-purple-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
370 |                             <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
371 |                           </svg>
372 |                           <span className="text-sm text-slate-300 leading-relaxed">{note}</span>
373 |                         </div>
374 |                       ))}
375 |                     </div>
376 |                   </div>
377 |                 )}
378 |               </div>
379 |             )}
380 |           </div>
381 |         </div>
382 | 
383 |         {/* Weekly Plans */}
384 |         <div className="mb-12">
385 |           <h2 className="text-2xl font-bold text-white mb-6">Weekly Learning Plan</h2>
386 |           <div className="space-y-4">
387 |             {pathway.weeks.map((week) => (
388 |               <WeekCard
389 |                 key={week.weekNumber}
390 |                 week={week}
391 |                 onToggleComplete={handleToggleWeekComplete}
392 |               />
393 |             ))}
394 |           </div>
395 |         </div>
396 | 
397 |         {/* Portfolio Checklist */}
398 |         <div className="mb-12">
399 |           <h2 className="text-2xl font-bold text-white mb-6">Final Portfolio Checklist</h2>
400 |           <div className="bg-slate-900 rounded-xl border border-slate-800 p-6">
401 |             <ul className="space-y-3">
402 |               {pathway.finalPortfolioChecklist.map((item, index) => (
403 |                 <li key={index} className="flex items-start space-x-3">
404 |                   <div className="w-6 h-6 bg-slate-800 rounded border border-slate-700 flex items-center justify-center flex-shrink-0 mt-0.5">
405 |                     <svg className="w-4 h-4 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
406 |                       <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
407 |                     </svg>
408 |                   </div>
409 |                   <span className="text-slate-300">{item}</span>
410 |                 </li>
411 |               ))}
412 |             </ul>
413 |           </div>
414 |         </div>
415 | 
416 |         {/* Federal Job Opportunities */}
417 |         <div className="mb-12">
418 |           <h2 className="text-2xl font-bold text-white mb-6">Federal Job Opportunities</h2>
419 |           
420 |           {/* Search Box */}
421 |           <div className="bg-slate-900/50 backdrop-blur-sm rounded-xl border border-slate-800 p-6 mb-6">
422 |             <div className="flex flex-col md:flex-row gap-4">
423 |               <div className="flex-1">
424 |                 <label htmlFor="jobLocation" className="block text-sm font-medium text-slate-300 mb-2">
425 |                   Location (optional)
426 |                 </label>
427 |                 <input
428 |                   type="text"
429 |                   id="jobLocation"
430 |                   value={jobLocation}
431 |                   onChange={(e) => setJobLocation(e.target.value)}
432 |                   placeholder="e.g., Orlando, Florida, or leave empty for nationwide"
433 |                   className="w-full px-4 py-3 bg-slate-800/50 border border-slate-700 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
434 |                 />
435 |               </div>
436 |               <div className="flex items-end">
437 |                 <button
438 |                   onClick={handleSearchJobs}
439 |                   disabled={jobsLoading}
440 |                   className="px-6 py-3 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold rounded-lg hover:from-blue-600 hover:to-purple-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2 shadow-lg hover:shadow-xl hover:shadow-blue-500/30"
441 |                 >
442 |                   {jobsLoading ? (
443 |                     <>
444 |                       <svg className="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
445 |                         <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
446 |                         <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
447 |                       </svg>
448 |                       <span>Searching...</span>
449 |                     </>
450 |                   ) : (
451 |                     <>
452 |                       <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
453 |                         <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
454 |                       </svg>
455 |                       <span>Search Jobs</span>
456 |                     </>
457 |                   )}
458 |                 </button>
459 |               </div>
460 |             </div>
461 |             
462 |             {/* Search Info */}
463 |             {jobsData && (
464 |               <div className="mt-4 flex items-center space-x-2 text-sm text-slate-400">
465 |                 <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
466 |                   <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
467 |                 </svg>
468 |                 <span>
469 |                   Searching for: <strong className="text-white">{jobsData.keyword}</strong>
470 |                   {jobsData.originalLocation && (
471 |                     <> in <strong className="text-white">{jobsData.originalLocation}</strong></>
472 |                   )}
473 |                 </span>
474 |               </div>
475 |             )}
476 |           </div>
477 | 
478 |           {/* Fallback Message */}
479 |           {jobsData?.fallbackMessage && (
480 |             <div className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-4 mb-6 flex items-start space-x-3">
481 |               <svg className="w-5 h-5 text-blue-400 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
482 |                 <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
483 |               </svg>
484 |               <p className="text-blue-300">{jobsData.fallbackMessage}</p>
485 |             </div>
486 |           )}
487 | 
488 |           {/* Error Message */}
489 |           {jobsError && (
490 |             <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 mb-6 flex items-start space-x-3">
491 |               <svg className="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
492 |                 <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
493 |               </svg>
494 |               <p className="text-red-400">{jobsError}</p>
495 |             </div>
496 |           )}
497 | 
498 |           {/* Jobs List */}
499 |           {jobsData && jobsData.count > 0 ? (
500 |             <div className="space-y-4">
501 |               <div className="flex items-center justify-between mb-4">
502 |                 <p className="text-slate-400">
503 |                   Found <strong className="text-white">{jobsData.count}</strong> job{jobsData.count !== 1 ? 's' : ''}
504 |                 </p>
505 |                 <span className="px-3 py-1 bg-slate-800 text-slate-300 text-xs font-medium rounded-full border border-slate-700">
506 |                   {jobsData.searchLevel === 'city' ? '📍 City' : jobsData.searchLevel === 'state' ? '🗺️ State' : '🌎 Nationwide'}
507 |                 </span>
508 |               </div>
509 |               {jobsData.jobs.map((job, index) => (
510 |                 <JobCard key={index} job={job} />
511 |               ))}
512 |             </div>
513 |           ) : jobsData && jobsData.count === 0 ? (
514 |             <div className="bg-slate-900/50 backdrop-blur-sm rounded-xl border border-slate-800 p-8 text-center">
515 |               <div className="w-16 h-16 bg-slate-800 rounded-full flex items-center justify-center mx-auto mb-4">
516 |                 <svg className="w-8 h-8 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
517 |                   <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
518 |                 </svg>
519 |               </div>
520 |               <h3 className="text-xl font-bold text-white mb-2">No Jobs Found</h3>
521 |               <p className="text-slate-400">
522 |                 Try adjusting your search location or check back later for new postings.
523 |               </p>
524 |             </div>
525 |           ) : !jobsLoading && !jobsData && (
526 |             <div className="bg-slate-900/50 backdrop-blur-sm rounded-xl border border-slate-800 p-8 text-center">
527 |               <div className="w-16 h-16 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center mx-auto mb-4">
528 |                 <svg className="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
529 |                   <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
530 |                 </svg>
531 |               </div>
532 |               <h3 className="text-xl font-bold text-white mb-2">Discover Federal Opportunities</h3>
533 |               <p className="text-slate-400">
534 |                 Click "Search Jobs" to find federal positions related to your career goal.
535 |               </p>
536 |             </div>
537 |           )}
538 |         </div>
539 | 
540 |         {/* GitHub Projects - ALWAYS SHOW SECTION */}
541 |         <div className="mb-12">
542 |           <h2 className="text-2xl font-bold text-white mb-6">Recommended GitHub Projects</h2>
543 |           <p className="text-slate-400 mb-6">
544 |             Explore these beginner-friendly projects to practice your skills and build your portfolio.
545 |           </p>
546 |           
547 |           {pathway.githubProjects && pathway.githubProjects.length > 0 ? (
548 |             <div className="grid md:grid-cols-2 gap-4">
549 |               {pathway.githubProjects
550 |                 .filter(project => {
551 |                   // Only filter out projects without valid URLs
552 |                   const hasValidUrl = project.url && project.url !== '#' && project.url !== '';
553 |                   return hasValidUrl;
554 |                 })
555 |                 .map((project, index) => {
556 |                   // Reduce debug logging - only log once per project
557 |                   if (index === 0) {
558 |                     console.log(`🐙 Rendering ${pathway.githubProjects.length} GitHub projects`);
559 |                   }
560 |                   
561 |                   // Get confidence level
562 |                   const confidence = project.confidence || 'medium';
563 |                   const confidenceColors = {
564 |                     high: 'bg-green-500/10 text-green-400 border-green-500/30',
565 |                     medium: 'bg-blue-500/10 text-blue-400 border-blue-500/30',
566 |                     low: 'bg-yellow-500/10 text-yellow-400 border-yellow-500/30'
567 |                   };
568 |                   
569 |                   return (
570 |                     <a
571 |                       key={index}
572 |                       href={project.url}
573 |                       target="_blank"
574 |                       rel="noopener noreferrer"
575 |                       className="group bg-slate-900/50 backdrop-blur-sm rounded-xl p-6 border border-slate-800 hover:border-purple-500/50 transition-all hover:shadow-xl hover:shadow-purple-500/10"
576 |                     >
577 |                       <div className="flex items-start justify-between mb-3">
578 |                         <div className="flex items-center space-x-3 flex-1 min-w-0">
579 |                           <div className="w-10 h-10 bg-gradient-to-br from-purple-500 to-purple-600 rounded-lg flex items-center justify-center flex-shrink-0">
580 |                             <svg className="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
581 |                               <path fillRule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clipRule="evenodd" />
582 |                             </svg>
583 |                           </div>
584 |                           <h3 className="text-lg font-bold text-white group-hover:text-purple-400 transition-colors truncate">{project.name}</h3>
585 |                         </div>
586 |                         <div className="flex items-center space-x-2 flex-shrink-0 ml-2">
587 |                           {project.stars > 0 && (
588 |                             <div className="flex items-center space-x-1 text-yellow-400">
589 |                               <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
590 |                                 <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
591 |                               </svg>
592 |                               <span className="text-sm font-medium">{project.stars.toLocaleString()}</span>
593 |                             </div>
594 |                           )}
595 |                         </div>
596 |                       </div>
597 |                       
598 |                       <p className="text-slate-300 text-sm leading-relaxed mb-4 line-clamp-2">{project.description || 'No description available'}</p>
599 |                       
600 |                       <div className="flex items-center justify-between flex-wrap gap-2">
601 |                         <div className="flex items-center space-x-2">
602 |                           {project.language && (
603 |                             <span className="px-3 py-1 bg-blue-500/10 text-blue-400 text-xs font-medium rounded-full border border-blue-500/30">
604 |                               {project.language}
605 |                             </span>
606 |                           )}
607 |                           {project.confidence && (
608 |                             <span className={`px-2.5 py-1 text-xs font-bold rounded-full border ${confidenceColors[confidence]}`} title={`Match confidence: ${confidence}`}>
609 |                               {confidence === 'high' ? '✓✓' : confidence === 'medium' ? '✓' : '~'} {confidence}
610 |                             </span>
611 |                           )}
612 |                         </div>
613 |                         <span className="text-slate-500 text-xs flex items-center">
614 |                           <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
615 |                             <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
616 |                           </svg>
617 |                           View on GitHub
618 |                         </span>
619 |                       </div>
620 |                       
621 |                       {/* Additional metadata */}
622 |                       {(project.forks > 0 || project.updated_at || project.reason) && (
623 |                         <div className="mt-4 pt-4 border-t border-slate-700/50 space-y-2">
624 |                           {project.forks > 0 && (
625 |                             <div className="flex items-center text-xs text-slate-400">
626 |                               <svg className="w-3.5 h-3.5 mr-1.5" fill="currentColor" viewBox="0 0 16 16">
627 |                                 <path fillRule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path>
628 |                               </svg>
629 |                               {project.forks.toLocaleString()} forks
630 |                             </div>
631 |                           )}
632 |                           {project.updated_at && (
633 |                             <div className="flex items-center text-xs text-slate-400">
634 |                               <svg className="w-3.5 h-3.5 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
635 |                                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
636 |                               </svg>
637 |                               Updated {new Date(project.updated_at).toLocaleDateString()}
638 |                             </div>
639 |                           )}
640 |                           {project.reason && (
641 |                             <div className="flex items-start text-xs text-slate-400 italic">
642 |                               <svg className="w-3.5 h-3.5 mr-1.5 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
643 |                                 <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
644 |                               </svg>
645 |                               <span className="leading-tight">{project.reason}</span>
646 |                             </div>
647 |                           )}
648 |                         </div>
649 |                       )}
650 |                     </a>
651 |                   );
652 |                 })}
653 |             </div>
654 |           ) : (
655 |             <div className="bg-slate-900/50 backdrop-blur-sm rounded-xl border border-slate-800 p-8 text-center">
656 |               <div className="w-16 h-16 bg-slate-800 rounded-full flex items-center justify-center mx-auto mb-4">
657 |                 <svg className="w-8 h-8 text-slate-500" fill="currentColor" viewBox="0 0 24 24">
658 |                   <path fillRule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clipRule="evenodd" />
659 |                 </svg>
660 |               </div>
661 |               <h3 className="text-xl font-bold text-white mb-2">No GitHub Projects Found</h3>
662 |               <p className="text-slate-400">
663 |                 No strong GitHub projects found for this path yet. Check back after generating a new roadmap.
664 |               </p>
665 |             </div>
666 |           )}
667 |         </div>
668 | 
669 |         {/* Recommended Certifications */}
670 |         {pathway.recommendedCertifications && pathway.recommendedCertifications.length > 0 && (
671 |           <div className="mb-12">
672 |             <h2 className="text-2xl font-bold text-white mb-6">Recommended Certifications</h2>
673 |             <div className="grid md:grid-cols-2 gap-4">
674 |               {pathway.recommendedCertifications.map((cert, index) => (
675 |                 <div
676 |                   key={index}
677 |                   className="bg-slate-900 rounded-xl border border-slate-800 p-6"
678 |                 >
679 |                   <div className="flex items-start justify-between mb-3">
680 |                     <h3 className="text-lg font-semibold text-white">{cert.name}</h3>
681 |                     <span className={`px-3 py-1 rounded-full text-xs font-medium ${
682 |                       cert.priority === 'essential'
683 |                         ? 'bg-red-500/10 text-red-500 border border-red-500/20'
684 |                         : cert.priority === 'recommended'
685 |                         ? 'bg-yellow-500/10 text-yellow-500 border border-yellow-500/20'
686 |                         : 'bg-blue-500/10 text-blue-500 border border-blue-500/20'
687 |                     }`}>
688 |                       {cert.priority}
689 |                     </span>
690 |                   </div>
691 |                   <p className="text-slate-400 text-sm mb-4">{cert.provider}</p>
692 |                   <div className="flex items-center justify-between text-sm">
693 |                     <span className="text-slate-500">Cost: {cert.cost}</span>
694 |                     <span className="text-slate-500">{cert.timeToComplete}</span>
695 |                   </div>
696 |                 </div>
697 |               ))}
698 |             </div>
699 |           </div>
700 |         )}
701 | 
702 |         {/* Action Buttons */}
703 |         <div className="mt-12 flex justify-center space-x-4">
704 |           <Link
705 |             to="/generate"
706 |             className="px-6 py-3 bg-slate-800 text-white font-semibold rounded-lg hover:bg-slate-700 transition-colors border border-slate-700"
707 |           >
708 |             Generate New Pathway
709 |           </Link>
710 |         </div>
711 |       </div>
712 |     </div>
713 |   );
714 | }
715 | 
716 | export default PathwayPage;
717 | 
718 | // Made with Bob
</content>
</file>
<file><path>client/src/utils/api.js</path>
<content lines="1-536">
  1 | import axios from 'axios';
  2 | 
  3 | /**
  4 |  * API utility functions for PathPilot AI
  5 |  * Handles communication with the FastAPI backend
  6 |  */
  7 | 
  8 | // Base URL for the API
  9 | const API_BASE_URL = 'http://localhost:8000';
 10 | 
 11 | /**
 12 |  * Create an axios instance with default config
 13 |  */
 14 | const api = axios.create({
 15 |   baseURL: API_BASE_URL,
 16 |   headers: {
 17 |     'Content-Type': 'application/json',
 18 |   },
 19 |   timeout: 30000, // 30 seconds timeout
 20 | });
 21 | 
 22 | /**
 23 |  * Check if the API is healthy
 24 |  * @returns {Promise<Object>} Health status
 25 |  */
 26 | export const checkHealth = async () => {
 27 |   try {
 28 |     const response = await api.get('/');
 29 |     return response.data;
 30 |   } catch (error) {
 31 |     console.error('Health check failed:', error);
 32 |     throw error;
 33 |   }
 34 | };
 35 | 
 36 | /**
 37 |  * Generate a career pathway
 38 |  * @param {Object} formData - The form data from the user
 39 |  * @param {string} formData.goal - Career goal
 40 |  * @param {string} formData.level - Skill level (beginner, intermediate, advanced)
 41 |  * @param {number} formData.weeks - Number of weeks
 42 |  * @param {number} formData.daysPerWeek - Days per week
 43 |  * @param {number} formData.hoursPerDay - Hours per day
 44 |  * @param {Array<string>} formData.preferences - Learning preferences
 45 |  * @param {string} formData.budget - Budget preference
 46 |  * @returns {Promise<Object>} Generated pathway
 47 |  */
 48 | export const generatePathway = async (formData) => {
 49 |   try {
 50 |     const response = await api.post('/api/pathways/generate', formData);
 51 |     return response.data;
 52 |   } catch (error) {
 53 |     console.error('Failed to generate pathway:', error);
 54 |     
 55 |     // Provide more detailed error message
 56 |     if (error.response) {
 57 |       // Server responded with error
 58 |       throw new Error(error.response.data.detail || 'Failed to generate pathway', { cause: error });
 59 |     } else if (error.request) {
 60 |       // Request made but no response
 61 |       throw new Error('Cannot connect to server. Make sure the backend is running at http://localhost:8000', { cause: error });
 62 |     } else {
 63 |       // Something else happened
 64 |       throw new Error('An unexpected error occurred', { cause: error });
 65 |     }
 66 |   }
 67 | };
 68 | 
 69 | /**
 70 |  * Adapt an existing pathway based on user feedback
 71 |  * @param {Object} pathway - The current pathway object
 72 |  * @param {string} feedback - User feedback for adaptation
 73 |  * @returns {Promise<Object>} Adapted pathway
 74 |  */
 75 | export const adaptPathway = async (pathway, feedback) => {
 76 |   try {
 77 |     console.log('📡 Sending adapt request to API...');
 78 |     console.log('Request payload:', { pathway, feedback });
 79 |     
 80 |     const response = await api.post('/api/pathways/adapt', {
 81 |       pathway,
 82 |       feedback,
 83 |     });
 84 |     
 85 |     console.log('📡 API Response received:', response.data);
 86 |     return response.data;
 87 |   } catch (error) {
 88 |     console.error('❌ API Error:', error);
 89 |     console.error('Error response:', error.response?.data);
 90 |     
 91 |     // Provide more detailed error message
 92 |     if (error.response) {
 93 |       throw new Error(error.response.data.detail || 'Failed to adapt pathway', { cause: error });
 94 |     } else if (error.request) {
 95 |       throw new Error('Cannot connect to server. Make sure the backend is running at http://localhost:8000', { cause: error });
 96 |     } else {
 97 |       throw new Error('An unexpected error occurred', { cause: error });
 98 |     }
 99 |   }
100 | };
101 | 
102 | /**
103 |  * Generate an AI-powered career roadmap using IBM watsonx.ai
104 |  * @param {Object} requestData - The roadmap request data
105 |  * @param {string} requestData.careerGoal - Target career role (e.g., "SOC Analyst")
106 |  * @param {Array<string>} requestData.currentSkills - List of current skills
107 |  * @param {string} requestData.timeframe - Available timeframe (e.g., "3 months")
108 |  * @returns {Promise<Object>} AI-generated roadmap with metadata
109 |  */
110 | export const generateRoadmap = async (requestData) => {
111 |   try {
112 |     console.log('🤖 Generating AI roadmap with watsonx.ai...');
113 |     console.log('Request data:', requestData);
114 |     
115 |     const response = await api.post('/api/generate-roadmap', requestData, {
116 |       timeout: 90000, // 90 seconds for AI generation
117 |     });
118 |     
119 |     console.log('✅ Roadmap generated successfully');
120 |     console.log('📦 Raw response from backend:', response.data);
121 |     return response.data;
122 |   } catch (error) {
123 |     console.error('❌ Failed to generate roadmap:', error);
124 |     
125 |     if (error.response) {
126 |       throw new Error(error.response.data.detail || 'Failed to generate roadmap', { cause: error });
127 |     } else if (error.request) {
128 |       throw new Error('Cannot connect to server. Make sure the backend is running at http://localhost:8000', { cause: error });
129 |     } else {
130 |       throw new Error('An unexpected error occurred', { cause: error });
131 |     }
132 |   }
133 | };
134 | 
135 | /**
136 |  * Transform Watsonx.ai roadmap response to match frontend PathwayResponse format
137 |  * @param {Object} roadmapResponse - Response from /api/generate-roadmap
138 |  * @param {Object} formData - Original form data from user
139 |  * @returns {Object} Transformed pathway object for frontend
140 |  */
141 | export const transformRoadmapToPathway = (roadmapResponse, formData) => {
142 |   console.log('='.repeat(80));
143 |   console.log('🔄 TRANSFORMING ROADMAP TO PATHWAY FORMAT');
144 |   console.log('='.repeat(80));
145 |   console.log('📦 Raw backend response:', JSON.stringify(roadmapResponse, null, 2));
146 |   console.log('📋 Form data:', formData);
147 |   
148 |   const roadmap = roadmapResponse.roadmap || {};
149 |   const metadata = roadmapResponse.metadata || {};
150 |   
151 |   // Log whether WatsonX was used
152 |   console.log('\n' + '='.repeat(80));
153 |   if (metadata.usedWatsonx === true) {
154 |     console.log('✅ USING WATSONX.AI GENERATED ROADMAP');
155 |     console.log(`   Model: ${metadata.model || 'unknown'}`);
156 |     console.log(`   Tokens: ${metadata.tokens || 0}`);
157 |     console.log(`   GitHub Projects: ${metadata.usedGitHub ? 'Yes' : 'No'}`);
158 |     console.log(`   Local Resources: ${metadata.matchedLocalResources || 0}`);
159 |   } else {
160 |     console.warn('⚠️  USING FALLBACK TEMPLATE DATA (WatsonX unavailable)');
161 |     console.warn(`   Reason: ${metadata.fallbackReason || 'unknown'}`);
162 |   }
163 |   console.log('='.repeat(80) + '\n');
164 |   
165 |   // Log roadmap structure
166 |   console.log('📊 Roadmap structure:');
167 |   console.log(`   Phases: ${roadmap.phases?.length || 0}`);
168 |   console.log(`   Weekly Plans: ${roadmap.weeklyPlan?.length || 0}`);
169 |   console.log(`   Skills: ${roadmap.skills?.length || 0}`);
170 |   console.log(`   Resources: ${roadmap.resources?.length || 0}`);
171 |   console.log(`   GitHub Projects: ${roadmap.githubProjects?.length || 0}`);
172 |   console.log(`   Portfolio Projects: ${roadmap.portfolioProjects?.length || 0}`);
173 |   
174 |   // DEBUG: Check if weeklyPlan items have resources
175 |   console.log('\n📊 RESOURCE ALLOCATION CHECK:');
176 |   console.log(`   Global resources: ${roadmap.resources?.length || 0}`);
177 |   if (roadmap.weeklyPlan && roadmap.weeklyPlan.length > 0) {
178 |     roadmap.weeklyPlan.forEach((week, idx) => {
179 |       const weekNum = week.week || idx + 1;
180 |       const resourceCount = week.resources?.length || 0;
181 |       console.log(`   Week ${weekNum}: ${resourceCount} resources ${resourceCount > 0 ? '✅' : '❌'}`);
182 |     });
183 |   }
184 |   console.log('=' .repeat(80));
185 |   
186 |   // Transform phases into weeks
187 |   const weeks = [];
188 |   const phases = roadmap.phases || [];
189 |   const weeklyPlan = roadmap.weeklyPlan || [];
190 |   
191 |   // BACKEND NOW ENFORCES CORRECT TIMEFRAME
192 |   // Trust the backend's weeklyPlan length
193 |   let totalWeeks = weeklyPlan.length || formData.weeks || 12;
194 |   
195 |   console.log(`\n📅 TIMEFRAME FROM BACKEND:`);
196 |   console.log(`   User requested: ${formData.weeks} weeks`);
197 |   console.log(`   Backend returned: ${weeklyPlan.length} weekly plans`);
198 |   console.log(`   Using: ${totalWeeks} weeks`);
199 |   
200 |   // Warn if mismatch (should not happen with enforcer)
201 |   if (weeklyPlan.length !== formData.weeks) {
202 |       console.warn(`⚠️  MISMATCH: Backend returned ${weeklyPlan.length} weeks but user requested ${formData.weeks}`);
203 |       console.warn(`   This should not happen - check backend enforcer`);
204 |   }
205 |   
206 |   // Create weeks from weekly plan (backend should provide exact count)
207 |   for (let i = 0; i < totalWeeks; i++) {
208 |       const weekNum = i + 1;
209 |       const phaseIndex = Math.floor(i / Math.ceil(totalWeeks / Math.max(phases.length, 1)));
210 |       const phase = phases[phaseIndex] || phases[0] || {};
211 |       const weekPlan = weeklyPlan[i] || {};
212 |       
213 |       // If weekPlan is missing, warn (should not happen)
214 |       if (!weekPlan || Object.keys(weekPlan).length === 0) {
215 |           console.error(`❌ Week ${weekNum} has no plan from backend!`);
216 |       }
217 |     
218 |     console.log(`\n📆 Week ${weekNum}:`, {
219 |       focus: weekPlan.focus,
220 |       topics: weekPlan.topics,
221 |       dailyTasks: weekPlan.dailyTasks,
222 |       phase: phase.title
223 |     });
224 |     
225 |     // Generate daily plan using AI-provided data
226 |     const dailyPlan = [];
227 |     const daysPerWeek = formData.daysPerWeek || 5;
228 |     const hoursPerDay = formData.hoursPerDay || 2;
229 |     
230 |     // Use AI-generated daily tasks and topics
231 |     const aiDailyTasks = weekPlan.dailyTasks || [];
232 |     const aiTopics = weekPlan.topics || [];
233 |     const weekFocus = weekPlan.focus || phase.focus || phase.title || `Week ${weekNum} Learning`;
234 |     
235 |     console.log(`   Daily tasks (${aiDailyTasks.length}):`, aiDailyTasks);
236 |     console.log(`   Topics (${aiTopics.length}):`, aiTopics);
237 |     
238 |     // Create daily plan cards - one card per day showing the week's focus
239 |     for (let day = 1; day <= daysPerWeek; day++) {
240 |       const dayTasks = [];
241 |       
242 |       // Use AI-generated tasks, distributed across days
243 |       if (aiDailyTasks.length > 0) {
244 |         // Distribute tasks across days
245 |         const tasksPerDay = Math.ceil(aiDailyTasks.length / daysPerWeek);
246 |         const startIdx = (day - 1) * tasksPerDay;
247 |         const endIdx = Math.min(startIdx + tasksPerDay, aiDailyTasks.length);
248 |         
249 |         for (let t = startIdx; t < endIdx; t++) {
250 |           if (aiDailyTasks[t]) {
251 |             dayTasks.push(aiDailyTasks[t]);
252 |           }
253 |         }
254 |       }
255 |       
256 |       // Add topics as tasks if we don't have enough tasks
257 |       if (dayTasks.length === 0 && aiTopics.length > 0) {
258 |         const topicIdx = (day - 1) % aiTopics.length;
259 |         if (aiTopics[topicIdx]) {
260 |           dayTasks.push(`Study: ${aiTopics[topicIdx]}`);
261 |         }
262 |       }
263 |       
264 |       // Add practice task
265 |       if (aiTopics.length > 0) {
266 |         const practiceTopicIdx = day % aiTopics.length;
267 |         if (aiTopics[practiceTopicIdx]) {
268 |           dayTasks.push(`Practice: ${aiTopics[practiceTopicIdx]}`);
269 |         }
270 |       }
271 |       
272 |       // Ensure at least one task
273 |       if (dayTasks.length === 0) {
274 |         dayTasks.push(`Work on ${weekFocus}`);
275 |       }
276 |       
277 |       dailyPlan.push({
278 |         day,
279 |         focus: `${weekFocus} - Day ${day}`,
280 |         tasks: dayTasks,
281 |         estimatedHours: hoursPerDay
282 |       });
283 |     }
284 |     
285 |     // BACKEND NOW ALLOCATES RESOURCES TO EACH WEEK
286 |     // Use week-specific resources from weekPlan if available
287 |     let resourcesForWeek = weekPlan.resources || [];
288 |     
289 |     console.log(`\n📚 Week ${weekNum} BEFORE allocation:`, {
290 |       weekPlanHasResources: !!weekPlan.resources,
291 |       weekPlanResourcesLength: weekPlan.resources?.length || 0,
292 |       resourcesForWeekLength: resourcesForWeek.length
293 |     });
294 |     
295 |     // Fallback: if backend didn't allocate, distribute from roadmap.resources
296 |     if (resourcesForWeek.length === 0) {
297 |         console.warn(`⚠️  Week ${weekNum}: Backend didn't allocate resources, using fallback`);
298 |         const allResources = roadmap.resources || [];
299 |         console.log(`   Total global resources: ${allResources.length}`);
300 |         
301 |         const resourcesPerWeek = Math.max(Math.ceil(allResources.length / totalWeeks), 1);
302 |         console.log(`   Resources per week (calculated): ${resourcesPerWeek}`);
303 |         
304 |         const startIdx = i * resourcesPerWeek;
305 |         const endIdx = Math.min(startIdx + resourcesPerWeek, allResources.length);
306 |         console.log(`   Slicing resources[${startIdx}:${endIdx}]`);
307 |         
308 |         resourcesForWeek = allResources.slice(startIdx, endIdx);
309 |         console.log(`   Resources after slice: ${resourcesForWeek.length}`);
310 |         
311 |         if (resourcesForWeek.length === 0 && allResources.length > 0) {
312 |             const reuseIdx = i % allResources.length;
313 |             resourcesForWeek = [allResources[reuseIdx]];
314 |             console.warn(`   ⚠️  Reusing resource ${reuseIdx + 1}`);
315 |         }
316 |     } else {
317 |         console.log(`✅ Week ${weekNum}: Using ${resourcesForWeek.length} resources from backend weekPlan`);
318 |     }
319 |     
320 |     console.log(`\n📚 Week ${weekNum} AFTER allocation (${resourcesForWeek.length} resources):`, resourcesForWeek.map(r => r.title));
321 |     
322 |     // Map resources with proper field handling and URL validation
323 |     const mappedResources = resourcesForWeek.map((r, idx) => {
324 |       // Extract provider from URL if not provided
325 |       let provider = r.provider || '';
326 |       const url = r.url || r.link || r.href || '#';
327 |       
328 |       if (!provider && url !== '#') {
329 |         try {
330 |           const urlObj = new URL(url);
331 |           const hostname = urlObj.hostname.replace('www.', '');
332 |           provider = hostname.split('.')[0];
333 |           // Capitalize first letter
334 |           provider = provider.charAt(0).toUpperCase() + provider.slice(1);
335 |         } catch {
336 |           provider = 'External';
337 |         }
338 |       }
339 |       
340 |       const resource = {
341 |         title: r.title || r.name || `${provider} ${r.type || 'Resource'}`,
342 |         type: r.type || 'course',
343 |         url: url,
344 |         provider: provider,
345 |         duration: r.duration || r.estimatedTime || '1-2 hours',
346 |         isFree: r.isFree !== undefined ? r.isFree : (r.cost === 'free' || r.cost === 'Free' || !r.cost)
347 |       };
348 |       
349 |       console.log(`   Resource ${idx + 1}:`, resource);
350 |       return resource;
351 |     });
352 |     
353 |     // Get project for this week - use phase-based or week-specific
354 |     const projectForWeek = roadmap.portfolioProjects?.[phaseIndex] || roadmap.portfolioProjects?.[i] || {};
355 |     
356 |     // Ensure skills is always an array
357 |     let projectSkills = projectForWeek.skills || aiTopics || phase.skills || roadmap.skills?.slice(0, 3) || [];
358 |     
359 |     // Convert to array if it's not already
360 |     if (!Array.isArray(projectSkills)) {
361 |       projectSkills = [projectSkills];
362 |     }
363 |     
364 |     // Filter out empty/undefined values
365 |     projectSkills = projectSkills.filter(skill => skill && typeof skill === 'string' && skill.trim() !== '');
366 |     
367 |     // If still empty, provide default
368 |     if (projectSkills.length === 0) {
369 |       projectSkills = ['Problem Solving', 'Critical Thinking', 'Project Management'];
370 |     }
371 |     
372 |     // Get project URL
373 |     const projectUrl = projectForWeek.url || projectForWeek.link || projectForWeek.githubUrl || projectForWeek.sourceUrl || '';
374 |     
375 |     console.log(`\n🎯 Week ${weekNum} project BEFORE mapping:`, {
376 |       projectForWeek,
377 |       title: projectForWeek.title,
378 |       description: projectForWeek.description,
379 |       skills: projectForWeek.skills,
380 |       url: projectUrl
381 |     });
382 |     
383 |     console.log(`\n🎯 Week ${weekNum} project AFTER processing:`, {
384 |       title: projectForWeek.title || `Week ${weekNum}: ${weekPlan.focus || 'Practical Project'}`,
385 |       skills: projectSkills,
386 |       skillsType: typeof projectSkills,
387 |       skillsIsArray: Array.isArray(projectSkills),
388 |       skillsLength: projectSkills.length,
389 |       url: projectUrl
390 |     });
391 |     
392 |     // Create week object
393 |     weeks.push({
394 |       weekNumber: weekNum,
395 |       title: weekPlan.focus || phase.title || `Week ${weekNum}`,
396 |       objectives: aiTopics.length > 0 ? aiTopics : (phase.skills || roadmap.skills?.slice(0, 3) || ['Learn core concepts', 'Practice skills', 'Build projects']),
397 |       dailyPlan,
398 |       resources: mappedResources,
399 |       guidedProject: {
400 |         title: projectForWeek.title || `Week ${weekNum}: ${weekPlan.focus || 'Practical Project'}`,
401 |         description: projectForWeek.description || `Build a project demonstrating ${weekPlan.focus || 'your skills'}`,
402 |         skills: projectSkills,
403 |         estimatedHours: hoursPerDay * 2,
404 |         difficulty: formData.level || 'beginner',
405 |         url: projectUrl,
406 |         link: projectUrl,
407 |         githubUrl: projectUrl
408 |       },
409 |       resumeBullet: (roadmap.resumeBullets?.[phaseIndex] || `Completed ${weekPlan.focus || `week ${weekNum}`} training in ${formData.goal}`),
410 |       completed: false
411 |     });
412 |   }
413 |   
414 |   // Build the pathway object
415 |   const pathway = {
416 |     title: `${formData.goal} Career Pathway`,
417 |     goal: formData.goal,
418 |     level: formData.level || 'beginner',
419 |     summary: roadmap.summary || `A comprehensive pathway to become a ${formData.goal}`,
420 |     weeklyTimeCommitment: `${(formData.hoursPerDay || 2) * (formData.daysPerWeek || 5)} hours/week`,
421 |     weeks,
422 |     finalPortfolioChecklist: roadmap.nextSteps || [
423 |       'Complete all weekly projects',
424 |       'Build a portfolio website',
425 |       'Create a professional resume',
426 |       'Practice technical interviews',
427 |       'Apply to relevant positions'
428 |     ],
429 |     recommendedCertifications: (roadmap.certifications || []).map(cert => ({
430 |       name: cert.name || cert.title,
431 |       provider: cert.provider || 'Various',
432 |       cost: cert.cost || 'Varies',
433 |       timeToComplete: cert.timeToComplete || cert.duration || 'Varies',
434 |       priority: cert.priority || 'recommended'
435 |     })),
436 |     // Add GitHub projects if available - PRESERVE ALL FIELDS
437 |     githubProjects: (roadmap.githubProjects || []).map(project => {
438 |       console.log('🐙 Mapping GitHub project:', project);
439 |       return {
440 |         name: project.name || project.title || 'GitHub Project',
441 |         fullName: project.fullName || project.full_name || project.name,
442 |         description: project.description || 'No description available',
443 |         url: project.url || project.link || project.html_url || '#',
444 |         stars: project.stars || project.stargazers_count || 0,
445 |         forks: project.forks || project.forks_count || 0,
446 |         language: project.language || 'Unknown',
447 |         topics: project.topics || [],
448 |         updated_at: project.updated_at || project.updatedAt,
449 |         qualityScore: project.qualityScore || project.quality_score,
450 |         confidence: project.confidence || 'medium',
451 |         reason: project.reason || '',
452 |         source: project.source || 'github'
453 |       };
454 |     }),
455 |     // Add metadata for debugging
456 |     _metadata: {
457 |       usedWatsonx: metadata.usedWatsonx !== false,
458 |       generatedAt: new Date().toISOString(),
459 |       githubProjectsCount: roadmap.githubProjects?.length || 0,
460 |       originalTimeframe: formData.timeframe,
461 |       originalRoadmap: roadmap
462 |     }
463 |   };
464 |   
465 |   console.log('\n' + '='.repeat(80));
466 |   console.log('✅ TRANSFORMATION COMPLETE');
467 |   console.log('='.repeat(80));
468 |   console.log(`📦 Pathway title: ${pathway.title}`);
469 |   console.log(`📅 Weeks: ${pathway.weeks.length} (requested: ${formData.weeks})`);
470 |   console.log(`📚 Total resources across all weeks: ${pathway.weeks.reduce((sum, w) => sum + w.resources.length, 0)}`);
471 |   console.log(`🐙 GitHub projects: ${pathway.githubProjects.length}`);
472 |   
473 |   // Log each GitHub project to verify data
474 |   if (pathway.githubProjects.length > 0) {
475 |     console.log('\n🐙 GitHub Projects Details:');
476 |     pathway.githubProjects.forEach((proj, idx) => {
477 |       console.log(`   ${idx + 1}. ${proj.name}`);
478 |       console.log(`      URL: ${proj.url}`);
479 |       console.log(`      Stars: ${proj.stars}`);
480 |       console.log(`      Language: ${proj.language}`);
481 |       console.log(`      Confidence: ${proj.confidence}`);
482 |       console.log(`      Source: ${proj.source}`);
483 |     });
484 |   }
485 |   
486 |   console.log(`\n🎓 Certifications: ${pathway.recommendedCertifications.length}`);
487 |   console.log(`🤖 Used WatsonX: ${pathway._metadata.usedWatsonx ? 'Yes' : 'No'}`);
488 |   console.log('='.repeat(80) + '\n');
489 |   
490 |   return pathway;
491 | };
492 | 
493 | /**
494 |  * Search USAJOBS for federal job postings
495 |  * @param {string} keyword - Search keyword (e.g., "cybersecurity")
496 |  * @param {string} location - Optional location (e.g., "Orlando", "Florida")
497 |  * @returns {Promise<Object>} Job search results with fallback information
498 |  */
499 | export const searchUSAJobs = async (keyword, location = null) => {
500 |   try {
501 |     const params = new URLSearchParams({ keyword });
502 |     if (location) {
503 |       params.append('location', location);
504 |     }
505 |     
506 |     const response = await api.get(`/api/usajobs/search?${params.toString()}`);
507 |     return response.data;
508 |   } catch (error) {
509 |     console.error('Failed to search USAJOBS:', error);
510 |     
511 |     if (error.response) {
512 |       throw new Error(error.response.data.detail || 'Failed to search jobs', { cause: error });
513 |     } else if (error.request) {
514 |       throw new Error('Cannot connect to server. Make sure the backend is running at http://localhost:8000', { cause: error });
515 |     } else {
516 |       throw new Error('An unexpected error occurred', { cause: error });
517 |     }
518 |   }
519 | };
520 | 
521 | /**
522 |  * Test the API connection
523 |  * @returns {Promise<boolean>} True if connected, false otherwise
524 |  */
525 | export const testConnection = async () => {
526 |   try {
527 |     await checkHealth();
528 |     return true;
529 |   } catch {
530 |     return false;
531 |   }
532 | };
533 | 
534 | export default api;
535 | 
536 | // Made with Bob
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files
server\main.py

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,README.md,server/.env,server/main.py,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:14:32.812Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$0.03

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

<read_file>
<args>
<file>
<path>server/routes/roadmap.py</path>
</file>
<file>
<path>server/services/watsonx_service.py</path>
</file>
<file>
<path>server/services/github_service.py</path>
</file>
<file>
<path>server/routes/usajobs.py</path>
</file>
<file>
<path>README.md</path>
</file>
</args>
</read_file>

---

**User:**

[read_file for 5 files] Result:
<files>
<file><path>server/routes/roadmap.py</path>
<content lines="1-628">
  1 | from fastapi import APIRouter, HTTPException
  2 | from pydantic import BaseModel, Field
  3 | from typing import List, Optional, Dict, Any
  4 | import json
  5 | import os
  6 | from services.watsonx_service import generate_roadmap_with_ai
  7 | from services.github_service import search_github_projects
  8 | from services.resource_validator import resource_validator
  9 | from services.project_validator import project_validator
 10 | from services.response_normalizer import normalize_roadmap_response, ensure_minimum_resources
 11 | from services.roadmap_enforcer import enforce_roadmap_requirements
 12 | import logging
 13 | 
 14 | logger = logging.getLogger(__name__)
 15 | 
 16 | router = APIRouter(prefix="/api", tags=["roadmap"])
 17 | 
 18 | 
 19 | class RoadmapRequest(BaseModel):
 20 |     """Request model for AI-powered roadmap generation"""
 21 |     careerGoal: str = Field(..., description="Target career role (e.g., 'SOC Analyst')")
 22 |     currentSkills: List[str] = Field(default=[], description="List of current skills")
 23 |     timeframe: str = Field(..., description="Available timeframe (e.g., '3 months', '6 months')")
 24 |     weeks: Optional[int] = Field(default=None, description="Explicit number of weeks if provided")
 25 | 
 26 | 
 27 | class RoadmapResponse(BaseModel):
 28 |     """Response model for generated roadmap"""
 29 |     success: bool
 30 |     careerGoal: str
 31 |     roadmap: Optional[Dict[str, Any]] = None
 32 |     metadata: Optional[Dict[str, Any]] = None
 33 |     error: Optional[str] = None
 34 | 
 35 | 
 36 | def load_json_file(filepath: str) -> Any:
 37 |     """Load and parse a JSON file"""
 38 |     try:
 39 |         full_path = os.path.join(os.path.dirname(__file__), "..", "data", filepath)
 40 |         with open(full_path, 'r', encoding='utf-8') as f:
 41 |             return json.load(f)
 42 |     except FileNotFoundError:
 43 |         logger.warning(f"File not found: {filepath}")
 44 |         return None
 45 |     except json.JSONDecodeError as e:
 46 |         logger.error(f"Error parsing JSON from {filepath}: {str(e)}")
 47 |         return None
 48 |     except Exception as e:
 49 |         logger.error(f"Error loading {filepath}: {str(e)}")
 50 |         return None
 51 | 
 52 | 
 53 | def match_role_data(career_goal: str) -> Optional[Dict[str, Any]]:
 54 |     """Match career goal to role data"""
 55 |     roles = load_json_file("roles.json")
 56 |     if not roles:
 57 |         return None
 58 |     
 59 |     career_goal_lower = career_goal.lower()
 60 |     
 61 |     # Try exact match first
 62 |     for role in roles:
 63 |         if role.get("title", "").lower() == career_goal_lower:
 64 |             return role
 65 |     
 66 |     # Try partial match
 67 |     for role in roles:
 68 |         title = role.get("title", "").lower()
 69 |         if career_goal_lower in title or title in career_goal_lower:
 70 |             return role
 71 |     
 72 |     # Try matching by keywords
 73 |     for role in roles:
 74 |         keywords = role.get("beginnerKeywords", [])
 75 |         for keyword in keywords:
 76 |             if keyword.lower() in career_goal_lower:
 77 |                 return role
 78 |     
 79 |     return None
 80 | 
 81 | 
 82 | def get_resources_for_skills(skills: List[str], career_goal: str = "") -> Dict[str, Any]:
 83 |     """
 84 |     Get learning resources for given skills with improved matching.
 85 |     
 86 |     Args:
 87 |         skills: List of skills to match
 88 |         career_goal: Career goal for additional context
 89 |     
 90 |     Returns:
 91 |         Dict with resources list
 92 |     """
 93 |     all_resources = load_json_file("resources.json")
 94 |     if not all_resources:
 95 |         return {"resources": []}
 96 |     
 97 |     matched_resources = []
 98 |     matched_skills = set()
 99 |     
100 |     # First pass: exact skill matches
101 |     for skill in skills:
102 |         skill_lower = skill.lower()
103 |         for resource_group in all_resources:
104 |             group_skill = resource_group.get("skill", "").lower()
105 |             if skill_lower in group_skill or group_skill in skill_lower:
106 |                 resources = resource_group.get("resources", [])
107 |                 matched_resources.extend(resources[:5])  # Top 5 per skill (increased from 3)
108 |                 matched_skills.add(group_skill)
109 |                 break
110 |     
111 |     # Second pass: if we don't have enough, try verified resources
112 |     if len(matched_resources) < 5:
113 |         logger.info(f"Only {len(matched_resources)} resources from skills, trying verified resources...")
114 |         verified = resource_validator.match_verified_resources(
115 |             career_goal=career_goal,
116 |             topics=skills,
117 |             max_resources=10
118 |         )
119 |         matched_resources.extend(verified)
120 |     
121 |     # Remove duplicates by URL
122 |     seen_urls = set()
123 |     unique_resources = []
124 |     for resource in matched_resources:
125 |         url = resource.get("url", "")
126 |         if url and url not in seen_urls:
127 |             seen_urls.add(url)
128 |             unique_resources.append(resource)
129 |     
130 |     # Ensure minimum count
131 |     unique_resources = ensure_minimum_resources(unique_resources, career_goal, min_count=5)
132 |     
133 |     logger.info(f"✅ Matched {len(unique_resources)} resources for skills: {skills}")
134 |     
135 |     return {"resources": unique_resources}
136 | 
137 | 
138 | def get_projects_for_skills(skills: List[str]) -> List[Dict[str, Any]]:
139 |     """Get project ideas for given skills"""
140 |     all_projects = load_json_file("projects.json")
141 |     if not all_projects:
142 |         return []
143 |     
144 |     matched_projects = []
145 |     
146 |     for skill in skills:
147 |         skill_lower = skill.lower()
148 |         for project_group in all_projects:
149 |             if skill_lower in project_group.get("skill", "").lower():
150 |                 projects = project_group.get("projects", [])
151 |                 matched_projects.extend(projects[:2])  # Top 2 per skill
152 |                 break
153 |     
154 |     return matched_projects
155 | 
156 | 
157 | def get_certifications_for_role(role_title: str) -> List[Dict[str, Any]]:
158 |     """Get certification recommendations for a role"""
159 |     all_certs = load_json_file("certifications.json")
160 |     if not all_certs:
161 |         return []
162 |     
163 |     role_lower = role_title.lower()
164 |     
165 |     for cert_group in all_certs:
166 |         if role_lower in cert_group.get("role", "").lower():
167 |             return cert_group.get("certifications", [])
168 |     
169 |     return []
170 | 
171 | 
172 | async def search_github_for_role(career_goal: str, role_data: Optional[Dict[str, Any]], skills: List[str] = []) -> List[Dict[str, Any]]:
173 |     """
174 |     Search GitHub for relevant beginner projects and merge with verified projects
175 |     
176 |     Args:
177 |         career_goal: Target career role
178 |         role_data: Optional role data with keywords
179 |         skills: List of skills for matching
180 |     
181 |     Returns:
182 |         List of project dictionaries with URLs and metadata
183 |     """
184 |     logger.info("=" * 80)
185 |     logger.info("🐙 GITHUB PROJECT SEARCH")
186 |     logger.info("=" * 80)
187 |     logger.info(f"Career Goal: {career_goal}")
188 |     logger.info(f"Skills: {skills}")
189 |     
190 |     try:
191 |         # Use role keywords if available
192 |         if role_data and role_data.get("beginnerKeywords"):
193 |             search_query = " ".join(role_data["beginnerKeywords"][:2])
194 |         else:
195 |             search_query = career_goal
196 |         
197 |         logger.info(f"Search Query: {search_query}")
198 |         
199 |         result = await search_github_projects(search_query)
200 |         
201 |         # Check if result is an error response
202 |         from models.schemas import ErrorResponse, GitHubProjectsResponse
203 |         
204 |         if isinstance(result, ErrorResponse):
205 |             logger.warning(f"❌ GitHub search failed: {result.error}")
206 |             logger.warning(f"   Will use verified local projects instead")
207 |             github_projects = []
208 |         elif isinstance(result, GitHubProjectsResponse):
209 |             github_projects = []
210 |             for repo in result.repositories[:5]:
211 |                 github_projects.append({
212 |                     "name": repo.name,
213 |                     "description": repo.description or "No description",
214 |                     "stars": repo.stars,
215 |                     "language": repo.language or "Unknown",
216 |                     "url": repo.url
217 |                 })
218 |             logger.info(f"✅ Found {len(github_projects)} GitHub projects")
219 |         else:
220 |             logger.warning(f"⚠️  Unexpected result type from GitHub API")
221 |             github_projects = []
222 |         
223 |         # Merge with verified projects to ensure minimum count
224 |         merged_projects = project_validator.merge_github_and_verified_projects(
225 |             github_projects=github_projects,
226 |             career_goal=career_goal,
227 |             skills=skills,
228 |             min_projects=3
229 |         )
230 |         
231 |         # Ensure all projects have URL field
232 |         final_projects = [project_validator.ensure_project_has_url(p) for p in merged_projects]
233 |         
234 |         logger.info(f"✅ Final project count: {len(final_projects)}")
235 |         for i, project in enumerate(final_projects, 1):
236 |             source = project.get('source', 'unknown')
237 |             has_url = project.get('hasUrl', False)
238 |             logger.info(f"   {i}. {project.get('name', 'Unknown')} (source: {source}, has_url: {has_url})")
239 |         
240 |         logger.info("=" * 80)
241 |         
242 |         return final_projects
243 |     
244 |     except Exception as e:
245 |         logger.error(f"Error searching GitHub: {str(e)}")
246 |         return []
247 | 
248 | 
249 | def _generate_weekly_plan(
250 |     weeks: int,
251 |     skills: List[str],
252 |     tools: List[str],
253 |     career_goal: str
254 | ) -> List[Dict[str, Any]]:
255 |     """Generate weekly plan based on total weeks"""
256 |     weekly_plan = []
257 |     
258 |     # Generate plans for each week
259 |     for week in range(1, min(weeks + 1, 13)):  # Cap at 12 weeks for fallback
260 |         if week == 1:
261 |             weekly_plan.append({
262 |                 "week": week,
263 |                 "focus": f"Environment Setup & {skills[0] if skills else 'Fundamentals'}",
264 |                 "topics": [f"Setting up {tools[0] if tools else 'development environment'}", "Basic concepts", "First exercises"],
265 |                 "dailyTasks": [
266 |                     f"Install and configure {tools[0] if tools else 'required tools'}",
267 |                     f"Learn basics of {skills[0] if skills else 'core concepts'}",
268 |                     "Complete beginner tutorials",
269 |                     "Join online communities",
270 |                     "Set up learning schedule"
271 |                 ]
272 |             })
273 |         elif week <= weeks // 3:
274 |             weekly_plan.append({
275 |                 "week": week,
276 |                 "focus": f"Core {skills[min(week-1, len(skills)-1)] if skills else 'Concepts'} & Practice",
277 |                 "topics": ["Core concepts", "Hands-on exercises", "Problem solving"],
278 |                 "dailyTasks": [
279 |                     "Deep dive into fundamentals",
280 |                     "Complete coding challenges",
281 |                     "Build mini-projects",
282 |                     "Review and debug code",
283 |                     "Document your learning"
284 |                 ]
285 |             })
286 |         elif week <= (weeks * 2) // 3:
287 |             weekly_plan.append({
288 |                 "week": week,
289 |                 "focus": f"Advanced Topics & Project Development",
290 |                 "topics": ["Advanced concepts", "Project planning", "Best practices"],
291 |                 "dailyTasks": [
292 |                     "Learn advanced techniques",
293 |                     "Work on portfolio project",
294 |                     "Apply best practices",
295 |                     "Seek feedback from community",
296 |                     "Refactor and optimize code"
297 |                 ]
298 |             })
299 |         else:
300 |             weekly_plan.append({
301 |                 "week": week,
302 |                 "focus": "Portfolio & Job Preparation",
303 |                 "topics": ["Resume writing", "Interview prep", "Job applications"],
304 |                 "dailyTasks": [
305 |                     "Complete portfolio projects",
306 |                     "Create professional resume",
307 |                     "Optimize LinkedIn profile",
308 |                     "Practice technical interviews",
309 |                     "Apply to positions"
310 |                 ]
311 |             })
312 |     
313 |     return weekly_plan
314 | 
315 | 
316 | def create_fallback_roadmap(
317 |     career_goal: str,
318 |     current_skills: List[str],
319 |     timeframe: str,
320 |     role_data: Optional[Dict[str, Any]],
321 |     local_resources: Dict[str, Any],
322 |     github_projects: List[Dict[str, Any]]
323 | ) -> Dict[str, Any]:
324 |     """Create a fallback roadmap if watsonx.ai fails - respects user's timeframe"""
325 |     
326 |     import re
327 |     
328 |     skills_to_learn = role_data.get("coreSkills", ["Problem Solving", "Communication"]) if role_data else []
329 |     tools = role_data.get("tools", []) if role_data else []
330 |     
331 |     # Parse timeframe to get number of weeks
332 |     timeframe_lower = timeframe.lower()
333 |     weeks = 12  # default
334 |     
335 |     if 'month' in timeframe_lower:
336 |         match = re.search(r'(\d+)', timeframe_lower)
337 |         if match:
338 |             months = int(match.group(1))
339 |             weeks = months * 4
340 |     elif 'week' in timeframe_lower:
341 |         match = re.search(r'(\d+)', timeframe_lower)
342 |         if match:
343 |             weeks = int(match.group(1))
344 |     
345 |     # Calculate phase durations based on total weeks
346 |     phase_weeks = weeks // 3
347 |     phase1_end = phase_weeks
348 |     phase2_end = phase_weeks * 2
349 |     
350 |     return {
351 |         "summary": f"A practical {timeframe} roadmap to become a {career_goal}. This plan focuses on building essential skills through hands-on projects and real-world practice.",
352 |         "phases": [
353 |             {
354 |                 "phase": 1,
355 |                 "title": "Foundation & Setup",
356 |                 "duration": f"Weeks 1-{phase1_end}",
357 |                 "focus": "Learn the basics and set up your learning environment",
358 |                 "skills": skills_to_learn[:2] if len(skills_to_learn) >= 2 else skills_to_learn
359 |             },
360 |             {
361 |                 "phase": 2,
362 |                 "title": "Core Skills Development",
363 |                 "duration": f"Weeks {phase1_end + 1}-{phase2_end}",
364 |                 "focus": "Build practical skills through projects",
365 |                 "skills": skills_to_learn[2:4] if len(skills_to_learn) >= 4 else skills_to_learn
366 |             },
367 |             {
368 |                 "phase": 3,
369 |                 "title": "Portfolio & Job Prep",
370 |                 "duration": f"Weeks {phase2_end + 1}-{weeks}",
371 |                 "focus": "Create portfolio projects and prepare for job applications",
372 |                 "skills": ["Portfolio Development", "Resume Writing", "Interview Prep"]
373 |             }
374 |         ],
375 |         "skills": skills_to_learn,
376 |         "tools": tools,
377 |         "resources": local_resources.get("resources", [])[:10],
378 |         "githubProjects": github_projects,
379 |         "portfolioProjects": [
380 |             {
381 |                 "title": f"Beginner {career_goal} Project",
382 |                 "description": "Build a practical project demonstrating your skills",
383 |                 "skills": skills_to_learn[:3]
384 |             },
385 |             {
386 |                 "title": f"Intermediate {career_goal} Project",
387 |                 "description": "Create a more complex project for your portfolio",
388 |                 "skills": skills_to_learn
389 |             }
390 |         ],
391 |         "resumeBullets": [
392 |             f"Developed hands-on skills in {', '.join(skills_to_learn[:3])}",
393 |             f"Completed {timeframe} intensive training program in {career_goal}",
394 |             f"Built portfolio projects demonstrating practical application of {skills_to_learn[0] if skills_to_learn else 'core skills'}",
395 |             f"Gained experience with industry tools including {', '.join(tools[:3])}",
396 |             "Actively learning and applying best practices in the field"
397 |         ],
398 |         "weeklyPlan": _generate_weekly_plan(weeks, skills_to_learn, tools, career_goal),
399 |         "nextSteps": [
400 |             f"Start with the first recommended resource for {skills_to_learn[0] if skills_to_learn else 'your chosen skill'}",
401 |             "Set up your development environment and tools",
402 |             "Join relevant online communities and forums",
403 |             "Create a GitHub account and start documenting your learning",
404 |             "Dedicate consistent time each day to learning and practice",
405 |             "Build your first small project within the first 2 weeks",
406 |             "Connect with others in the field on LinkedIn"
407 |         ]
408 |     }
409 | 
410 | 
411 | @router.post("/generate-roadmap", response_model=RoadmapResponse)
412 | async def generate_roadmap(request: RoadmapRequest):
413 |     """
414 |     Generate an AI-powered career roadmap using IBM watsonx.ai.
415 |     
416 |     This endpoint:
417 |     1. Loads curated resources from local JSON files
418 |     2. Matches resources related to the career goal
419 |     3. Searches GitHub for relevant beginner-friendly projects
420 |     4. Builds a structured prompt for IBM watsonx.ai
421 |     5. Calls watsonx.ai to generate a personalized roadmap
422 |     6. Returns a structured AI-generated roadmap
423 |     
424 |     Security: All API keys are stored in environment variables and never exposed to the frontend.
425 |     """
426 |     try:
427 |         # Validate input
428 |         if not request.careerGoal or not request.careerGoal.strip():
429 |             raise HTTPException(status_code=400, detail="Career goal is required")
430 |         
431 |         if not request.timeframe or not request.timeframe.strip():
432 |             raise HTTPException(status_code=400, detail="Timeframe is required")
433 |         
434 |         logger.info(f"Generating roadmap for: {request.careerGoal}")
435 |         
436 |         # Step 1: Match role data
437 |         role_data = match_role_data(request.careerGoal)
438 |         
439 |         # Step 2: Get skills to learn
440 |         if role_data:
441 |             skills_to_learn = role_data.get("coreSkills", [])
442 |         else:
443 |             # Use current skills as a base if no role match
444 |             skills_to_learn = request.currentSkills if request.currentSkills else ["Problem Solving"]
445 |         
446 |         # Step 3: Load local resources (pass career_goal for better matching)
447 |         local_resources = get_resources_for_skills(
448 |             skills=skills_to_learn,
449 |             career_goal=request.careerGoal
450 |         )
451 |         
452 |         # Step 4: Search GitHub for projects (non-blocking, can fail gracefully)
453 |         github_projects = await search_github_for_role(request.careerGoal, role_data, skills_to_learn)
454 |         
455 |         # Step 5: Get certifications
456 |         certifications = get_certifications_for_role(request.careerGoal)
457 |         
458 |         # Step 6: Call watsonx.ai to generate roadmap
459 |         logger.info("=" * 80)
460 |         logger.info("🤖 ATTEMPTING WATSONX.AI ROADMAP GENERATION")
461 |         logger.info("=" * 80)
462 |         logger.info(f"Career Goal: {request.careerGoal}")
463 |         logger.info(f"Timeframe: {request.timeframe}")
464 |         logger.info(f"Current Skills: {request.currentSkills}")
465 |         
466 |         ai_roadmap = await generate_roadmap_with_ai(
467 |             career_goal=request.careerGoal,
468 |             current_skills=request.currentSkills,
469 |             timeframe=request.timeframe,
470 |             local_resources=local_resources,
471 |             github_projects=github_projects
472 |         )
473 |         
474 |         # Step 7: Handle AI response or create fallback
475 |         if ai_roadmap:
476 |             logger.info("=" * 80)
477 |             logger.info("✅ SUCCESS: WATSONX.AI GENERATED ROADMAP")
478 |             logger.info("=" * 80)
479 |             logger.info(f"Model: {ai_roadmap.get('metadata', {}).get('model', 'unknown')}")
480 |             logger.info(f"Tokens: {ai_roadmap.get('metadata', {}).get('tokens', 0)}")
481 |             logger.info(f"Phases: {len(ai_roadmap.get('phases', []))}")
482 |             logger.info(f"Weekly Plans: {len(ai_roadmap.get('weeklyPlan', []))}")
483 |             logger.info("=" * 80)
484 |             roadmap = ai_roadmap
485 |             
486 |             # Step 7a: Validate and replace resources
487 |             logger.info("🔗 Validating resource URLs...")
488 |             resources = roadmap.get("resources", [])
489 |             if resources:
490 |                 topics = roadmap.get("skills", []) + roadmap.get("tools", [])
491 |                 validated_resources = await resource_validator.validate_and_replace_resources(
492 |                     resources=resources,
493 |                     career_goal=request.careerGoal,
494 |                     topics=topics
495 |                 )
496 |                 roadmap["resources"] = validated_resources
497 |                 
498 |                 # Count validation results
499 |                 verified_count = sum(1 for r in validated_resources if r.get("urlVerified", False))
500 |                 replaced_count = sum(1 for r in validated_resources if r.get("source") == "local_verified_replacement")
501 |                 
502 |                 logger.info(f"✅ Resource validation complete:")
503 |                 logger.info(f"   Total resources: {len(validated_resources)}")
504 |                 logger.info(f"   Verified URLs: {verified_count}")
505 |                 logger.info(f"   Replaced URLs: {replaced_count}")
506 |                 
507 |                 # Add validation metadata
508 |                 if "metadata" not in roadmap:
509 |                     roadmap["metadata"] = {}
510 |                 roadmap["metadata"]["resourceValidationEnabled"] = True
511 |                 roadmap["metadata"]["validatedResources"] = verified_count
512 |                 roadmap["metadata"]["replacedResources"] = replaced_count
513 |             else:
514 |                 logger.warning("⚠️  No resources to validate")
515 |         else:
516 |             logger.warning("=" * 80)
517 |             logger.warning("⚠️  FALLBACK: WATSONX.AI FAILED - USING TEMPLATE DATA")
518 |             logger.warning("=" * 80)
519 |             logger.warning("This means the roadmap will be generic and not AI-personalized")
520 |             logger.warning("Possible reasons:")
521 |             logger.warning("  1. WatsonX authentication failed (check API key)")
522 |             logger.warning("  2. WatsonX API call failed (check network/service status)")
523 |             logger.warning("  3. WatsonX returned invalid/incomplete JSON (check parsing errors above)")
524 |             logger.warning("  4. WatsonX response was truncated (hit max_new_tokens limit)")
525 |             logger.warning("")
526 |             logger.warning("Check the detailed logs above to identify the specific issue")
527 |             logger.warning("If you see 'RESPONSE APPEARS TRUNCATED', increase max_new_tokens")
528 |             logger.warning("=" * 80)
529 |             
530 |             roadmap = create_fallback_roadmap(
531 |                 career_goal=request.careerGoal,
532 |                 current_skills=request.currentSkills,
533 |                 timeframe=request.timeframe,
534 |                 role_data=role_data,
535 |                 local_resources=local_resources,
536 |                 github_projects=github_projects
537 |             )
538 |             roadmap["metadata"] = {
539 |                 "usedWatsonx": False,
540 |                 "usedGitHub": len(github_projects) > 0,
541 |                 "matchedLocalResources": len(local_resources.get("resources", [])),
542 |                 "fallbackReason": "watsonx.ai failed - check logs for details"
543 |             }
544 |         
545 |         # Step 8: Add certifications to roadmap
546 |         if certifications and "certifications" not in roadmap:
547 |             roadmap["certifications"] = certifications
548 |         
549 |         # Step 8.5: ENFORCE BACKEND REQUIREMENTS (timeframe, resources, GitHub validation)
550 |         logger.info("=" * 80)
551 |         logger.info("🔒 APPLYING BACKEND ENFORCEMENT")
552 |         logger.info("=" * 80)
553 |         roadmap = enforce_roadmap_requirements(
554 |             roadmap=roadmap,
555 |             career_goal=request.careerGoal,
556 |             requested_timeframe=request.timeframe,
557 |             form_weeks=request.weeks,
558 |             github_projects=github_projects
559 |         )
560 |         
561 |         # Step 9: Normalize response before returning
562 |         normalized_roadmap = normalize_roadmap_response(
563 |             roadmap=roadmap,
564 |             career_goal=request.careerGoal,
565 |             requested_timeframe=request.timeframe,
566 |             github_projects=roadmap.get("githubProjects", []),  # Use enforced GitHub projects
567 |             metadata=roadmap.get("metadata")
568 |         )
569 |         
570 |         # FINAL DEBUG LOGGING
571 |         logger.info("=" * 80)
572 |         logger.info("📤 FINAL RESPONSE TO FRONTEND")
573 |         logger.info("=" * 80)
574 |         logger.info(f"✅ Roadmap generation complete for {request.careerGoal}")
575 |         logger.info(f"   Career Goal: {request.careerGoal}")
576 |         logger.info(f"   Matched Career Path: {role_data.get('title') if role_data else 'None'}")
577 |         logger.info(f"   Resources: {len(normalized_roadmap.get('resources', []))}")
578 |         logger.info(f"   GitHub Projects: {len(normalized_roadmap.get('githubProjects', []))}")
579 |         logger.info(f"   Portfolio Projects: {len(normalized_roadmap.get('portfolioProjects', []))}")
580 |         logger.info(f"   Weekly Plans: {len(normalized_roadmap.get('weeklyPlan', []))}")
581 |         
582 |         # Log GitHub project details
583 |         github_projects_list = normalized_roadmap.get('githubProjects', [])
584 |         logger.info(f"\n🐙 GitHub Projects Details ({len(github_projects_list)} total):")
585 |         for i, proj in enumerate(github_projects_list, 1):
586 |             logger.info(f"   {i}. {proj.get('name', 'Unknown')}")
587 |             logger.info(f"      URL: {proj.get('url', 'No URL')}")
588 |             logger.info(f"      Stars: {proj.get('stars', 0)}")
589 |             logger.info(f"      Language: {proj.get('language', 'Unknown')}")
590 |         
591 |         # Log metadata
592 |         metadata_obj = normalized_roadmap.get("metadata", {})
593 |         logger.info(f"\n📊 Metadata:")
594 |         logger.info(f"   GitHub Raw Count: {len(github_projects)}")
595 |         logger.info(f"   GitHub Filtered Count: {len(github_projects)}")
596 |         logger.info(f"   GitHub Shown Count: {len(github_projects_list)}")
597 |         logger.info(f"   Matched Resource Count: {len(normalized_roadmap.get('resources', []))}")
598 |         logger.info(f"   Requested Timeframe: {request.timeframe}")
599 |         logger.info(f"   Total Weeks: {len(normalized_roadmap.get('weeklyPlan', []))}")
600 |         logger.info("=" * 80)
601 |         
602 |         # Add counts to metadata
603 |         metadata_obj.update({
604 |             "githubRawCount": len(github_projects),
605 |             "githubFilteredCount": len(github_projects),
606 |             "githubShownCount": len(github_projects_list),
607 |             "matchedResourceCount": len(normalized_roadmap.get('resources', [])),
608 |             "totalWeeks": len(normalized_roadmap.get('weeklyPlan', []))
609 |         })
610 |         
611 |         return RoadmapResponse(
612 |             success=True,
613 |             careerGoal=request.careerGoal,
614 |             roadmap=normalized_roadmap,
615 |             metadata=metadata_obj
616 |         )
617 |     
618 |     except HTTPException:
619 |         raise
620 |     
621 |     except Exception as e:
622 |         logger.error(f"Error generating roadmap: {str(e)}", exc_info=True)
623 |         raise HTTPException(
624 |             status_code=500,
625 |             detail=f"Failed to generate roadmap. Please try again later."
626 |         )
627 | 
628 | # Made with Bob
</content>
</file>
<file><path>server/services/watsonx_service.py</path>
<content lines="1-738">
  1 | import os
  2 | import httpx
  3 | import json
  4 | from typing import Optional, Dict, Any
  5 | import logging
  6 | from dotenv import load_dotenv
  7 | from pathlib import Path
  8 | 
  9 | # Load environment variables before anything else
 10 | env_path = Path(__file__).parent.parent / '.env'
 11 | load_dotenv(dotenv_path=env_path)
 12 | 
 13 | logger = logging.getLogger(__name__)
 14 | 
 15 | 
 16 | class WatsonxService:
 17 |     """
 18 |     Service for interacting with IBM watsonx.ai API.
 19 |     Handles authentication and text generation requests.
 20 |     """
 21 |     
 22 |     def __init__(self):
 23 |         # Load environment variables with detailed logging
 24 |         self.api_key = os.getenv("WATSONX_API_KEY")
 25 |         self.project_id = os.getenv("WATSONX_PROJECT_ID")
 26 |         self.url = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
 27 |         self.model_id = os.getenv("WATSONX_MODEL_ID", "ibm/granite-3-8b-instruct")
 28 |         self.iam_token = None
 29 |         self.token_expiry = 0
 30 |         
 31 |         # Log environment variable status (safely)
 32 |         logger.info("=" * 80)
 33 |         logger.info("🔧 WATSONX SERVICE INITIALIZATION")
 34 |         logger.info("=" * 80)
 35 |         logger.info(f"Loading .env from: {env_path}")
 36 |         logger.info(f".env exists: {env_path.exists()}")
 37 |         
 38 |         if self.api_key:
 39 |             masked_key = self.api_key[:8] + "..." + self.api_key[-4:] if len(self.api_key) > 12 else "***"
 40 |             logger.info(f"✅ WATSONX_API_KEY: {masked_key}")
 41 |         else:
 42 |             logger.error("❌ WATSONX_API_KEY: NOT FOUND")
 43 |             
 44 |         if self.project_id:
 45 |             logger.info(f"✅ WATSONX_PROJECT_ID: {self.project_id}")
 46 |         else:
 47 |             logger.error("❌ WATSONX_PROJECT_ID: NOT FOUND")
 48 |             
 49 |         logger.info(f"✅ WATSONX_URL: {self.url}")
 50 |         logger.info(f"✅ WATSONX_MODEL_ID: {self.model_id}")
 51 |         logger.info("=" * 80)
 52 |     
 53 |     async def get_iam_token(self) -> Optional[str]:
 54 |         """
 55 |         Get IBM Cloud IAM access token using API key.
 56 |         Tokens are cached and reused until they expire.
 57 |         """
 58 |         import time
 59 |         
 60 |         # Return cached token if still valid (with 5 min buffer)
 61 |         if self.iam_token and time.time() < (self.token_expiry - 300):
 62 |             logger.info("♻️  Using cached IAM token")
 63 |             return self.iam_token
 64 |         
 65 |         if not self.api_key:
 66 |             logger.error("❌ Cannot get IAM token: WATSONX_API_KEY not set")
 67 |             return None
 68 |         
 69 |         logger.info("🔑 Requesting new IAM token from IBM Cloud...")
 70 |         
 71 |         try:
 72 |             url = "https://iam.cloud.ibm.com/identity/token"
 73 |             headers = {
 74 |                 "Content-Type": "application/x-www-form-urlencoded",
 75 |                 "Accept": "application/json"
 76 |             }
 77 |             data = {
 78 |                 "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
 79 |                 "apikey": self.api_key
 80 |             }
 81 |             
 82 |             logger.info(f"IAM Token URL: {url}")
 83 |             logger.info(f"Request headers: {headers}")
 84 |             logger.info(f"Grant type: {data['grant_type']}")
 85 |             
 86 |             async with httpx.AsyncClient() as client:
 87 |                 response = await client.post(url, headers=headers, data=data, timeout=30.0)
 88 |                 
 89 |                 logger.info(f"IAM Response Status: {response.status_code}")
 90 |                 
 91 |                 if response.status_code != 200:
 92 |                     logger.error(f"❌ Failed to get IAM token: HTTP {response.status_code}")
 93 |                     logger.error(f"Response body: {response.text[:500]}")
 94 |                     
 95 |                     # Try to parse error details
 96 |                     try:
 97 |                         error_data = response.json()
 98 |                         logger.error(f"Error details: {error_data}")
 99 |                     except:
100 |                         pass
101 |                     
102 |                     return None
103 |                 
104 |                 token_data = response.json()
105 |                 self.iam_token = token_data.get("access_token")
106 |                 expires_in = token_data.get("expires_in", 3600)
107 |                 self.token_expiry = time.time() + expires_in
108 |                 
109 |                 if self.iam_token:
110 |                     masked_token = self.iam_token[:20] + "..." + self.iam_token[-10:] if len(self.iam_token) > 30 else "***"
111 |                     logger.info(f"✅ IAM token obtained successfully: {masked_token}")
112 |                     logger.info(f"Token expires in: {expires_in} seconds")
113 |                 else:
114 |                     logger.error("❌ No access_token in response")
115 |                     logger.error(f"Response keys: {list(token_data.keys())}")
116 |                 
117 |                 return self.iam_token
118 |         
119 |         except httpx.TimeoutException:
120 |             logger.error("❌ IAM token request timed out")
121 |             return None
122 |         
123 |         except Exception as e:
124 |             logger.error(f"❌ Error getting IAM token: {str(e)}")
125 |             logger.exception("Full exception details:")
126 |             return None
127 |     
128 |     async def generate_text(
129 |         self,
130 |         prompt: str,
131 |         model_id: str = "ibm/granite-3-8b-instruct",
132 |         max_tokens: int = 2000,
133 |         temperature: float = 0.7,
134 |         top_p: float = 1.0,
135 |         top_k: int = 50,
136 |         max_retries: int = 2
137 |     ) -> Optional[Dict[str, Any]]:
138 |         """
139 |         Generate text using IBM watsonx.ai with retry logic.
140 |         
141 |         Args:
142 |             prompt: The input prompt for text generation
143 |             model_id: Model to use (default: IBM Granite 13B Chat)
144 |             max_tokens: Maximum tokens to generate
145 |             temperature: Sampling temperature (0.0-2.0)
146 |             top_p: Nucleus sampling parameter
147 |             top_k: Top-k sampling parameter
148 |             max_retries: Maximum number of retry attempts (default: 2)
149 |         
150 |         Returns:
151 |             Dictionary with generated text and metadata, or None on error
152 |         """
153 |         if not self.project_id:
154 |             logger.error("❌ Cannot generate text: WATSONX_PROJECT_ID not set")
155 |             return None
156 |         
157 |         # Get IAM token
158 |         logger.info("🔐 Getting IAM token for WatsonX...")
159 |         token = await self.get_iam_token()
160 |         if not token:
161 |             logger.error("❌ Failed to get IAM token for watsonx.ai")
162 |             return None
163 |         
164 |         logger.info("✅ IAM token obtained, calling WatsonX API...")
165 |         
166 |         # Retry loop
167 |         last_error = None
168 |         for attempt in range(max_retries + 1):
169 |             if attempt > 0:
170 |                 import asyncio
171 |                 wait_time = 2 ** attempt  # Exponential backoff: 2s, 4s, 8s
172 |                 logger.warning(f"⏳ Retry attempt {attempt}/{max_retries} after {wait_time}s...")
173 |                 await asyncio.sleep(wait_time)
174 |         
175 |             try:
176 |                 # Construct API endpoint
177 |                 endpoint = f"{self.url}/ml/v1/text/generation?version=2023-05-29"
178 |                 
179 |                 # Request headers
180 |                 headers = {
181 |                     "Accept": "application/json",
182 |                     "Content-Type": "application/json",
183 |                     "Authorization": f"Bearer {token}"
184 |                 }
185 |                 
186 |                 # Request body
187 |                 body = {
188 |                     "input": prompt,
189 |                     "parameters": {
190 |                         "decoding_method": "greedy",
191 |                         "max_new_tokens": max_tokens,
192 |                         "temperature": temperature,
193 |                         "top_p": top_p,
194 |                         "top_k": top_k,
195 |                         "repetition_penalty": 1.1,
196 |                         "stop_sequences": []  # Prevent premature stopping
197 |                     },
198 |                     "model_id": model_id,
199 |                     "project_id": self.project_id
200 |                 }
201 |                 
202 |                 # Log full request details (only on first attempt)
203 |                 if attempt == 0:
204 |                     logger.info("=" * 80)
205 |                     logger.info("📤 WATSONX API REQUEST")
206 |                     logger.info("=" * 80)
207 |                     logger.info(f"Endpoint: {endpoint}")
208 |                     logger.info(f"Model: {model_id}")
209 |                     logger.info(f"Project ID: {self.project_id}")
210 |                     logger.info(f"Prompt length: {len(prompt)} characters")
211 |                     logger.info("")
212 |                     logger.info("Request Parameters:")
213 |                     logger.info(f"  decoding_method: {body['parameters']['decoding_method']}")
214 |                     logger.info(f"  max_new_tokens: {body['parameters']['max_new_tokens']}")
215 |                     logger.info(f"  temperature: {body['parameters']['temperature']}")
216 |                     logger.info(f"  top_p: {body['parameters']['top_p']}")
217 |                     logger.info(f"  top_k: {body['parameters']['top_k']}")
218 |                     logger.info(f"  repetition_penalty: {body['parameters']['repetition_penalty']}")
219 |                     logger.info("=" * 80)
220 |                 
221 |                 # Make request
222 |                 async with httpx.AsyncClient() as client:
223 |                     response = await client.post(
224 |                         endpoint,
225 |                         headers=headers,
226 |                         json=body,
227 |                         timeout=60.0
228 |                     )
229 |                     
230 |                     logger.info(f"WatsonX Response Status: {response.status_code}")
231 |                     
232 |                     if response.status_code != 200:
233 |                         error_msg = f"HTTP {response.status_code}"
234 |                         logger.error(f"❌ watsonx.ai API error: {error_msg}")
235 |                         logger.error(f"Response body: {response.text[:1000]}")
236 |                         
237 |                         # Try to parse error details
238 |                         try:
239 |                             error_data = response.json()
240 |                             logger.error(f"Error details: {error_data}")
241 |                         except:
242 |                             pass
243 |                         
244 |                         # Retry on 5xx errors (server errors)
245 |                         if 500 <= response.status_code < 600 and attempt < max_retries:
246 |                             last_error = error_msg
247 |                             continue
248 |                         
249 |                         return None
250 |                     
251 |                     result = response.json()
252 |                     
253 |                     # Log full response structure
254 |                     logger.info("=" * 80)
255 |                     logger.info("📥 WATSONX API RESPONSE")
256 |                     logger.info("=" * 80)
257 |                     
258 |                     # Extract generated text
259 |                     results_array = result.get("results", [])
260 |                     if not results_array:
261 |                         logger.error("❌ No results array in response")
262 |                         logger.error(f"Response keys: {list(result.keys())}")
263 |                         return None
264 |                     
265 |                     first_result = results_array[0]
266 |                     generated_text = first_result.get("generated_text", "")
267 |                     token_count = first_result.get("generated_token_count", 0)
268 |                     stop_reason = first_result.get("stop_reason", "unknown")
269 |                     
270 |                     # Log response metadata
271 |                     logger.info(f"Generated token count: {token_count}")
272 |                     logger.info(f"Stop reason: {stop_reason}")
273 |                     logger.info(f"Generated text length: {len(generated_text)} characters")
274 |                     logger.info(f"Generated text first 200 chars: {generated_text[:200]}")
275 |                     logger.info(f"Generated text last 200 chars: {generated_text[-200:]}")
276 |                     logger.info(f"Text ends with: '{generated_text[-50:]}'")
277 |                     logger.info(f"Ends with closing brace: {generated_text.rstrip().endswith('}')}")
278 |                     logger.info("=" * 80)
279 |                     
280 |                     logger.info(f"✅ WatsonX generation successful!")
281 |                     
282 |                     return {
283 |                         "generated_text": generated_text,
284 |                         "model_id": model_id,
285 |                         "token_count": token_count,
286 |                         "stop_reason": stop_reason,
287 |                         "attempts": attempt + 1
288 |                     }
289 |             
290 |             except httpx.TimeoutException as e:
291 |                 error_msg = "Request timed out (60s)"
292 |                 logger.error(f"❌ watsonx.ai {error_msg}")
293 |                 last_error = error_msg
294 |                 # Retry on timeout
295 |                 if attempt < max_retries:
296 |                     continue
297 |                 return None
298 |             
299 |             except httpx.HTTPError as e:
300 |                 error_msg = f"HTTP Error: {str(e)}"
301 |                 logger.error(f"❌ watsonx.ai {error_msg}")
302 |                 last_error = error_msg
303 |                 # Retry on network errors
304 |                 if attempt < max_retries:
305 |                     continue
306 |                 return None
307 |             
308 |             except Exception as e:
309 |                 logger.error(f"❌ Error calling watsonx.ai: {str(e)}")
310 |                 logger.exception("Full exception details:")
311 |                 last_error = str(e)
312 |                 # Don't retry on unexpected errors
313 |                 return None
314 |         
315 |         # All retries exhausted
316 |         logger.error(f"❌ All {max_retries + 1} attempts failed. Last error: {last_error}")
317 |         return None
318 |     
319 |     async def generate_career_roadmap(
320 |         self,
321 |         career_goal: str,
322 |         current_skills: list,
323 |         timeframe: str,
324 |         local_resources: dict,
325 |         github_projects: list
326 |     ) -> Optional[Dict[str, Any]]:
327 |         """
328 |         Generate a structured career roadmap using watsonx.ai.
329 |         
330 |         Args:
331 |             career_goal: Target career role
332 |             current_skills: List of current skills
333 |             timeframe: Available timeframe (e.g., "3 months")
334 |             local_resources: Curated resources from local data
335 |             github_projects: Relevant GitHub projects
336 |         
337 |         Returns:
338 |             Structured roadmap dictionary or None on error
339 |         """
340 |         # Build context from local resources
341 |         resources_context = ""
342 |         if local_resources.get("resources"):
343 |             resources_context = "\n".join([
344 |                 f"- {r['title']} ({r['type']}): {r['url']}"
345 |                 for r in local_resources["resources"][:5]
346 |             ])
347 |         
348 |         # Build context from GitHub projects
349 |         github_context = ""
350 |         if github_projects:
351 |             github_context = "\n".join([
352 |                 f"- {p['name']}: {p['description']} ({p['stars']} stars)"
353 |                 for p in github_projects[:5]
354 |             ])
355 |         
356 |         # Build skills context
357 |         skills_text = ", ".join(current_skills) if current_skills else "none"
358 |         
359 |         # Construct prompt with strict JSON requirements and MINIMAL structure
360 |         prompt = f"""Generate a career roadmap JSON for: {career_goal}
361 | 
362 | Current skills: {skills_text}
363 | Timeframe: {timeframe}
364 | 
365 | CRITICAL: The roadmap MUST be achievable within EXACTLY {timeframe}. Do NOT change or extend this timeframe.
366 | 
367 | Available verified resources:
368 | {resources_context if resources_context else "Use well-known learning platforms"}
369 | 
370 | {f'''Relevant GitHub projects to include:
371 | {github_context}''' if github_context else ''}
372 | 
373 | Return ONLY valid JSON with NO markdown, NO code fences, NO explanations.
374 | 
375 | Required structure:
376 | {{
377 |   "summary": "Brief 1-sentence overview",
378 |   "phases": [
379 |     {{"phase": 1, "title": "Foundation", "duration": "4 weeks", "focus": "Learn basics", "skills": ["skill1", "skill2"]}},
380 |     {{"phase": 2, "title": "Practice", "duration": "4 weeks", "focus": "Build projects", "skills": ["skill3", "skill4"]}},
381 |     {{"phase": 3, "title": "Portfolio", "duration": "4 weeks", "focus": "Create portfolio", "skills": ["skill5", "skill6"]}}
382 |   ],
383 |   "skills": ["skill1", "skill2", "skill3", "skill4", "skill5"],
384 |   "tools": ["tool1", "tool2", "tool3", "tool4"],
385 |   "resources": [
386 |     {{"title": "Excel Fundamentals Course", "type": "course", "url": "https://www.coursera.org/learn/excel-basics", "provider": "Coursera"}},
387 |     {{"title": "SQL Tutorial for Beginners", "type": "tutorial", "url": "https://www.w3schools.com/sql/", "provider": "W3Schools"}}
388 |   ],
389 |   "githubProjects": [
390 |     {{"name": "Project 1", "description": "Beginner project", "difficulty": "beginner"}},
391 |     {{"name": "Project 2", "description": "Intermediate project", "difficulty": "intermediate"}}
392 |   ],
393 |   "portfolioProjects": [
394 |     {{"title": "Portfolio Project 1", "description": "Build something", "skills": ["skill1", "skill2"], "estimatedHours": 8, "difficulty": "beginner"}},
395 |     {{"title": "Portfolio Project 2", "description": "Build advanced", "skills": ["skill3", "skill4"], "estimatedHours": 16, "difficulty": "intermediate"}}
396 |   ],
397 |   "resumeBullets": [
398 |     "Completed {{timeframe}} training in {{career_goal}}",
399 |     "Built 2 portfolio projects demonstrating key skills",
400 |     "Gained hands-on experience with industry tools"
401 |   ],
402 |   "weeklyPlan": [
403 |     {{"week": 1, "focus": "Environment setup", "topics": ["Install tools", "Learn basics"], "dailyTasks": ["Setup workspace", "First tutorial"]}},
404 |     {{"week": 2, "focus": "Core concepts", "topics": ["Study fundamentals", "Practice"], "dailyTasks": ["Read docs", "Do exercises"]}},
405 |     {{"week": 3, "focus": "First project", "topics": ["Plan project", "Start coding"], "dailyTasks": ["Design", "Implement"]}},
406 |     {{"week": 4, "focus": "Complete project", "topics": ["Finish coding", "Test"], "dailyTasks": ["Debug", "Deploy"]}}
407 |   ],
408 |   "nextSteps": [
409 |     "Start with first resource",
410 |     "Set up development environment",
411 |     "Join online community",
412 |     "Begin first project"
413 |   ]
414 | }}
415 | 
416 | IMPORTANT for resources:
417 | - Use DESCRIPTIVE titles (not "Resource 1")
418 | - Only use URLs from well-known platforms: Coursera, edX, Udemy, W3Schools, MDN, freeCodeCamp, Khan Academy, YouTube
419 | - Include provider name if possible
420 | - Use homepage URLs if specific course URLs are uncertain
421 | 
422 | IMPORTANT:
423 | - The timeframe is {timeframe} - do NOT change this in your response
424 | - Include GitHub projects in the githubProjects array if provided above
425 | - Use DESCRIPTIVE titles for resources (not "Resource 1")
426 | - Only use URLs from well-known platforms: Coursera, edX, Udemy, W3Schools, MDN, freeCodeCamp, Khan Academy, YouTube
427 | - Include provider name for each resource
428 | - Make the weekly plan fit EXACTLY within {timeframe}
429 | 
430 | CRITICAL: Return ONLY the JSON object. Start with {{ and end with }}. NO markdown. NO explanations. Complete the ENTIRE JSON."""
431 |         
432 |         # Generate with watsonx.ai - increased token limit to prevent truncation
433 |         # 6000 tokens allows for complete roadmaps with all fields
434 |         result = await self.generate_text(
435 |             prompt=prompt,
436 |             max_tokens=6000,
437 |             temperature=0.7
438 |         )
439 |         
440 |         if not result:
441 |             logger.error("❌ WatsonX returned None result")
442 |             return None
443 |         
444 |         # Initialize cleaned_text for error handling
445 |         cleaned_text = ""
446 |         
447 |         try:
448 |             # Get raw generated text
449 |             generated_text = result["generated_text"]
450 |             
451 |             # Log raw response for debugging
452 |             logger.info("=" * 80)
453 |             logger.info("📄 RAW GENERATED TEXT FROM WATSONX")
454 |             logger.info("=" * 80)
455 |             logger.info(f"Total length: {len(generated_text)} characters")
456 |             logger.info(f"Token count: {result.get('token_count', 'unknown')}")
457 |             logger.info(f"Stop reason: {result.get('stop_reason', 'unknown')}")
458 |             logger.info("")
459 |             logger.info(f"First 500 characters:")
460 |             logger.info(generated_text[:500])
461 |             logger.info("")
462 |             logger.info(f"Last 500 characters:")
463 |             logger.info(generated_text[-500:])
464 |             logger.info("")
465 |             logger.info(f"Ends with closing brace: {generated_text.rstrip().endswith('}')}")
466 |             logger.info("=" * 80)
467 |             
468 |             # Clean and extract JSON
469 |             cleaned_text = generated_text.strip()
470 |             logger.info("🧹 Starting JSON extraction...")
471 |             logger.info(f"Initial cleaned length: {len(cleaned_text)} characters")
472 |             
473 |             # Remove markdown code fences if present
474 |             if "```json" in cleaned_text:
475 |                 logger.info("🔧 Found ```json markdown wrapper, removing...")
476 |                 parts = cleaned_text.split("```json")
477 |                 if len(parts) > 1:
478 |                     cleaned_text = parts[1].split("```")[0].strip()
479 |                     logger.info(f"   After removing markdown: {len(cleaned_text)} characters")
480 |             elif "```" in cleaned_text:
481 |                 logger.info("🔧 Found ``` markdown wrapper, removing...")
482 |                 parts = cleaned_text.split("```")
483 |                 if len(parts) >= 3:
484 |                     cleaned_text = parts[1].strip()
485 |                     logger.info(f"   After removing markdown: {len(cleaned_text)} characters")
486 |             
487 |             # Remove any text before first { and after last }
488 |             first_brace = cleaned_text.find("{")
489 |             last_brace = cleaned_text.rfind("}")
490 |             
491 |             logger.info(f"🔍 Looking for JSON braces...")
492 |             logger.info(f"   First {{ found at position: {first_brace}")
493 |             logger.info(f"   Last }} found at position: {last_brace}")
494 |             
495 |             if first_brace == -1 or last_brace == -1:
496 |                 logger.error("=" * 80)
497 |                 logger.error("❌ NO JSON OBJECT FOUND IN RESPONSE")
498 |                 logger.error("=" * 80)
499 |                 logger.error(f"First {{ position: {first_brace}")
500 |                 logger.error(f"Last }} position: {last_brace}")
501 |                 logger.error(f"Full cleaned text (first 1000 chars):")
502 |                 logger.error(cleaned_text[:1000])
503 |                 logger.error("=" * 80)
504 |                 return None
505 |             
506 |             if first_brace > 0:
507 |                 removed_prefix = cleaned_text[:first_brace]
508 |                 logger.info(f"🔧 Removing {first_brace} characters before first {{")
509 |                 logger.info(f"   Removed text: '{removed_prefix[:100]}'...")
510 |             
511 |             if last_brace < len(cleaned_text) - 1:
512 |                 removed_suffix = cleaned_text[last_brace + 1:]
513 |                 logger.info(f"🔧 Removing {len(cleaned_text) - last_brace - 1} characters after last }}")
514 |                 logger.info(f"   Removed text: '...{removed_suffix[-100:]}'")
515 |             
516 |             cleaned_text = cleaned_text[first_brace:last_brace + 1]
517 |             logger.info(f"✅ Extracted JSON object: {len(cleaned_text)} characters")
518 |             
519 |             # Check if response appears truncated
520 |             response_ends_properly = cleaned_text.rstrip().endswith("}")
521 |             if not response_ends_properly:
522 |                 logger.error("=" * 80)
523 |                 logger.error("❌ RESPONSE APPEARS TRUNCATED")
524 |                 logger.error("=" * 80)
525 |                 logger.error(f"Response length: {len(generated_text)} characters")
526 |                 logger.error(f"Cleaned text length: {len(cleaned_text)} characters")
527 |                 logger.error(f"Last 200 characters: {cleaned_text[-200:]}")
528 |                 logger.error(f"Response ends with: '{cleaned_text[-50:]}'")
529 |                 logger.error(f"Stop reason: {result.get('stop_reason', 'unknown')}")
530 |                 logger.error("=" * 80)
531 |                 logger.error("LIKELY CAUSE: WatsonX hit max_new_tokens limit before completing JSON")
532 |                 logger.error(f"Current max_new_tokens: 6000")
533 |                 logger.error("ATTEMPTING JSON COMPLETION...")
534 |                 logger.error("=" * 80)
535 |                 
536 |                 # Attempt to complete the JSON by adding missing closing braces
537 |                 try:
538 |                     # Count opening and closing braces
539 |                     open_braces = cleaned_text.count('{')
540 |                     close_braces = cleaned_text.count('}')
541 |                     missing_braces = open_braces - close_braces
542 |                     
543 |                     if missing_braces > 0 and missing_braces <= 5:
544 |                         logger.info(f"🔧 Attempting to add {missing_braces} missing closing braces")
545 |                         completed_text = cleaned_text + ('}' * missing_braces)
546 |                         
547 |                         # Try to parse the completed JSON
548 |                         test_parse = json.loads(completed_text)
549 |                         logger.info("✅ JSON completion successful!")
550 |                         cleaned_text = completed_text
551 |                     else:
552 |                         logger.error(f"❌ Too many missing braces ({missing_braces}), cannot auto-complete")
553 |                         return None
554 |                 except json.JSONDecodeError as e:
555 |                     logger.error(f"❌ JSON completion failed: {e}")
556 |                     return None
557 |                 except Exception as e:
558 |                     logger.error(f"❌ Unexpected error during JSON completion: {e}")
559 |                     return None
560 |             
561 |             # Log cleaned text
562 |             logger.info("=" * 80)
563 |             logger.info("🧹 CLEANED JSON TEXT")
564 |             logger.info("=" * 80)
565 |             logger.info(f"Length: {len(cleaned_text)} characters")
566 |             logger.info(f"First 300 chars: {cleaned_text[:300]}")
567 |             logger.info("=" * 80)
568 |             
569 |             # Attempt to parse JSON
570 |             logger.info("🔍 Attempting to parse JSON...")
571 |             roadmap = json.loads(cleaned_text)
572 |             logger.info("✅ JSON parsed successfully!")
573 |             
574 |             # Validate required fields
575 |             required_fields = ["summary", "phases", "skills", "weeklyPlan"]
576 |             missing_fields = [field for field in required_fields if field not in roadmap]
577 |             
578 |             if missing_fields:
579 |                 logger.warning(f"⚠️  Missing required fields: {missing_fields}")
580 |             else:
581 |                 logger.info("✅ All required fields present")
582 |             
583 |             # Log structure
584 |             logger.info(f"📊 Roadmap structure:")
585 |             logger.info(f"   - Phases: {len(roadmap.get('phases', []))}")
586 |             logger.info(f"   - Skills: {len(roadmap.get('skills', []))}")
587 |             logger.info(f"   - Tools: {len(roadmap.get('tools', []))}")
588 |             logger.info(f"   - Resources: {len(roadmap.get('resources', []))}")
589 |             logger.info(f"   - Portfolio Projects: {len(roadmap.get('portfolioProjects', []))}")
590 |             logger.info(f"   - Weekly Plans: {len(roadmap.get('weeklyPlan', []))}")
591 |             
592 |             # Add metadata
593 |             roadmap["metadata"] = {
594 |                 "usedWatsonx": True,
595 |                 "usedGitHub": len(github_projects) > 0,
596 |                 "matchedLocalResources": len(local_resources.get("resources", [])),
597 |                 "model": result.get("model_id", "unknown"),
598 |                 "tokens": result.get("token_count", 0)
599 |             }
600 |             
601 |             logger.info("✅ WatsonX roadmap generation complete!")
602 |             return roadmap
603 |         
604 |         except json.JSONDecodeError as e:
605 |             logger.error("=" * 80)
606 |             logger.error("❌ JSON PARSING FAILED")
607 |             logger.error("=" * 80)
608 |             logger.error(f"Error: {str(e)}")
609 |             logger.error(f"Error at line {e.lineno}, column {e.colno}")
610 |             logger.error(f"Error message: {e.msg}")
611 |             logger.error("=" * 80)
612 |             logger.error("RAW RESPONSE:")
613 |             logger.error(result.get('generated_text', 'NO TEXT')[:1000])
614 |             logger.error("=" * 80)
615 |             logger.error("CLEANED TEXT:")
616 |             logger.error(cleaned_text[:1000] if 'cleaned_text' in locals() else 'NOT AVAILABLE')
617 |             logger.error("=" * 80)
618 |             return None
619 |         
620 |         except Exception as e:
621 |             logger.error(f"❌ Error processing watsonx.ai response: {str(e)}")
622 |             logger.exception("Full exception:")
623 |             return None
624 | 
625 | 
626 | # Global instance
627 | watsonx_service = WatsonxService()
628 | 
629 | 
630 | async def generate_roadmap_with_ai(
631 |     career_goal: str,
632 |     current_skills: list,
633 |     timeframe: str,
634 |     local_resources: dict,
635 |     github_projects: list
636 | ) -> Optional[Dict[str, Any]]:
637 |     """
638 |     Generate a career roadmap using watsonx.ai with intelligent strategy selection.
639 |     
640 |     Strategy selection:
641 |     - 1 month (4 weeks): Single call with 3000 tokens
642 |     - 2 months (8 weeks): Single call with 4000 tokens
643 |     - 3+ months (12+ weeks): Multi-call strategy
644 |     
645 |     Args:
646 |         career_goal: Target career role
647 |         current_skills: List of current skills
648 |         timeframe: Available timeframe (e.g., "3 months")
649 |         local_resources: Curated resources from local data
650 |         github_projects: Relevant GitHub projects
651 |     
652 |     Returns:
653 |         Structured roadmap dictionary or None on error
654 |     """
655 |     import re
656 |     from services.watsonx_multi_call import multi_call_generator
657 |     
658 |     logger.info("=" * 80)
659 |     logger.info("🎯 INTELLIGENT ROADMAP GENERATION STRATEGY SELECTION")
660 |     logger.info("=" * 80)
661 |     logger.info(f"Career Goal: {career_goal}")
662 |     logger.info(f"Timeframe: {timeframe}")
663 |     
664 |     # Calculate weeks from timeframe
665 |     timeframe_lower = timeframe.lower()
666 |     weeks_needed = 12  # default
667 |     
668 |     if 'month' in timeframe_lower:
669 |         match = re.search(r'(\d+)', timeframe_lower)
670 |         if match:
671 |             months = int(match.group(1))
672 |             weeks_needed = months * 4
673 |     elif 'week' in timeframe_lower:
674 |         match = re.search(r'(\d+)', timeframe_lower)
675 |         if match:
676 |             weeks_needed = int(match.group(1))
677 |     
678 |     logger.info(f"📅 Weeks needed: {weeks_needed}")
679 |     
680 |     # Strategy selection
681 |     if weeks_needed <= 4:
682 |         # 1 month: Single call with 3000 tokens
683 |         logger.info("📋 Strategy: SINGLE CALL (3000 tokens)")
684 |         logger.info("   Reason: Short timeframe (≤4 weeks)")
685 |         logger.info("=" * 80)
686 |         
687 |         result = await watsonx_service.generate_career_roadmap(
688 |             career_goal=career_goal,
689 |             current_skills=current_skills,
690 |             timeframe=timeframe,
691 |             local_resources=local_resources,
692 |             github_projects=github_projects
693 |         )
694 |         
695 |         if result:
696 |             result['metadata']['generationStrategy'] = 'single_call'
697 |             result['metadata']['maxTokensUsed'] = 3000
698 |         
699 |         return result
700 |     
701 |     elif weeks_needed <= 8:
702 |         # 2 months: Single call with 4000 tokens
703 |         logger.info("📋 Strategy: SINGLE CALL (4000 tokens)")
704 |         logger.info("   Reason: Medium timeframe (5-8 weeks)")
705 |         logger.info("=" * 80)
706 |         
707 |         result = await watsonx_service.generate_career_roadmap(
708 |             career_goal=career_goal,
709 |             current_skills=current_skills,
710 |             timeframe=timeframe,
711 |             local_resources=local_resources,
712 |             github_projects=github_projects
713 |         )
714 |         
715 |         if result:
716 |             result['metadata']['generationStrategy'] = 'single_call'
717 |             result['metadata']['maxTokensUsed'] = 4000
718 |         
719 |         return result
720 |     
721 |     else:
722 |         # 3+ months: Multi-call strategy
723 |         logger.info("📋 Strategy: MULTI-CALL")
724 |         logger.info(f"   Reason: Long timeframe ({weeks_needed} weeks)")
725 |         logger.info("   Approach: Summary + Weekly chunks")
726 |         logger.info("=" * 80)
727 |         
728 |         result = await multi_call_generator.generate_full_roadmap(
729 |             career_goal=career_goal,
730 |             current_skills=current_skills,
731 |             timeframe=timeframe,
732 |             local_resources=local_resources,
733 |             github_projects=github_projects
734 |         )
735 |         
736 |         return result
737 | 
738 | # Made with Bob - AI Career Roadmap Generator
</content>
</file>
<file><path>server/services/github_service.py</path>
<content lines="1-176">
  1 | import os
  2 | import httpx
  3 | import asyncio
  4 | import logging
  5 | from typing import Optional
  6 | from models.schemas import GitHubRepository, GitHubProjectsResponse, ErrorResponse
  7 | 
  8 | logger = logging.getLogger(__name__)
  9 | 
 10 | 
 11 | async def search_github_projects(
 12 |     skill: str,
 13 |     max_retries: int = 3,
 14 |     min_stars: int = 50
 15 | ) -> GitHubProjectsResponse | ErrorResponse:
 16 |     """
 17 |     Search GitHub repositories for beginner projects based on a skill.
 18 |     Includes retry logic with exponential backoff and quality filtering.
 19 |     
 20 |     Args:
 21 |         skill: The skill to search for (e.g., "python", "react", "cybersecurity")
 22 |         max_retries: Maximum number of retry attempts (default: 3)
 23 |         min_stars: Minimum stars for quality filtering (default: 50)
 24 |     
 25 |     Returns:
 26 |         GitHubProjectsResponse with top 5 repositories or ErrorResponse on failure
 27 |     """
 28 |     # Construct search query with quality filters
 29 |     query = f"{skill} beginner project stars:>={min_stars}"
 30 |     
 31 |     # GitHub API endpoint
 32 |     url = "https://api.github.com/search/repositories"
 33 |     
 34 |     # Query parameters
 35 |     params = {
 36 |         "q": query,
 37 |         "sort": "stars",
 38 |         "order": "desc",
 39 |         "per_page": 10  # Get more to filter
 40 |     }
 41 |     
 42 |     # Headers
 43 |     headers = {
 44 |         "Accept": "application/vnd.github.v3+json",
 45 |         "User-Agent": "PathPilot-AI-Hackathon"
 46 |     }
 47 |     
 48 |     # Add authentication if token is available
 49 |     github_token = os.getenv("GITHUB_TOKEN")
 50 |     if github_token:
 51 |         headers["Authorization"] = f"Bearer {github_token}"
 52 |     
 53 |     # Retry loop with exponential backoff
 54 |     last_error = None
 55 |     for attempt in range(max_retries + 1):
 56 |         if attempt > 0:
 57 |             wait_time = 2 ** attempt  # Exponential backoff: 2s, 4s, 8s
 58 |             logger.warning(f"🔄 GitHub API retry attempt {attempt}/{max_retries} after {wait_time}s...")
 59 |             await asyncio.sleep(wait_time)
 60 |         
 61 |         try:
 62 |             # Make request to GitHub API
 63 |             async with httpx.AsyncClient() as client:
 64 |                 response = await client.get(url, params=params, headers=headers, timeout=10.0)
 65 |                 
 66 |                 # Handle rate limiting - retry if we have attempts left
 67 |                 if response.status_code == 403:
 68 |                     error_msg = "Rate limit exceeded"
 69 |                     logger.warning(f"⚠️  GitHub API: {error_msg}")
 70 |                     
 71 |                     if attempt < max_retries:
 72 |                         last_error = error_msg
 73 |                         continue
 74 |                     
 75 |                     return ErrorResponse(
 76 |                         error=error_msg,
 77 |                         detail="GitHub API rate limit reached. Please try again later or add a GITHUB_TOKEN to your .env file for higher limits."
 78 |                     )
 79 |                 
 80 |                 # Retry on server errors (5xx)
 81 |                 if 500 <= response.status_code < 600:
 82 |                     error_msg = f"Server error: HTTP {response.status_code}"
 83 |                     logger.warning(f"⚠️  GitHub API: {error_msg}")
 84 |                     
 85 |                     if attempt < max_retries:
 86 |                         last_error = error_msg
 87 |                         continue
 88 |                     
 89 |                     return ErrorResponse(
 90 |                         error="GitHub API server error",
 91 |                         detail=f"GitHub API returned status code {response.status_code}"
 92 |                     )
 93 |                 
 94 |                 # Handle other errors (don't retry)
 95 |                 if response.status_code != 200:
 96 |                     return ErrorResponse(
 97 |                         error="GitHub API error",
 98 |                         detail=f"GitHub API returned status code {response.status_code}"
 99 |                     )
100 |                 
101 |                 # Parse response
102 |                 data = response.json()
103 |                 
104 |                 # Extract and filter repository information
105 |                 repositories = []
106 |                 for item in data.get("items", []):
107 |                     # Quality filters
108 |                     stars = item.get("stargazers_count", 0)
109 |                     has_description = bool(item.get("description"))
110 |                     
111 |                     # Skip low-quality repos
112 |                     if stars < min_stars or not has_description:
113 |                         continue
114 |                     
115 |                     repo = GitHubRepository(
116 |                         name=item.get("full_name", "Unknown"),
117 |                         description=item.get("description"),
118 |                         stars=stars,
119 |                         language=item.get("language"),
120 |                         url=item.get("html_url", "")
121 |                     )
122 |                     repositories.append(repo)
123 |                     
124 |                     # Stop when we have 5 quality repos
125 |                     if len(repositories) >= 5:
126 |                         break
127 |                 
128 |                 logger.info(f"✅ GitHub API: Found {len(repositories)} quality repositories")
129 |                 
130 |                 return GitHubProjectsResponse(
131 |                     skill=skill,
132 |                     repositories=repositories,
133 |                     total_count=data.get("total_count", 0)
134 |                 )
135 |         
136 |         except httpx.TimeoutException:
137 |             error_msg = "Request timeout"
138 |             logger.warning(f"⚠️  GitHub API: {error_msg}")
139 |             
140 |             if attempt < max_retries:
141 |                 last_error = error_msg
142 |                 continue
143 |             
144 |             return ErrorResponse(
145 |                 error=error_msg,
146 |                 detail="GitHub API request timed out. Please try again."
147 |             )
148 |         
149 |         except httpx.RequestError as e:
150 |             error_msg = f"Network error: {str(e)}"
151 |             logger.warning(f"⚠️  GitHub API: {error_msg}")
152 |             
153 |             if attempt < max_retries:
154 |                 last_error = error_msg
155 |                 continue
156 |             
157 |             return ErrorResponse(
158 |                 error="Network error",
159 |                 detail=f"Failed to connect to GitHub API: {str(e)}"
160 |             )
161 |         
162 |         except Exception as e:
163 |             logger.error(f"❌ GitHub API unexpected error: {str(e)}")
164 |             return ErrorResponse(
165 |                 error="Unexpected error",
166 |                 detail=f"An unexpected error occurred: {str(e)}"
167 |             )
168 |     
169 |     # All retries exhausted
170 |     logger.error(f"❌ GitHub API: All {max_retries + 1} attempts failed. Last error: {last_error}")
171 |     return ErrorResponse(
172 |         error="GitHub API failed",
173 |         detail=f"Failed after {max_retries + 1} attempts: {last_error}"
174 |     )
175 | 
176 | # Made with Bob
</content>
</file>
<file><path>server/routes/usajobs.py</path>
<content lines="1-73">
 1 | """
 2 | USAJOBS API Routes
 3 | Endpoints for searching live federal job postings.
 4 | """
 5 | 
 6 | from fastapi import APIRouter, HTTPException, Query
 7 | from typing import Dict, Optional
 8 | from services.usajobs_service import usajobs_service
 9 | 
10 | 
11 | router = APIRouter(
12 |     prefix="/api/usajobs",
13 |     tags=["USAJOBS"]
14 | )
15 | 
16 | 
17 | @router.get("/search")
18 | async def search_usajobs(
19 |     keyword: str = Query(..., description="Search keyword for jobs", min_length=1),
20 |     location: Optional[str] = Query(None, description="Optional location filter (city, state, or zip)")
21 | ) -> Dict:
22 |     """
23 |     Search USAJOBS for live federal job postings.
24 |     
25 |     This endpoint searches the USAJOBS database for current job openings matching
26 |     the provided keyword and optional location. Results include job details such as
27 |     title, organization, location, salary range, and summary.
28 |     
29 |     Args:
30 |         keyword: Search term for jobs (e.g., "cybersecurity", "data analyst")
31 |         location: Optional location filter (e.g., "Orlando", "Florida", "32801")
32 |         
33 |     Returns:
34 |         Dictionary containing:
35 |         - success: Boolean indicating if the search was successful
36 |         - keyword: The search keyword used
37 |         - originalLocation: The original location searched
38 |         - searchLevel: "city", "state", or "nationwide"
39 |         - locationUsed: Actual location used for results
40 |         - count: Number of jobs found
41 |         - jobs: List of matching jobs with details including:
42 |             - title: Job title
43 |             - organization: Hiring organization
44 |             - location: Job location
45 |             - url: Link to job posting
46 |             - minimumSalary: Minimum salary (if available)
47 |             - maximumSalary: Maximum salary (if available)
48 |             - summary: Job summary (if available)
49 |         - fallbackMessage: Optional message if fallback was used
50 |         
51 |     Examples:
52 |         GET /api/usajobs/search?keyword=cybersecurity
53 |         GET /api/usajobs/search?keyword=cybersecurity&location=Orlando
54 |         GET /api/usajobs/search?keyword=data%20analyst&location=Florida
55 |     """
56 |     try:
57 |         result = await usajobs_service.search_jobs(keyword, location)
58 |         
59 |         if not result.get("success"):
60 |             # Return the error response from the service
61 |             return result
62 |         
63 |         return result
64 |         
65 |     except ValueError as e:
66 |         raise HTTPException(status_code=400, detail=str(e))
67 |     except Exception as e:
68 |         raise HTTPException(
69 |             status_code=500,
70 |             detail=f"Internal server error while searching USAJOBS: {str(e)}"
71 |         )
72 | 
73 | # Made with Bob
</content>
</file>
<file><path>README.md</path>
<content lines="1-434">
  1 | # PathPilot AI 🚀
  2 | 
  3 | An AI-powered career pathway generator built for the IBM Hackathon. PathPilot AI uses **IBM watsonx.ai** to create personalized, zero-to-resume-ready career roadmaps enriched with GitHub project discovery, curated resources, and real-world job opportunities.
  4 | 
  5 | ## 🌟 Features
  6 | 
  7 | - **AI-Powered Roadmap Generation**: Uses IBM watsonx.ai (Granite models) to generate intelligent, personalized career roadmaps
  8 | - **GitHub Project Discovery**: Automatically finds relevant beginner-friendly projects on GitHub
  9 | - **Curated Learning Resources**: Matches users with high-quality, free learning resources
 10 | - **Real Job Opportunities**: Integrates with USAJOBS API to show actual federal job openings
 11 | - **Structured Learning Paths**: Week-by-week plans with skills, tools, certifications, and portfolio projects
 12 | - **Resume-Ready Output**: Generates resume bullet points and portfolio project ideas
 13 | - **Secure & Private**: All API keys stored securely in environment variables, never exposed to frontend
 14 | 
 15 | ## 🎯 Supported Career Paths
 16 | 
 17 | - **SOC Analyst** - Security Operations Center
 18 | - **IT Help Desk** - Technical Support
 19 | - **Network Technician** - Network Infrastructure
 20 | - **Cybersecurity Analyst** - Information Security
 21 | - **Cloud Support Associate** - Cloud Computing
 22 | - **Software Developer** - Software Development
 23 | 
 24 | ## 🛠️ Tech Stack
 25 | 
 26 | ### Backend
 27 | - **FastAPI** - Modern Python web framework
 28 | - **IBM watsonx.ai** - AI-powered text generation (Granite models)
 29 | - **GitHub API** - Project discovery
 30 | - **USAJOBS API** - Federal job listings
 31 | - **O*NET API** - Career data
 32 | 
 33 | ### Frontend
 34 | - **React** - UI framework
 35 | - **Vite** - Build tool
 36 | - **TailwindCSS** - Styling
 37 | - **Axios** - HTTP client
 38 | 
 39 | ## 📋 Prerequisites
 40 | 
 41 | - **Python 3.8+**
 42 | - **Node.js 16+**
 43 | - **npm or yarn**
 44 | - **IBM Cloud Account** (for watsonx.ai)
 45 | - **GitHub Account** (optional, for higher API rate limits)
 46 | 
 47 | ## 🚀 Quick Start
 48 | 
 49 | ### 1. Clone the Repository
 50 | 
 51 | ```bash
 52 | git clone https://github.com/yourusername/PathPilot-AI.git
 53 | cd PathPilot-AI
 54 | ```
 55 | 
 56 | ### 2. Backend Setup
 57 | 
 58 | ```bash
 59 | cd server
 60 | 
 61 | # Create virtual environment
 62 | python -m venv .venv
 63 | 
 64 | # Activate virtual environment
 65 | # On Windows:
 66 | .venv\Scripts\activate
 67 | # On macOS/Linux:
 68 | source .venv/bin/activate
 69 | 
 70 | # Install dependencies
 71 | pip install -r requirements.txt
 72 | 
 73 | # Create .env file from example
 74 | copy .env.example .env  # Windows
 75 | # OR
 76 | cp .env.example .env    # macOS/Linux
 77 | ```
 78 | 
 79 | ### 3. Configure Environment Variables
 80 | 
 81 | Edit `server/.env` and add your API credentials:
 82 | 
 83 | ```env
 84 | # IBM watsonx.ai Configuration (REQUIRED for AI roadmap generation)
 85 | WATSONX_API_KEY=your_watsonx_api_key_here
 86 | WATSONX_PROJECT_ID=your_watsonx_project_id_here
 87 | WATSONX_URL=https://us-south.ml.cloud.ibm.com
 88 | 
 89 | # GitHub API Configuration (OPTIONAL - for higher rate limits)
 90 | GITHUB_TOKEN=your_github_token_here
 91 | 
 92 | # O*NET Web Services API Configuration (OPTIONAL)
 93 | ONET_API_KEY=your_onet_api_key_here
 94 | 
 95 | # USAJOBS API Configuration (OPTIONAL)
 96 | USAJOBS_EMAIL=your_email@example.com
 97 | USAJOBS_API_KEY=your_usajobs_api_key
 98 | 
 99 | # Server Configuration
100 | PORT=5000
101 | ENVIRONMENT=development
102 | ```
103 | 
104 | #### Getting API Keys:
105 | 
106 | **IBM watsonx.ai** (Required):
107 | 1. Go to [IBM Cloud](https://cloud.ibm.com/)
108 | 2. Create a watsonx.ai project
109 | 3. Get your API key from IBM Cloud IAM
110 | 4. Copy your Project ID from watsonx.ai
111 | 
112 | **GitHub Token** (Optional but recommended):
113 | 1. Go to [GitHub Settings > Tokens](https://github.com/settings/tokens)
114 | 2. Generate a new personal access token
115 | 3. No special scopes needed for public repo search
116 | 
117 | **O*NET API** (Optional):
118 | 1. Register at [O*NET Web Services](https://services.onetcenter.org/)
119 | 2. Get your API key from the dashboard
120 | 
121 | **USAJOBS API** (Optional):
122 | 1. Register at [USAJOBS Developer](https://developer.usajobs.gov/)
123 | 2. Get your API key and use your email
124 | 
125 | ### 4. Start the Backend
126 | 
127 | ```bash
128 | # Make sure you're in the server directory with venv activated
129 | python -m uvicorn main:app --reload --port 8000
130 | ```
131 | 
132 | The backend will be available at `http://localhost:8000`
133 | 
134 | API Documentation: `http://localhost:8000/docs`
135 | 
136 | ### 5. Frontend Setup
137 | 
138 | Open a new terminal:
139 | 
140 | ```bash
141 | cd client
142 | 
143 | # Install dependencies
144 | npm install
145 | 
146 | # Start development server
147 | npm run dev
148 | ```
149 | 
150 | The frontend will be available at `http://localhost:5173`
151 | 
152 | ## 🧪 Testing
153 | 
154 | ### Automated Testing Scripts
155 | 
156 | We provide several testing scripts to validate the application:
157 | 
158 | #### 1. Data Validation
159 | ```bash
160 | cd server
161 | python validate_data.py
162 | ```
163 | This validates all data files (resources, projects, certifications) for:
164 | - Required fields
165 | - Valid URLs
166 | - Consistent structure
167 | - No duplicates
168 | 
169 | #### 2. API Endpoint Testing
170 | ```bash
171 | cd server
172 | # Make sure backend is running first!
173 | python test_api_endpoints.py
174 | ```
175 | This tests the `/api/generate-roadmap` endpoint with:
176 | - Multiple career paths
177 | - Different timeframes (4 weeks, 6 weeks, 3 months, 6 months)
178 | - Various skill combinations
179 | - Response validation
180 | 
181 | #### 3. Career Path Testing
182 | ```bash
183 | cd server
184 | python test_career_paths.py
185 | ```
186 | This tests all 6 career paths with different timeframes to ensure:
187 | - Resources are matched correctly
188 | - GitHub projects are found
189 | - Watsonx.ai generates valid roadmaps
190 | - Timeframes are preserved
191 | 
192 | ### Manual Testing
193 | 
194 | #### Using the Frontend
195 | 
196 | 1. Navigate to `http://localhost:5173`
197 | 2. Click "Generate Pathway"
198 | 3. Fill in the form:
199 |    - **Career Goal**: "SOC Analyst" (or any supported role)
200 |    - **Timeframe**: Select weeks (4, 6, 8, 12, etc.)
201 |    - **Other settings**: Adjust as needed
202 | 4. Click "Generate My Pathway"
203 | 5. Verify the roadmap displays:
204 |    - Correct timeframe in the header
205 |    - 5+ learning resources with clickable links
206 |    - GitHub projects (if available)
207 |    - Portfolio project ideas
208 |    - Weekly plan
209 |    - Resume bullets
210 | 
211 | #### Using the API Directly
212 | 
213 | ```bash
214 | # Test the AI roadmap endpoint
215 | curl -X POST http://localhost:5000/api/generate-roadmap \
216 |   -H "Content-Type: application/json" \
217 |   -d '{
218 |     "careerGoal": "SOC Analyst",
219 |     "currentSkills": ["Python", "basic networking", "Wireshark"],
220 |     "timeframe": "3 months"
221 |   }'
222 | ```
223 | 
224 | #### Test Different Timeframes
225 | ```bash
226 | # 4 weeks
227 | curl -X POST http://localhost:5000/api/generate-roadmap \
228 |   -H "Content-Type: application/json" \
229 |   -d '{"careerGoal": "IT Help Desk", "currentSkills": [], "timeframe": "4 weeks"}'
230 | 
231 | # 6 weeks
232 | curl -X POST http://localhost:5000/api/generate-roadmap \
233 |   -H "Content-Type: application/json" \
234 |   -d '{"careerGoal": "Network Technician", "currentSkills": [], "timeframe": "6 weeks"}'
235 | 
236 | # 3 months
237 | curl -X POST http://localhost:5000/api/generate-roadmap \
238 |   -H "Content-Type: application/json" \
239 |   -d '{"careerGoal": "Cybersecurity Analyst", "currentSkills": [], "timeframe": "3 months"}'
240 | ```
241 | 
242 | ### Sample Request Body
243 | 
244 | ```json
245 | {
246 |   "careerGoal": "SOC Analyst",
247 |   "currentSkills": ["Python", "basic networking", "Wireshark"],
248 |   "timeframe": "3 months"
249 | }
250 | ```
251 | 
252 | ### Expected Response Format
253 | 
254 | ```json
255 | {
256 |   "success": true,
257 |   "careerGoal": "SOC Analyst",
258 |   "roadmap": {
259 |     "summary": "A comprehensive 3-month pathway to become a SOC Analyst...",
260 |     "phases": [
261 |       {
262 |         "phase": 1,
263 |         "title": "Foundation & Setup",
264 |         "duration": "Weeks 1-4",
265 |         "focus": "Learn security fundamentals",
266 |         "skills": ["Security Monitoring", "Incident Response"]
267 |       }
268 |     ],
269 |     "skills": ["Security Monitoring", "SIEM Tools", "Log Analysis"],
270 |     "tools": ["Splunk", "Wireshark", "Security Onion"],
271 |     "resources": [
272 |       {
273 |         "title": "IBM SkillsBuild - Cybersecurity Fundamentals",
274 |         "type": "course",
275 |         "url": "https://skillsbuild.org/..."
276 |       }
277 |     ],
278 |     "githubProjects": [
279 |       {
280 |         "name": "awesome-security",
281 |         "description": "A collection of security resources",
282 |         "stars": 5000,
283 |         "url": "https://github.com/..."
284 |       }
285 |     ],
286 |     "portfolioProjects": [...],
287 |     "resumeBullets": [...],
288 |     "weeklyPlan": [...],
289 |     "nextSteps": [...]
290 |   },
291 |   "metadata": {
292 |     "usedWatsonx": true,
293 |     "usedGitHub": true,
294 |     "matchedLocalResources": 5
295 |   }
296 | }
297 | ```
298 | 
299 | ## 🔒 Security
300 | 
301 | - **API Keys**: Never commit `.env` files. All secrets are stored in environment variables.
302 | - **Backend-Only API Calls**: Frontend never directly calls watsonx.ai or GitHub - all requests go through our secure backend.
303 | - **Error Handling**: Error messages are sanitized to prevent credential leaks.
304 | - **CORS**: Configured to only allow requests from the frontend origin.
305 | 
306 | ## 📁 Project Structure
307 | 
308 | ```
309 | PathPilot-AI/
310 | ├── client/                 # React frontend
311 | │   ├── src/
312 | │   │   ├── components/    # Reusable UI components
313 | │   │   ├── pages/         # Page components
314 | │   │   └── utils/         # API utilities
315 | │   └── package.json
316 | ├── server/                # FastAPI backend
317 | │   ├── data/             # Curated data files
318 | │   │   ├── roles.json           # Career role definitions
319 | │   │   ├── resources.json       # Learning resources
320 | │   │   ├── projects.json        # Project ideas
321 | │   │   └── certifications.json  # Certification recommendations
322 | │   ├── models/           # Pydantic schemas
323 | │   ├── routes/           # API endpoints
324 | │   │   └── roadmap.py          # AI roadmap generation endpoint
325 | │   ├── services/         # Business logic
326 | │   │   ├── watsonx_service.py  # IBM watsonx.ai integration
327 | │   │   └── github_service.py   # GitHub API integration
328 | │   ├── main.py           # FastAPI app
329 | │   ├── requirements.txt  # Python dependencies
330 | │   └── .env.example      # Environment variables template
331 | └── README.md
332 | ```
333 | 
334 | ## 🎨 Key Endpoints
335 | 
336 | ### AI Roadmap Generation
337 | - **POST** `/api/generate-roadmap` - Generate AI-powered career roadmap
338 | 
339 | ### Legacy Endpoints
340 | - **POST** `/api/pathways/generate` - Generate sample pathway (mock data)
341 | - **POST** `/api/pathways/adapt` - Adapt existing pathway
342 | - **GET** `/api/github/projects/{skill}` - Search GitHub projects
343 | - **GET** `/api/usajobs/search` - Search federal jobs
344 | - **POST** `/api/recommendations` - Get career recommendations
345 | 
346 | ## 🐛 Troubleshooting
347 | 
348 | ### Backend won't start
349 | - Ensure Python 3.8+ is installed: `python --version`
350 | - Activate virtual environment
351 | - Install dependencies: `pip install -r requirements.txt`
352 | - Check `.env` file exists in `server/` directory
353 | 
354 | ### Frontend won't start
355 | - Ensure Node.js 16+ is installed: `node --version`
356 | - Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
357 | - Check if port 5173 is available
358 | 
359 | ### AI Roadmap Generation Fails
360 | - Verify `WATSONX_API_KEY` and `WATSONX_PROJECT_ID` are set correctly
361 | - Check IBM Cloud IAM token is valid
362 | - Review backend logs for detailed error messages
363 | - The system will fall back to a template-based roadmap if watsonx.ai is unavailable
364 | 
365 | ### GitHub Projects Not Showing
366 | - **Fixed**: Response normalizer now ensures `githubProjects` array always exists
367 | - Check backend logs for GitHub API errors
368 | - Verify `GITHUB_TOKEN` is set for higher rate limits
369 | - The system falls back to verified local projects if GitHub fails
370 | 
371 | ### Wrong Timeframe Displayed
372 | - **Fixed**: Frontend now preserves exact user-selected timeframe
373 | - **Fixed**: Watsonx prompt explicitly instructs to preserve timeframe
374 | - If issue persists, check backend logs for prompt/response details
375 | 
376 | ### Insufficient Resources
377 | - **Fixed**: Resource matching now uses career goal context and aliases
378 | - **Fixed**: Minimum 5 resources guaranteed via fallback to verified resources
379 | - Run `python validate_data.py` to check data files
380 | - Add more resources to `server/data/verified_resources.json` if needed
381 | 
382 | ### GitHub API Rate Limit
383 | - Add `GITHUB_TOKEN` to `.env` for higher rate limits (5000 requests/hour vs 60)
384 | - The system gracefully handles rate limit errors and uses local projects
385 | 
386 | ### Watsonx Response Truncated
387 | - **Fixed**: Increased `max_new_tokens` to 4000
388 | - **Fixed**: Added retry logic with exponential backoff
389 | - **Fixed**: Response normalizer ensures all required fields exist
390 | - Check logs for "RESPONSE APPEARS TRUNCATED" warnings
391 | 
392 | ## 📝 Development Notes
393 | 
394 | ### Adding New Career Roles
395 | 
396 | 1. Add role definition to `server/data/roles.json`
397 | 2. Add resources to `server/data/resources.json`
398 | 3. Add projects to `server/data/projects.json`
399 | 4. Add certifications to `server/data/certifications.json`
400 | 
401 | ### Customizing AI Prompts
402 | 
403 | Edit the prompt in `server/services/watsonx_service.py` in the `generate_career_roadmap` method.
404 | 
405 | ### Changing AI Model
406 | 
407 | Update the `model_id` parameter in `watsonx_service.py`:
408 | - `ibm/granite-13b-chat-v2` (default)
409 | - `ibm/granite-20b-multilingual`
410 | - Other available watsonx.ai models
411 | 
412 | ## 🤝 Contributing
413 | 
414 | This project was built for the IBM Hackathon. Contributions are welcome!
415 | 
416 | ## 📄 License
417 | 
418 | MIT License - see LICENSE file for details
419 | 
420 | ## 🙏 Acknowledgments
421 | 
422 | - **IBM watsonx.ai** for AI-powered roadmap generation
423 | - **GitHub** for project discovery
424 | - **USAJOBS** for federal job listings
425 | - **O*NET** for career data
426 | - **IBM SkillsBuild** for learning resources
427 | 
428 | ## 📧 Support
429 | 
430 | For issues or questions, please open an issue on GitHub.
431 | 
432 | ---
433 | 
434 | **Made with ❤️ for the IBM Hackathon**
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files
server\main.py

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,README.md,server/.env,server/main.py,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:14:37.266Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$0.13

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

<update_todo_list>
<todos>
[x] Read project files (package.json, requirements.txt, .env.example, main.py)
[x] Read frontend files (App.jsx, pages, api.js)
[x] Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py)
[x] Read current README.md
[-] Analyze actual features implemented
[ ] Update README with accurate information
[ ] Verify no API keys or sensitive data exposed
</todos>
</update_todo_list>

---

**User:**

[update_todo_list] Result:
Todo list updated successfully.
<environment_details>
# VSCode Visible Files
server\main.py

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,README.md,server/.env,server/main.py,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:14:46.074Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$0.30

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Read project files (package.json, requirements.txt, .env.example, main.py) | Completed |
| 2 | Read frontend files (App.jsx, pages, api.js) | Completed |
| 3 | Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py) | Completed |
| 4 | Read current README.md | Completed |
| 5 | Analyze actual features implemented | In Progress |
| 6 | Update README with accurate information | Pending |
| 7 | Verify no API keys or sensitive data exposed | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

<read_file>
<args>
<file>
<path>server/services/usajobs_service.py</path>
</file>
<file>
<path>server/routes/onet.py</path>
</file>
<file>
<path>server/services/onet_service.py</path>
</file>
<file>
<path>client/src/components/PathwayForm.jsx</path>
</file>
<file>
<path>server/data/roles.json</path>
<line_range>1-50</line_range>
</file>
</args>
</read_file>

---

**User:**

[read_file for 5 files] Result:
<files>
<file><path>server/services/usajobs_service.py</path>
<content lines="1-329">
  1 | """
  2 | USAJOBS API Integration
  3 | Provides access to live federal job postings from USAJOBS.
  4 | """
  5 | 
  6 | import os
  7 | import httpx
  8 | import re
  9 | from typing import Dict, List, Optional, Tuple
 10 | 
 11 | 
 12 | class UsaJobsService:
 13 |     """Service for interacting with USAJOBS Search API"""
 14 |     
 15 |     BASE_URL = "https://data.usajobs.gov/api/search"
 16 |     
 17 |     def __init__(self):
 18 |         """Initialize USAJOBS service"""
 19 |         self._email = None
 20 |         self._api_key = None
 21 |     
 22 |     @property
 23 |     def email(self):
 24 |         """Lazy load email from environment variables"""
 25 |         if self._email is None:
 26 |             self._email = os.getenv("USAJOBS_EMAIL")
 27 |             if not self._email:
 28 |                 raise ValueError(
 29 |                     "USAJOBS email not found. Please set USAJOBS_EMAIL environment variable."
 30 |                 )
 31 |         return self._email
 32 |     
 33 |     @property
 34 |     def api_key(self):
 35 |         """Lazy load API key from environment variables"""
 36 |         if self._api_key is None:
 37 |             self._api_key = os.getenv("USAJOBS_API_KEY")
 38 |             if not self._api_key:
 39 |                 raise ValueError(
 40 |                     "USAJOBS API key not found. Please set USAJOBS_API_KEY environment variable."
 41 |                 )
 42 |         return self._api_key
 43 |     
 44 |     def _get_headers(self) -> Dict[str, str]:
 45 |         """Get required headers for USAJOBS API requests"""
 46 |         return {
 47 |             "Host": "data.usajobs.gov",
 48 |             "User-Agent": self.email,
 49 |             "Authorization-Key": self.api_key
 50 |         }
 51 |     
 52 |     def _parse_location(self, location: str) -> Tuple[Optional[str], Optional[str]]:
 53 |         """
 54 |         Parse location string to extract city and state.
 55 |         
 56 |         Args:
 57 |             location: Location string (e.g., "Orlando", "Florida", "Orlando, FL")
 58 |             
 59 |         Returns:
 60 |             Tuple of (city, state) where either can be None
 61 |         """
 62 |         if not location:
 63 |             return None, None
 64 |         
 65 |         location = location.strip()
 66 |         
 67 |         # Common US state abbreviations and full names
 68 |         us_states = {
 69 |             'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
 70 |             'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
 71 |             'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
 72 |             'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
 73 |             'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY',
 74 |             'DC', 'ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
 75 |             'COLORADO', 'CONNECTICUT', 'DELAWARE', 'FLORIDA', 'GEORGIA',
 76 |             'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS',
 77 |             'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS',
 78 |             'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA',
 79 |             'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO',
 80 |             'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA',
 81 |             'OREGON', 'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA',
 82 |             'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT',
 83 |             'VIRGINIA', 'WASHINGTON', 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING',
 84 |             'DISTRICT OF COLUMBIA'
 85 |         }
 86 |         
 87 |         # Check if location contains comma (e.g., "Orlando, FL")
 88 |         if ',' in location:
 89 |             parts = [p.strip() for p in location.split(',')]
 90 |             if len(parts) == 2:
 91 |                 city, state = parts
 92 |                 if state.upper() in us_states:
 93 |                     return city, state
 94 |                 return city, None
 95 |         
 96 |         # Check if it's just a state
 97 |         if location.upper() in us_states:
 98 |             return None, location
 99 |         
100 |         # Otherwise, assume it's a city
101 |         return location, None
102 |     
103 |     async def _perform_search(self, keyword: str, location: Optional[str] = None) -> Dict:
104 |         """
105 |         Perform a single USAJOBS search.
106 |         
107 |         Args:
108 |             keyword: Search term for jobs
109 |             location: Optional location filter
110 |             
111 |         Returns:
112 |             Dictionary containing search results
113 |         """
114 |         params = {
115 |             "Keyword": keyword.strip(),
116 |             "ResultsPerPage": 25
117 |         }
118 |         
119 |         if location and location.strip():
120 |             params["LocationName"] = location.strip()
121 |         
122 |         async with httpx.AsyncClient() as client:
123 |             response = await client.get(
124 |                 self.BASE_URL,
125 |                 params=params,
126 |                 headers=self._get_headers(),
127 |                 timeout=30.0
128 |             )
129 |             response.raise_for_status()
130 |             
131 |             data = response.json()
132 |             
133 |             # Extract search result info
134 |             search_result = data.get("SearchResult", {})
135 |             search_result_count = search_result.get("SearchResultCount", 0)
136 |             search_result_items = search_result.get("SearchResultItems", [])
137 |             
138 |             # Clean and format job results
139 |             jobs = []
140 |             for item in search_result_items:
141 |                 matched_object_descriptor = item.get("MatchedObjectDescriptor", {})
142 |                 
143 |                 # Extract position details
144 |                 position_title = matched_object_descriptor.get("PositionTitle", "N/A")
145 |                 organization_name = matched_object_descriptor.get("OrganizationName", "N/A")
146 |                 
147 |                 # Extract location info
148 |                 position_location = matched_object_descriptor.get("PositionLocation", [{}])
149 |                 location_name = "N/A"
150 |                 if position_location and len(position_location) > 0:
151 |                     first_location = position_location[0]
152 |                     city = first_location.get("CityName", "")
153 |                     state = first_location.get("StateCode", "")
154 |                     location_name = f"{city}, {state}" if city and state else (city or state or "N/A")
155 |                 
156 |                 # Extract URL
157 |                 position_uri = matched_object_descriptor.get("PositionURI", "")
158 |                 
159 |                 # Extract salary info
160 |                 position_remuneration = matched_object_descriptor.get("PositionRemuneration", [{}])
161 |                 min_salary = None
162 |                 max_salary = None
163 |                 if position_remuneration and len(position_remuneration) > 0:
164 |                     first_remuneration = position_remuneration[0]
165 |                     min_salary = first_remuneration.get("MinimumRange")
166 |                     max_salary = first_remuneration.get("MaximumRange")
167 |                 
168 |                 # Extract summary
169 |                 user_area = matched_object_descriptor.get("UserArea", {})
170 |                 brief_summary = user_area.get("Details", {}).get("JobSummary", "")
171 |                 
172 |                 job = {
173 |                     "title": position_title,
174 |                     "organization": organization_name,
175 |                     "location": location_name,
176 |                     "url": position_uri,
177 |                     "minimumSalary": min_salary,
178 |                     "maximumSalary": max_salary,
179 |                     "summary": brief_summary[:500] if brief_summary else None
180 |                 }
181 |                 
182 |                 jobs.append(job)
183 |             
184 |             return {
185 |                 "count": search_result_count,
186 |                 "jobs": jobs
187 |             }
188 |     
189 |     async def search_jobs(self, keyword: str, location: Optional[str] = None) -> Dict:
190 |         """
191 |         Search USAJOBS with fallback logic: city → state → nationwide.
192 |         
193 |         Args:
194 |             keyword: Search term for jobs
195 |             location: Optional location filter (city, state, or zip code)
196 |             
197 |         Returns:
198 |             Dictionary containing:
199 |             - success: Boolean
200 |             - keyword: Search keyword
201 |             - originalLocation: Original location searched
202 |             - searchLevel: "city", "state", or "nationwide"
203 |             - locationUsed: Actual location used for results
204 |             - count: Number of jobs found
205 |             - jobs: List of job postings
206 |             - fallbackMessage: Optional message if fallback was used
207 |         """
208 |         if not keyword or not keyword.strip():
209 |             raise ValueError("Keyword cannot be empty")
210 |         
211 |         original_location = location
212 |         
213 |         try:
214 |             # Try city search first if location provided
215 |             if location and location.strip():
216 |                 city, state = self._parse_location(location)
217 |                 
218 |                 # Level 1: Try exact location (city or full location string)
219 |                 result = await self._perform_search(keyword, location)
220 |                 
221 |                 if result["count"] > 0:
222 |                     return {
223 |                         "success": True,
224 |                         "keyword": keyword,
225 |                         "originalLocation": original_location,
226 |                         "searchLevel": "city" if city else "state",
227 |                         "locationUsed": location,
228 |                         "count": result["count"],
229 |                         "jobs": result["jobs"]
230 |                     }
231 |                 
232 |                 # Level 2: If city search returned 0 and we have a state, try state
233 |                 if city and state:
234 |                     result = await self._perform_search(keyword, state)
235 |                     
236 |                     if result["count"] > 0:
237 |                         return {
238 |                             "success": True,
239 |                             "keyword": keyword,
240 |                             "originalLocation": original_location,
241 |                             "searchLevel": "state",
242 |                             "locationUsed": state,
243 |                             "count": result["count"],
244 |                             "jobs": result["jobs"],
245 |                             "fallbackMessage": f"No exact {city} matches found, showing {state} results instead."
246 |                         }
247 |                 
248 |                 # Level 3: Try nationwide if both city and state returned 0
249 |                 result = await self._perform_search(keyword, None)
250 |                 
251 |                 if result["count"] > 0:
252 |                     location_desc = city if city else location
253 |                     return {
254 |                         "success": True,
255 |                         "keyword": keyword,
256 |                         "originalLocation": original_location,
257 |                         "searchLevel": "nationwide",
258 |                         "locationUsed": None,
259 |                         "count": result["count"],
260 |                         "jobs": result["jobs"],
261 |                         "fallbackMessage": f"No {location_desc} matches found, showing nationwide results instead."
262 |                     }
263 |                 
264 |                 # No results at any level
265 |                 return {
266 |                     "success": True,
267 |                     "keyword": keyword,
268 |                     "originalLocation": original_location,
269 |                     "searchLevel": "nationwide",
270 |                     "locationUsed": None,
271 |                     "count": 0,
272 |                     "jobs": []
273 |                 }
274 |             
275 |             # No location provided - search nationwide
276 |             result = await self._perform_search(keyword, None)
277 |             
278 |             return {
279 |                 "success": True,
280 |                 "keyword": keyword,
281 |                 "originalLocation": None,
282 |                 "searchLevel": "nationwide",
283 |                 "locationUsed": None,
284 |                 "count": result["count"],
285 |                 "jobs": result["jobs"]
286 |             }
287 |                 
288 |         except httpx.HTTPStatusError as e:
289 |             error_msg = f"USAJOBS API request failed with status {e.response.status_code}"
290 |             if e.response.status_code == 401:
291 |                 error_msg = "USAJOBS authentication failed. Please check your API key and email."
292 |             elif e.response.status_code == 403:
293 |                 error_msg = "USAJOBS API access forbidden. Please verify your credentials."
294 |             elif e.response.status_code == 404:
295 |                 error_msg = "USAJOBS API endpoint not found."
296 |             
297 |             return {
298 |                 "success": False,
299 |                 "error": error_msg,
300 |                 "keyword": keyword,
301 |                 "location": location,
302 |                 "count": 0,
303 |                 "jobs": []
304 |             }
305 |             
306 |         except httpx.RequestError as e:
307 |             return {
308 |                 "success": False,
309 |                 "error": f"USAJOBS API request error: {str(e)}",
310 |                 "keyword": keyword,
311 |                 "location": location,
312 |                 "count": 0,
313 |                 "jobs": []
314 |             }
315 |         except Exception as e:
316 |             return {
317 |                 "success": False,
318 |                 "error": f"Unexpected error: {str(e)}",
319 |                 "keyword": keyword,
320 |                 "location": location,
321 |                 "count": 0,
322 |                 "jobs": []
323 |             }
324 | 
325 | 
326 | # Create a singleton instance
327 | usajobs_service = UsaJobsService()
328 | 
329 | # Made with Bob
</content>
</file>
<file><path>server/routes/onet.py</path>
<content lines="1-127">
  1 | """
  2 | O*NET API Routes
  3 | Endpoints for searching O*NET occupation data.
  4 | """
  5 | 
  6 | from fastapi import APIRouter, HTTPException, Query
  7 | from typing import Dict
  8 | import logging
  9 | from services.onet_service import onet_service
 10 | 
 11 | # Set up logging
 12 | logger = logging.getLogger(__name__)
 13 | 
 14 | 
 15 | router = APIRouter(
 16 |     prefix="/api/onet",
 17 |     tags=["O*NET"]
 18 | )
 19 | 
 20 | 
 21 | @router.get("/debug")
 22 | async def debug_onet_connection() -> Dict:
 23 |     """
 24 |     Debug endpoint to test O*NET API connection.
 25 |     
 26 |     This endpoint tests the O*NET API connection without exposing sensitive credentials.
 27 |     It calls the O*NET /about/ endpoint to verify authentication is working.
 28 |     
 29 |     Returns:
 30 |         Dictionary containing:
 31 |         - success: Boolean indicating if connection test passed
 32 |         - status_code: HTTP status code from O*NET API
 33 |         - api_key_configured: Boolean indicating if API key is set (not the actual key)
 34 |         - response_preview: Small preview of API response (if successful)
 35 |         - error: Error message (if failed)
 36 |         
 37 |     Example:
 38 |         GET /api/onet/debug
 39 |     """
 40 |     try:
 41 |         result = await onet_service.test_connection()
 42 |         return result
 43 |         
 44 |     except Exception as e:
 45 |         raise HTTPException(
 46 |             status_code=500,
 47 |             detail=f"Debug test failed: {str(e)}"
 48 |         )
 49 | 
 50 | 
 51 | @router.get("/search")
 52 | async def search_onet_occupations(
 53 |     keyword: str = Query(..., description="Search keyword for occupations", min_length=1)
 54 | ) -> Dict:
 55 |     """
 56 |     Search O*NET occupations by keyword.
 57 |     
 58 |     This endpoint searches the O*NET database for occupations matching the provided keyword.
 59 |     O*NET provides official occupation data including skills, tasks, and knowledge requirements.
 60 |     
 61 |     Args:
 62 |         keyword: Search term for occupations (e.g., "cybersecurity", "software engineer")
 63 |         
 64 |     Returns:
 65 |         Dictionary containing:
 66 |         - success: Boolean indicating if the search was successful
 67 |         - keyword: The search keyword used
 68 |         - count: Number of occupations found
 69 |         - occupations: List of matching occupations with details
 70 |         
 71 |     Example:
 72 |         GET /api/onet/search?keyword=cybersecurity
 73 |     """
 74 |     logger.info(f"Local route hit: GET /api/onet/search?keyword={keyword}")
 75 |     
 76 |     try:
 77 |         result = await onet_service.search_occupations(keyword)
 78 |         
 79 |         # If O*NET returns errors, raise appropriate HTTP exceptions
 80 |         if not result.get("success"):
 81 |             status_code = result.get("status_code")
 82 |             error_detail = result.get("error", "O*NET request failed")
 83 |             
 84 |             # Authentication errors
 85 |             if status_code in [401, 403]:
 86 |                 raise HTTPException(
 87 |                     status_code=status_code,
 88 |                     detail=error_detail
 89 |                 )
 90 |             # Invalid/missing parameter
 91 |             elif status_code == 422:
 92 |                 raise HTTPException(
 93 |                     status_code=422,
 94 |                     detail=error_detail
 95 |                 )
 96 |             # Rate limit exceeded
 97 |             elif status_code == 429:
 98 |                 raise HTTPException(
 99 |                     status_code=429,
100 |                     detail=error_detail
101 |                 )
102 |             # Other HTTP errors from O*NET
103 |             elif status_code:
104 |                 raise HTTPException(
105 |                     status_code=status_code,
106 |                     detail=error_detail
107 |                 )
108 |             # Network or other errors (no status code)
109 |             else:
110 |                 raise HTTPException(
111 |                     status_code=503,
112 |                     detail=f"O*NET service unavailable: {error_detail}"
113 |                 )
114 |         
115 |         return result
116 |         
117 |     except HTTPException:
118 |         raise
119 |     except ValueError as e:
120 |         raise HTTPException(status_code=400, detail=str(e))
121 |     except Exception as e:
122 |         raise HTTPException(
123 |             status_code=500,
124 |             detail=f"Internal server error while searching O*NET: {str(e)}"
125 |         )
126 | 
127 | # Made with Bob
</content>
</file>
<file><path>server/services/onet_service.py</path>
<content lines="1-297">
  1 | """
  2 | O*NET Web Services Integration
  3 | Provides access to official occupation, skills, and task data from O*NET.
  4 | """
  5 | 
  6 | import os
  7 | import httpx
  8 | import logging
  9 | from typing import Dict, List, Optional
 10 | 
 11 | # Set up logging
 12 | logger = logging.getLogger(__name__)
 13 | 
 14 | 
 15 | class OnetService:
 16 |     """Service for interacting with O*NET Web Services API"""
 17 |     
 18 |     # Use the v2 API (api-v2.onetcenter.org)
 19 |     BASE_URL = "https://api-v2.onetcenter.org"
 20 |     ABOUT_URL = "https://api-v2.onetcenter.org/about/"
 21 |     SEARCH_URL = "https://api-v2.onetcenter.org/online/search"
 22 |     
 23 |     def __init__(self):
 24 |         """Initialize O*NET service"""
 25 |         self._api_key = None
 26 |     
 27 |     @property
 28 |     def api_key(self):
 29 |         """Lazy load API key from environment variables"""
 30 |         if self._api_key is None:
 31 |             self._api_key = os.getenv("ONET_API_KEY")
 32 |             if not self._api_key:
 33 |                 raise ValueError(
 34 |                     "O*NET API key not found. Please set ONET_API_KEY environment variable."
 35 |                 )
 36 |         return self._api_key
 37 |     
 38 |     def _get_headers(self) -> Dict[str, str]:
 39 |         """Get required headers for O*NET API requests"""
 40 |         return {
 41 |             "X-API-Key": self.api_key,
 42 |             "Accept": "application/json"
 43 |         }
 44 |     
 45 |     async def test_connection(self) -> Dict:
 46 |         """
 47 |         Test O*NET API connection using the /about/ endpoint.
 48 |         
 49 |         Returns:
 50 |             Dictionary with connection test results (no API key exposed)
 51 |         """
 52 |         api_key_loaded = bool(self._api_key or os.getenv("ONET_API_KEY"))
 53 |         
 54 |         logger.info(f"Testing O*NET connection to: {self.ABOUT_URL}")
 55 |         logger.info(f"API key loaded: {api_key_loaded}")
 56 |         
 57 |         try:
 58 |             async with httpx.AsyncClient() as client:
 59 |                 response = await client.get(
 60 |                     self.ABOUT_URL,
 61 |                     headers=self._get_headers(),
 62 |                     timeout=30.0
 63 |                 )
 64 |                 
 65 |                 logger.info(f"O*NET /about/ response status: {response.status_code}")
 66 |                 
 67 |                 # Try to parse JSON response
 68 |                 try:
 69 |                     data = response.json()
 70 |                     logger.info(f"O*NET response preview: {str(data)[:200]}")
 71 |                 except Exception as json_err:
 72 |                     logger.warning(f"Could not parse O*NET response as JSON: {json_err}")
 73 |                     data = {}
 74 |                 
 75 |                 return {
 76 |                     "success": response.status_code == 200,
 77 |                     "upstreamStatus": response.status_code,
 78 |                     "keyLoaded": api_key_loaded,
 79 |                     "responsePreview": {
 80 |                         "api_version": data.get("api_version", "N/A"),
 81 |                         "api_title": data.get("api_title", "N/A")
 82 |                     } if data else {"raw": response.text[:200]}
 83 |                 }
 84 |                 
 85 |         except httpx.HTTPStatusError as e:
 86 |             logger.error(f"O*NET HTTP error: {e.response.status_code}")
 87 |             return {
 88 |                 "success": False,
 89 |                 "upstreamStatus": e.response.status_code,
 90 |                 "keyLoaded": api_key_loaded,
 91 |                 "error": f"HTTP error: {e.response.status_code}"
 92 |             }
 93 |         except httpx.RequestError as e:
 94 |             logger.error(f"O*NET request error: {str(e)}")
 95 |             return {
 96 |                 "success": False,
 97 |                 "upstreamStatus": None,
 98 |                 "keyLoaded": api_key_loaded,
 99 |                 "error": f"Request error: {str(e)}"
100 |             }
101 |         except Exception as e:
102 |             logger.error(f"O*NET unexpected error: {str(e)}")
103 |             return {
104 |                 "success": False,
105 |                 "upstreamStatus": None,
106 |                 "keyLoaded": api_key_loaded,
107 |                 "error": f"Unexpected error: {str(e)}"
108 |             }
109 |     
110 |     async def search_occupations(self, keyword: str) -> Dict:
111 |         """
112 |         Search O*NET occupations based on a keyword.
113 |         
114 |         Args:
115 |             keyword: Search term for occupations
116 |             
117 |         Returns:
118 |             Dictionary containing search results with occupation data
119 |             
120 |         Raises:
121 |             ValueError: If keyword is empty
122 |         """
123 |         if not keyword or not keyword.strip():
124 |             raise ValueError("Keyword cannot be empty")
125 |         
126 |         # O*NET search endpoint - use v2 API
127 |         url = self.SEARCH_URL
128 |         
129 |         params = {
130 |             "keyword": keyword.strip(),
131 |             "start": 1,
132 |             "end": 10
133 |         }
134 |         
135 |         api_key_exists = bool(os.getenv("ONET_API_KEY"))
136 |         
137 |         logger.info("=" * 60)
138 |         logger.info("O*NET SEARCH REQUEST")
139 |         logger.info(f"Upstream URL: {url}")
140 |         logger.info(f"Search params: {params}")
141 |         logger.info(f"ONET_API_KEY exists: {api_key_exists}")
142 |         logger.info("=" * 60)
143 |         
144 |         try:
145 |             async with httpx.AsyncClient() as client:
146 |                 response = await client.get(
147 |                     url,
148 |                     params=params,
149 |                     headers=self._get_headers(),
150 |                     timeout=30.0
151 |                 )
152 |                 
153 |                 logger.info(f"Upstream status code: {response.status_code}")
154 |                 
155 |                 # Log first 300 characters of response body
156 |                 try:
157 |                     response_text = response.text[:300]
158 |                     logger.info(f"Response body (first 300 chars): {response_text}")
159 |                 except Exception as e:
160 |                     logger.warning(f"Could not log response body: {e}")
161 |                 
162 |                 # Log exact URL for 404 debugging
163 |                 if response.status_code == 404:
164 |                     logger.error(f"O*NET 404 - Exact URL called: {response.url}")
165 |                     logger.error(f"O*NET 404 - Request headers (no key): X-API-Key: [REDACTED], Accept: application/json")
166 |                 
167 |                 # Check for authentication errors
168 |                 if response.status_code in [401, 403]:
169 |                     error_msg = "O*NET authentication failed. Please check your API key."
170 |                     logger.error(f"{error_msg} Status: {response.status_code}")
171 |                     return {
172 |                         "success": False,
173 |                         "error": error_msg,
174 |                         "upstreamStatus": response.status_code,
175 |                         "keyword": keyword,
176 |                         "count": 0,
177 |                         "occupations": []
178 |                     }
179 |                 
180 |                 # Check for invalid/missing parameter
181 |                 if response.status_code == 422:
182 |                     error_msg = "Invalid or missing parameter in O*NET request."
183 |                     logger.error(f"{error_msg} Status: {response.status_code}")
184 |                     return {
185 |                         "success": False,
186 |                         "error": error_msg,
187 |                         "upstreamStatus": response.status_code,
188 |                         "keyword": keyword,
189 |                         "count": 0,
190 |                         "occupations": []
191 |                     }
192 |                 
193 |                 # Check for rate limiting
194 |                 if response.status_code == 429:
195 |                     error_msg = "O*NET rate limit exceeded. Please retry later."
196 |                     logger.error(f"{error_msg} Status: {response.status_code}")
197 |                     return {
198 |                         "success": False,
199 |                         "error": error_msg,
200 |                         "upstreamStatus": response.status_code,
201 |                         "keyword": keyword,
202 |                         "count": 0,
203 |                         "occupations": []
204 |                     }
205 |                 
206 |                 # Raise for other HTTP errors
207 |                 response.raise_for_status()
208 |                 
209 |                 data = response.json()
210 |                 
211 |                 # Check if results exist
212 |                 if not data or "occupation" not in data:
213 |                     logger.info("O*NET returned no occupations")
214 |                     return {
215 |                         "success": True,
216 |                         "keyword": keyword,
217 |                         "upstreamStatus": response.status_code,
218 |                         "rawTotal": data.get("total", 0) if data else 0,
219 |                         "count": 0,
220 |                         "occupations": []
221 |                     }
222 |                 
223 |                 occupations = data.get("occupation", [])
224 |                 
225 |                 # Ensure occupations is a list
226 |                 if not isinstance(occupations, list):
227 |                     occupations = [occupations] if occupations else []
228 |                 
229 |                 # Extract required fields from each occupation
230 |                 formatted_occupations = []
231 |                 for occ in occupations:
232 |                     formatted_occupations.append({
233 |                         "title": occ.get("title", ""),
234 |                         "code": occ.get("code", ""),
235 |                         "href": occ.get("href", ""),
236 |                         "brightOutlook": occ.get("tags", {}).get("bright_outlook", False) if isinstance(occ.get("tags"), dict) else False
237 |                     })
238 |                 
239 |                 logger.info(f"O*NET returned {len(formatted_occupations)} occupations")
240 |                 
241 |                 return {
242 |                     "success": True,
243 |                     "keyword": keyword,
244 |                     "upstreamStatus": response.status_code,
245 |                     "rawTotal": data.get("total", len(formatted_occupations)),
246 |                     "count": len(formatted_occupations),
247 |                     "occupations": formatted_occupations
248 |                 }
249 |                 
250 |         except httpx.HTTPStatusError as e:
251 |             logger.error(f"O*NET HTTP error: {e.response.status_code}")
252 |             logger.error(f"O*NET error - Exact URL: {e.response.url}")
253 |             error_msg = f"O*NET API request failed with status {e.response.status_code}"
254 |             if e.response.status_code == 401:
255 |                 error_msg = "O*NET authentication failed. Please check your API key."
256 |             elif e.response.status_code == 403:
257 |                 error_msg = "O*NET access forbidden. Please verify your API key."
258 |             elif e.response.status_code == 404:
259 |                 error_msg = "O*NET API endpoint not found."
260 |             elif e.response.status_code == 422:
261 |                 error_msg = "Invalid or missing parameter in O*NET request."
262 |             elif e.response.status_code == 429:
263 |                 error_msg = "O*NET rate limit exceeded. Please retry later."
264 |             
265 |             return {
266 |                 "success": False,
267 |                 "error": error_msg,
268 |                 "upstreamStatus": e.response.status_code,
269 |                 "keyword": keyword,
270 |                 "count": 0,
271 |                 "occupations": []
272 |             }
273 |             
274 |         except httpx.RequestError as e:
275 |             logger.error(f"O*NET request error: {str(e)}")
276 |             return {
277 |                 "success": False,
278 |                 "error": f"O*NET API request error: {str(e)}",
279 |                 "keyword": keyword,
280 |                 "count": 0,
281 |                 "occupations": []
282 |             }
283 |         except Exception as e:
284 |             logger.error(f"O*NET unexpected error: {str(e)}")
285 |             return {
286 |                 "success": False,
287 |                 "error": f"Unexpected error: {str(e)}",
288 |                 "keyword": keyword,
289 |                 "count": 0,
290 |                 "occupations": []
291 |             }
292 | 
293 | 
294 | # Create a singleton instance
295 | onet_service = OnetService()
296 | 
297 | # Made with Bob
</content>
</file>
<file><path>client/src/components/PathwayForm.jsx</path>
<content lines="1-346">
  1 | import { useState } from 'react';
  2 | import { useNavigate } from 'react-router-dom';
  3 | import { generateRoadmap, transformRoadmapToPathway } from '../utils/api';
  4 | import { savePathway } from '../utils/localStorage';
  5 | 
  6 | /**
  7 |  * Form component for generating a career pathway
  8 |  */
  9 | function PathwayForm() {
 10 |   const navigate = useNavigate();
 11 |   const [loading, setLoading] = useState(false);
 12 |   const [error, setError] = useState('');
 13 | 
 14 |   const [formData, setFormData] = useState({
 15 |     goal: '',
 16 |     level: 'beginner',
 17 |     weeks: 6,
 18 |     daysPerWeek: 5,
 19 |     hoursPerDay: 2,
 20 |     preferences: [],
 21 |     budget: 'free-first',
 22 |   });
 23 | 
 24 |   const handleChange = (e) => {
 25 |     const { name, value, type, checked } = e.target;
 26 | 
 27 |     if (type === 'checkbox') {
 28 |       // Handle checkbox for preferences
 29 |       setFormData((prev) => ({
 30 |         ...prev,
 31 |         preferences: checked
 32 |           ? [...prev.preferences, value]
 33 |           : prev.preferences.filter((pref) => pref !== value),
 34 |       }));
 35 |     } else {
 36 |       setFormData((prev) => ({
 37 |         ...prev,
 38 |         [name]: type === 'number' ? parseInt(value) : value,
 39 |       }));
 40 |     }
 41 |   };
 42 | 
 43 |   const handleSubmit = async (e) => {
 44 |     e.preventDefault();
 45 |     setError('');
 46 |     setLoading(true);
 47 | 
 48 |     try {
 49 |       // Validate form
 50 |       if (!formData.goal.trim()) {
 51 |         throw new Error('Please enter a career goal');
 52 |       }
 53 | 
 54 |       console.log('🚀 Starting pathway generation with Watsonx.ai...');
 55 |       console.log('📋 Form data:', formData);
 56 | 
 57 |       // Normalize timeframe to weeks for consistency
 58 |       // Backend expects weeks format for accurate planning
 59 |       const timeframe = `${formData.weeks} weeks`;
 60 | 
 61 |       // Prepare request for Watsonx.ai roadmap endpoint
 62 |       const roadmapRequest = {
 63 |         careerGoal: formData.goal,
 64 |         currentSkills: [], // User hasn't specified current skills in this form
 65 |         timeframe: timeframe,
 66 |         weeks: formData.weeks  // Send explicit weeks to backend
 67 |       };
 68 | 
 69 |       console.log('📡 Calling Watsonx.ai roadmap API...');
 70 |       console.log('Request:', roadmapRequest);
 71 | 
 72 |       // Generate roadmap using Watsonx.ai
 73 |       const roadmapResponse = await generateRoadmap(roadmapRequest);
 74 | 
 75 |       console.log('=' .repeat(80));
 76 |       console.log('✅ RECEIVED ROADMAP FROM BACKEND');
 77 |       console.log('=' .repeat(80));
 78 |       console.log('📦 Full response:', roadmapResponse);
 79 |       console.log('🔑 Response keys:', Object.keys(roadmapResponse));
 80 |       console.log('🗺️  Roadmap keys:', Object.keys(roadmapResponse.roadmap || {}));
 81 |       console.log('🐙 GitHub projects in response:', roadmapResponse.roadmap?.githubProjects?.length || 0);
 82 |       if (roadmapResponse.roadmap?.githubProjects && roadmapResponse.roadmap.githubProjects.length > 0) {
 83 |         console.log('🐙 GitHub projects:', roadmapResponse.roadmap.githubProjects);
 84 |       }
 85 |       console.log('📚 Resources in response:', roadmapResponse.roadmap?.resources?.length || 0);
 86 |       console.log('📅 Weekly plans in response:', roadmapResponse.roadmap?.weeklyPlan?.length || 0);
 87 |       console.log('=' .repeat(80));
 88 | 
 89 |       // Transform the Watsonx.ai response to match frontend expectations
 90 |       const pathway = transformRoadmapToPathway(roadmapResponse, {
 91 |         ...formData,
 92 |         timeframe
 93 |       });
 94 | 
 95 |       console.log('=' .repeat(80));
 96 |       console.log('✅ PATHWAY TRANSFORMATION COMPLETE');
 97 |       console.log('=' .repeat(80));
 98 |       console.log('📦 Final pathway object:', pathway);
 99 |       console.log('🔑 Pathway keys:', Object.keys(pathway));
100 |       console.log('🐙 GitHub projects in pathway:', pathway.githubProjects?.length || 0);
101 |       if (pathway.githubProjects && pathway.githubProjects.length > 0) {
102 |         console.log('🐙 GitHub projects:', pathway.githubProjects);
103 |       }
104 |       console.log('📚 Total resources across weeks:', pathway.weeks?.reduce((sum, w) => sum + (w.resources?.length || 0), 0) || 0);
105 |       console.log('📅 Weeks:', pathway.weeks?.length || 0);
106 |       console.log('=' .repeat(80));
107 | 
108 |       // Save to localStorage
109 |       savePathway(pathway);
110 |       console.log('💾 Saved pathway to localStorage');
111 |       
112 |       // CRITICAL FIX: Use correct localStorage key 'generatedPathway'
113 |       const savedPathway = JSON.parse(localStorage.getItem('generatedPathway') || '{}');
114 |       console.log('🔍 LOCALSTORAGE VERIFICATION:');
115 |       console.log('   Saved pathway keys:', Object.keys(savedPathway));
116 |       console.log('   githubProjects in saved:', savedPathway.githubProjects?.length || 0);
117 |       console.log('   weeks in saved:', savedPathway.weeks?.length || 0);
118 |       
119 |       if (savedPathway.githubProjects && savedPathway.githubProjects.length > 0) {
120 |         console.log('   First GitHub project:', savedPathway.githubProjects[0]);
121 |       }
122 |       
123 |       // Verify it matches what we tried to save
124 |       if (savedPathway.githubProjects?.length !== pathway.githubProjects?.length) {
125 |         console.error('❌ MISMATCH: Tried to save', pathway.githubProjects?.length, 'but localStorage has', savedPathway.githubProjects?.length);
126 |       } else {
127 |         console.log('✅ localStorage verification passed');
128 |       }
129 | 
130 |       // Redirect to pathway page
131 |       navigate('/pathway');
132 |     } catch (err) {
133 |       console.error('❌ Error generating pathway:', err);
134 |       console.error('Error details:', {
135 |         message: err.message,
136 |         cause: err.cause,
137 |         stack: err.stack
138 |       });
139 |       setError(err.message || 'Failed to generate pathway. Please try again.');
140 |     } finally {
141 |       setLoading(false);
142 |     }
143 |   };
144 | 
145 |   return (
146 |     <form onSubmit={handleSubmit} className="space-y-8">
147 |       {/* Error Message */}
148 |       {error && (
149 |         <div className="bg-red-500/10 border border-red-500/50 text-red-400 px-5 py-4 rounded-xl flex items-start space-x-3 animate-in fade-in slide-in-from-top-2 duration-300">
150 |           <svg className="w-5 h-5 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
151 |             <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
152 |           </svg>
153 |           <span>{error}</span>
154 |         </div>
155 |       )}
156 | 
157 |       {/* Career Goal */}
158 |       <div>
159 |         <label htmlFor="goal" className="block text-sm font-semibold text-slate-200 mb-3">
160 |           Career Goal *
161 |         </label>
162 |         <input
163 |           type="text"
164 |           id="goal"
165 |           name="goal"
166 |           value={formData.goal}
167 |           onChange={handleChange}
168 |           placeholder="e.g., Junior Web Developer, Data Analyst, UX Designer"
169 |           className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
170 |           required
171 |         />
172 |         <p className="mt-2 text-xs text-slate-500">What role are you aiming for?</p>
173 |       </div>
174 | 
175 |       {/* Skill Level */}
176 |       <div>
177 |         <label htmlFor="level" className="block text-sm font-semibold text-slate-200 mb-3">
178 |           Current Skill Level *
179 |         </label>
180 |         <select
181 |           id="level"
182 |           name="level"
183 |           value={formData.level}
184 |           onChange={handleChange}
185 |           className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all cursor-pointer"
186 |           required
187 |         >
188 |           <option value="beginner">🌱 Beginner - Just starting out</option>
189 |           <option value="intermediate">🚀 Intermediate - Some experience</option>
190 |           <option value="advanced">⭐ Advanced - Experienced learner</option>
191 |         </select>
192 |       </div>
193 | 
194 |       {/* Timeline */}
195 |       <div>
196 |         <h3 className="text-sm font-semibold text-slate-200 mb-4">Time Commitment *</h3>
197 |         <div className="grid md:grid-cols-3 gap-4">
198 |           <div>
199 |             <label htmlFor="weeks" className="block text-xs font-medium text-slate-400 mb-2">
200 |               Number of Weeks
201 |             </label>
202 |             <input
203 |               type="number"
204 |               id="weeks"
205 |               name="weeks"
206 |               value={formData.weeks}
207 |               onChange={handleChange}
208 |               min="1"
209 |               max="52"
210 |               className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-center font-semibold"
211 |               required
212 |             />
213 |           </div>
214 | 
215 |           <div>
216 |             <label htmlFor="daysPerWeek" className="block text-xs font-medium text-slate-400 mb-2">
217 |               Days per Week
218 |             </label>
219 |             <input
220 |               type="number"
221 |               id="daysPerWeek"
222 |               name="daysPerWeek"
223 |               value={formData.daysPerWeek}
224 |               onChange={handleChange}
225 |               min="1"
226 |               max="7"
227 |               className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-center font-semibold"
228 |               required
229 |             />
230 |           </div>
231 | 
232 |           <div>
233 |             <label htmlFor="hoursPerDay" className="block text-xs font-medium text-slate-400 mb-2">
234 |               Hours per Day
235 |             </label>
236 |             <input
237 |               type="number"
238 |               id="hoursPerDay"
239 |               name="hoursPerDay"
240 |               value={formData.hoursPerDay}
241 |               onChange={handleChange}
242 |               min="1"
243 |               max="24"
244 |               className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-center font-semibold"
245 |               required
246 |             />
247 |           </div>
248 |         </div>
249 |         <p className="mt-3 text-xs text-slate-500">
250 |           Total: {formData.weeks * formData.daysPerWeek * formData.hoursPerDay} hours of learning
251 |         </p>
252 |       </div>
253 | 
254 |       {/* Learning Preferences */}
255 |       <div>
256 |         <label className="block text-sm font-semibold text-slate-200 mb-3">
257 |           Learning Preferences
258 |         </label>
259 |         <p className="text-xs text-slate-500 mb-4">Select all that apply</p>
260 |         <div className="grid md:grid-cols-2 gap-3">
261 |           {[
262 |             { value: 'projects', label: 'Project-Based', icon: '🛠️' },
263 |             { value: 'videos', label: 'Video Tutorials', icon: '🎥' },
264 |             { value: 'reading', label: 'Reading & Docs', icon: '📚' },
265 |             { value: 'interactive', label: 'Interactive', icon: '💻' }
266 |           ].map((pref) => (
267 |             <label
268 |               key={pref.value}
269 |               className={`flex items-center space-x-3 bg-slate-800/50 border rounded-xl px-4 py-3.5 cursor-pointer transition-all ${
270 |                 formData.preferences.includes(pref.value)
271 |                   ? 'border-blue-500 bg-blue-500/10'
272 |                   : 'border-slate-700 hover:border-slate-600 hover:bg-slate-800'
273 |               }`}
274 |             >
275 |               <input
276 |                 type="checkbox"
277 |                 name="preferences"
278 |                 value={pref.value}
279 |                 checked={formData.preferences.includes(pref.value)}
280 |                 onChange={handleChange}
281 |                 className="w-5 h-5 text-blue-500 bg-slate-700 border-slate-600 rounded focus:ring-2 focus:ring-blue-500"
282 |               />
283 |               <span className="text-xl">{pref.icon}</span>
284 |               <span className="text-white font-medium">{pref.label}</span>
285 |             </label>
286 |           ))}
287 |         </div>
288 |       </div>
289 | 
290 |       {/* Budget */}
291 |       <div>
292 |         <label htmlFor="budget" className="block text-sm font-semibold text-slate-200 mb-3">
293 |           Budget Preference *
294 |         </label>
295 |         <select
296 |           id="budget"
297 |           name="budget"
298 |           value={formData.budget}
299 |           onChange={handleChange}
300 |           className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all cursor-pointer"
301 |           required
302 |         >
303 |           <option value="free-first">💚 Free resources first</option>
304 |           <option value="paid-ok">💙 Paid resources OK</option>
305 |           <option value="premium">💎 Premium resources preferred</option>
306 |         </select>
307 |       </div>
308 | 
309 |       {/* Submit Button */}
310 |       <div className="pt-4">
311 |         <button
312 |           type="submit"
313 |           disabled={loading}
314 |           className="w-full px-6 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-bold rounded-xl hover:from-blue-600 hover:to-purple-700 transition-all transform hover:scale-[1.02] disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none shadow-xl hover:shadow-2xl hover:shadow-purple-500/30"
315 |         >
316 |           {loading ? (
317 |             <span className="flex items-center justify-center">
318 |               <svg className="animate-spin -ml-1 mr-3 h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
319 |                 <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
320 |                 <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
321 |               </svg>
322 |               <span className="text-lg">Generating Your Pathway...</span>
323 |             </span>
324 |           ) : (
325 |             <span className="flex items-center justify-center text-lg">
326 |               Generate My Pathway
327 |               <svg className="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
328 |                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
329 |               </svg>
330 |             </span>
331 |           )}
332 |         </button>
333 | 
334 |         {loading && (
335 |           <p className="text-sm text-slate-400 text-center mt-4 animate-pulse">
336 |             ✨ Creating your personalized learning path... This may take a few seconds.
337 |           </p>
338 |         )}
339 |       </div>
340 |     </form>
341 |   );
342 | }
343 | 
344 | export default PathwayForm;
345 | 
346 | // Made with Bob
</content>
</file>
<file><path>server/data/roles.json</path>
<content lines="1-50">
 1 | [
 2 |   {
 3 |     "id": "soc-analyst",
 4 |     "title": "SOC Analyst",
 5 |     "category": "Cybersecurity",
 6 |     "description": "Security Operations Center (SOC) Analysts monitor and defend against cyber threats in real-time. They analyze security alerts, investigate incidents, and respond to breaches.",
 7 |     "coreSkills": ["Security Monitoring", "Incident Response", "SIEM Tools", "Network Security", "Log Analysis"],
 8 |     "tools": ["Splunk", "Wireshark", "Nmap", "Metasploit", "Security Onion", "ELK Stack"],
 9 |     "certifications": ["CompTIA Security+", "CEH", "GIAC GSEC", "CySA+"],
10 |     "beginnerKeywords": ["soc", "security monitoring", "incident response", "cybersecurity beginner"],
11 |     "estimatedTimeToJob": "3-6 months with intensive study"
12 |   },
13 |   {
14 |     "id": "it-help-desk",
15 |     "title": "IT Help Desk",
16 |     "category": "IT Support",
17 |     "description": "IT Help Desk technicians provide first-line technical support to end users, troubleshooting hardware, software, and network issues.",
18 |     "coreSkills": ["Troubleshooting", "Customer Service", "Windows/Mac OS", "Active Directory", "Ticketing Systems"],
19 |     "tools": ["ServiceNow", "Jira Service Desk", "Remote Desktop", "Active Directory", "Office 365"],
20 |     "certifications": ["CompTIA A+", "CompTIA Network+", "ITIL Foundation", "Microsoft 365 Certified"],
21 |     "beginnerKeywords": ["help desk", "it support", "troubleshooting", "technical support"],
22 |     "estimatedTimeToJob": "2-4 months"
23 |   },
24 |   {
25 |     "id": "network-technician",
26 |     "title": "Network Technician",
27 |     "category": "Networking",
28 |     "description": "Network Technicians install, configure, and maintain computer networks. They ensure reliable connectivity and troubleshoot network issues.",
29 |     "coreSkills": ["Networking Fundamentals", "TCP/IP", "Routing & Switching", "Network Troubleshooting", "Cabling"],
30 |     "tools": ["Cisco IOS", "Wireshark", "PuTTY", "Network Analyzers", "Cable Testers"],
31 |     "certifications": ["CompTIA Network+", "CCNA", "CompTIA A+"],
32 |     "beginnerKeywords": ["networking", "cisco", "network admin", "tcp ip"],
33 |     "estimatedTimeToJob": "3-5 months"
34 |   },
35 |   {
36 |     "id": "cybersecurity-analyst",
37 |     "title": "Cybersecurity Analyst",
38 |     "category": "Cybersecurity",
39 |     "description": "Cybersecurity Analysts protect organizations from cyber threats by implementing security measures, conducting risk assessments, and monitoring for vulnerabilities.",
40 |     "coreSkills": ["Risk Assessment", "Vulnerability Management", "Security Frameworks", "Penetration Testing", "Compliance"],
41 |     "tools": ["Nessus", "Burp Suite", "Metasploit", "Kali Linux", "Nmap", "OWASP ZAP"],
42 |     "certifications": ["CompTIA Security+", "CEH", "CISSP", "CISM"],
43 |     "beginnerKeywords": ["cybersecurity", "infosec", "penetration testing", "ethical hacking"],
44 |     "estimatedTimeToJob": "4-6 months"
45 |   },
46 |   {
47 |     "id": "cloud-support-associate",
48 |     "title": "Cloud Support Associate",
49 |     "category": "Cloud Computing",
50 |     "description": "Cloud Support Associates help customers deploy and manage cloud infrastructure, troubleshoot issues, and optimize cloud resources.",
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files
server\main.py

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,README.md,server/.env,server/main.py,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:14:50.659Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$0.48

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Read project files (package.json, requirements.txt, .env.example, main.py) | Completed |
| 2 | Read frontend files (App.jsx, pages, api.js) | Completed |
| 3 | Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py) | Completed |
| 4 | Read current README.md | Completed |
| 5 | Analyze actual features implemented | In Progress |
| 6 | Update README with accurate information | Pending |
| 7 | Verify no API keys or sensitive data exposed | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

<update_todo_list>
<todos>
[x] Read project files (package.json, requirements.txt, .env.example, main.py)
[x] Read frontend files (App.jsx, pages, api.js)
[x] Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py)
[x] Read current README.md
[x] Analyze actual features implemented
[-] Update README with accurate information
[ ] Verify no API keys or sensitive data exposed
</todos>
</update_todo_list>

---

**User:**

[update_todo_list] Result:
Todo list updated successfully.
<environment_details>
# VSCode Visible Files
server\main.py

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,README.md,server/.env,server/main.py,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:14:57.297Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$0.69

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Read project files (package.json, requirements.txt, .env.example, main.py) | Completed |
| 2 | Read frontend files (App.jsx, pages, api.js) | Completed |
| 3 | Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py) | Completed |
| 4 | Read current README.md | Completed |
| 5 | Analyze actual features implemented | Completed |
| 6 | Update README with accurate information | In Progress |
| 7 | Verify no API keys or sensitive data exposed | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

Now I'll update the README with accurate information based on the actual codebase:

<apply_diff>
<path>README.md</path>
<diff>
<<<<<<< SEARCH
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
=======
# PathPilot AI 🚀

An AI-powered career pathway generator built for the IBM Hackathon. PathPilot AI uses **IBM watsonx.ai** to create personalized, week-by-week career roadmaps with curated resources, GitHub projects, and real federal job opportunities.

## 🌟 Key Features

### Core Functionality
- **AI-Powered Roadmap Generation**: Uses IBM watsonx.ai (Granite 3-8B Instruct model) to generate intelligent, personalized career roadmaps
- **Week-by-Week Learning Plans**: Structured daily tasks and objectives for each week of your journey
- **Adaptive Pathways**: Modify your roadmap based on feedback (e.g., "I only have 1 hour per day now")
- **Progress Tracking**: Mark weeks as complete and track your learning journey
- **Portfolio Checklist**: Final checklist to ensure you're job-ready

### Resource Discovery
- **GitHub Project Discovery**: Automatically finds relevant beginner-friendly projects with quality filtering (50+ stars)
- **Curated Learning Resources**: Matches users with verified, high-quality learning resources from trusted platforms
- **Resource Validation**: Backend validates URLs and replaces broken links with verified alternatives
- **Federal Job Search**: Live integration with USAJOBS API showing actual federal job openings with smart fallback (city → state → nationwide)

### Smart Features
- **Intelligent Timeframe Enforcement**: Backend ensures AI respects your exact timeframe (4 weeks, 6 weeks, 3 months, etc.)
- **Multi-Call Strategy**: For longer roadmaps (12+ weeks), uses intelligent chunking to avoid token limits
- **Graceful Fallbacks**: If APIs fail, system uses curated local data to ensure you always get a roadmap
- **Retry Logic**: Exponential backoff for API calls ensures reliability

## 🎯 Supported Career Paths

Pre-configured with curated data for:
- **SOC Analyst** - Security Operations Center
- **IT Help Desk** - Technical Support  
- **Network Technician** - Network Infrastructure
- **Cybersecurity Analyst** - Information Security
- **Cloud Support Associate** - Cloud Computing
- **Software Developer** - Software Development

**Plus**: Works with any career goal you enter - AI generates custom roadmaps even for paths not in the database.
>>>>>>> REPLACE
</diff>
</apply_diff>

---

**User:**

[apply_diff for 'README.md'] Result:
<file_write_result>
<path>README.md</path>
<operation>modified</operation>
<notice>
<i>You do not need to re-read the file, as you have seen all changes</i>
<i>Proceed with the task using these changes as the new baseline.</i>
</notice>
</file_write_result>

<notice>Making multiple related changes in a single apply_diff is more efficient. If other changes are needed in this file, please include them as additional SEARCH/REPLACE blocks.</notice>
<environment_details>
# VSCode Visible Files
README.md

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,server/.env,server/main.py,README.md,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Recently Modified Files
These files have been modified since you last accessed them (file was just edited so you may need to re-read it before editing):
README.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:15:18.024Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$0.92

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Read project files (package.json, requirements.txt, .env.example, main.py) | Completed |
| 2 | Read frontend files (App.jsx, pages, api.js) | Completed |
| 3 | Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py) | Completed |
| 4 | Read current README.md | Completed |
| 5 | Analyze actual features implemented | Completed |
| 6 | Update README with accurate information | In Progress |
| 7 | Verify no API keys or sensitive data exposed | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

<apply_diff>
<path>README.md</path>
<diff>
<<<<<<< SEARCH
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
=======
## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework with automatic API documentation
- **IBM watsonx.ai** - AI-powered roadmap generation using Granite 3-8B Instruct model
- **Python 3.8+** - Core language
- **httpx** - Async HTTP client for API calls
- **Pydantic** - Data validation and schemas

### Frontend
- **React 19** - UI framework
- **Vite 8** - Lightning-fast build tool
- **TailwindCSS 4** - Utility-first CSS framework
- **React Router 6** - Client-side routing
- **Axios** - HTTP client for API communication
- **LocalStorage** - Client-side pathway persistence

### APIs Integrated
- **IBM watsonx.ai** - AI roadmap generation (Granite models)
- **GitHub REST API** - Project discovery with quality filtering
- **USAJOBS API** - Live federal job postings with smart location fallback
- **O*NET Web Services** - Official occupation data (optional)
>>>>>>> REPLACE
</diff>
</apply_diff>

---

**User:**

[apply_diff for 'README.md'] Result:
<file_write_result>
<path>README.md</path>
<operation>modified</operation>
<notice>
<i>You do not need to re-read the file, as you have seen all changes</i>
<i>Proceed with the task using these changes as the new baseline.</i>
</notice>
</file_write_result>

<notice>Making multiple related changes in a single apply_diff is more efficient. If other changes are needed in this file, please include them as additional SEARCH/REPLACE blocks.</notice>
<environment_details>
# VSCode Visible Files
README.md

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,server/.env,server/main.py,README.md,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:15:27.342Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$1.14

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Read project files (package.json, requirements.txt, .env.example, main.py) | Completed |
| 2 | Read frontend files (App.jsx, pages, api.js) | Completed |
| 3 | Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py) | Completed |
| 4 | Read current README.md | Completed |
| 5 | Analyze actual features implemented | Completed |
| 6 | Update README with accurate information | In Progress |
| 7 | Verify no API keys or sensitive data exposed | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

<apply_diff>
<path>README.md</path>
<diff>
<<<<<<< SEARCH
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
=======
### 3. Configure Environment Variables

Edit `server/.env` and add your API credentials:

```env
# IBM watsonx.ai Configuration (REQUIRED for AI roadmap generation)
WATSONX_API_KEY=your_ibm_cloud_api_key_here
WATSONX_PROJECT_ID=your_watsonx_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-3-8b-instruct

# GitHub API Configuration (OPTIONAL - for higher rate limits)
# Without token: 60 requests/hour. With token: 5000 requests/hour
GITHUB_TOKEN=ghp_your_github_personal_access_token_here

# O*NET Web Services API Configuration (OPTIONAL)
ONET_API_KEY=your_onet_api_key_here

# USAJOBS API Configuration (OPTIONAL)
USAJOBS_EMAIL=your_email@example.com
USAJOBS_API_KEY=your_usajobs_api_key_here

# Server Configuration
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
ENVIRONMENT=development
```

#### Getting API Keys:

**IBM watsonx.ai** (Required for AI features):
1. Create an account at [IBM Cloud](https://cloud.ibm.com/)
2. Create a watsonx.ai project in your IBM Cloud account
3. Get your **API key** from IBM Cloud IAM (Identity and Access Management)
4. Copy your **Project ID** from the watsonx.ai project settings
5. The default model is `ibm/granite-3-8b-instruct` (can be changed in .env)

**GitHub Token** (Optional but recommended):
1. Go to [GitHub Settings > Developer Settings > Personal Access Tokens](https://github.com/settings/tokens)
2. Generate a new token (classic)
3. **No special scopes needed** for public repository search
4. Increases rate limit from 60 to 5000 requests/hour

**O*NET API** (Optional - for occupation data):
1. Register at [O*NET Web Services](https://services.onetcenter.org/)
2. Request an API key from your account dashboard
3. Used for official occupation skills and task data

**USAJOBS API** (Optional - for federal job listings):
1. Register at [USAJOBS Developer Portal](https://developer.usajobs.gov/)
2. Get your API key and authorization email
3. Provides live federal job postings with location-based search
>>>>>>> REPLACE
</diff>
</apply_diff>

---

**User:**

[apply_diff for 'README.md'] Result:
<file_write_result>
<path>README.md</path>
<operation>modified</operation>
<notice>
<i>You do not need to re-read the file, as you have seen all changes</i>
<i>Proceed with the task using these changes as the new baseline.</i>
</notice>
</file_write_result>

<notice>Making multiple related changes in a single apply_diff is more efficient. If other changes are needed in this file, please include them as additional SEARCH/REPLACE blocks.</notice>
<environment_details>
# VSCode Visible Files
README.md

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,server/.env,server/main.py,README.md,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:15:44.399Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$1.37

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Read project files (package.json, requirements.txt, .env.example, main.py) | Completed |
| 2 | Read frontend files (App.jsx, pages, api.js) | Completed |
| 3 | Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py) | Completed |
| 4 | Read current README.md | Completed |
| 5 | Analyze actual features implemented | Completed |
| 6 | Update README with accurate information | In Progress |
| 7 | Verify no API keys or sensitive data exposed | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

<apply_diff>
<path>README.md</path>
<diff>
<<<<<<< SEARCH
## 🎨 Key Endpoints

### AI Roadmap Generation
- **POST** `/api/generate-roadmap` - Generate AI-powered career roadmap

### Legacy Endpoints
- **POST** `/api/pathways/generate` - Generate sample pathway (mock data)
- **POST** `/api/pathways/adapt` - Adapt existing pathway
- **GET** `/api/github/projects/{skill}` - Search GitHub projects
- **GET** `/api/usajobs/search` - Search federal jobs
- **POST** `/api/recommendations` - Get career recommendations
=======
## 🎨 API Endpoints

### Core Endpoints
- **POST** `/api/generate-roadmap` - Generate AI-powered career roadmap using watsonx.ai
  - Request: `{ careerGoal, currentSkills, timeframe, weeks }`
  - Returns: Complete roadmap with phases, weekly plans, resources, GitHub projects
  
- **POST** `/api/pathways/adapt` - Adapt existing pathway based on user feedback
  - Request: `{ pathway, feedback }`
  - Returns: Modified pathway with adaptation history

### Resource Discovery
- **GET** `/api/usajobs/search?keyword={keyword}&location={location}` - Search federal jobs
  - Smart fallback: city → state → nationwide
  - Returns: Job listings with salary, location, and application links

- **GET** `/api/onet/search?keyword={keyword}` - Search O*NET occupations (optional)
  - Returns: Official occupation data with skills and tasks

### Health Check
- **GET** `/` - API health check
- **GET** `/health` - Alternative health endpoint
- **GET** `/docs` - Interactive API documentation (Swagger UI)
>>>>>>> REPLACE
</diff>
</apply_diff>

---

**User:**

[apply_diff for 'README.md'] Result:
<file_write_result>
<path>README.md</path>
<operation>modified</operation>
<notice>
<i>You do not need to re-read the file, as you have seen all changes</i>
<i>Proceed with the task using these changes as the new baseline.</i>
</notice>
</file_write_result>

<notice>Making multiple related changes in a single apply_diff is more efficient. If other changes are needed in this file, please include them as additional SEARCH/REPLACE blocks.</notice>
<environment_details>
# VSCode Visible Files
README.md

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,server/.env,server/main.py,README.md,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:15:54.777Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$1.60

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Read project files (package.json, requirements.txt, .env.example, main.py) | Completed |
| 2 | Read frontend files (App.jsx, pages, api.js) | Completed |
| 3 | Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py) | Completed |
| 4 | Read current README.md | Completed |
| 5 | Analyze actual features implemented | Completed |
| 6 | Update README with accurate information | In Progress |
| 7 | Verify no API keys or sensitive data exposed | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

<apply_diff>
<path>README.md</path>
<diff>
<<<<<<< SEARCH
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
=======
## 🐛 Troubleshooting

### Backend Issues

**Backend won't start:**
- Ensure Python 3.8+ is installed: `python --version`
- Activate virtual environment: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Mac/Linux)
- Install dependencies: `pip install -r requirements.txt`
- Check `.env` file exists in `server/` directory with required variables

**AI Roadmap Generation Fails:**
- Verify `WATSONX_API_KEY` and `WATSONX_PROJECT_ID` are set correctly in `.env`
- Check IBM Cloud IAM authentication in backend logs
- Review backend console for detailed error messages
- **Fallback behavior**: System automatically uses template-based roadmap if watsonx.ai is unavailable

**USAJOBS Search Fails:**
- Verify `USAJOBS_EMAIL` and `USAJOBS_API_KEY` are set
- Check backend logs for authentication errors (401/403)
- **Fallback behavior**: System shows error message but app continues to work

### Frontend Issues

**Frontend won't start:**
- Ensure Node.js 16+ is installed: `node --version`
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Check if port 5173 is available (Vite default)
- Verify backend is running at `http://localhost:8000`

**Pathway not displaying:**
- Check browser console for errors
- Verify localStorage has `generatedPathway` key
- Clear localStorage and regenerate pathway
- Check backend returned valid JSON response

### API Issues

**GitHub API Rate Limit:**
- **Without token**: 60 requests/hour (unauthenticated)
- **With token**: 5000 requests/hour (authenticated)
- Add `GITHUB_TOKEN` to `.env` for higher limits
- **Fallback behavior**: System uses verified local projects when rate limited

**Watsonx Token Limit:**
- Current limit: 6000 tokens for roadmap generation
- For 12+ week roadmaps, system uses multi-call strategy
- Check logs for "RESPONSE APPEARS TRUNCATED" warnings
- **Fallback behavior**: System attempts JSON completion or uses template

### Known Limitations

1. **Watsonx.ai Required**: AI features require valid IBM Cloud credentials
2. **GitHub Rate Limits**: Unauthenticated requests limited to 60/hour
3. **USAJOBS Location**: Some locations may have no results (fallback to nationwide)
4. **Browser Storage**: Pathways stored in localStorage (cleared if browser data is cleared)
>>>>>>> REPLACE
</diff>
</apply_diff>

---

**User:**

[apply_diff for 'README.md'] Result:
<file_write_result>
<path>README.md</path>
<operation>modified</operation>
<notice>
<i>You do not need to re-read the file, as you have seen all changes</i>
<i>Proceed with the task using these changes as the new baseline.</i>
</notice>
</file_write_result>

<notice>Making multiple related changes in a single apply_diff is more efficient. If other changes are needed in this file, please include them as additional SEARCH/REPLACE blocks.</notice>
<environment_details>
# VSCode Visible Files
README.md

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,server/.env,server/main.py,README.md,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:16:17.440Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$1.84

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Read project files (package.json, requirements.txt, .env.example, main.py) | Completed |
| 2 | Read frontend files (App.jsx, pages, api.js) | Completed |
| 3 | Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py) | Completed |
| 4 | Read current README.md | Completed |
| 5 | Analyze actual features implemented | Completed |
| 6 | Update README with accurate information | In Progress |
| 7 | Verify no API keys or sensitive data exposed | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

<apply_diff>
<path>README.md</path>
<diff>
<<<<<<< SEARCH
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
=======
## 🔒 Security & Privacy

### API Key Security
- **Never commit `.env` files** - All secrets stored in environment variables
- **Backend-only API calls** - Frontend never directly calls watsonx.ai, GitHub, or USAJOBS
- **Error sanitization** - Error messages are sanitized to prevent credential leaks
- **CORS protection** - Configured to only allow requests from frontend origin

### Data Privacy
- **No user data stored** - Pathways stored only in browser localStorage
- **No tracking** - No analytics or user tracking implemented
- **API keys masked** - Logs show masked versions of API keys (first 8 + last 4 chars)

## 🚀 How It Works

### Roadmap Generation Flow

1. **User Input**: User enters career goal, timeframe, and preferences in the frontend form
2. **API Request**: Frontend sends request to `/api/generate-roadmap` endpoint
3. **Data Matching**: Backend matches career goal to curated resources and certifications
4. **GitHub Search**: Backend searches GitHub for relevant beginner projects (with retry logic)
5. **AI Generation**: Backend calls IBM watsonx.ai with structured prompt including:
   - Career goal and timeframe
   - Matched resources and GitHub projects
   - Required JSON structure
6. **Response Processing**: Backend validates and normalizes AI response
7. **Enforcement**: Backend enforces timeframe, resource allocation, and data quality
8. **Frontend Transform**: Frontend transforms backend response to UI format
9. **Display**: User sees personalized week-by-week roadmap with resources and projects

### Fallback Behavior

**When APIs Fail:**
- **Watsonx.ai fails**: Uses template-based roadmap with curated data
- **GitHub fails**: Uses verified local project database
- **USAJOBS fails**: Shows error but app continues working
- **Resource URLs broken**: Backend validates and replaces with verified alternatives

**Smart Fallbacks:**
- USAJOBS: city → state → nationwide search
- Resources: Minimum 5 resources guaranteed via verified database
- GitHub: Quality filtering (50+ stars) with local project fallback

## 📝 Development Notes

### Adding New Career Roles

1. Add role definition to `server/data/roles.json` with:
   - Core skills, tools, certifications
   - Beginner keywords for matching
2. Add resources to `server/data/resources.json` for each skill
3. Add projects to `server/data/projects.json`
4. Add certifications to `server/data/certifications.json`
5. Run `python server/validate_data.py` to verify data integrity

### Customizing AI Behavior

**Change AI Model:**
Edit `WATSONX_MODEL_ID` in `.env`:
- `ibm/granite-3-8b-instruct` (default, fast)
- `ibm/granite-13b-chat-v2` (more capable)
- `ibm/granite-20b-multilingual` (multilingual support)

**Adjust Token Limits:**
Edit `max_tokens` in `server/services/watsonx_service.py`:
- Current: 6000 tokens
- Increase for longer roadmaps (may increase cost)

**Modify Prompts:**
Edit prompts in `server/services/watsonx_service.py` → `generate_career_roadmap` method

### Testing

Run validation scripts:
```bash
cd server
python validate_data.py              # Validate all data files
python test_api_endpoints.py         # Test API endpoints
python test_career_paths.py          # Test all career paths
```
>>>>>>> REPLACE
</diff>
</apply_diff>

---

**User:**

[apply_diff for 'README.md'] Result:
<file_write_result>
<path>README.md</path>
<operation>modified</operation>
<notice>
<i>You do not need to re-read the file, as you have seen all changes</i>
<i>Proceed with the task using these changes as the new baseline.</i>
</notice>
</file_write_result>

<notice>Making multiple related changes in a single apply_diff is more efficient. If other changes are needed in this file, please include them as additional SEARCH/REPLACE blocks.</notice>
<environment_details>
# VSCode Visible Files
README.md

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,server/.env,server/main.py,README.md,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:16:38.733Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$2.08

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Read project files (package.json, requirements.txt, .env.example, main.py) | Completed |
| 2 | Read frontend files (App.jsx, pages, api.js) | Completed |
| 3 | Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py) | Completed |
| 4 | Read current README.md | Completed |
| 5 | Analyze actual features implemented | Completed |
| 6 | Update README with accurate information | In Progress |
| 7 | Verify no API keys or sensitive data exposed | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

<apply_diff>
<path>README.md</path>
<diff>
<<<<<<< SEARCH
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
=======
## 🎯 Future Improvements

Potential enhancements for future versions:

- **User Accounts**: Save multiple pathways and track progress across devices
- **Social Features**: Share pathways, collaborate with peers
- **Advanced Analytics**: Track learning velocity, suggest pace adjustments
- **Mobile App**: Native iOS/Android apps for on-the-go learning
- **More APIs**: LinkedIn Learning, Coursera, Udemy integrations
- **AI Mentorship**: Chat with AI mentor for personalized guidance
- **Certification Tracking**: Track certification progress and deadlines
- **Job Application Tracking**: Integrate with job application workflow

## 🤝 Contributing

This project was built for the IBM Hackathon. Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- **IBM watsonx.ai** - AI-powered roadmap generation using Granite models
- **GitHub** - Project discovery and version control
- **USAJOBS** - Federal job listings API
- **O*NET** - Official occupation data
- **IBM SkillsBuild** - Curated learning resources
- **FastAPI** - Modern Python web framework
- **React & Vite** - Frontend framework and build tool

## 📧 Support

For issues or questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review backend logs for detailed error messages

---

**Built with ❤️ for the IBM Hackathon**  
**Powered by IBM watsonx.ai Granite Models**
>>>>>>> REPLACE
</diff>
</apply_diff>

---

**User:**

[apply_diff for 'README.md'] Result:
<file_write_result>
<path>README.md</path>
<operation>modified</operation>
<notice>
<i>You do not need to re-read the file, as you have seen all changes</i>
<i>Proceed with the task using these changes as the new baseline.</i>
</notice>
</file_write_result>

<notice>Making multiple related changes in a single apply_diff is more efficient. If other changes are needed in this file, please include them as additional SEARCH/REPLACE blocks.</notice>
<environment_details>
# VSCode Visible Files
README.md

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,server/.env,server/main.py,README.md,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:16:51.774Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$2.32

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Read project files (package.json, requirements.txt, .env.example, main.py) | Completed |
| 2 | Read frontend files (App.jsx, pages, api.js) | Completed |
| 3 | Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py) | Completed |
| 4 | Read current README.md | Completed |
| 5 | Analyze actual features implemented | Completed |
| 6 | Update README with accurate information | In Progress |
| 7 | Verify no API keys or sensitive data exposed | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

<update_todo_list>
<todos>
[x] Read project files (package.json, requirements.txt, .env.example, main.py)
[x] Read frontend files (App.jsx, pages, api.js)
[x] Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py)
[x] Read current README.md
[x] Analyze actual features implemented
[x] Update README with accurate information
[-] Verify no API keys or sensitive data exposed
</todos>
</update_todo_list>

---

**User:**

[update_todo_list] Result:
The user denied this operation.
[update_todo_list] Result:
User declined to update the todoList.
<environment_details>
# VSCode Visible Files
README.md

# VSCode Open Tabs
server/services/github_service.py,server/routes/github_projects.py,docs/bob-architecture-notes.md,server/services/usajobs_service.py,server/routes/usajobs.py,client/src/components/JobCard.jsx,client/src/pages/PathwayPage.jsx,server/.env.example,server/data/roles.json,server/data/certifications.json,server/routes/roadmap.py,client/src/utils/api.js,server/.env,server/main.py,README.md,server/test_watsonx_models.py,server/services/watsonx_service.py,test_roadmap.json,test_api.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-17T00:17:01.296Z
User time zone: America/New_York, UTC-4:00

# Current Cost
$2.57

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Read project files (package.json, requirements.txt, .env.example, main.py) | Completed |
| 2 | Read frontend files (App.jsx, pages, api.js) | Completed |
| 3 | Read backend routes and services (roadmap.py, watsonx_service.py, github_service.py, usajobs.py) | Completed |
| 4 | Read current README.md | Completed |
| 5 | Analyze actual features implemented | Completed |
| 6 | Update README with accurate information | In Progress |
| 7 | Verify no API keys or sensitive data exposed | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

