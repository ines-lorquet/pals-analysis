
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px


# Configuration
st.set_page_config(
    page_title="analyse des Pals",
    page_icon="img/pal-icon.webp",
    layout="wide",
    initial_sidebar_state="expanded")
alt.themes.enable("dark")

# Load data ----- TO BE UPDATED, WORK IN PROGRESS
df_1 = pd.read_csv('data/Palworld_Data--Palu combat attribute table.csv')
df_2 = pd.read_csv('data/Palworld_Data--Palu refresh level.csv')
df_3 = pd.read_csv('data/Palworld_Data-comparison of ordinary BOSS attributes.csv')
df_4 = pd.read_csv('data/Palworld_Data-hide pallu attributes.csv')
df_5 = pd.read_csv('data/Palworld_Data-Palu Job Skills Table.csv')
df_6 = pd.read_csv('data/Palworld_Data-Tower BOSS attribute comparison.csv')

######################################################

# Title
st.title('Analyse des Pals')

# Display data 1
st.write('Voici les données des fichiers .csv originaux :')
st.dataframe(df_1)
st.dataframe(df_2)
st.dataframe(df_3)
st.dataframe(df_4)
st.dataframe(df_5)
st.dataframe(df_6)


# # Display data 2
# st.write('Voici les données du deuxième fichier .csv :')
# st.dataframe(df_2)
# # Check the columnns
# if 'Unnamed:1' in df_2.columns and 'Unnamed:2' in df_2.columns:
#     # Converts column names inton  appropriate type if needed
#     df_2['Unnamed:1'] = df_2['Unnamed:1'].astype(str)
#     df_2['Unnamed:2'] = pd.to_numeric(df_2['Unnamed:2'], errors='coerce')


#     # With Altair
#     st.subheader('Visualisation avec Altair')
#     chart = alt.Chart(df_2).mark_bar().encode(
#         x='Unnamed:1',
#         y='Unnamed:2'
#     )
#     st.altair_chart(chart, use_container_width=True)


#     # With Plotly
#     st.subheader('Visualisation avec Plotly')
#     fig = px.bar(df_2, x='Unnamed:1', y='Unnamed:2')
#     st.plotly_chart(fig, use_container_width=True)

# else:
#     st.write("Les colonnes 'Unnamed: 1' et 'Unnamed: 2' ne sont pas présentes dans le DataFrame.")