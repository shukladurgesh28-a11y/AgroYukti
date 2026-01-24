import requests
import json

url = "http://localhost:8000/chat"
payload = {"message": "Hello, this is a test from the debugger."}
headers = {"Content-Type": "application/json"}

try:
    print(f"Testing {url}...")
    response = requests.post(url, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:500]}")
    
    if response.status_code == 200:
        print("SUCCESS: Chat endpoint is working.")
    else:
        print("FAILURE: Chat endpoint returned error.")
        
except Exception as e:
    print(f"ERROR: Failed to connect. {e}")
