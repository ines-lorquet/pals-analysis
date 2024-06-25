import mysql.connector
from dotenv import load_dotenv
from db import connect, close


# 6 requests to create 6 empty tables
create_combat_attribute = """
CREATE TABLE combat_attribute (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Chinese_name VARCHAR(50),
    Name VARCHAR(50),
    code_name VARCHAR(50) NOT NULL UNIQUE,
    IsPal BOOLEAN,
    Tribe VARCHAR(50),
    BPClass VARCHAR(50),
    Variant BOOLEAN,
    Volume_size VARCHAR(10),
    Rarity INT,
    Element1 VARCHAR(50),
    Element2 VARCHAR(50),
	Genus_category VARCHAR(50),
	Organisation VARCHAR(50),
	Weapon VARCHAR(50),
	Weapon_equip BOOLEAN,
	Noctumal BOOLEAN,
	`4D_total` INT,
	HP INT,
	Melee_attack INT,
	Remote_attack INT,
	Defense INT,
	Support INT,
	Speed_of_work INT,
	Level_1 INT,
	Level_20 INT,
	Level_50 INT,
	Air_response VARCHAR(50),
	Al_sight_response ENUM('none', 'other_value1', 'other_value2'),
	Endurance INT,
    Slow_walking_speed INT,
    Walking_speed INT,
    Running_speed INT,
    Riding_sprint_speed INT,
    Being_damage_multiplier VARCHAR(50),
    Catch_rate INT,
    Experience_multiplier VARCHAR(50),
    Price INT,
    Must_bring_entry_1 VARCHAR(50),
    Must_bring_entry_2 VARCHAR(50),
    Numerical_description VARCHAR(50),
    lv1 INT,
    lv2 INT,
    lv3 INT,
    lv4 INT,
    lv5 INT,
    Skill_description TEXT
)
"""

create_job_skill = """
    CREATE TABLE palu_combat_attribute (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    English_name VARCHAR(100),
    Chinese_name VARCHAR(100),
    Volume_size VARCHAR(50),
    Food_intake INT,
    Night_shift INT,
    Total_skills INT,
    Make_a_fire INT,
    Watering INT,
    Planting INT,
    Generate_electricity INT,
    Manual INT,
    Collection INT,
    Logging INT,
    Mining INT,
    Pharmaceutical INT,
    Cool_down INT,
    Pasture INT,
    Carry INT,
    Handling_speed INT,
    Ranch_items VARCHAR(50),
    Pasture_minimum_output INT,
    Largest_ranch ENUM('Rank', 'partner_skill_level')
);

"""
# Ines
create_hidden_attribute = """
    CREATE TABLE hidden_attribute (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    English_name VARCHAR(100),
);
"""

create_refresh_area = """
CREATE TABLE IF NOT EXISTS palu_refresh_level (
    ID FLOAT,
    name VARCHAR(255),
    minimum_level FLOAT,
    maximum_level FLOAT,
    Unnamed_4 FLOAT,
    ID_1 INT,
    name_1 VARCHAR(255),
    minimum_level_1 INT,
    fecundity INT,
    Pallu_refresh_type VARCHAR(255),
    Night_only VARCHAR(255),
    refresh_area VARCHAR(255),
    Unnamed_12 FLOAT,
    ID_2 FLOAT,
    name_2 VARCHAR(255),
    maximum_level_1 FLOAT,
    Pallu_refresh_type_1 VARCHAR(255),
    Night_only_1 VARCHAR(255),
    refresh_area_1 VARCHAR(255)
);
"""

create_ordinary_boss = """
    CREATE TABLE ordinary_boss (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    English_name VARCHAR(100),
);
"""
# Ines
create_tower_boss = """
    CREATE TABLE tower_boss (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    English_name VARCHAR(100),
);
"""



if __name__ == "__main__":

    load_dotenv()
    con = connect()
    cursor = con.cursor(buffered=True)

    try:
        cursor.execute(create_combat_attribute)
        cursor.execute(create_job_skill)
        cursor.execute(create_hidden_attribute)
        cursor.execute(create_refresh_area)
        cursor.execute(create_ordinary_boss)
        cursor.execute(create_tower_boss)


    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")

finally:
    # fermer la database une seule fois, a la fin
    if con is not None and con.is_connected():
        con.close()


