import pandas as pd

# === Load tracker ===
input_path = "C:/Users/Khemb/Documents/TS_Project/data/processed/refined_master_tracker.xlsx"
df = pd.read_excel(input_path, sheet_name=None)

# === Combine solicitation and no solicitation ===
combined_df = pd.concat(df.values(), ignore_index=True)

# === Base agency summary ===
agency_summary = (
    combined_df['agency/texas_smartbuy_member_number']
    .astype(str)
    .value_counts()
    .reset_index()
)
agency_summary.columns = ['agency_or_member_number', 'contract_count']

# === Build agency name map ===
agency_name_map = (
    combined_df[['agency/texas_smartbuy_member_number', 'project_name']]
    .dropna()
    .groupby('agency/texas_smartbuy_member_number')['project_name']
    .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0])
    .reset_index()
)
agency_name_map.columns = ['agency_or_member_number', 'agency_name']

# === Merge counts + names ===
enriched_agency_summary = pd.merge(
    agency_summary,
    agency_name_map,
    on='agency_or_member_number',
    how='left'
)

# === Reorder columns for clarity ===
enriched_agency_summary = enriched_agency_summary[['agency_or_member_number', 'agency_name', 'contract_count']]

# === Save to Excel ===
output_path = "C:/Users/Khemb/Documents/TS_Project/data/analysis/top_agencies_enriched.xlsx"
enriched_agency_summary.to_excel(output_path, index=False)

# === Done ===
print("\n✅ Enriched agency summary saved.")
print(f"📁 File location: {output_path}")
print(f"🔢 Top agencies:\n{enriched_agency_summary.head(10)}")