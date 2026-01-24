import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_ollama_chat():
    """Test the Ollama-powered chat endpoint in the backend."""
    
    # URL of your local backend chat endpoint
    # Adjust port if your backend runs on a different one (default 8000)
    url = "http://localhost:8000/chat"
    
    # Sample question
    payload = {
        "message": "What is the best soil for growing bananas?"
    }
    
    logger.info(f"Sending request to {url} with payload: {payload}")
    
    try:
        response = requests.post(url, json=payload)
        
        logger.info(f"Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            logger.info("Response Data:")
            logger.info(json.dumps(data, indent=2))
            
            if "response" in data:
                print("\n[SUCCESS] Chatbot replied successfully!")
                print(f"Bot Response: {data['response']}")
            else:
                print("\n[WARNING] Response received but 'response' key missing.")
        else:
            print(f"\n[ERROR] Request failed with status code {response.status_code}")
            print(f"Error details: {response.text}")
            
    except Exception as e:
        print(f"\n[EXCEPTION] connection failed: {e}")
        print("Make sure the backend is running (python main.py)")

if __name__ == "__main__":
    test_ollama_chat()
