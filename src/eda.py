import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv("data/Cleaned_Water_Quality_Dataset.csv")

# Display the first 5 rows
print(df.head())

# Display the shape
print("\nDataset Shape:")
print(df.shape)


# Pollution Level Distribution
plt.figure(figsize=(6,4))

df["Pollution_Level"].value_counts().sort_index().plot(kind="bar")

plt.title("Pollution Level Distribution")
plt.xlabel("Pollution Level")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("outputs/pollution_level_distribution.png")

print("Graph saved successfully in outputs folder.")




# -------------------------------------
# Histograms of Numerical Features
# -------------------------------------

numerical_columns = [
    "pH",
    "Turbidity (NTU)",
    "Temperature (°C)",
    "DO (mg/L)",
    "BOD (mg/L)",
    "Lead (mg/L)",
    "Mercury (mg/L)",
    "Arsenic (mg/L)"
]

df[numerical_columns].hist(
    figsize=(15,10),
    bins=20,
    edgecolor="black"
)

plt.suptitle("Distribution of Numerical Features", fontsize=16)

plt.tight_layout()

plt.savefig("outputs/numerical_features_histogram.png")

print("Histogram saved successfully!")




# -------------------------------------
# Box Plots of Numerical Features
# -------------------------------------

plt.figure(figsize=(15, 8))

df[numerical_columns].boxplot()

plt.title("Box Plot of Numerical Features")
plt.xticks(rotation=45)
plt.ylabel("Values")

plt.tight_layout()

plt.savefig("outputs/boxplot_numerical_features.png")

print("Box Plot saved successfully!")




import seaborn as sns

# -------------------------------------
# Correlation Heatmap
# -------------------------------------

plt.figure(figsize=(10,8))

correlation = df[numerical_columns + ["Pollution_Level"]].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("outputs/correlation_heatmap.png")

print("Correlation Heatmap saved successfully!")




# -------------------------------------
# Scatter Plot
# -------------------------------------

plt.figure(figsize=(7,5))

plt.scatter(
    df["DO (mg/L)"],
    df["BOD (mg/L)"],
    alpha=0.6
)

plt.title("DO vs BOD")
plt.xlabel("DO (mg/L)")
plt.ylabel("BOD (mg/L)")

plt.tight_layout()

plt.savefig("outputs/do_vs_bod_scatter.png")

print("Scatter Plot saved successfully!")