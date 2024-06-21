
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
# alt.themes.enable("dark")



# Load data ----- TO BE UPDATED, WORK IN PROGRESS
df_1 = pd.read_csv('data/Palworld_Data--Palu combat attribute table.csv')
df_2 = pd.read_csv('data/Palworld_Data--Palu refresh level.csv')
df_3 = pd.read_csv('data/Palworld_Data-comparison of ordinary BOSS attributes.csv')
df_4 = pd.read_csv('data/Palworld_Data-hide pallu attributes.csv')
df_5 = pd.read_csv('data/Palworld_Data-Palu Job Skills Table.csv')
df_6 = pd.read_csv('data/Palworld_Data-Tower BOSS attribute comparison.csv')



#######################
st.title('Analyse des Pals')
st.write('Voici les données du premier fichier .csv :')




# Display data
st.dataframe(df_2)


# Check the columnns
if 'Unnamed:1' in df_2.columns and 'Unnamed:2' in df_2.columns:
    # Converts column names inton  appropriate type if needed
    df_1['Unnamed:1'] = df_1['Unnamed:1'].astype(str)
    df_1['Unnamed:2'] = pd.to_numeric(df_1['Unnamed:2'], errors='coerce')


    # With Altair
    st.subheader('Visualisation avec Altair')
    chart = alt.Chart(df_1).mark_bar().encode(
        x='Unnamed:1',
        y='Unnamed:2'
    )
    st.altair_chart(chart, use_container_width=True)


    # With Plotly
    st.subheader('Visualisation avec Plotly')
    fig = px.bar(df_1, x='Unnamed:1', y='Unnamed:2')
    st.plotly_chart(fig, use_container_width=True)

else:
    st.write("Les colonnes 'Unnamed: 1' et 'Unnamed: 2' ne sont pas présentes dans le DataFrame.")