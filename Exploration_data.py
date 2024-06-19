import mysql.connector
from mysql.connector import Error
import pandas as pd

# Configuration de la connexion à la base de données MySQL
db_config = {
    'host': 'localhost',
    'database': 'palworld_database',
    'user': 'root',
    'password': 'root'
}

# Chemins vers les fichiers CSV contenant les données
csv_files = {
    'combat_attribute': 'data/Palworld_Data--Palu combat attribute table.csv',
    'job_skill': 'data/Palworld_Data-Palu Job Skills Table.csv',
    'hidden_attribute': 'data/Palworld_Data-hide pallu attributes.csv',
    'refresh_area': 'data/Palworld_Data--Palu refresh level.csv',
    'ordinary_boss_attribute': 'data/Palworld_Data-comparison of ordinary BOSS attributes.csv',
    'tower_boss_attribute': 'data/Palworld_Data-Tower BOSS attribute comparison.csv'
}

# Colonnes spécifiques pour chaque table (ajustez selon vos fichiers CSV)
table_columns = {
    'combat_attribute': ['Column1', 'Column2', 'Column3', ...],  # Remplacez par les vrais noms de colonnes
    'job_skill': ['Column1', 'Column2', 'Column3', ...],
    'hidden_attribute': ['Column1', 'Column2', 'Column3', ...],
    'refresh_area': ['Column1', 'Column2', 'Column3', ...],
    'ordinary_boss_attribute': ['Column1', 'Column2', 'Column3', ...],
    'tower_boss_attribute': ['Column1', 'Column2', 'Column3', ...]
}

def import_data_to_mysql(table_name, file_path, columns):
    try:
        # Connexion à la base de données MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Lecture du fichier CSV en spécifiant les noms de colonnes
        df = pd.read_csv(file_path, skiprows=1, names=columns)

        # Conversion du DataFrame pandas en liste de tuples (valeurs de lignes)
        data = df.to_records(index=False).tolist()

        # Création de la requête SQL pour l'insertion des données
        sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"

        # Insertion des données dans la base de données
        cursor.executemany(sql, data)
        connection.commit()

        print(f"Données importées avec succès dans la table '{table_name}' de la base de données '{db_config['database']}'.")

    except Error as e:
        print(f"Erreur lors de l'importation des données dans la table '{table_name}': {e}")

    finally:
        # Fermeture du curseur et de la connexion à la base de données
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Importation des données pour chaque table
for table_name, csv_file_path in csv_files.items():
    import_data_to_mysql(table_name, csv_file_path, table_columns.get(table_name, []))
