import mysql.connector
from dotenv import load_dotenv
import os
import math

# Loads variables from .env (password, user_id, database name...)
load_dotenv()

def connect():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=int(os.getenv('DB_PORT', 3306))
    )
    cursor = connection.cursor()
    return connection, cursor

def disconnect(connection, cursor):
    cursor.close()
    connection.close()

def fetch(query, params=None):
    connection, cursor = connect()
    cursor.execute(query, params or ())
    result = cursor.fetchall()
    # disconnect(connection, cursor)
    return result

def fetch_one(query, params=None):
    connection, cursor = connect()
    cursor.execute(query, params or ())
    result = cursor.fetchone()
    # disconnect(connection, cursor)
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
    sql = "SELECT rarity, COUNT(*) FROM `combat_attribute` GROUP BY rarity ORDER BY COUNT(*) DESC;"
    return fetch_one(sql)

# e
def count_food():
    sql = "SELECT `Food intake`, COUNT(*) FROM `job_skill` GROUP BY `Food intake` ORDER BY COUNT(*) DESC;"
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

# h
def select_attack():
    sql = "SELECT melee_attack, remote_attack, defense FROM combat_attribute;"
    return fetch(sql)

def mean(values):
    return sum(values) / len(values)

def stddev(values, mean_value):
    return math.sqrt(sum((x - mean_value) ** 2 for x in values) / len(values))

def pearson_correlation(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    stddev_x = stddev(x, mean_x)
    stddev_y = stddev(y, mean_y)
    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))) / len(x)
    return covariance / (stddev_x * stddev_y)

def calculate_combat_attribute_correlations():
    data = select_attack()
    melee_attacks = [row[0] for row in data]
    remote_attacks = [row[1] for row in data]
    defenses = [row[2] for row in data]

    corr_melee_remote = pearson_correlation(melee_attacks, remote_attacks)
    corr_melee_defense = pearson_correlation(melee_attacks, defenses)
    corr_remote_defense = pearson_correlation(remote_attacks, defenses)

    return {
        'melee_remote': corr_melee_remote,
        'melee_defense': corr_melee_defense,
        'remote_defense': corr_remote_defense
    }

# i
""" pas encore"""

# j
def get_average_rarity_of_top_power_pals():
    query = """
        WITH MaxTotalPower AS (
            SELECT 
                MAX(total_power) AS max_power
            FROM combat_attribute
        ),
        TopPals AS (
            SELECT 
                rarity
            FROM combat_attribute
            WHERE total_power = (SELECT max_power FROM MaxTotalPower)
        )
        SELECT 
            AVG(rarity) AS average_rarity
        FROM TopPals;
    """
    result = fetch_one(query)
    return result[0] if result else None

# k
"""pas encore"""

# l

# m

#n

# o

# p
def count_night():
    sql = "SELECT COUNT(*) FROM job_skill WHERE night_shift = 'yes';"
    return fetch(sql)
# q

# r

# s
def max_speed():
    sql = "SELECT English name,Handling speed FROM job_skill WHERE Handling speed = (SELECT MAX(Handling speed) FROM job_skill);"
    return fetch_one(sql)
# t

# v

# w
def count_area():
    sql = "SELECT refresh_area, COUNT(*) AS nombre_d_apparitions FROM refresh_area GROUP BY refresh_area ORDER BY nombre_d_apparitions DESC;"
    return fetch_one(sql)


#a
print(count_size())
#b
print(count_category())
#c
print(count_hp())
#d
print(count_rarity())
#'e
print(count_food())
#f
print(select_items())
#g
print(count_melee())
print(count_remote())
print(count_defense())
print(top_10_pals())
#h
correlation_matrix = calculate_combat_attribute_correlations()
print(correlation_matrix)
#i
#...  
# j
average_rarity = get_average_rarity_of_top_power_pals()
print(f"Rareté moyenne des Pals ayant la puissance d'attaque totale la plus élevée : {average_rarity}")

#s
print(max_speed())
#t
 
#u

#v

#w
print(count_area())
connection, cursor = connect()
disconnect(connection, cursor)
