import pandas as pd


# nregistrer le fichier csvdans une variable
combat_attribute_df = pd.read_csv('raw_data/Palworld_Data--Palu combat attribute table.csv')
# affiche les 5 première lignes pour vérifier l'import
# print(combat_attribute_df.head())

# Vérifier si toutes les valeurs sont identiques
if combat_attribute_df['ispal'].nunique() == 1:
    print("Toutes les valeurs sont identiques.")
else:
    print("Toutes les valeurs ne sont pas identiques.")