import mysql.connector
from dotenv import load_dotenv
import os

# Loads variables from .env (password, user_id, database name...)
load_dotenv()

# Configure connection to DB
db_config = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': int(os.getenv('DB_PORT', 3306))  # port 3306 by default, convert into integer
}

# Global variable, to be called in every function linked to the table
connection = None

def connection():
    global connection
    try:
        connection = mysql.connector.connect(host='host', database='palworld_database', user='root', password='root')

        if connection.is_connected():
            print("Connexion réussie à la base de données")
            # REQUESTS SHOULD GO HERE
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")

def add_table():
    global connection
    pass

def close_connection():
    global connection
    if connection.is_connected():
        connection.close()
        print("La connexion à la base de données a été fermée")






# Connection
connection()

add_table()
# Close connection
close_connection()