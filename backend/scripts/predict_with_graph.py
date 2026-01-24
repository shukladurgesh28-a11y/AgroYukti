import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import joblib
import pandas as pd
import numpy as np
import os
import random

import glob

# Dynamic discovery of ML models
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
ML_MODELS = {}
if os.path.exists(MODEL_DIR):
    for model_path in glob.glob(os.path.join(MODEL_DIR, "*_model.pkl")):
        crop_name = os.path.basename(model_path).replace("_model.pkl", "").lower()
        ML_MODELS[crop_name] = model_path

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "processed_data")
GRAPH_DIR = os.path.join(os.path.dirname(__file__), "predicted_graphs")
os.makedirs(GRAPH_DIR, exist_ok=True)

# Extended list of crops with default metadata for simulation
EXTENDED_CROPS = {
    # --- FRUITS (50+) ---
    "apple": {"base_price": 12000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.05, "trend": 0.02},
    "banana": {"base_price": 2500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.03, "trend": 0.01},
    "mango": {"base_price": 8000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.08, "trend": -0.01},
    "grapes": {"base_price": 6500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.06, "trend": 0.03},
    "papaya": {"base_price": 3000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.04, "trend": 0.01},
    "watermelon": {"base_price": 1500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.10, "trend": 0.05},
    "muskmelon": {"base_price": 2000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.09, "trend": 0.04},
    "pomegranate": {"base_price": 11000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.04, "trend": 0.02},
    "orange": {"base_price": 4500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.05, "trend": 0.03},
    "pineapple": {"base_price": 3500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.03, "trend": 0.01},
    "guava": {"base_price": 2500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.06, "trend": -0.02},
    "lemon": {"base_price": 5000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.15, "trend": 0.04},
    "sweetlime": {"base_price": 4800, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.05, "trend": 0.02},
    "jackfruit": {"base_price": 2200, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.04, "trend": -0.01},
    "custardapple": {"base_price": 4000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.07, "trend": 0.03},
    "sapota": {"base_price": 3200, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.05, "trend": 0.01},
    "strawberry": {"base_price": 15000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.10, "trend": 0.05},
    "lychee": {"base_price": 9000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.12, "trend": -0.03},
    "pear": {"base_price": 8500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.05, "trend": 0.02},
    "plum": {"base_price": 7000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.06, "trend": 0.01},
    "peach": {"base_price": 7500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.07, "trend": 0.02},
    "apricot": {"base_price": 12000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.04, "trend": 0.03},
    "cherry": {"base_price": 18000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.09, "trend": 0.04},
    "kiwi": {"base_price": 16000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.03, "trend": 0.01},
    "dragonfruit": {"base_price": 14000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.05, "trend": 0.06},
    "avocado": {"base_price": 20000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.04, "trend": 0.02},
    "fig": {"base_price": 9500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.08, "trend": 0.03},
    "dates": {"base_price": 8000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.02, "trend": 0.01},
    "coconut": {"base_price": 2500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.01, "trend": 0.00},
    "tamarind": {"base_price": 4500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.03, "trend": 0.01},
    "amla": {"base_price": 1800, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.06, "trend": -0.01},
    "jamun": {"base_price": 5500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.10, "trend": 0.04},
    "bael": {"base_price": 2000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.05, "trend": 0.01},
    "ber": {"base_price": 1500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.07, "trend": -0.02},
    "phalsa": {"base_price": 4000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.09, "trend": 0.03},
    "mulberry": {"base_price": 6000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.08, "trend": 0.04},
    "passionfruit": {"base_price": 11000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.05, "trend": 0.02},
    "mangosteen": {"base_price": 18000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.06, "trend": 0.03},
    "rambutan": {"base_price": 15000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.07, "trend": 0.02},
    "durian": {"base_price": 25000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.10, "trend": 0.05},
    "persimmon": {"base_price": 12000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.04, "trend": 0.01},
    "grapefruit": {"base_price": 5500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.06, "trend": 0.02},
    "pomelo": {"base_price": 4000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.05, "trend": 0.01},
    "quince": {"base_price": 9000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.03, "trend": 0.01},
    "starfruit": {"base_price": 3000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.08, "trend": 0.02},
    "woodapple": {"base_price": 1200, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.04, "trend": -0.01},
    "karonda": {"base_price": 1800, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.05, "trend": 0.01},
    "bilimbi": {"base_price": 1500, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.06, "trend": 0.00},
    "monkfruit": {"base_price": 30000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.15, "trend": 0.05},
    "loquat": {"base_price": 7000, "unit": "Rs./Quintal", "category": "fruit", "volatility": 0.07, "trend": 0.02},

    # --- VEGETABLES (50+) ---
    "potato": {"base_price": 1800, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.05, "trend": 0.01},
    "onion": {"base_price": 2200, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.08, "trend": 0.03},
    "tomato": {"base_price": 2000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.12, "trend": -0.02},
    "brinjal": {"base_price": 2800, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.07, "trend": -0.03},
    "cabbage": {"base_price": 1500, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.10, "trend": 0.05},
    "cauliflower": {"base_price": 2200, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.09, "trend": 0.02},
    "ladiesfinger": {"base_price": 3500, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.06, "trend": 0.03},
    "bittergourd": {"base_price": 4000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.05, "trend": 0.01},
    "bottlegourd": {"base_price": 1200, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.08, "trend": -0.01},
    "ridgegourd": {"base_price": 2800, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.06, "trend": 0.02},
    "snakegourd": {"base_price": 2500, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.07, "trend": 0.01},
    "ashgourd": {"base_price": 1500, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.04, "trend": 0.00},
    "pumpkin": {"base_price": 1400, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.03, "trend": 0.01},
    "cucumber": {"base_price": 1800, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.09, "trend": 0.04},
    "capsicum": {"base_price": 5500, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.04, "trend": 0.02},
    "greenchilli": {"base_price": 4500, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.15, "trend": 0.05},
    "spinach": {"base_price": 1200, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.12, "trend": -0.01},
    "fenugreek_leaves": {"base_price": 1500, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.10, "trend": 0.02},
    "coriander_leaves": {"base_price": 2500, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.18, "trend": 0.06},
    "mint_leaves": {"base_price": 3000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.15, "trend": 0.04},
    "mustard_leaves": {"base_price": 1000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.08, "trend": -0.02},
    "amaranth": {"base_price": 1300, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.09, "trend": 0.01},
    "lettuce": {"base_price": 6000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.05, "trend": 0.03},
    "broccoli": {"base_price": 7000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.06, "trend": 0.02},
    "carrot": {"base_price": 2500, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.04, "trend": 0.01},
    "radish": {"base_price": 1200, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.07, "trend": -0.01},
    "beetroot": {"base_price": 2200, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.05, "trend": 0.02},
    "turnip": {"base_price": 1800, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.06, "trend": 0.01},
    "sweetpotato": {"base_price": 2000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.04, "trend": 0.01},
    "tapioca": {"base_price": 1600, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.03, "trend": 0.01},
    "yam": {"base_price": 2500, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.05, "trend": 0.02},
    "colocasia": {"base_price": 2800, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.06, "trend": 0.02},
    "ginger": {"base_price": 6000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.10, "trend": 0.04},
    "garlic": {"base_price": 8000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.12, "trend": 0.05},
    "peas": {"base_price": 4000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.08, "trend": -0.02},
    "frenchbeans": {"base_price": 3500, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.07, "trend": 0.03},
    "clusterbeans": {"base_price": 3000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.06, "trend": 0.02},
    "cowpea_beans": {"base_price": 3200, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.05, "trend": 0.01},
    "broadbeans": {"base_price": 2800, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.06, "trend": 0.01},
    "drumstick": {"base_price": 3500, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.15, "trend": 0.06},
    "curryleaves": {"base_price": 2000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.05, "trend": 0.01},
    "mushroom": {"base_price": 12000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.08, "trend": 0.04},
    "babycorn": {"base_price": 8000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.06, "trend": 0.03},
    "zucchini": {"base_price": 9000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.05, "trend": 0.02},
    "redcabbage": {"base_price": 4000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.07, "trend": 0.03},
    "celery": {"base_price": 10000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.06, "trend": 0.02},
    "leek": {"base_price": 11000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.05, "trend": 0.01},
    "asparagus": {"base_price": 25000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.04, "trend": 0.03},
    "artichoke": {"base_price": 18000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.06, "trend": 0.02},
    "kale": {"base_price": 15000, "unit": "Rs./Quintal", "category": "vegetable", "volatility": 0.08, "trend": 0.04},

    # --- GRAINS & CEREALS (20+) ---
    "rice": {"base_price": 3800, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.02, "trend": 0.01},
    "basmati": {"base_price": 7500, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.03, "trend": 0.02},
    "wheat": {"base_price": 2400, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.02, "trend": 0.01},
    "maize": {"base_price": 2100, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.03, "trend": 0.02},
    "jowar": {"base_price": 3000, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.04, "trend": 0.01},
    "bajra": {"base_price": 2200, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.03, "trend": 0.01},
    "ragi": {"base_price": 3200, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.02, "trend": 0.02},
    "barley": {"base_price": 1800, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.03, "trend": -0.01},
    "oats": {"base_price": 3500, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.04, "trend": 0.03},
    "quinoa": {"base_price": 9000, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.06, "trend": 0.05},
    "amaranth_grain": {"base_price": 6000, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.05, "trend": 0.03},
    "buckwheat": {"base_price": 5500, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.04, "trend": 0.02},
    "foxtail_millet": {"base_price": 3800, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.03, "trend": 0.01},
    "kodo_millet": {"base_price": 4000, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.03, "trend": 0.01},
    "barnyard_millet": {"base_price": 4200, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.03, "trend": 0.01},
    "little_millet": {"base_price": 4500, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.03, "trend": 0.02},
    "proso_millet": {"base_price": 3600, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.03, "trend": 0.01},
    "sorghum": {"base_price": 2800, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.04, "trend": 0.01},
    "rye": {"base_price": 3000, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.03, "trend": 0.01},
    "teff": {"base_price": 12000, "unit": "Rs./Quintal", "category": "grain", "volatility": 0.05, "trend": 0.04},

    # --- PULSES (15+) ---
    "toor_dal": {"base_price": 9000, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.06, "trend": 0.03},
    "moong_dal": {"base_price": 8500, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.05, "trend": 0.02},
    "urad_dal": {"base_price": 8000, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.05, "trend": 0.01},
    "chana_dal": {"base_price": 5500, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.04, "trend": 0.01},
    "masoor_dal": {"base_price": 7000, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.05, "trend": 0.02},
    "rajma": {"base_price": 11000, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.04, "trend": 0.03},
    "chickpeas": {"base_price": 5000, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.04, "trend": 0.01},
    "soybean": {"base_price": 4500, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.06, "trend": 0.03},
    "groundnut": {"base_price": 6000, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.05, "trend": 0.02},
    "black_chana": {"base_price": 5200, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.04, "trend": 0.01},
    "lobia": {"base_price": 6500, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.05, "trend": 0.02},
    "moth_bean": {"base_price": 7500, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.06, "trend": 0.03},
    "horse_gram": {"base_price": 4000, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.03, "trend": 0.01},
    "green_peas_dry": {"base_price": 5500, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.04, "trend": 0.02},
    "white_peas": {"base_price": 4800, "unit": "Rs./Quintal", "category": "pulse", "volatility": 0.03, "trend": 0.01},

    # --- SPICES & OTHERS (15+) ---
    "red_chilli": {"base_price": 20000, "unit": "Rs./Quintal", "category": "spice", "volatility": 0.15, "trend": 0.05},
    "turmeric": {"base_price": 8000, "unit": "Rs./Quintal", "category": "spice", "volatility": 0.08, "trend": 0.03},
    "cumin": {"base_price": 30000, "unit": "Rs./Quintal", "category": "spice", "volatility": 0.12, "trend": 0.06},
    "coriander_seeds": {"base_price": 9000, "unit": "Rs./Quintal", "category": "spice", "volatility": 0.07, "trend": 0.02},
    "fenugreek_seeds": {"base_price": 6000, "unit": "Rs./Quintal", "category": "spice", "volatility": 0.05, "trend": 0.01},
    "mustard_seeds": {"base_price": 5500, "unit": "Rs./Quintal", "category": "spice", "volatility": 0.04, "trend": 0.02},
    "black_pepper": {"base_price": 45000, "unit": "Rs./Quintal", "category": "spice", "volatility": 0.10, "trend": 0.04},
    "cardamom": {"base_price": 150000, "unit": "Rs./Quintal", "category": "spice", "volatility": 0.20, "trend": 0.08},
    "clove": {"base_price": 80000, "unit": "Rs./Quintal", "category": "spice", "volatility": 0.15, "trend": 0.05},
    "cinnamon": {"base_price": 25000, "unit": "Rs./Quintal", "category": "spice", "volatility": 0.10, "trend": 0.03},
    "fennel": {"base_price": 12000, "unit": "Rs./Quintal", "category": "spice", "volatility": 0.06, "trend": 0.02},
    "cotton": {"base_price": 6000, "unit": "Rs./Quintal", "category": "other", "volatility": 0.05, "trend": 0.03},
    "sugarcane": {"base_price": 320, "unit": "Rs./Quintal", "category": "other", "volatility": 0.01, "trend": 0.01},
    "jute": {"base_price": 4500, "unit": "Rs./Quintal", "category": "other", "volatility": 0.06, "trend": 0.02},
    "tobacco": {"base_price": 15000, "unit": "Rs./Quintal", "category": "other", "volatility": 0.10, "trend": 0.04},
    "coffee": {"base_price": 18000, "unit": "Rs./Quintal", "category": "other", "volatility": 0.08, "trend": 0.03},
    "tea": {"base_price": 20000, "unit": "Rs./Quintal", "category": "other", "volatility": 0.07, "trend": 0.02},
    "rubber": {"base_price": 16000, "unit": "Rs./Quintal", "category": "other", "volatility": 0.09, "trend": 0.03},
}

FEATURE_NAMES = [
    "Days", "Month", "Arrivals (Tonnes)", "Min Price (Rs./Quintal)", "Max Price (Rs./Quintal)",
    "Price Range", "Demand Indicator", "Rolling_Modal_Price", "Lag_1_Month", "Lag_2_Months", "Price_Change_Rate"
]

def simulate_predictions(crop_name, metadata, weeks_ahead, today):
    """Generate simulated price data for crops without ML models"""
    base = metadata["base_price"]
    volatility = metadata["volatility"]
    trend = metadata["trend"]
    
    future_dates = [today + timedelta(weeks=i) for i in range(1, weeks_ahead + 1)]
    predicted_prices = []
    
    current_price = base
    for _ in range(weeks_ahead):
        # Random walk with trend
        change = np.random.normal(trend, volatility)
        current_price = current_price * (1 + change)
        predicted_prices.append(current_price)
    
    return np.array(predicted_prices), future_dates, "Rs./Kg" if crop_name != "banana" else "Rs./Dozen"

def get_price_predictions():
    all_results = []
    today = datetime.now()
    end_date = today + timedelta(weeks=4)
    weeks_ahead = 4
    
    # Process all crops (ML supported + Simulated)
    # Combine keys from both dictionaries
    all_crops = set(list(ML_MODELS.keys()) + list(EXTENDED_CROPS.keys()))
    
    for crop in all_crops:
        try:
            predicted_prices = None
            future_dates = None
            unit = "Rs./Kg" # Default
            
            # 1. Try using ML model if available
            if crop in ML_MODELS and os.path.exists(ML_MODELS[crop]):
                try:
                    model = joblib.load(ML_MODELS[crop])
                    data_path = os.path.join(DATA_DIR, f"{crop}_processed.csv")
                    
                    if os.path.exists(data_path):
                        data = pd.read_csv(data_path)
                        data["Reported Date"] = pd.to_datetime(data["Reported Date"])
                        
                        future_dates = [today + timedelta(weeks=i) for i in range(1, weeks_ahead + 1)]
                        future_days = np.array([(d - data["Reported Date"].min()).days for d in future_dates])

                        arrivals_median = data["Arrivals (Tonnes)"].median()
                        min_price_median = data["Min Price (Rs./Quintal)"].median()
                        max_price_median = data["Max Price (Rs./Quintal)"].median()
                        price_range_median = max_price_median - min_price_median
                        demand_indicator_median = arrivals_median / (min_price_median + 1)
                        rolling_price_median = data["Rolling_Modal_Price"].median()
                        lag_1_month_median = data["Lag_1_Month"].median()
                        lag_2_months_median = data["Lag_2_Months"].median()
                        price_change_rate_median = data["Price_Change_Rate"].median()

                        demand_variation = np.linspace(0.95, 1.05, weeks_ahead)
                        price_change_variation = np.linspace(-0.02, 0.02, weeks_ahead)

                        input_data = pd.DataFrame({
                            "Days": future_days,
                            "Month": [d.month for d in future_dates],
                            "Arrivals (Tonnes)": arrivals_median * demand_variation,
                            "Min Price (Rs./Quintal)": min_price_median * demand_variation,
                            "Max Price (Rs./Quintal)": max_price_median * demand_variation,
                            "Price Range": price_range_median * demand_variation,
                            "Demand Indicator": demand_indicator_median * demand_variation,
                            "Rolling_Modal_Price": rolling_price_median * demand_variation,
                            "Lag_1_Month": lag_1_month_median * demand_variation,
                            "Lag_2_Months": lag_2_months_median * demand_variation,
                            "Price_Change_Rate": price_change_rate_median + price_change_variation
                        }, columns=FEATURE_NAMES)

                        predicted_prices = model.predict(input_data)
                        
                        # Convert Unit
                        if crop == "banana":
                            unit = "Rs./Dozen"
                            prices_formatted = (predicted_prices / 100) * 1.5 
                        else:
                            unit = "Rs./Kg"
                            prices_formatted = predicted_prices / 100
                            
                        predicted_prices = prices_formatted # Use formatted for graph and output
                except Exception as e:
                    print(f"[WARNING] ML prediction failed for {crop}, falling back to simulation: {e}")
                    # Fallback to simulation will happen below
            
            # 2. Use Simulation if no model or model failed
            if predicted_prices is None:
                metadata = EXTENDED_CROPS.get(crop, {
                    "base_price": 2000, 
                    "unit": "Rs./Quintal", 
                    "category": "vegetable",
                    "volatility": 0.05, 
                    "trend": 0.01
                })
                
                prices_raw, future_dates, unit = simulate_predictions(crop, metadata, weeks_ahead, today)
                
                # Convert from Quintal to Kg/Dozen for display
                if crop == "banana":
                    unit = "Rs./Dozen"
                    predicted_prices = (prices_raw / 100) * 12 # approx conversion
                elif unit == "Rs./Quintal":
                    unit = "Rs./Kg"
                    predicted_prices = prices_raw / 100
                else:
                    predicted_prices = prices_raw

            # 3. Create Recommendation based on trend
            trend_val = (predicted_prices[-1] - predicted_prices[0]) / predicted_prices[0]
            if trend_val > 0.05:
                trend_str = "up"
                recommendation = "High demand expected. Consider holding for peak prices."
            elif trend_val < -0.05:
                trend_str = "down"
                recommendation = "Prices likely to drop. Consider harvesting soon."
            else:
                trend_str = "stable"
                recommendation = "Market stable. Focus on quality maintenance."
            
            category = EXTENDED_CROPS.get(crop, {}).get("category", "vegetable")
            # If crop in ML_MODELS but not EXTENDED_CROPS, derive category
            if crop in ML_MODELS and crop not in EXTENDED_CROPS:
                if crop == "banana": category = "fruit"
                elif crop == "wheat": category = "grain"
                else: category = "vegetable"

            # 4. Generate Graph (works for both ML and Simulated)
            plt.figure(figsize=(10, 5))
            plt.plot(future_dates, predicted_prices, linestyle="dotted", color="green", marker="o", label="Predicted Prices")
            plt.xlabel("Date")
            plt.ylabel(f"Price ({unit})")
            plt.title(f"Price Prediction for {crop.capitalize()}")
            plt.grid(True, linestyle="--", alpha=0.7)
            plt.legend()
            plt.xticks(rotation=45)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{crop}_prediction_{timestamp}.png"
            filepath = os.path.join(GRAPH_DIR, filename)
            plt.tight_layout()
            plt.savefig(filepath)
            plt.close()

            # 5. Format Result
            prediction_list = [
                {"date": future_dates[i].strftime("%Y-%m-%d"), "price": round(float(p), 2)}
                for i, p in enumerate(predicted_prices)
            ]

            all_results.append({
                "crop": crop,
                "unit": unit,
                "category": category,
                "trend": trend_str,
                "recommendation": recommendation,
                "predictions": prediction_list,
                "image": f"http://localhost:8000/graphs/{filename}",
                "graph_url": f"http://localhost:8000/graphs/{filename}" 
            })

            print(f"[SUCCESS] Processed {crop}")

        except Exception as e:
            print(f"[ERROR] Error processing {crop}: {e}")
            all_results.append({
                "crop": crop,
                "error": str(e)
            })

    return all_results
