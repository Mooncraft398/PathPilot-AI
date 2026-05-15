# PathPilot AI - Backend API

FastAPI backend for the PathPilot AI career pathway generator.

## 🚀 Quick Start

### 1. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Server

```bash
# From the server directory
python main.py

# Or use uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## 📁 Project Structure

```
server/
├── main.py                 # FastAPI app entry point
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── models/                # Pydantic models
│   ├── __init__.py
│   └── schemas.py         # Request/response schemas
├── routes/                # API endpoints
│   ├── __init__.py
│   └── pathways.py        # Pathway generation routes
└── services/              # Business logic
    ├── __init__.py
    └── pathway_generator.py  # Pathway generation logic
```

## 🔌 API Endpoints

### Health Check
- **GET** `/` - API health check
- **GET** `/health` - Alternative health check

### Pathways
- **POST** `/api/pathways/generate` - Generate a career pathway

## 📝 Example Request

### Generate Pathway

**Endpoint**: `POST http://localhost:8000/api/pathways/generate`

**Request Body**:
```json
{
  "goal": "Junior Web Developer",
  "level": "beginner",
  "weeks": 6,
  "daysPerWeek": 5,
  "hoursPerDay": 2,
  "preferences": ["projects", "videos"],
  "budget": "free-first"
}
```

**Response**: Returns a structured pathway with:
- Weekly learning plans
- Daily schedules
- Learning resources
- Guided projects
- Resume bullets
- Certifications

## 🧪 Testing with cURL

```bash
# Health check
curl http://localhost:8000/

# Generate pathway
curl -X POST http://localhost:8000/api/pathways/generate \
  -H "Content-Type: application/json" \
  -d "{\"goal\":\"Junior Web Developer\",\"level\":\"beginner\",\"weeks\":6,\"daysPerWeek\":5,\"hoursPerDay\":2,\"preferences\":[\"projects\",\"videos\"],\"budget\":\"free-first\"}"
```

## 🧪 Testing with Python

```python
import requests

# Health check
response = requests.get("http://localhost:8000/")
print(response.json())

# Generate pathway
payload = {
    "goal": "Junior Web Developer",
    "level": "beginner",
    "weeks": 6,
    "daysPerWeek": 5,
    "hoursPerDay": 2,
    "preferences": ["projects", "videos"],
    "budget": "free-first"
}

response = requests.post(
    "http://localhost:8000/api/pathways/generate",
    json=payload
)
print(response.json())
```

## 🔧 Configuration

Copy `.env.example` to `.env` and configure as needed:

```bash
cp .env.example .env
```

## 📦 Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI
- **Pydantic**: Data validation using Python type hints
- **python-dotenv**: Environment variable management

## 🚧 Future Enhancements

- [ ] IBM Bob AI integration
- [ ] MongoDB Atlas connection
- [ ] User authentication
- [ ] Progress tracking
- [ ] Resume generation
- [ ] Email notifications

## 🐛 Troubleshooting

### Port Already in Use
If port 8000 is already in use, change the port:
```bash
uvicorn main:app --reload --port 8001
```

### Import Errors
Make sure you're in the server directory and virtual environment is activated:
```bash
cd server
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### CORS Issues
The API is configured to accept requests from:
- http://localhost:5173 (Vite default)
- http://localhost:3000 (React alternative)

If your frontend runs on a different port, update the CORS settings in `main.py`.

## 📚 Documentation

Visit http://localhost:8000/docs for interactive API documentation powered by Swagger UI.