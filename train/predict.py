import pandas as pd
import joblib
import sys

# Load model & scaler
clf = joblib.load("kepler_model.pkl")
scaler = joblib.load("scaler.pkl")

# Command line CSV input
if len(sys.argv) < 2:
    print("Usage: python predict.py <user_input.csv>")
    sys.exit(1)

csv_path = sys.argv[1]
user_df = pd.read_csv(csv_path)

# Training features
train_features = ['orbital_period', 'transit_duration', 'transit_depth', 'planet_radius', 
                  'snr', 'semi_major_axis', 'stellar_density', 'equilibrium_temp', 
                  'inclination', 'stellar_radius', 'stellar_mass', 'impact_parameter']

# 1️⃣ Add missing columns with 0 (or median if you prefer)
for col in train_features:
    if col not in user_df.columns:
        print(f"⚠️ Column '{col}' missing, filling with 0")
        user_df[col] = 0

# 2️⃣ Keep only required features
user_input = user_df[train_features]

# 3️⃣ Scale input
scaled_input = scaler.transform(user_input)

# 4️⃣ Predict
predictions = clf.predict(scaled_input)
user_input["Prediction"] = predictions

# 5️⃣ Save predictions
user_input.to_csv("predictions.csv", index=False)
print("✅ Predictions saved to predictions.csv")
print(user_input)
