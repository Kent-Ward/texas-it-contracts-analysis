import pandas as pd

# === Load refined tracker ===
input_path = "C:/Users/Khemb/Documents/TS_Project/data/processed/refined_master_tracker.xlsx"
df = pd.read_excel(input_path, sheet_name="no_solicitation")

# === Clean PO Amount column ===
df['po_amount'] = pd.to_numeric(df['po_amount'], errors='coerce')

# === Drop missing or zero values ===
df_valid = df[df['po_amount'].notna() & (df['po_amount'] > 0)]

# === Calculate summary stats ===
summary = {
    'Total Contracts w/ PO': len(df_valid),
    'Average PO Amount': df_valid['po_amount'].mean(),
    'Median PO Amount': df_valid['po_amount'].median(),
    'Minimum PO Amount': df_valid['po_amount'].min(),
    'Maximum PO Amount': df_valid['po_amount'].max(),
    'Total PO Amount': df_valid['po_amount'].sum()
}

# === Convert to DataFrame for export ===
summary_df = pd.DataFrame.from_dict(summary, orient='index', columns=['Value'])
output_path = "C:/Users/Khemb/Documents/TS_Project/data/analysis/contract_value_summary.xlsx"
summary_df.to_excel(output_path)

# === Display summary ===
print("\n💰 Contract Value Summary (No Solicitation Only):\n")
print(summary_df)
print(f"\n✅ Saved to: {output_path}")


