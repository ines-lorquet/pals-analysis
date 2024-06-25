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
CREATE TABLE job_skill (
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
CREATE TABLE hidden_attribute(
    Chinese_name VARCHAR(255),
    code_name VARCHAR(255),
    OverrideNameTextID VARCHAR(255),
    NamePrefixID VARCHAR(255),
    OverridePartnerSkillTextID VARCHAR(255),
    IsPal BOOLEAN,
    Tribe VARCHAR(255),
    BPClass VARCHAR(255),
    Pictorial_ID BIGINT,
    ZukanIndexSuffix DOUBLE PRECISION,
    Size VARCHAR(255),
    rarity BIGINT,
    Element1 VARCHAR(255),
    Element2 VARCHAR(255),
    GenusCategory VARCHAR(255),
    Organization VARCHAR(255),
    weapon VARCHAR(255),
    WeaponEquip BOOLEAN,
    HP BIGINT,
    melee_attack BIGINT,
    Remote_attack BIGINT,
    defense BIGINT,
    support BIGINT,
    CraftSpeed BIGINT,
    being_damage_multiplier VARCHAR(255),
    Capture_probability VARCHAR(255),
    Experience_multiplier BIGINT,
    price BIGINT,
    AIRResponse VARCHAR(255),
    AISightResponse DOUBLE PRECISION,
    slow_walking_speed BIGINT,
    walking_speed BIGINT,
    running_speed BIGINT,
    Riding_sprint_speed BIGINT,
    Handling_speed BIGINT,
    IsBoss BOOLEAN,
    IsTowerBoss BOOLEAN,
    BattleBGM VARCHAR(255),
    IgnoreLeanBack BOOLEAN,
    IgnoreBlowAway BOOLEAN,
    MaxFullStomach BIGINT,
    FullStomachDecreaseRate BIGINT,
    FoodAmount BIGINT,
    ViewingDistance BIGINT,
    ViewingAngle BIGINT,
    HearingRate BIGINT,
    NooseTrap BOOLEAN,
    Nocturnal BOOLEAN,
    BiologicalGrade BIGINT,
    Predator BOOLEAN,
    Edible BOOLEAN,
    endurance BIGINT,
    Male_probability BIGINT,
    fecundity BIGINT,
    Breathing_fire BIGINT,
    watering BIGINT,
    planting BIGINT,
    generate_electricity BIGINT,
    manual BIGINT,
    collection BIGINT,
    logging BIGINT,
    Mining BIGINT,
    OilExtraction_not_shown_in_game BIGINT,
    pharmaceutical BIGINT,
    cool_down BIGINT,
    carry BIGINT,
    pasture BIGINT,
    Passive_skill_1 VARCHAR(255),
    Passive_skill_2 VARCHAR(255),
    Passive_skill_3 DOUBLE PRECISION,
    Passive_skill_4 DOUBLE PRECISION
);
"""

create_refresh_area = """
CREATE TABLE refresh_area (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    minimum_level INT,
    maximum_level INT,
    fecundity INT,
    palu_refresh_type VARCHAR(50),
    night_only BOOLEAN,
    refresh_area VARCHAR(50)
);
"""

create_ordinary_boss = """
CREATE TABLE ordinary_boss (
    name VARCHAR(50),
    hp INT,
    remote_attack INT,
    riding_speed INT
);
"""
# Ines
create_tower_boss = """
    CREATE TABLE tower_boss (
    name VARCHAR(50),
    hp INT,
    melee_attack INT,
    remote_attack INT,
    defense INT,
    support INT,
    experience_ratio INT,
    slow_walking_speed INT,
    walking_speed INT,
    running_speed INT,
    riding_speed INT,
    handling_speed INT,
    ignore_bluntness BOOLEAN,
    ignore_displacement BOOLEAN,
    biological_grade INT,
    endurance INT,
    fecundity INT
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


