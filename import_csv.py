import mysql.connector
from dotenv import load_dotenv
from db import connect, close
import os
import csv
from tables import (create_combat_attribute,
                    create_job_skill, 
                    create_hidden_attribute,
                    create_refresh_area,
                    create_ordinary_boss,
                    create_tower_boss)

'''
Gets connection parameters from .env and db.py
Gets the table structure from tables.py

Imports the data from raw_data
Fills the tables with the data
'''
def import_csv_to_db(csv_file_name, table_name):
    conn = connect()
    if conn is None:
        print("Failed to connect to the database.")
        return
    
    cursor = conn.cursor()

    with open(csv_file_name, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the header row
        header = next(csv_reader)  

        placeholders = ', '.join(['%s'] * len(header))
        columns = ', '.join(header)

        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        for row in csv_reader:
            cursor.execute(insert_query, row)
    
    conn.commit()
    cursor.close()
    close(conn)
    print(f"Data imported successfully into table {table_name}.")


if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor(buffered=True)

    path = 'raw_data'

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
        csv_file_name = os.path.join(path, csv_file)
        print(csv_file_name)
        import_csv_to_db(csv_file_name, table_name)

    print("Les données ont été importées avec succès dans les tables.")
