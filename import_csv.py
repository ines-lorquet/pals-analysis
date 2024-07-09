import mysql.connector
from dotenv import load_dotenv
import os
import csv
from db import connect, close  

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
        header = next(csv_reader)
        
        columns = ', '.join(header)
        placeholders = ', '.join(['%s'] * len(header))

        # insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        insert_query = f"INSERT IGNORE INTO {table_name} ({columns}) VALUES ({placeholders})"


        for row in csv_reader:
            # Remplacer les valeurs vides par None (ce qui devient NULL dans MySQL)
            row = [None if val == '' else val for val in row]
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

    # Fichiers .csv et tables correspondantes
    csv_files_and_tables = [
        ('Palworld_Data--Palu combat attribute table.csv',           'combat_attribute'),
        ('Palworld_Data--Palu refresh level.csv',                    'refresh_area'),
        ('Palworld_Data-comparison of ordinary BOSS attributes.csv', 'ordinary_boss'),
        ('Palworld_Data-hide pallu attributes.csv',                  'hidden_attribute'),
        ('Palworld_Data-Palu Job Skills Table.csv',                  'job_skill'),
        ('Palworld_Data-Tower BOSS attribute comparison.csv',        'tower_boss')
    ]

    # Importation des données
    for csv_file, table_name in csv_files_and_tables:
        csv_file_name = os.path.join(path, csv_file)
        print(f"Importation des données depuis {csv_file_name} vers la table {table_name}...")
        import_csv_to_db(csv_file_name, table_name)




    # -----------------------NETTOYAGE DES TABLES EN SQL---------------

    # COMBAT_ATTRIBUTE

    # remplace les valeurs 'yes' de la colonne nocturnal par 1, et les NULL par 0
    # -------------NE FONCTIONNE PAS---------------------------------------------
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

    # HIDDEN_ATTRIBUTE
    cursor.execute("ALTER TABLE hidden_attribute DROP COLUMN is_pal;")


    # REFRESH_AREA
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


    # ORDINARY_BOSS
    cursor.execute("ALTER TABLE ordinary_boss DROP COLUMN name_2;")
    cursor.execute("ALTER TABLE ordinary_boss DROP COLUMN name_3;")








    cursor.close()
    close(conn)

