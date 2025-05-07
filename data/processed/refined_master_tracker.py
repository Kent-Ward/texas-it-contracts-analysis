import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# === File paths ===
input_path = "C:/Users/Khemb/Documents/TS_Project/data/processed/master_tracker.xlsx"
output_path = "C:/Users/Khemb/Documents/TS_Project/data/processed/refined_master_tracker.xlsx"

# === Columns to keep ===
refined_columns = [
    'project_name', 'vendor_name', 'nigp_codes', 'status', 'po_amount',
    'vendor_email', 'solicitation_id', 'vendor_id',
    'agency/texas_smartbuy_member_number', 'contract_type',
    'vendor_contact_number', 'award_date'
]

# === Load and prep the master tracker ===
df = pd.read_excel(input_path)
df['contract_pdf'] = ''  # Add placeholder PDF column
df = df[refined_columns + ['contract_pdf']]  # Keep only what’s needed

# === Replace missing values with 'Undefined' ===
df = df.fillna("Undefined")

# === Add helper columns for key NIGP codes ===
target_codes = [
    '204',  # Computer hardware
    '208',  # Software (systems/cloud)
    '209',  # Data software
    '918',  # Consulting
    '920',  # IT & Telecom
    '958',  # Data Processing
    '962',  # Communication services
    '965',  # Printing/Document services
    '985',  # Rental IT Equipment
    '990'   # Security Services
]

for code in target_codes:
    col_name = f'contains_{code}'
    df[col_name] = df['nigp_codes'].astype(str).str.contains(code).map({True: 'Yes', False: 'No'})

# === Split by contract_type into 2 tabs ===
solicitation_df = df[df['contract_type'].str.lower() == 'solicitation']
no_solicitation_df = df[df['contract_type'].str.lower() == 'no solicitation']

# === Create Excel workbook with 2 sheets ===
wb = Workbook()

# --- No Solicitation Sheet ---
ws1 = wb.active
ws1.title = "No Solicitation"
ws1.append(no_solicitation_df.columns.tolist())
for row in dataframe_to_rows(no_solicitation_df, index=False, header=False):
    ws1.append(row)

# --- Solicitation Sheet ---
ws2 = wb.create_sheet(title="Solicitation")
ws2.append(solicitation_df.columns.tolist())
for row in dataframe_to_rows(solicitation_df, index=False, header=False):
    ws2.append(row)

# === Save the file ===
wb.save(output_path)

# ✅ Summary
print(f"\n✅ Refined tracker saved to: {output_path}")
print(f"📊 Total rows: {len(df)}")
print(f"📊 Solicitation rows: {len(solicitation_df)}")
print(f"📊 No Solicitation rows: {len(no_solicitation_df)}")