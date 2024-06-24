import mysql.connector
from dotenv import load_dotenv
import os

# Loads variables from .env to connect to database
load_dotenv()

def connect():
    try:
        con = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port= int(os.getenv('DB_PORT')),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        print(con)

        if con.is_connected():
            print("Connexion réussie à la base de données")
            return con
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")

def close(con):
    if con.is_connected():
        con.close()
        print("La connexion à la base de données a été fermée")


##############################################
if __name__ == "__main__":
    con = connect()
    close(con)
