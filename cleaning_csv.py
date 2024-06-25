import csv
import os

'''
Delete the unnecessary top linnes of the raw csv files
rename and saves csv files in precessed-data folder
'''

# combat_attribute = 'raw-data/Palworld_Data--Palu combat attribute table.csv'
# refresh_level = 'raw-data/Palworld_Data--Palu refresh level.csv'
# ordinary_boss = 'raw-data/Palworld_Data-comparison of ordinary BOSS attributes.csv'
# hidden_attributes = 'raw-data/Palworld_Data-hide pallu attributes.csv'
# job_skills = 'raw-data/Palworld_Data-Palu Job Skills Table.csv'
# tower_boss = 'raw-data/Palworld_Data-Tower BOSS attribute comparison.csv'combat_attribute = 'raw-data/Palworld_Data--Palu combat attribute table.csv'
combat_attribute = 'Palworld_Data--Palu combat attribute table.csv'
refresh_level = 'Palworld_Data--Palu refresh level.csv'
ordinary_boss = 'Palworld_Data-comparison of ordinary BOSS attributes.csv'
hidden_attributes = 'Palworld_Data-hide pallu attributes.csv'
job_skills = 'Palworld_Data-Palu Job Skills Table.csv'
tower_boss = 'Palworld_Data-Tower BOSS attribute comparison.csv'



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
    (ordinary_boss, 3),
    (job_skills, 1)
]

# Ensure the processed_data directory exists
raw_data_dir = 'raw_data'
processed_data_dir = 'processed_data'
os.makedirs(processed_data_dir, exist_ok=True)

# Process each file
for file_name, rows_to_skip in files_to_clean:
    input_path = os.path.join(raw_data_dir, file_name)
    output_path = os.path.join(processed_data_dir, file_name)
    clean_csv(input_path, rows_to_skip, output_path)

print("Les fichiers CSV ont été nettoyés et enregistrés avec succès.")