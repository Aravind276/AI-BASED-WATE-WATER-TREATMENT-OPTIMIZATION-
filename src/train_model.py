import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# Load cleaned dataset
df = pd.read_csv("data/Cleaned_Water_Quality_Dataset.csv")


# Input features
features = [
    "pH",
    "Turbidity (NTU)",
    "Temperature (°C)",
    "DO (mg/L)",
    "BOD (mg/L)",
    "Lead (mg/L)",
    "Mercury (mg/L)",
    "Arsenic (mg/L)"
]

X = df[features]


# Target variable
y = df["Pollution_Level"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

print("Random Forest model created successfully!")

print("\nNumber of training samples:", len(X_train))
print("Number of testing samples:", len(X_test))


# Train the Random Forest model
model.fit(X_train, y_train)

print("\nRandom Forest model trained successfully!")


# Make predictions on the test data
y_pred = model.predict(X_test)

print("\nPredictions generated successfully!")

print("\nFirst 10 Actual Values:")
print(y_test.head(10).values)

print("\nFirst 10 Predicted Values:")
print(y_pred[:10])


# Save the trained model
joblib.dump(model, "models/random_forest_model.pkl")

print("\nTrained model saved successfully!")
print("Saved as: models/random_forest_model.pkl")


# Save test predictions
results = X_test.copy()

results["Actual_Pollution_Level"] = y_test.values
results["Predicted_Pollution_Level"] = y_pred

results.to_csv(
    "outputs/model_predictions.csv",
    index=False
)

print("\nPredictions saved successfully!")
print("Saved as: outputs/model_predictions.csv")