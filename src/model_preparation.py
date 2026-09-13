import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/Cleaned_Water_Quality_Dataset.csv")

print("Dataset loaded successfully!")

print("\nDataset Shape:")
print(df.shape)

# Select input features
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

print("\nInput Features:")
print(X.head())

print("\nShape of Input Features:")
print(X.shape)

# Select target variable
y = df["Pollution_Level"]

print("\nTarget Variable:")
print(y.head())

print("\nTarget Shape:")
print(y.shape)

# Check target class distribution
print("\nPollution Level Distribution:")
print(y.value_counts().sort_index())

from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)

print("\nTraining Target Distribution:")
print(y_train.value_counts().sort_index())

print("\nTesting Target Distribution:")
print(y_test.value_counts().sort_index())