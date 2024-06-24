import mysql.connector
from dotenv import load_dotenv
import os

# Loads variables from .env (password, user_id, database name...)
load_dotenv()



# Global variable, to be called in every function linked to the table
# connection = None

def connect():
    # global connection
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port= 3306,
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        print(connection)

        if connection.is_connected():
            print("Connexion réussie à la base de données")
            return connection
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")



def close():
    global connection
    if connection.is_connected():
        connection.close()
        print("La connexion à la base de données a été fermée")


##############################################
if __name__ == "__main__":
    # Connection
    connect()

    # Close connection
    # close_connection()

