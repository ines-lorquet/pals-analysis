import csv
import os
from csv_name import combat_attribute, refresh_level, ordinary_boss, job_skills

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

def process_files():
    # Directories
    raw_data_dir = 'raw_data'
    processed_data_dir = 'processed_data'
    os.makedirs(processed_data_dir, exist_ok=True)

    # List of CSV files to process and the number of rows to skip for each
    files_to_clean = [
        (combat_attribute, 1),
        (refresh_level, 4),
        (ordinary_boss, 3),
        (job_skills, 1)
    ]

    # Process each file
    for file_name, rows_to_skip in files_to_clean:
        input_path = os.path.join(raw_data_dir, file_name)
        output_path = os.path.join(processed_data_dir, file_name)
        clean_csv(input_path, rows_to_skip, output_path)

    print("Les fichiers CSV ont été nettoyés et enregistrés avec succès.")
