# O*NET API Testing Guide

## Prerequisites

1. **Set up your API key** in `server/.env`:
   ```bash
   ONET_API_KEY=your_actual_api_key_here
   ```

2. **Install dependencies** (if not already done):
   ```bash
   cd server
   pip install -r requirements.txt
   ```

## Method 1: Using the Test Script (Recommended)

1. **Start the FastAPI server** in one terminal:
   ```bash
   cd server
   uvicorn main:app --reload
   ```

2. **Run the test script** in another terminal:
   ```bash
   cd server
   python test_onet.py
   ```

   This will test both:
   - `/api/onet/debug` - Connection test
   - `/api/onet/search?keyword=software` - Search test

## Method 2: Using cURL

1. **Start the server**:
   ```bash
   cd server
   uvicorn main:app --reload
   ```

2. **Test the debug endpoint**:
   ```bash
   curl http://localhost:8000/api/onet/debug
   ```

3. **Test the search endpoint**:
   ```bash
   curl "http://localhost:8000/api/onet/search?keyword=cybersecurity"
   ```

## Method 3: Using Browser

1. **Start the server**:
   ```bash
   cd server
   uvicorn main:app --reload
   ```

2. **Open in browser**:
   - Debug: http://localhost:8000/api/onet/debug
   - Search: http://localhost:8000/api/onet/search?keyword=cybersecurity

3. **View API docs** (interactive testing):
   - http://localhost:8000/docs

## Method 4: Using Python Requests

```python
import requests

# Test debug endpoint
response = requests.get('http://localhost:8000/api/onet/debug')
print(response.json())

# Test search endpoint
response = requests.get('http://localhost:8000/api/onet/search', params={'keyword': 'cybersecurity'})
print(response.json())
```

## Expected Successful Response

### Debug Endpoint
```json
{
  "success": true,
  "upstreamStatus": 200,
  "keyLoaded": true,
  "responsePreview": {
    "api_version": "2.0",
    "api_title": "O*NET Web Services"
  }
}
```

### Search Endpoint
```json
{
  "success": true,
  "keyword": "cybersecurity",
  "upstreamStatus": 200,
  "rawTotal": 50,
  "count": 10,
  "occupations": [
    {
      "title": "Information Security Analysts",
      "code": "15-1212.00",
      "href": "/ws/online/occupations/15-1212.00",
      "brightOutlook": true
    }
  ]
}
```

## Checking Logs

The server will log detailed information:

```
INFO:     O*NET SEARCH REQUEST
INFO:     Upstream URL: https://api-v2.onetcenter.org/online/search
INFO:     Search params: {'keyword': 'cybersecurity', 'start': 1, 'end': 10}
INFO:     ONET_API_KEY exists: True
INFO:     Upstream status code: 200
INFO:     Response body (first 300 chars): {"occupation":[{"code":"15-1212.00","title":"Information Security Analysts"...
```

## Troubleshooting

### Error: "O*NET API key not found"
- Check that `ONET_API_KEY` is set in `server/.env`
- Restart the server after adding the key

### Error: "Could not connect to server"
- Make sure the server is running: `uvicorn main:app --reload`
- Check that port 8000 is not in use

### Error: 401 Unauthorized
- Your API key is invalid or expired
- Get a new key at: https://services.onetcenter.org/

### Error: 404 Not Found
- This should be fixed now (we updated to v2 API)
- Check logs to see the exact URL being called

## Quick Test Commands

```bash
# Terminal 1: Start server
cd server && uvicorn main:app --reload

# Terminal 2: Run tests
cd server && python test_onet.py

# Or test with curl
curl "http://localhost:8000/api/onet/search?keyword=software"