import pandas as pd

# 1. Load the datasets, skipping lines that are completely blank
df_bejaia = pd.read_csv("Bejaia Region ForestFire Dataset.csv", skip_blank_lines=True)
df_sidi = pd.read_csv("Sidi-Bel Abbes Region ForestFire Dataset.csv", skip_blank_lines=True)

# 2. Clean up trailing/leading spaces in column headers (Very common in this dataset)
df_bejaia.columns = df_bejaia.columns.str.strip()
df_sidi.columns = df_sidi.columns.str.strip()

# 3. Drop rows where ALL elements are missing (NaN) to remove unwanted blank lines
df_bejaia = df_bejaia.dropna(how='all')
df_sidi = df_sidi.dropna(how='all')

output_file = "Combined_ForestFire_Dataset.csv"

# 4. Write to file using 'newline=""' to prevent Windows from adding extra blank rows
with open(output_file, "w", encoding="utf-8", newline="") as f:
    # Write first dataset section
    f.write("Bejaia Region ForestFire Dataset\n")
    df_bejaia.to_csv(f, index=False)
    
    # Write exactly ONE single blank line to separate the datasets
    f.write("\n")
    
    # Write second dataset section
    f.write("Sidi-Bel Abbes Region ForestFire Dataset\n")
    df_sidi.to_csv(f, index=False)

print(f"Successfully cleaned and combined into '{output_file}'!")