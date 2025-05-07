import pandas as pd

# === Load refined tracker ===
input_path = "C:/Users/Khemb/Documents/TS_Project/data/processed/refined_master_tracker.xlsx"
df = pd.read_excel(input_path, sheet_name=None)

# === Combine sheets ===
combined_df = pd.concat(df.values(), ignore_index=True)

# === Filter out blanks and unknown vendors ===
vendor_df = combined_df[['vendor_name']].dropna()
vendor_df = vendor_df[vendor_df['vendor_name'].str.strip().str.lower() != 'undefined']

# === Count contracts per vendor ===
vendor_summary = (
    vendor_df['vendor_name']
    .value_counts()
    .reset_index()
)

vendor_summary.columns = ['vendor_name', 'contract_count']

# === Save to Excel ===
output_path = "C:/Users/Khemb/Documents/TS_Project/data/analysis/top_vendors.xlsx"
vendor_summary.to_excel(output_path, index=False)

# === Output to terminal ===
print("\n🏆 Top Vendors by Contract Count:")
print(vendor_summary.head(15))
print(f"\n✅ Top vendors saved to: {output_path}")