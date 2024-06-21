#######################
# Import libraries
import streamlit as st
import pandas as pd
# import altair as alt
# import plotly.express as px

#######################
# Page configuration
st.set_page_config(
    page_title="analyse des Pals",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded")

# alt.themes.enable("dark")


#######################
# Load data
df_reshaped = pd.read_csv('data/------.csv')