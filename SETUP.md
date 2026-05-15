# PathPilot AI - Complete Setup Guide

Quick setup guide for the PathPilot AI hackathon project.

## 📋 Prerequisites

- **Node.js** (v18 or higher) - [Download](https://nodejs.org/)
- **Python** (v3.9 or higher) - [Download](https://www.python.org/)
- **Git** - [Download](https://git-scm.com/)

## 🚀 Quick Start (5 Minutes)

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd PathPilot-AI
```

### Step 2: Set Up Backend (FastAPI)

```bash
# Navigate to server directory
cd server

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the backend server
python main.py
```

**Backend will run at:** http://localhost:8000

**API Docs:** http://localhost:8000/docs

### Step 3: Set Up Frontend (React)

Open a **new terminal** (keep the backend running):

```bash
# Navigate to client directory
cd client

# Install dependencies
npm install

# Run the development server
npm run dev
```

**Frontend will run at:** http://localhost:5173

### Step 4: Test the Application

1. Open http://localhost:5173 in your browser
2. Click "Generate My Pathway"
3. Fill out the form
4. Submit and view your generated pathway!

## 📁 Project Structure

```
PathPilot-AI/
├── client/                 # React frontend
│   ├── src/
│   │   ├── components/     # UI components
│   │   ├── pages/          # Page components
│   │   ├── utils/          # Utilities (API, localStorage)
│   │   ├── App.jsx         # Main app with routing
│   │   └── main.jsx        # Entry point
│   └── package.json
│
├── server/                 # FastAPI backend
│   ├── models/             # Pydantic schemas
│   ├── routes/             # API endpoints
│   ├── services/           # Business logic
│   ├── main.py             # FastAPI app
│   └── requirements.txt
│
├── docs/                   # Documentation
├── README.md               # Project overview
└── SETUP.md               # This file
```

## 🔧 Detailed Setup Instructions

### Backend Setup (Windows)

```powershell
# Navigate to server directory
cd server

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verify installation
pip list

# Run the server
python main.py
```

### Backend Setup (macOS/Linux)

```bash
# Navigate to server directory
cd server

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verify installation
pip list

# Run the server
python main.py
```

### Frontend Setup

```bash
# Navigate to client directory
cd client

# Install dependencies
npm install

# Verify installation
npm list --depth=0

# Run development server
npm run dev
```

## 🧪 Testing the Setup

### Test Backend

1. **Health Check:**
   ```bash
   curl http://localhost:8000/
   ```
   Expected: `{"status":"healthy","message":"PathPilot AI API is running! Visit /docs for API documentation."}`

2. **Interactive API Docs:**
   Open http://localhost:8000/docs in your browser

3. **Generate Pathway:**
   ```bash
   curl -X POST http://localhost:8000/api/pathways/generate \
     -H "Content-Type: application/json" \
     -d @server/test_request.json
   ```

### Test Frontend

1. Open http://localhost:5173
2. You should see the PathPilot AI landing page
3. Click "Generate My Pathway"
4. Fill out the form and submit
5. View your generated pathway

## 🐛 Troubleshooting

### Backend Issues

**Problem:** `python: command not found`
- **Solution:** Use `python3` instead of `python`

**Problem:** `pip: command not found`
- **Solution:** Use `python -m pip` instead of `pip`

**Problem:** Port 8000 already in use
- **Solution:** Change port in `server/main.py` or kill the process using port 8000

**Problem:** Import errors (fastapi, pydantic not found)
- **Solution:** Make sure virtual environment is activated and dependencies are installed

**Problem:** CORS errors
- **Solution:** Check that frontend URL is in CORS origins in `server/main.py`

### Frontend Issues

**Problem:** `npm: command not found`
- **Solution:** Install Node.js from https://nodejs.org/

**Problem:** Port 5173 already in use
- **Solution:** Vite will automatically use the next available port (5174, 5175, etc.)

**Problem:** Cannot connect to backend
- **Solution:** 
  - Make sure backend is running at http://localhost:8000
  - Check `client/src/utils/api.js` for correct API URL
  - Verify CORS is configured in backend

**Problem:** Blank page or errors in console
- **Solution:**
  - Check browser console for errors
  - Make sure all dependencies are installed (`npm install`)
  - Try clearing browser cache
  - Restart the dev server

### VS Code Python Interpreter Issues

**Problem:** Import errors in VS Code (red squiggly lines)
- **Solution:**
  1. Press `Ctrl + Shift + P` (Windows) or `Cmd + Shift + P` (Mac)
  2. Type "Python: Select Interpreter"
  3. Select the interpreter from `server/venv/Scripts/python.exe` (Windows) or `server/venv/bin/python` (Mac/Linux)

## 📝 Development Workflow

### Starting Development

```bash
# Terminal 1 - Backend
cd server
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
python main.py

# Terminal 2 - Frontend
cd client
npm run dev
```

### Making Changes

- **Backend changes:** Server auto-reloads (if using `uvicorn --reload`)
- **Frontend changes:** Vite hot-reloads automatically

### Stopping Servers

- Press `Ctrl + C` in each terminal

## 🎯 Next Steps

1. ✅ Backend running at http://localhost:8000
2. ✅ Frontend running at http://localhost:5173
3. ✅ Test pathway generation
4. 🔄 Integrate IBM Bob AI (replace mock data in `server/services/pathway_generator.py`)
5. 🔄 Connect MongoDB Atlas (when ready)
6. 🔄 Deploy to production

## 📚 Additional Resources

- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **React Docs:** https://react.dev/
- **Vite Docs:** https://vitejs.dev/
- **Tailwind CSS:** https://tailwindcss.com/

## 🆘 Getting Help

If you encounter issues:

1. Check the error message carefully
2. Look in the troubleshooting section above
3. Check browser console (F12) for frontend errors
4. Check terminal output for backend errors
5. Verify all dependencies are installed
6. Make sure both servers are running

## 🎉 Success Checklist

- [ ] Backend running at http://localhost:8000
- [ ] Frontend running at http://localhost:5173
- [ ] Can access API docs at http://localhost:8000/docs
- [ ] Can see landing page at http://localhost:5173
- [ ] Can navigate to /generate page
- [ ] Can fill out and submit the form
- [ ] Can see generated pathway at /pathway page
- [ ] No errors in browser console
- [ ] No errors in terminal

If all checkboxes are checked, you're ready to develop! 🚀