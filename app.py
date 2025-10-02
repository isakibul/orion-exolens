import os
import pandas as pd
import joblib
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Load model + scaler
model = joblib.load("kepler_model.pkl")
scaler = joblib.load("scaler.pkl")

# Features needed for prediction
FEATURES = [
    "orbital_period", "transit_duration", "transit_depth",
    "planet_radius", "snr", "semi_major_axis",
    "stellar_density", "equilibrium_temp", "inclination",
    "stellar_radius", "stellar_mass", "impact_parameter"
]

# Flask setup
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/single", methods=["GET", "POST"])
def single():
    if request.method == "POST":
        # Collect inputs
        data = [float(request.form.get(f, 0)) for f in FEATURES]
        df = pd.DataFrame([data], columns=FEATURES)

        # Scale + predict
        X_scaled = scaler.transform(df)
        pred = model.predict(X_scaled)[0]

        return render_template("single.html", prediction=pred, values=df.to_dict(orient="records")[0])

    return render_template("single.html", prediction=None)

import json

@app.route("/bulk", methods=["GET", "POST"])
def bulk():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".csv"):
            df = pd.read_csv(file)

            # Ensure all required features exist
            for col in FEATURES:
                if col not in df.columns:
                    df[col] = 0

            X_scaled = scaler.transform(df[FEATURES])
            preds = model.predict(X_scaled)
            df["Prediction"] = preds

            # Convert dataframe to JSON (list of dicts)
            json_data = df.to_dict(orient="records")

            return render_template(
                "bulk.html",
                tables=df.to_html(classes="table table-bordered", index=False),
                data=json.dumps(json_data)
            )

    return render_template("bulk.html", tables=None, data=None)

@app.route("/planet-view")
def planet_view():
    temp = request.args.get("temp", 270)
    try:
        temp = float(temp)
    except:
        temp = 270
    return render_template("planet-view.html", temp=temp)

@app.route("/csv-guide")
def csv_guide():
    return render_template("csv-guide.html")

if __name__ == "__main__":
    app.run(debug=True)
