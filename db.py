import mysql.connector
from dotenv import load_dotenv
import os

# Loads variables from .env
load_dotenv()

# Configure connection to DB
db_config = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

# Example 
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Connexion réussie à la base de données")
        # REQUESTS
except mysql.connector.Error as err:
    print(f"Erreur: {err}")
finally:
    if connection.is_connected():
        connection.close()
        print("La connexion à la base de données a été fermée")
