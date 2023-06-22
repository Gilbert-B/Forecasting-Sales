import streamlit as st
import pandas as pd
import numpy as np
import datetime
from sklearn.linear_model import LinearRegression
from PIL import Image
import requests
import tempfile

# Set Page Configurations
st.set_page_config(page_title="ETA Prediction App", page_icon="fas fa-chart-line", layout="wide", initial_sidebar_state="auto")

# Loading GIF
gif_url = "https://raw.githubusercontent.com/Gilbert-B/ETA-Prediction/main/assets/pictures/sonic2.gif"

# Load the banner image
banner_image_url = "https://raw.githubusercontent.com/Gilbert-B/Forecasting-Sales/0d7b869515bdf5551672f71b6e1f62be9902e3dc/app/seer.png"
banner_image = Image.open(requests.get(banner_image_url, stream=True).raw)

# Display the banner image
st.image(banner_image, use_column_width=True)


# Set up sidebar
st.sidebar.header('Navigation')
menu = ['Home', 'About']
choice = st.sidebar.selectbox("Select an option", menu)


# Home section
if choice == 'Home':
    st.image(gif_url,use_column_width=True)
    st.markdown("<h1 style='text-align: center;'>Welcome</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>This is an ETA Prediction App.</p>", unsafe_allow_html=True)


# About section
elif choice == 'About':
    st.title('About')
    st.markdown('''
            <p style='font-size: 20px; font-style: italic;font-style: bold;'>
            ZAP uses advanced algorithms and real-time data to accurately estimate the time it will take for users to reach their destinations. 
            By considering factors like distance, traffic conditions, and historical patterns, the app provides reliable ETA estimates. 
            This information allows users to plan their day or trip effectively, optimizing their time and avoiding unnecessary stress.
            Knowing the ETA helps users prioritize their tasks and be more productive. By understanding how long it will take to reach a destination, 
            individuals can allocate their time efficiently, focusing on important tasks before they need to leave. This approach improves productivity and reduces the risk of leaving tasks unfinished.
            Additionally, ZAP facilitates efficient communication. If unexpected delays occur, users can promptly inform others about their updated ETA, 
            allowing them to adjust their plans accordingly. This proactive communication helps prevent inconvenience or misunderstandings, promoting smoother coordination.
            In summary, ZAP empowers users to make informed decisions, effectively manage their time, and enhance communication. 
            By providing accurate ETA estimates, ZAP enables individuals to plan their day or trip more efficiently, prioritize tasks, and communicate effectively with others.
            </p>
            ''',unsafe_allow_html=True)


# Set Page Title
st.title('ZAP- An ETA Prediction APP')
st.markdown('Select your features and click on Submit')