import csv
import os
from csv_name import combat_attribute, refresh_level, ordinary_BOSS_attributes, Palu_Job_Skills_Table

def clean_csv(file_path, rows_to_skip, output_path):
    # Read the CSV file
    with open(file_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        data = list(reader)

    # Skip the specified number of rows
    cleaned_data = data[rows_to_skip:]

    # Write the cleaned data to the output file
    with open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_data)

# List of CSV files to process and the number of rows to skip for each
files_to_clean = [
    (combat_attribute, 1),
    (refresh_level, 4),
    (ordinary_BOSS_attributes, 3),
    (Palu_Job_Skills_Table, 1)
]

# Ensure the processed_data directory exists
raw_data_dir = 'raw_data'
processed_data_dir = 'processed_data'
os.makedirs(processed_data_dir, exist_ok=True)

# Process each file
for file_path, rows_to_skip in files_to_clean:
    input_path = os.path.join(raw_data_dir, file_path)
    output_path = os.path.join(processed_data_dir, file_path)
    clean_csv(input_path, rows_to_skip, output_path)

print("Les fichiers CSV ont été nettoyés et enregistrés avec succès.")
