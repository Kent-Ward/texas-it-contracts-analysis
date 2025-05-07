import pandas as pd

# Load both sheets from refined tracker
input_path = "C:/Users/Khemb/Documents/TS_Project/data/processed/refined_master_tracker.xlsx"
df = pd.read_excel(input_path, sheet_name=None)

# Combine solicitation and no solicitation sheets
combined_df = pd.concat(df.values(), ignore_index=True)

# Group and count by agency/member number
agency_summary = (
    combined_df['agency/texas_smartbuy_member_number']
    .astype(str)
    .value_counts()
    .reset_index()
)

agency_summary.columns = ['agency_or_member_number', 'contract_count']

# Show top 15
print("\n🏛️ Top Contracting Agencies:")
print(agency_summary.head(15))

# Save to file
output_path = "C:/Users/Khemb/Documents/TS_Project/data/analysis/top_agencies.xlsx"
agency_summary.to_excel(output_path, index=False)
print(f"\n✅ Top agencies saved to: {output_path}")



# Show sample rows where we have member number and project_name
sample_check = combined_df[['agency/texas_smartbuy_member_number', 'project_name']].dropna()
print("\n🧪 Sample of agency number + project name:")
print(sample_check.drop_duplicates().head(15))

# Count how many unique agency/member numbers have a valid project_name
count_valid = sample_check['agency/texas_smartbuy_member_number'].nunique()
print(f"\n🔎 Unique agencies with project_name: {count_valid}")