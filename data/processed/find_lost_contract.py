import pandas as pd
import glob
import os

# Path to your solicitation Excel files
solicitations_path = 'C:/Users/Khemb/Documents/TS_Project/data/raw/solicitations/'

# Define the NIGP codes to search for (as strings, stripped of * or spaces)
target_nigp_codes = [
    '20800', '20820', '92003', '92005', '92039', '92040', '92064', '92065'
]

# Prepare list to collect matches
matches = []

# Scan each file in the folder
all_files = glob.glob(os.path.join(solicitations_path, '*.xlsx'))

for file in all_files:
    try:
        xl = pd.ExcelFile(file)
        for sheet in xl.sheet_names:
            df = xl.parse(sheet)
            df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

            if 'nigp_codes' in df.columns:
                df['nigp_codes'] = df['nigp_codes'].astype(str).str.replace(r'[\s*-]', '', regex=True)

                filtered = df[df['nigp_codes'].apply(
                    lambda x: any(code in x for code in target_nigp_codes)
                )]

                if not filtered.empty:
                    filtered['source_file'] = os.path.basename(file)
                    filtered['source_sheet'] = sheet
                    matches.append(filtered)

    except Exception as e:
        print(f"⚠️ Error reading {file}: {e}")

# Combine and export results
if matches:
    result_df = pd.concat(matches, ignore_index=True)
    output_path = 'C:/Users/Khemb/Documents/TS_Project/data/processed/lost_contracts_found.xlsx'
    result_df.to_excel(output_path, index=False)
    print(f"✅ Found {len(result_df)} matching rows. Saved to:\n{output_path}")
else:
    print("❌ No matching contracts found.")