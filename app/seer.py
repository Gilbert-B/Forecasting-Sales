import streamlit as st
import pandas as pd
import numpy as np
import datetime
from sklearn.linear_model import LinearRegression
from PIL import Image


# Set Page Configurations
st.set_page_config(page_title="ETA Prediction App", page_icon="🚗", layout="wide", initial_sidebar_state="auto")


# Load the background image
background_image = Image.open("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fforest-road-cartoon&psig=AOvVaw2Ru6TiYGRxAN_JKQLkkR-Z&ust=1686570971411000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCMCPvNGUu_8CFQAAAAAdAAAAABAE")

# Set the background image as the app's background
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fforest-road-cartoon&psig=AOvVaw2Ru6TiYGRxAN_JKQLkkR-Z&ust=1686570971411000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCMCPvNGUu_8CFQAAAAAdAAAAABAE');
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set up sidebar
st.sidebar.header('Input Parameters')
distance = st.sidebar.number_input("Distance (in kilometers)", min_value=0.1, max_value=1000.0, step=0.1)
average_speed = st.sidebar.number_input("Average Speed (in km/h)", min_value=1, max_value=200, step=1)



