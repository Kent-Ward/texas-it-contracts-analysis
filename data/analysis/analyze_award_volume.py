import pandas as pd

# === Load refined tracker ===
input_path = "C:/Users/Khemb/Documents/TS_Project/data/processed/refined_master_tracker.xlsx"
df = pd.read_excel(input_path, sheet_name=None)  # Load both sheets

# === Combine sheets for full analysis ===
combined_df = pd.concat(df.values(), ignore_index=True)

# === Group by NIGP Codes and count ===
nigp_summary = (
    combined_df['nigp_codes']
    .dropna()
    .astype(str)
    .str.split(';')  # Handle multiple codes per row
    .explode()
    .str.strip()
    .value_counts()
    .reset_index()
)

nigp_summary.columns = ['nigp_code', 'contract_count']

# === Show top 15 NIGP codes by award volume
print("\n📊 Top Awarded NIGP Class Codes:")
print(nigp_summary.head(15))

output_path = "C:/Users/Khemb/Documents/TS_Project/data/analysis/nigp_award_volume.xlsx"
nigp_summary.to_excel(output_path, index=False)
print(f"\n✅ Summary saved to: {output_path}")

