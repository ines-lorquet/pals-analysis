import mysql.connector
from dotenv import load_dotenv
from db import connect, close
import os
from cleaning_csv import *
import csv
from tables import (create_combat_attribute,
                    create_job_skill, 
                    create_hidden_attribute,
                    create_refresh_area,
                    create_ordinary_boss,
                    create_tower_boss)


load_dotenv()
con = connect()
cursor = con.cursor(buffered=True)

path = 'processed_data'

# Create tables
cursor.execute(create_combat_attribute)
cursor.execute(create_job_skill)
cursor.execute(create_hidden_attribute)
cursor.execute(create_refresh_area)
cursor.execute(create_ordinary_boss)
cursor.execute(create_tower_boss)

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
for csv_file, table_name in csv_files_and_tables:
    csv_file_path = os.path.join(path, csv_file)
    import_csv_to_db(csv_file_path, table_name)

print("Les données ont été importées avec succès dans les tables.")
