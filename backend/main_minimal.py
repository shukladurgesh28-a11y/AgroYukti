"""
AgriYuti Backend API - Minimal Version
This version starts without loading any models to ensure deployment success
"""
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="AgriYuti API", version="1.0.0")

# ✅ CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://superb-patience-production.up.railway.app",
        "http://localhost:5173",
        "http://localhost:3000",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root endpoint
@app.get("/")
def root():
    return {"message": "AgriYuti API is running", "status": "healthy", "version": "1.0.0"}

# ✅ Health check routes
@app.get("/health")
def health_check():
    return {"status": "API is running"}

@app.get("/healthz")
def health_check_detailed():
    return {"status": "healthy", "message": "AgriYuti API is running"}

# ✅ Model status endpoint
@app.get("/models/status")
def model_status():
    return {
        "soil_model": "not_loaded",
        "plant_disease_model": "not_loaded", 
        "price_prediction_model": "not_loaded",
        "message": "Models will be loaded on first use"
    }

# ✅ Placeholder endpoints that return appropriate messages
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    return {
        "message": "Plant disease prediction service is temporarily unavailable",
        "class": "Service unavailable",
        "confidence": 0.0,
        "status": "UNAVAILABLE"
    }

@app.get("/market-predictions")
def get_predictions_for_graph():
    return {
        "status": "unavailable",
        "message": "Market prediction service is temporarily unavailable",
        "data": []
    }

@app.post("/predict-soil")
async def predict_soil(file: UploadFile = File(...)):
    return {
        "message": "Soil prediction service is temporarily unavailable",
        "prediction": "Service unavailable",
        "confidence": 0.0,
        "notes": "Service is temporarily unavailable",
        "crops": [],
        "care": []
    }

# ✅ Chatbot Endpoint
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # Load knowledge base
        try:
            with open(os.path.join(os.path.dirname(__file__), "data", "knowledge_base.json"), "r") as f:
                kb_data = f.read()
        except Exception as e:
            logger.warning(f"Failed to load knowledge base: {e}")
            kb_data = "Basic agricultural knowledge available."

        # Hardcoding the known valid key (Note: In production, use env vars)
        API_KEY = "AIzaSyAi1Awxm-EZul1iwpAUUNBicepEAsPXb5s"
        
        # Construct Prompt
        prompt = f"""You are AgriBot, an agriculture advisory assistant for farmers in India.

RULES (IMPORTANT):
1. Answer ONLY using the data provided in CONTEXT.
2. If the answer is not present in the context, clearly say:
   "I do not have exact data for this. Please consult a local agriculture expert."
3. Do NOT guess or hallucinate.
4. Keep answers short, clear, and practical.
5. Use simple language suitable for farmers.
6. Mention crop stage, soil type, and season when relevant.
7. If the question is unsafe (medicine dosage, chemicals), give general guidance only.

CONTEXT DATA:
{kb_data}

FARMER QUESTION:
{request.message}

RESPONSE FORMAT:
- Crop / Topic:
- Recommendation:
- Reason:
- Precautions:
- Confidence Level (High / Medium / Low)
"""

        # Gemini API call
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }
        
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            result = response.json()
            if result.get('candidates') and result['candidates'][0].get('content'):
                bot_text = result['candidates'][0]['content']['parts'][0]['text']
                return {"response": bot_text}
            else:
                return {"response": "I'm sorry, I couldn't understand that. Could you try asking in a different way?"}
        else:
            logger.error(f"Gemini API Error: {response.text}")
            return {"response": "I'm having trouble connecting to my knowledge base right now. Please try again later."}
            
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        return {"response": "An internal error occurred. Please try again later."}

@app.on_event("startup")
async def startup_event():
    logger.info("🚀 AgriYuti API (Minimal Version) Starting...")
    logger.info("📋 Registered Routes:")
    for route in app.routes:
        if hasattr(route, 'path'):
            logger.info(f"➡️  {route.path}")
    logger.info("✅ AgriYuti API is ready!")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
