import mysql.connector
from dotenv import load_dotenv
from db import connect, close


# 6 requests to create 6 empty tables
create_combat_attribute = """
CREATE TABLE combat_attribute (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Chinese_name VARCHAR(50),
    name VARCHAR(50),
    code_name VARCHAR(50) NOT NULL UNIQUE,
    is_Pal BOOLEAN,
    tribe VARCHAR(50),
    bp_class VARCHAR(50),
    variant BOOLEAN,
    volume_size VARCHAR(10),
    rarity INT,
    element1 VARCHAR(50),
    element2 VARCHAR(50),
	genus_category VARCHAR(50),
	organisation VARCHAR(50),
	weapon VARCHAR(50),
	weapon_equip BOOLEAN,
	noctumal BOOLEAN,
	`4D_total` INT,
	hp INT,
	melee_attack INT,
	remote_attack INT,
	defense INT,
	support INT,
	speed_of_work INT,
	level_1 INT,
	level_20 INT,
	level_50 INT,
	air_response VARCHAR(50),
	al_sight_response ENUM('none', 'other_value1', 'other_value2'),
	endurance INT,
    slow_walking_speed INT,
    walking_speed INT,
    running_speed INT,
    riding_sprint_speed INT,
    being_damage_multiplier VARCHAR(50),
    catch_rate INT,
    experience_multiplier VARCHAR(50),
    price INT,
    must_bring_entry_1 VARCHAR(50),
    must_bring_entry_2 VARCHAR(50),
    numerical_description VARCHAR(50),
    lv1 INT,
    lv2 INT,
    lv3 INT,
    lv4 INT,
    lv5 INT,
    skill_description TEXT
)
"""

create_job_skill = """
CREATE TABLE job_skill (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    english_name VARCHAR(100),
    chinese_name VARCHAR(100),
    volume_size VARCHAR(50),
    food_intake INT,
    night_shift INT,
    total_skills INT,
    make_a_fire INT,
    watering INT,
    planting INT,
    generate_electricity INT,
    manual INT,
    collection INT,
    logging INT,
    mining INT,
    pharmaceutical INT,
    cool_down INT,
    pasture INT,
    carry INT,
    handling_speed INT,
    ranch_items VARCHAR(50),
    pasture_minimum_output INT,
    largest_ranch ENUM('Rank', 'partner_skill_level')
);

"""
# Ines
create_hidden_attribute = """
CREATE TABLE hidden_attribute(
    chinese_name VARCHAR(255),
    code_name VARCHAR(255),
    override_name_text_id VARCHAR(255),
    name_prefix_id VARCHAR(255),
    override_partner_skill_text_id VARCHAR(255),
    is_pal BOOLEAN,
    tribe VARCHAR(255),
    bp_class VARCHAR(255),
    pictorial_id BIGINT,
    zukan_index_suffix DOUBLE PRECISION,
    size VARCHAR(255),
    rarity BIGINT,
    element1 VARCHAR(255),
    element2 VARCHAR(255),
    genus_category VARCHAR(255),
    organization VARCHAR(255),
    weapon VARCHAR(255),
    weapon_equip BOOLEAN,
    hp BIGINT,
    melee_attack BIGINT,
    remote_attack BIGINT,
    defense BIGINT,
    support BIGINT,
    craft_speed BIGINT,
    being_damage_multiplier VARCHAR(255),
    capture_probability VARCHAR(255),
    experience_multiplier BIGINT,
    price BIGINT,
    air_response VARCHAR(255),
    ai_sight_response DOUBLE PRECISION,
    slow_walking_speed BIGINT,
    walking_speed BIGINT,
    running_speed BIGINT,
    riding_sprint_speed BIGINT,
    handling_speed BIGINT,
    is_boss BOOLEAN,
    is_tower_boss BOOLEAN,
    battle_bgm VARCHAR(255),
    ignore_lean_back BOOLEAN,
    ignore_blow_away BOOLEAN,
    max_full_stomach BIGINT,
    full_stomach_decrease_rate BIGINT,
    food_amount BIGINT,
    viewing_distance BIGINT,
    viewing_angle BIGINT,
    hearing_rate BIGINT,
    noose_trap BOOLEAN,
    nocturnal BOOLEAN,
    biological_grade BIGINT,
    predator BOOLEAN,
    edible BOOLEAN,
    endurance BIGINT,
    male_probability BIGINT,
    fecundity BIGINT,
    breathing_fire BIGINT,
    watering BIGINT,
    planting BIGINT,
    generate_electricity BIGINT,
    manual BIGINT,
    collection BIGINT,
    logging BIGINT,
    mining BIGINT,
    oil_extraction_not_shown_in_game BIGINT,
    pharmaceutical BIGINT,
    cool_down BIGINT,
    carry BIGINT,
    pasture BIGINT,
    passive_skill_1 VARCHAR(255),
    passive_skill_2 VARCHAR(255),
    passive_skill_3 DOUBLE PRECISION,
    passive_skill_4 DOUBLE PRECISION
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


