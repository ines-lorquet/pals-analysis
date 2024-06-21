import csv
from csv_name import *

def clean_csv(file_path, rows_to_skip):
    with open(file_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        data = list(reader)

    # Skip the specified number of rows
    cleaned_data = data[rows_to_skip:]

    with open(file_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_data)

# Fichiers CSV à traiter et nombre de lignes à supprimer
files_to_clean = [
    (combat_attribute, 1),
    (refresh_level, 4),
    (ordinary_BOSS_attributes, 3),
    (Palu_Job_Skills_Table, 1)
]

# Traiter chaque fichier
for file_path, rows_to_skip in files_to_clean:
    clean_csv(file_path, rows_to_skip)

print("Les fichiers CSV ont été nettoyés et enregistrés avec succès.")
