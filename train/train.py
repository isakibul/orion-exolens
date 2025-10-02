import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# 1️⃣ Load dataset
df = pd.read_csv("kepler_clean_dataset.csv")

# 2️⃣ Features & target
X = df.drop("koi_disposition", axis=1)
y = df["koi_disposition"]

# 3️⃣ Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5️⃣ Train model
clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X_train_scaled, y_train)

# 6️⃣ Evaluate
y_pred = clf.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 7️⃣ Save model & scaler
joblib.dump(clf, "kepler_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("✅ Model and scaler saved!")