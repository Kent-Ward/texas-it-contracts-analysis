# analyze_award_trends.py
import pandas as pd
import matplotlib.pyplot as plt

# === Load data ===
file_path = "data/processed/refined_master_tracker.xlsx"
df = pd.read_excel(file_path)
print("✅ Loaded data from:", file_path)

# === Check columns for debugging
print("\n📋 Column names found in the Excel file:")
for col in df.columns:
    print("-", col)

# === Clean award_date
df['award_date'] = pd.to_datetime(df['award_date'], errors='coerce')

# === Drop rows with missing award dates
df = df.dropna(subset=['award_date'])

# === Create readable Month-Year format
df['month_abbr'] = df['award_date'].dt.strftime('%b %Y')

# === Group by month and count awards
monthly_counts = df.groupby('month_abbr').size().reset_index(name='award_count')

# === Sort by time (optional for correct order)
monthly_counts['month_order'] = pd.to_datetime(monthly_counts['month_abbr'], format='%b %Y')
monthly_counts = monthly_counts.sort_values('month_order')

# === Plot the line chart
plt.figure(figsize=(14, 6))
plt.plot(monthly_counts['month_abbr'], monthly_counts['award_count'], marker='o')
plt.title("Award Activity Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Awards")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/analysis/charts/award_activity_trend.png")  # Save the chart
plt.show()

# === Save the chart
output_path = "data/analysis/charts/award_trends_over_time.png"
plt.savefig(output_path)
plt.show()

print(f"📈 Award trends chart saved to: {output_path}")