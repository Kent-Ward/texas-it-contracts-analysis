import pandas as pd

# === Load refined tracker with both sheets ===
input_path = "C:/Users/Khemb/Documents/TS_Project/data/processed/refined_master_tracker.xlsx"
df = pd.read_excel(input_path, sheet_name=None)  # Load all sheets

# === Combine both solicitation and no_solicitation
combined_df = pd.concat(df.values(), ignore_index=True)

# === Clean contract_type values (ensure lowercase, no trailing spaces)
combined_df['contract_type'] = combined_df['contract_type'].astype(str).str.strip().str.lower()

# === Replace blanks or unknowns
combined_df['contract_type'] = combined_df['contract_type'].replace(['nan', '', 'undefined'], 'unspecified')

# === Count types
contract_type_summary = (
    combined_df['contract_type']
    .value_counts()
    .reset_index()
)
contract_type_summary.columns = ['contract_type', 'contract_count']

# === Save output
output_path = "C:/Users/Khemb/Documents/TS_Project/data/analysis/contract_type_summary.xlsx"
contract_type_summary.to_excel(output_path, index=False)

# === Preview results
print("\n📦 Contract Type Breakdown:")
print(contract_type_summary)
print(f"\n✅ Saved to: {output_path}")