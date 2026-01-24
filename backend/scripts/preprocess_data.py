import pandas as pd
import os

import glob

# Dynamic file discovery containing market data
data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
all_csvs = glob.glob(os.path.join(data_dir, "*.csv"))

# Required columns to identify valid market data
REQUIRED_COLS = ["Reported Date", "Modal Price (Rs./Quintal)"]

for path in all_csvs:
    crop = os.path.basename(path).split(".")[0].lower()
    
    # Skip non-market files
    if "weather" in crop or "processed" in crop:
        continue
        
    try:
        data = pd.read_csv(path)
        
        # Validation: Check if it's a market data file
        if not all(col in data.columns for col in REQUIRED_COLS):
            print(f"⚠️ Skipping {crop}: Missing required columns")
            continue

        print(f"🔄 Processing {crop.capitalize()}...")
        
        data["Reported Date"] = data["Reported Date"].astype(str).str.strip().str.replace('"', '')

        date_formats = ["%d %b %Y", "%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"]
        converted = False
        for fmt in date_formats:
            data["Reported Date"] = pd.to_datetime(data["Reported Date"], format=fmt, errors="coerce")
            if data["Reported Date"].notna().sum() > 0:
                print(f"✅ {crop.capitalize()} - Successfully converted dates using format: {fmt}")
                converted = True
                break  
        
        if not converted:
             print(f"⚠️ Warning: Could not parse dates for {crop}. Skipping.")
             continue

        data = data.dropna(subset=["Reported Date"])

        if len(data) == 0:
            print(f"⚠️ Warning: No valid dates found for {crop}. Skipping processing.")
            continue  

        data["Days"] = (data["Reported Date"] - data["Reported Date"].min()).dt.days
        
        # Handle optional columns with defaults
        if "Min Price (Rs./Quintal)" not in data.columns:
            data["Min Price (Rs./Quintal)"] = data["Modal Price (Rs./Quintal)"] * 0.9
        if "Max Price (Rs./Quintal)" not in data.columns:
            data["Max Price (Rs./Quintal)"] = data["Modal Price (Rs./Quintal)"] * 1.1
        if "Arrivals (Tonnes)" not in data.columns:
            data["Arrivals (Tonnes)"] = 100 # Default
            
        data["Price Range"] = data["Max Price (Rs./Quintal)"] - data["Min Price (Rs./Quintal)"]
        data["Demand Indicator"] = data["Arrivals (Tonnes)"] / (data["Modal Price (Rs./Quintal)"] + 1)

        data["Rolling_Modal_Price"] = data["Modal Price (Rs./Quintal)"].rolling(window=30, min_periods=1).mean()

        data["Lag_1_Month"] = data["Modal Price (Rs./Quintal)"].shift(30).bfill()
        data["Lag_2_Months"] = data["Modal Price (Rs./Quintal)"].shift(60).bfill()

        data["Price_Change_Rate"] = data["Modal Price (Rs./Quintal)"].pct_change().fillna(0)

        numeric_cols = data.select_dtypes(include=["number"]).columns
        data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())

        # Save to processed directory relative to script or absolute
        processed_dir = os.path.join(os.path.dirname(__file__), "..", "processed_data")
        os.makedirs(processed_dir, exist_ok=True)
        processed_file = os.path.join(processed_dir, f"{crop}_processed.csv")
        data.to_csv(processed_file, index=False)

        print(f"✅ Processed data saved: {processed_file}\n")

    except Exception as e:
        print(f"❌ Error processing {crop}: {e}")
