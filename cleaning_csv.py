import csv
import os
from db import connect

'''
Delete the unnecessary top lines of the raw csv files
rename and save csv files in processed_data folder
'''

# List of CSV files and the number of rows to skip for each
files_to_clean = [
    ('Palworld_Data--Palu combat attribute table.csv', 1),
    ('Palworld_Data--Palu refresh level.csv', 1),
    ('Palworld_Data-comparison of ordinary BOSS attributes.csv', 1),
    ('Palworld_Data-hide pallu attributes.csv', 1),
    ('Palworld_Data-Palu Job Skills Table.csv', 1),
    ('Palworld_Data-Tower BOSS attribute comparison.csv', 1)
]

def clean_csv(file_path, rows_to_skip, output_path):
    try:
        # Read the CSV file
        with open(file_path, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            data = list(reader)
        
        # for row in data[:rows_to_skip]:
        #     print(row)

        from tables import (create_combat_attribute,
                    create_job_skill, 
                    create_hidden_attribute,
                    create_refresh_area,
                    create_ordinary_boss,
                    create_tower_boss)
        conn = connect()
        cursor = conn.cursor(buffered=True)


        # Create tables
        # supprime les doublons
        cursor.execute(create_combat_attribute)
        cursor.execute("SELECT DISTINCT * FROM combat_attribute;")
        cursor.execute(create_job_skill)
        cursor.execute("SELECT DISTINCT * FROM job_skill;")
        cursor.execute(create_hidden_attribute)
        cursor.execute("SELECT DISTINCT * FROM hidden_attribute;")
        # cursor.execute(create_refresh_area)
        # cursor.execute("SELECT DISTINCT * FROM refresh_area;")
        cursor.execute(create_ordinary_boss)
        cursor.execute("SELECT DISTINCT * FROM ordinary_boss;")
        cursor.execute(create_tower_boss)
        cursor.execute("SELECT DISTINCT * FROM tower_boss;")


        data = [row for row in data if row[1] != 'valeur_indesirable'] 
        
        # Skip the specified number of rows
        cleaned_data = data[rows_to_skip:]

        # Write the cleaned data to the output file
        with open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(cleaned_data)

        print(f"Fichier nettoyé enregistré sous : {output_path}")
    
    except Exception as e:
        print(f"Erreur lors du traitement du fichier {file_path}: {e}")

# Ensure the processed_data directory exists
raw_data_dir = 'raw_data'
processed_data_dir = 'processed_data'
os.makedirs(processed_data_dir, exist_ok=True)

# Process each file
for file_name, rows_to_skip in files_to_clean:
    input_path = os.path.join(raw_data_dir, file_name)
    output_path = os.path.join(processed_data_dir, file_name)
    
    if os.path.exists(input_path):
        clean_csv(input_path, rows_to_skip, output_path)
    else:
        print(f"Fichier {input_path} non trouvé. Skipping...")

print("Les fichiers CSV ont été nettoyés et enregistrés avec succès.")

