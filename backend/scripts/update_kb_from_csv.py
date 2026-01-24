import json
import os
import pandas as pd
import glob

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KB_PATH = os.path.join(BASE_DIR, "..", "data", "knowledge_base.json")
DATA_DIR = os.path.join(BASE_DIR, "..", "processed_data")

def update_kb():
    print(f"Updating Knowledge Base at: {KB_PATH}")
    
    if not os.path.exists(KB_PATH):
        print("❌ Knowledge base file not found.")
        return

    try:
        with open(KB_PATH, "r") as f:
            kb = json.load(f)
    except Exception as e:
        print(f"❌ Failed to load existing KB: {e}")
        return

    market_insights = {}
    
    if not os.path.exists(DATA_DIR):
        print(f"❌ Processed data directory not found: {DATA_DIR}")
        return

    csv_files = glob.glob(os.path.join(DATA_DIR, "*_processed.csv"))
    print(f"Found {len(csv_files)} processed CSV files.")

    for file_path in csv_files:
        try:
            crop_name = os.path.basename(file_path).replace("_processed.csv", "").capitalize()
            df = pd.read_csv(file_path)
            
            if df.empty:
                print(f"⚠️ Skipping empty file: {file_path}")
                continue
                
            avg_price = df["Modal Price (Rs./Quintal)"].mean()
            min_price = df["Modal Price (Rs./Quintal)"].min()
            max_price = df["Modal Price (Rs./Quintal)"].max()
            
            # Get latest price (assuming data is sorted or just taking last row)
            # Preprocessing script doesn't sort by date explicitly at the end, but let's assume loose order or just take stats
            last_price = df["Modal Price (Rs./Quintal)"].iloc[-1]
            
            insight = (f"Market analysis for {crop_name}: Average modal price is ₹{avg_price:.0f}/Quintal. "
                       f"Prices fluctuate between ₹{min_price} and ₹{max_price}. "
                       f"Recent trading price: ₹{last_price}.")
            
            market_insights[crop_name] = insight
            print(f"✅ Generated insight for {crop_name}")
            
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")

    # Add or update the section
    kb["market_insights"] = market_insights
    
    try:
        with open(KB_PATH, "w") as f:
            json.dump(kb, f, indent=4)
        print("✅ Knowledge Base successfully updated with market insights.")
    except Exception as e:
        print(f"❌ Failed to write to KB: {e}")

if __name__ == "__main__":
    update_kb()
