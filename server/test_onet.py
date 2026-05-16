"""
Quick test script for O*NET API integration
"""
import httpx
import asyncio


async def test_onet_debug():
    """Test the O*NET debug endpoint"""
    print("Testing O*NET debug endpoint...")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('http://localhost:8000/api/onet/debug')
            print(f"\nStatus Code: {response.status_code}")
            print(f"Response: {response.json()}")
            
    except httpx.ConnectError:
        print("\nError: Could not connect to server. Make sure the server is running on port 8000.")
        print("Start the server with: uvicorn main:app --reload")
    except Exception as e:
        print(f"\nError: {e}")


async def test_onet_search():
    """Test the O*NET search endpoint"""
    print("\n\nTesting O*NET search endpoint...")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('http://localhost:8000/api/onet/search?keyword=software')
            print(f"\nStatus Code: {response.status_code}")
            
            try:
                result = response.json()
                print(f"Response: {result}")
                print(f"\nSuccess: {result.get('success')}")
                print(f"Upstream Status: {result.get('upstreamStatus')}")
                print(f"Count: {result.get('count')}")
                if result.get('occupations'):
                    print(f"First occupation: {result['occupations'][0].get('title', 'N/A')}")
            except Exception as e:
                print(f"Could not parse response: {e}")
                print(f"Raw response: {response.text[:500]}")
            
    except httpx.ConnectError:
        print("\nError: Could not connect to server.")
    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    asyncio.run(test_onet_debug())
    asyncio.run(test_onet_search())

# Made with Bob
