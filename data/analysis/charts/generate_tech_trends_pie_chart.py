import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = 'data/analysis/tech_trend_summary.xlsx'
df = pd.read_excel(file_path)

# Show column names to verify
print("📋 Column names found in the Excel file:")
for col in df.columns:
    print(f"- {col}")

# Set column references
tech_col = 'technology'
count_col = 'match_count'

# Data
labels = df[tech_col]
sizes = df[count_col]

# Colors and explode
colors = plt.get_cmap('tab10').colors  # Matplotlib default 10-color palette
explode = [0.05 if val < 5 else 0 for val in sizes]

# Pie Chart without labels directly on slices
plt.figure(figsize=(8, 6))
wedges, _, autotexts = plt.pie(
    sizes,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors[:len(sizes)],
    explode=explode,
    textprops={'fontsize': 9, 'color': 'black'}
)

# Add clean legend instead of cluttered slice labels
plt.legend(
    wedges,
    labels,
    title="Technology Area",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=9
)

plt.title("Technology Trends in Awarded Contracts", fontsize=13)
plt.tight_layout()
plt.savefig("data/analysis/charts/tech_trends_pie_chart_legend.png", dpi=300)
plt.show()