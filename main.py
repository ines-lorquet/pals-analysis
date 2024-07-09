import mysql.connector
from db import connect, close
import os
from import_csv import import_csv_to_db
import csv
from tables import (create_combat_attribute,
                    create_job_skill, 
                    create_hidden_attribute,
                    create_refresh_area,
                    create_ordinary_boss,
                    create_tower_boss)
from cleaning_csv import clean_csv, files_to_clean


# connexion
conn = connect()  
cursor = conn.cursor(buffered=True)



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
        print(f"Fichier {input_path} non trouve. Skipping...")

print("Les fichiers CSV ont ete nettoyes et enregistres avec succes.")



# .csv files and corresponding tables
csv_files_and_tables = [
    ('Palworld_Data--Palu combat attribute table.csv',           'combat_attribute'),
    ('Palworld_Data--Palu refresh level.csv',                    'refresh_area'),
    ('Palworld_Data-comparison of ordinary BOSS attributes.csv', 'ordinary_boss_attribute'),
    ('Palworld_Data-hide pallu attributes.csv',                  'hidden_attribute'),
    ('Palworld_Data-Palu Job Skills Table.csv',                  'job_skill'),
    ('Palworld_Data-Tower BOSS attribute comparison.csv',        'tower_boss_attribute')
]


# Import data
# path = 'processed_data'
# Import raw data
path = 'raw_data'

for csv_file, table_name in csv_files_and_tables:
    csv_file_name = os.path.join(path, csv_file)
    print(f"Importation des donnees depuis {csv_file_name} vers la table {table_name}...")
    import_csv_to_db(csv_file_name, table_name)

print("Les donnees ont ete importees avec succes dans les tables.")


 


# -----------------------NETTOYAGE DES TABLES EN SQL---------------

# table combat_attribute
# remplace les valeurs de nocturnal par True et False -- NE FONCTIONNE PAS  ---
try:
    cursor.execute("""
        UPDATE combat_attribute
        SET nocturnal = CASE 
            WHEN LOWER(nocturnal) = 'yes' THEN TRUE
            ELSE FALSE
        END;
    """)
except mysql.connector.Error as err:
    print(f"Erreur lors de la mise à jour de la colonne nocturnal : {err}")
# Supprime les doublons d'id
cursor.execute("""
    DELETE t1 FROM combat_attribute t1
    INNER JOIN combat_attribute t2 
    WHERE 
        t1.id < t2.id AND 
        t1.id = t2.id;
""")


# table hidden_attribute
cursor.execute("ALTER TABLE hidden_attribute DROP COLUMN is_pal;")


# table refresh_area
cursor.execute("ALTER TABLE refresh_area DROP COLUMN empty_1;")
cursor.execute("ALTER TABLE refresh_area DROP COLUMN empty_2;")
cursor.execute("ALTER TABLE refresh_area DROP COLUMN id_2;")
cursor.execute("ALTER TABLE refresh_area DROP COLUMN id_3;")
cursor.execute("ALTER TABLE refresh_area DROP COLUMN name_2;")
cursor.execute("ALTER TABLE refresh_area DROP COLUMN name_3;")
cursor.execute("ALTER TABLE refresh_area DROP COLUMN minimum_level_2;")
cursor.execute("ALTER TABLE refresh_area DROP COLUMN maximum_level_2;")
cursor.execute("ALTER TABLE refresh_area DROP COLUMN palu_refresh_type_2;")
cursor.execute("ALTER TABLE refresh_area DROP COLUMN night_only_2;")
cursor.execute("ALTER TABLE refresh_area DROP COLUMN refresh_area_2;")


# tabel ordinary_boss
cursor.execute("ALTER TABLE ordinary_boss DROP COLUMN name_2;")
cursor.execute("ALTER TABLE ordinary_boss DROP COLUMN name_3;")

# ----------------  FIN DU NETTOYAGE DES TABLES EN SQL  ------------

cursor.close()
close(conn)

