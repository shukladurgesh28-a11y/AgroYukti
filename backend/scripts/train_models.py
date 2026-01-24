import pandas as pd
import joblib
import os
from sklearn.model_selection import TimeSeriesSplit
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

import glob
import os

processed_dir = os.path.join(os.path.dirname(__file__), "..", "processed_data")
all_files = glob.glob(os.path.join(processed_dir, "*_processed.csv"))

if not all_files:
    print("⚠️ No processed data files found.")

for path in all_files:
    crop = os.path.basename(path).replace("_processed.csv", "").lower()
    try:
        data = pd.read_csv(path)

        if data.empty:
            print(f"⚠️ Warning: {crop.capitalize()} dataset is empty. Skipping training.")
            continue

        data["Reported Date"] = pd.to_datetime(data["Reported Date"])
        data["Days"] = (data["Reported Date"] - data["Reported Date"].min()).dt.days
        data["Month"] = data["Reported Date"].dt.month

        features = ["Days", "Month", "Arrivals (Tonnes)", "Min Price (Rs./Quintal)", "Max Price (Rs./Quintal)", 
                    "Price Range", "Demand Indicator", "Rolling_Modal_Price", "Lag_1_Month", "Lag_2_Months", "Price_Change_Rate"]
        target = "Modal Price (Rs./Quintal)"

        X = data[features]
        y = data[target]

        n_splits = min(6, len(X) - 1)  
        if n_splits < 2:
            print(f"⚠️ Warning: Not enough data for time-series split in {crop}. Using simple train-test split.")
            X_train, X_test = X.iloc[:-1], X.iloc[-1:]
            y_train, y_test = y.iloc[:-1], y.iloc[-1:]
        else:
            tscv = TimeSeriesSplit(n_splits=n_splits)
            for train_index, test_index in tscv.split(X):
                X_train, X_test = X.iloc[train_index], X.iloc[test_index]
                y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        model = XGBRegressor(n_estimators=300, learning_rate=0.03, objective="reg:squarederror", random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        mape = mean_absolute_percentage_error(y_test, y_pred)
        accuracy = 100 - (mape * 100)

        print(f"✅ {crop.upper()} Model Trained!")
        print(f"📉 MAE: {mae:.2f}")
        print(f"📈 Approx Accuracy: {accuracy:.2f}%")

        models_dir = os.path.join(os.path.dirname(__file__), "..", "models")
        os.makedirs(models_dir, exist_ok=True)
        model_file = os.path.join(models_dir, f"{crop}_model.pkl")
        joblib.dump(model, model_file)
        print(f"✅ Model saved: {model_file}")

    except Exception as e:
        print(f"❌ Error training model for {crop}: {e}")
