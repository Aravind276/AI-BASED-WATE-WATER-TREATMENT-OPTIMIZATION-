import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("data/Water_Quality_Dataset.csv")

# Display the first 5 rows
print(df.head())

# Display the shape of the dataset
print("\nShape of the Dataset:")
print(df.shape)

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Check Duplicate Records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Convert Timestamp to datetime format
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Check the updated data types
print("\nUpdated Data Types:")
print(df.dtypes)



# Save the cleaned dataset
df.to_csv("data/Cleaned_Water_Quality_Dataset.csv", index=False)

print("\n======================================")
print("Data Preprocessing Completed Successfully!")
print("Cleaned dataset saved as:")
print("data/Cleaned_Water_Quality_Dataset.csv")
print("======================================")