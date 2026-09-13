import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# Load the trained Random Forest model
model = joblib.load("models/random_forest_model.pkl")

print("Trained Random Forest model loaded successfully!")


# Load the saved test predictions
results = pd.read_csv("outputs/model_predictions.csv")

print("Test predictions loaded successfully!")


# Get actual and predicted values
y_test = results["Actual_Pollution_Level"]
y_pred = results["Predicted_Pollution_Level"]


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(accuracy)


# Classification report
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=["Low", "Medium", "High"],
    yticklabels=["Low", "Medium", "High"]
)

plt.xlabel("Predicted Pollution Level")
plt.ylabel("Actual Pollution Level")
plt.title("Confusion Matrix - Random Forest")

plt.tight_layout()

plt.savefig("outputs/confusion_matrix.png")

plt.close()

print("\nConfusion matrix graph saved successfully!")

# Feature Importance

importance = model.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": results.columns[:8],
    "Importance": importance
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(feature_importance)