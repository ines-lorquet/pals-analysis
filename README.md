# pals-analysis
## Etude des caractéristiques et du comportement de ces créatures.


Juin 2024

ATTENTION :
Les identifiants de connexion à la base de données sont dans le fichier .env  
Ce fichier ne doit pas être sur github, car c'est un repo public.

Pour que les script ai accès aux variables d'environnement (identifiants de connexion), il faut :  
- Le fichier .env
- Installer Le package dotenv
- Appeler .env dans db.py

Pour installez python-dotenv via pip :
```sh
pip install python-dotenv
``` 

## Contexte

A partir d'un dataset obtenu après une extraction des données du jeu, nous avons accès à des informations précises et en temps réel des Pals :

- attributs
- comportements
- compétences
- nature
- force
- etc...


## Création et manipulation d'une base de données avec [mysql](https://www.mysql.com/fr/).

### Création de 6 tables :

1. combat-attribute,
2. job-skill,
3. hidden-attribute,
4. refresh-area,
5. ordinary-boss-attribute,
6. tower-boss-attribute.

### Nettoyage des tables de la base de données.
Traitement des valeurs manquantes.
Normalisation des formats.
Correction des erreurs.
Suppression des des redondances.

## analyse exploratoire

Utilisation de SQL pour le traitement des données et de Python pour la création de visuels pertinents.

a. Quelle est la distribution de la taille des Pals ?  
b. Quelle est la distribution de la catégorie des Pals ?  
c. Quelle est la distribution des points de vie des Pals ?  
d. Quelle est la distribution de la rareté des Pals ?  
e. Quelle est la distribution de la consommation alimentaire des Pals ?  
f. Quels sont les Pals pouvant offrir des produits utiles à votre campement grâce au ranch (laine, oeuf, lait, ...) ?  
g. Quelle est la distribution de la puissance de combat parmi les Pals ? Fournissez une liste des 10 Pals les plus puissants (selon l’attaque, la défense,...).  
h. Quelles sont les corrélations entre les différents attributs de combat ?  
i. Comment la rareté d'un Pal affecte-t-elle les valeurs de ses attributs de base ?  
j. Quelle est la rareté moyenne des Pals ayant la puissance d'attaque la plus élevée ?  
k. La taille des Pals affecte-t-elle leur performance au combat ?  
l. Les Pals les plus rapides sont-ils généralement plus efficaces au combat ?  
m. Comment former l'équipe la plus équilibrée en combinant des Pals aux attributs complémentaires ? Proposez une équipe équilibrée de 5 Pals.  
n. Quelles sont les compétences de travail les plus répandues chez les Pals ?  
o. Quelles sont les compétences de travail les moins répandues chez les Pals ?  
p. Combien de Pals conviennent au travail de nuit ?  
q. Quelles sont les caractéristiques communes des Pals qui conviennent au travail de nuit ?  
r. Quelle est la rareté moyenne des Pals possédant le plus de compétences ?  
s. Quels sont les Pals qui ont la vitesse de travail la plus élevée ?  
t. Quels sont les Pals dont la probabilité de capture est la plus élevée ?  Comment cette information peut-elle être utilisée pour élaborer une stratégie de capture dans le jeu ?  
u. Quel Ordinary Boss ou Tower Boss a le score d'attributs de combat combinés le plus élevé ?  
v. Quelle est la répartition des niveaux d’apparition des Pals ?  
w. Quelle est la répartition des zones d’apparition ?  
x. De nombreuses autres observations peuvent être réalisées à l’aide des données et ne se limitent pas à la liste ci-dessus.  
y. Recherches et une étude complémentaire.
z. Conclusions.  
