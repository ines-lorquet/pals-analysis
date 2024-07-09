# import pandas as pd
# from dotenv import load_dotenv
# from db import connect, close

# load_dotenv()

import mysql.connector
import pandas as pd

host = 'localhost'
userdb = 'root'
password = 'azerty'
database = 'palworld_database'

def connect():
    connection = mysql.connector.connect(
        host=host,
        user=userdb,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    return connection, cursor

def disconnect(connection, cursor):
    cursor.close()
    connection.close()



def disconnect(connection, cursor):
    cursor.close()
    connection.close()

def fetch(query, params=None):
    connection, cursor = connect()
    cursor.execute(query, params or ())
    result = cursor.fetchall()
    disconnect(connection, cursor)
    return result

def fetch_one(query, params=None):
    connection, cursor = connect()
    cursor.execute(query, params or ())
    result = cursor.fetchone()
    disconnect(connection, cursor)
    return result

# a
def count_size():
    sql = "SELECT Size, COUNT(*) FROM `hidden-attribute` GROUP BY Size ORDER BY COUNT(*) DESC;"
    return fetch_one(sql)

# b
def count_category():
    sql = "SELECT GenusCategory, COUNT(*) FROM `hidden-attribute` GROUP BY GenusCategory ORDER BY COUNT(*) DESC;"
    return fetch_one(sql)

# c
def count_hp():
    sql = "SELECT HP, COUNT(*) FROM `hidden-attribute` GROUP BY HP ORDER BY COUNT(*) DESC;"
    return fetch_one(sql)

# d
def count_rarity():
    sql = "SELECT rarity, COUNT(*) FROM `combat-attribute` GROUP BY rarity ORDER BY COUNT(*) DESC;"
    return fetch_one(sql)

# e
def count_food():
    sql = "SELECT `Food intake`, COUNT(*) FROM `job-skill` GROUP BY `Food intake` ORDER BY COUNT(*) DESC;"
    return fetch_one(sql)

# f
def select_items():
    sql = "SELECT `English name` FROM `job-skill` WHERE `ranch items` IS NOT NULL;"
    return fetch(sql)

# g
def count_melee():
    sql = "SELECT melee_attack, COUNT(*) AS count FROM combat_attribute GROUP BY melee_attack ORDER BY melee_attack;"
    return fetch(sql)

def count_remote():
    sql = "SELECT remote_attack, COUNT(*) AS count FROM combat_attribute GROUP BY remote_attack ORDER BY remote_attack;"
    return fetch(sql)

def count_defense():
    sql = "SELECT defense, COUNT(*) AS count FROM combat_attribute GROUP BY defense ORDER BY defense;"
    return fetch(sql)

def top_10_pals():
    sql = "SELECT ID, melee_attack, remote_attack, defense, (melee_attack + remote_attack + defense) AS total_power FROM combat_attribute ORDER BY total_power DESC LIMIT 10;"
    return fetch(sql)

# h pip install pandas scipy
#  1 indique une corrélation positive parfaite.
# -1 indique une corrélation négative parfaite.
#  0 indique aucune corrélation.
def select_attack():
    sql="SELECT melee_attack, remote_attack, defense FROM combat_attribute;"
    return fetch(sql)

def calculate_combat_attribute_correlations():
    data = select_attack()
    df = pd.DataFrame(data, columns=['melee_attack', 'remote_attack', 'defense'])
    correlation_matrix = df.corr()
    return correlation_matrix

# i




print(count_size())
print(count_category())
print(count_hp())
print(count_rarity())
print(count_food())
print(select_items())
print(count_melee())
print(count_remote())
print(count_defense())
print(top_10_pals())

correlation_matrix = calculate_combat_attribute_correlations()
print(correlation_matrix)
