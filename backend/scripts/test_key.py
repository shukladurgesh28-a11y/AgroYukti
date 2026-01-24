import requests
import os

API_KEY = "AIzaSyAi1Awxm-EZul1iwpAUUNBicepEAsPXb5s"
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

try:
    print(f"Testing API Key with ListModels...")
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Success! Key is valid.")
        models = response.json().get('models', [])
        print(f"Found {len(models)} models.")
        for m in models:
            if 'generateContent' in m.get('supportedGenerationMethods', []):
                print(f"- {m['name']}")
    else:
        print("Failed.")
        print("Response:", response.text)
except Exception as e:
    print(f"Error: {e}")
