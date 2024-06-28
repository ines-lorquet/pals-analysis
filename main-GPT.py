from db import connect, close
import os
from cleaning_csv import clean_csv, files_to_clean
from import_csv import import_csv_to_db, csv_files_and_tables
from tables import (create_combat_attribute,
                    create_job_skill, 
                    create_hidden_attribute,
                    create_refresh_area,
                    create_ordinary_boss,
                    create_tower_boss)

# Clean the CSV files
raw_data_dir = 'raw_data'
processed_data_dir = 'processed_data'
os.makedirs(processed_data_dir, exist_ok=True)

for file_name, rows_to_skip in files_to_clean:
    input_path = os.path.join(raw_data_dir, file_name)
    output_path = os.path.join(processed_data_dir, file_name)
    clean_csv(input_path, rows_to_skip, output_path)

print("Les fichiers CSV ont été nettoyés et enregistrés avec succès.")


# Connect to the database and create tables
conn = connect()   
cursor = conn.cursor(buffered=True)
try:
    cursor.execute(create_combat_attribute)
    cursor.execute(create_job_skill)
    cursor.execute(create_hidden_attribute)
    cursor.execute(create_refresh_area)
    cursor.execute(create_ordinary_boss)
    cursor.execute(create_tower_boss)

    print("Les tables de la base de données ont été créées avec succès.")
except conn.connector.Error as err:
    print(f"Erreur MySQL : {err}")


# Import cleaned CSV data into the database tables
for csv_file, table_name in csv_files_and_tables:
    csv_file_name = os.path.join(processed_data_dir, csv_file)
    import_csv_to_db(csv_file_name, table_name)

print("Les données ont été importées avec succès dans les tables de la base de données.")

