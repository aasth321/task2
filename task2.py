import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

plt.switch_backend("Agg")

# Load dataset
df = sns.load_dataset("titanic")
num_cols = df.select_dtypes("number").columns

# Quick overview
print(df.head(), "\nShape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nSummary stats:\n", df[num_cols].describe().T)

# Histograms
df[num_cols].hist(figsize=(10, 8))
plt.tight_layout()
plt.savefig("histograms.png", dpi=300)
plt.close()

# Correlation heatmap
sns.heatmap(df[num_cols].corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.savefig("correlation.png", dpi=300)
plt.close()

# Interactive scatter
px.scatter(df.dropna(subset=["age", "fare"]), x="age", y="fare", color="survived",
           hover_data=["sex", "class"]).write_html("interactive.html")

# Insights
print("\nEDA insights:")
print("- Avg age:", round(df["age"].mean(), 2))
print("- Median fare:", round(df["fare"].median(), 2))
print("- Survival rate:", round(df["survived"].mean(), 2))
print("- Survival by class:\n", df.groupby("class")["survived"].mean().round(3))
print("- Survival by sex:\n", df.groupby("sex")["survived"].mean().round(3))
