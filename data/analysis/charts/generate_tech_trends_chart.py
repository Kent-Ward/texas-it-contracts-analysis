import pandas as pd
import matplotlib.pyplot as plt

# === Load data
file_path = "data/analysis/tech_trend_summary.xlsx"
df = pd.read_excel(file_path)

# === Plot using the correct column names
plt.bar(df['technology'], df['match_count'], color='skyblue')

# === Customize chart
plt.title("Contract Volume by Technology Focus Area")
plt.xlabel("Technology")
plt.ylabel("Number of Matching Contracts")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# === Save and display chart
plt.savefig("data/analysis/charts/tech_focus_chart.png")
plt.show()

print("✅ Chart created and saved successfully!")