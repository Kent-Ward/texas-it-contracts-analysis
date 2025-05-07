import pandas as pd

# === Load refined tracker ===
input_path = "C:/Users/Khemb/Documents/TS_Project/data/processed/refined_master_tracker.xlsx"
df = pd.read_excel(input_path, sheet_name=None)

# === Combine all sheets
combined_df = pd.concat(df.values(), ignore_index=True)

# === Combine searchable fields
combined_df['search_text'] = (
    combined_df['project_name'].astype(str).str.lower() + ' ' +
    combined_df['nigp_codes'].astype(str).str.lower()
)

# === Define keyword mapping (feel free to expand this!)
tech_keywords = {
    'microsoft_teams': ['microsoft teams', 'teams voice', 'teams direct routing'],
    'office_365': ['m365', 'office 365', 'exchange online'],
    'azure': ['azure', 'microsoft azure'],
    'aws': ['aws', 'amazon web services'],
    'virtualization': ['virtualization', 'vmware'],
    'voip': ['voip', 'voice over ip'],
    'unified_comms': ['unified communications', 'uc', 'telephony'],
    'cybersecurity': ['cybersecurity', 'security', 'risk'],
    'cloud_services': ['cloud', 'cloud migration', 'cloud hosting'],
    'disaster_recovery': ['dr', 'disaster recovery', 'business continuity']
}

# === Count matches
trend_counts = []

for trend, keywords in tech_keywords.items():
    mask = combined_df['search_text'].apply(
        lambda text: any(kw in text for kw in keywords)
    )
    count = mask.sum()
    trend_counts.append({'technology': trend, 'match_count': count})

# === Convert to DataFrame
trend_df = pd.DataFrame(trend_counts).sort_values(by='match_count', ascending=False)

# === Save output
output_path = "C:/Users/Khemb/Documents/TS_Project/data/analysis/tech_trend_summary.xlsx"
trend_df.to_excel(output_path, index=False)

# === Display in terminal
print("\n🔎 Technology Trend Summary:")
print(trend_df)
print(f"\n✅ Saved to: {output_path}")