import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
# from mysql.connector import Error
# import pandas as pd

# Configuration de la connexion à la base de données MySQL
db_config = {
    'host'= DB_HOST,
    'database'= DB_NAME,
    'user'= DB_USER,
    'password'= DB_PASSWORD
}

# db_config = {
#     'host': DB_HOST,
#     'database': DB_NAME,
#     'user': DB_USER,
#     'password': DB_PASSWORD
# }
