import mysql.connector
from db import connect


'''6 requests to create 6 empty tables with the appropriate columns to fit the .csv files''' 

create_combat_attribute ="""
CREATE TABLE IF NOT EXISTS combat_attribute (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    chinese_name VARCHAR(255),
    name VARCHAR(255),
    codename VARCHAR(255),
    overridenametextid VARCHAR(255),
    nameprefixid VARCHAR(255),
    overridepartnerskilltextid VARCHAR(255),
    ispal BOOLEAN,
    tribe VARCHAR(255),
    bpclass VARCHAR(255),
    variant VARCHAR(255),
    volume_size VARCHAR(255),
    rarity INT,
    element_1 VARCHAR(255),
    element_2 VARCHAR(255),
    genuscategory VARCHAR(255),
    organization VARCHAR(255),
    weapon VARCHAR(255),
    weaponequip VARCHAR(255),
    nocturnal BOOLEAN,
    d4_total INT,
    hp INT,
    melee_attack INT,
    remote_attack INT,
    defense INT,
    support INT,
    speed_of_work INT,
    level_1 VARCHAR(255),
    level_20 VARCHAR(255),
    level_50 VARCHAR(255),
    airresponse VARCHAR(255),
    aisightresponse VARCHAR(255),
    endurance INT,
    slow_walking_speed INT,
    walking_speed INT,
    running_speed INT,
    riding_sprint_speed INT,
    being_damage_multiplier VARCHAR(255),
    catch_rate VARCHAR(255),
    experience_multiplier VARCHAR(255),
    price INT,
    must_bring_entry_1 VARCHAR(255),
    must_bring_entry_2 VARCHAR(255),
    numerical_description VARCHAR(255),
    lv1 INT,
    lv2 INT,
    lv3 INT,
    lv4 INT,
    lv5 INT,
    skill_description TEXT
);
"""

create_job_skill = """
CREATE TABLE IF NOT EXISTS job_skill (
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

create_hidden_attribute = """
CREATE TABLE IF NOT EXISTS hidden_attribute(
    chinese_name VARCHAR(255),
    code_name VARCHAR(255),
    override_name_text_id VARCHAR(255),
    name_prefix_id VARCHAR(255),
    override_partner_skill_text_id VARCHAR(255),
    is_pal BOOLEAN,
    tribe VARCHAR(255),
    bp_class VARCHAR(255),
    pictorial_id BIGINT,
    zukan_index_suffix INT,
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
    ai_sight_response VARCHAR(255),
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
    passive_skill_3 VARCHAR(255),
    passive_skill_4 VARCHAR(255)
);


"""

# create_refresh_area = """
# CREATE TABLE IF NOT EXISTS refresh_area (
#     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(50),
#     `minimum_level` INT,
#     `maximum_level` INT,
#     empty1 INT,
#     fecundity INT,
#     `level` INT,
#     palu_refresh_type VARCHAR(50),
#     night_only BOOLEAN,
#     refresh_area VARCHAR(50)
# );
# """
# LE CSV COMPORTE DES DOUBLON DE COLONNES
create_refresh_area = """
CREATE TABLE IF NOT EXISTS refresh_area (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    minimum_level INT,
    maximum_level INT,
    empty_1 INT,
    id_2 INT,
    name_2 VARCHAR(255),
    minimum_level_2 INT,
    fecundity INT,
    palu_refresh_type_2 VARCHAR(255),
    night_only BOOLEAN,
    refresh_area VARCHAR(255),
    empty_2 INT,
    id_3 INT,
    name_3 VARCHAR(255),
    maximum_level_2 INT,
    palu_refresh_type VARCHAR(255),
    night_only_2 BOOLEAN,
    refresh_area_2 VARCHAR(255)
)
"""

create_ordinary_boss = """
CREATE TABLE IF NOT EXISTS ordinary_boss (
    name_2 VARCHAR(50),
    hp INT,
    empty_1 INT,
    name_3 VARCHAR(50),
    remote_attack INT,
    empty_2 VARCHAR(50),
    name VARCHAR(50),
    riding_speed INT
);
"""

    
create_tower_boss = """
CREATE TABLE IF NOT EXISTS tower_boss (
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
    conn = connect()
    cursor = conn.cursor(buffered=True)

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
        if conn is not None and conn.is_connected():
            conn.close()


