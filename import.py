import os
import csv
import gdown
from db import connect, close
from tables import (create_combat_attribute_table,
                    create_job_skill_table, 
                    create_hidden_attribute_table,
                    create_refresh_area_table,
                    create_ordinary_boss_table,
                    create_tower_boss_table)

def download_csv_from_drive(drive_folder_url, local_path):
    gdown.download_folder(url=drive_folder_url, output=local_path, quiet=False)

def import_csv_to_db(csv_file_path, table_name):
    con = connect()
    if con is None:
        print("Failed to connect to the database.")
        return
    
    cursor = con.cursor()

    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the header row
        header = next(csv_reader)  

        placeholders = ', '.join(['%s'] * len(header))
        columns = ', '.join(header)

        for row in csv_reader:
            cursor.execute(f"""
                INSERT INTO {table_name} (
                    Chinese_name, Name, code_name, IsPal, Tribe, BPClass, Variant, Volume_size, Rarity, Element1, Element2, Genus_category, Organisation, Weapon, Weapon_equip, Noctumal, `4D_total`, HP, Melee_attack, Remote_attack, Defense, Support, Speed_of_work, Level_1, Level_20, Level_50, Air_response, Al_sight_response, Endurance, Slow_walking_speed, Walking_speed, Running_speed, Riding_sprint_speed, Being_damage_multiplier, Catch_rate, Experience_multiplier, Price, Must_bring_entry_1, Must_bring_entry_2, Numerical_description, lv1, lv2, lv3, lv4, lv5, Skill_description
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, row)
    
    con.commit()
    cursor.close()
    close(con)
    print(f"Data imported successfully into table {table_name}.")

if __name__ == "__main__":
    drive_folder_url = 'https://drive.google.com/drive/folders/1K2xq7ShnBIJ-Hj9S3_sXobj2HNACk2mF'
    local_path = 'downloaded_csv_files'

    
    download_csv_from_drive(drive_folder_url, local_path)

    csv_files_and_tables = [
        ('Palworld_Data--Palu combat attribute table.csv',           'combat_attribute'),
        ('Palworld_Data--Palu refresh level.csv',                    'refresh_area'),
        ('Palworld_Data-comparison of ordinary BOSS attributes.csv', 'ordinary_boss_attribute'),
        ('Palworld_Data-hide pallu attributes.csv',                  'hidden_attribute'),
        ('Palworld_Data-Palu Job Skills Table.csv  ',                'job_skill'),
        ('Palworld_Data-Tower BOSS attribute comparison.csv',        'tower_boss_attribute')
    ]


    # # Create tables
    # create_combat_attribute_table()
    # create_refresh_area_table()
    # create_job_skill_table()
    # create_hidden_attribute_table()
    # create_ordinary_boss_table()
    # create_tower_boss_table()

    # Import data
    for csv_file, table_name in csv_files_and_tables:
        csv_file_path = os.path.join(local_path, csv_file)
        import_csv_to_db(csv_file_path, table_name)
