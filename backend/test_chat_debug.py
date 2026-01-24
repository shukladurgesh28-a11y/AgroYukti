import requests
import json
import time

# Wait for server to potentially restart if run manually, but here we just hit the endpoint
print("Testing AgriBot Persona...")

question = "What is the best soil for growing Cotton?"

try:
    response = requests.post(
        "http://localhost:8000/chat",
        headers={"Content-Type": "application/json"},
        json={"message": question}
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print("Response received:")
        print(response.json()['response'])
    else:
        print(f"Error: {response.text}")

except Exception as e:
    print(f"Connection Error: {e}")
