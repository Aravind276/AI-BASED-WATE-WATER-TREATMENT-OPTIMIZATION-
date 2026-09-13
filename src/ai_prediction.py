"""AI prediction module for wastewater pollution-level classification."""

from pathlib import Path

import joblib
import pandas as pd


FEATURE_COLUMNS = [
    "pH",
    "Turbidity (NTU)",
    "Temperature (°C)",
    "DO (mg/L)",
    "BOD (mg/L)",
    "Lead (mg/L)",
    "Mercury (mg/L)",
    "Arsenic (mg/L)",
]

POLLUTION_LABELS = {
    0: "Low",
    1: "Medium",
    2: "High",
}


def load_ai_model(model_path: Path):
    """Load the previously trained Random Forest AI model."""
    return joblib.load(model_path)


def predict_pollution_level(model, values):
    """Predict pollution level from eight wastewater-quality parameters."""
    if len(values) != len(FEATURE_COLUMNS):
        raise ValueError("Exactly eight wastewater parameters are required.")

    input_data = pd.DataFrame([values], columns=FEATURE_COLUMNS)
    predicted_level = int(model.predict(input_data)[0])

    if predicted_level not in POLLUTION_LABELS:
        raise ValueError("The AI model returned an unsupported pollution level.")

    return predicted_level, POLLUTION_LABELS[predicted_level]
