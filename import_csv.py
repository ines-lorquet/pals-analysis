import mysql.connector
from dotenv import load_dotenv
import os
import csv
from db import connect, close  # Assurez-vous que ces fonctions sont correctement implémentées dans db.py
from tables import (create_combat_attribute,
                    create_job_skill, 
                    create_hidden_attribute,
                    create_refresh_area,
                    create_ordinary_boss,
                    create_tower_boss)

'''
Récupère les paramètres de connexion depuis .env et db.py
Obtient la structure de table depuis tables.py

Importe les données depuis raw_data
Remplit les tables avec les données
'''
def import_csv_to_db(csv_file_name, table_name):
    conn = connect()
    if conn is None:
        print("Échec de la connexion à la base de données.")
        return
    
    cursor = conn.cursor()

    with open(csv_file_name, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Lire l'en-tête
        
        columns = ', '.join(header)
        placeholders = ', '.join(['%s'] * len(header))

        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        for row in csv_reader:
            try:
                cursor.execute(insert_query, row)
            except mysql.connector.Error as err:
                print(f"Erreur lors de l'insertion dans la table {table_name}: {err}")
    
    conn.commit()
    cursor.close()
    close(conn)
    print(f"Données importées avec succès dans la table {table_name}.")



if __name__ == "__main__":
    conn = connect()
    if conn is None:
        print("Échec de la connexion à la base de données principale.")
        exit(1)

    cursor = conn.cursor(buffered=True)

    path = 'raw_data'

    # Création des tables si elles n'existent pas déjà
    cursor.execute(create_combat_attribute)
    cursor.execute(create_job_skill)
    cursor.execute(create_hidden_attribute)
    cursor.execute(create_refresh_area)
    cursor.execute(create_ordinary_boss)
    cursor.execute(create_tower_boss)

    # Fichiers .csv et tables correspondantes
    csv_files_and_tables = [
        ('Palworld_Data--Palu combat attribute table.csv',           'combat_attribute'),
        ('Palworld_Data--Palu refresh level.csv',                    'refresh_area'),
        ('Palworld_Data-comparison of ordinary BOSS attributes.csv', 'ordinary_boss_attribute'),
        ('Palworld_Data-hide pallu attributes.csv',                  'hidden_attribute'),
        ('Palworld_Data-Palu Job Skills Table.csv',                  'job_skill'),
        ('Palworld_Data-Tower BOSS attribute comparison.csv',        'tower_boss_attribute')
    ]

    # Importation des données
    for csv_file, table_name in csv_files_and_tables:
        csv_file_name = os.path.join(path, csv_file)
        print(f"Importation des données depuis {csv_file_name} vers la table {table_name}...")
        import_csv_to_db(csv_file_name, table_name)

    cursor.close()
    close(conn)
    print("Les données ont été importées avec succès dans les tables.")
