import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
from bokeh.plotting import figure
from bokeh.models import HoverTool
import joblib
import os
from date_features import getDateFeatures


# Get the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the model from the pickle file
model_path = os.path.join(current_dir, 'model.pkl')
model = joblib.load(model_path)

# Load the scaler from the pickle file
encoder_path = os.path.join(current_dir, 'encoder.pkl')
encoder = joblib.load(encoder_path)


# Set Page Configurations
st.set_page_config(page_title="ETA Prediction App", page_icon="fas fa-chart-line", layout="wide", initial_sidebar_state="auto")

# Loading GIF
gif_url = "https://raw.githubusercontent.com/Gilbert-B/Forecasting-Sales/main/app/salesgif.gif"



def predict(sales_data):
    sales_data = getDateFeatures(sales_data).set_index('date')

    # Make predictions for the next 8 weeks
    prediction_inputs = []  # Initialize the list for prediction inputs

    for i in range(8):
        # Encode the prediction inputs
        numeric_columns = ['onpromotion', 'year', 'month', 'dayofmonth', 'dayofweek', 'dayofyear', 'weekofyear', 'quarter', 'year_weekofyear', 'sin(dayofyear)', 'cos(dayofyear)']
        categoric_columns = ['store_id','category_id','city','store_type','cluster','holiday_type','is_holiday','is_month_start','is_month_end','is_quarter_start','is_quarter_end','is_year_start','is_year_end','is_weekend', 'season']
        
        num = sales_data[numeric_columns]
        encoded_cat = encoder.transform(sales_data[categoric_columns])
        sales_data_encoded = pd.concat([num, encoded_cat], axis=1)

        # Make the prediction using the loaded machine learning model
        predicted_sales = model.predict(sales_data_encoded)

        # Store the prediction for the current week
        prediction_inputs.append(predicted_sales[0])

        # Update sales_data for the next iteration
        sales_data['weekofyear'] += 1
        sales_data['dayofweek'] = 1

    # Convert the list of prediction inputs to a DataFrame
    prediction_data = pd.DataFrame(prediction_inputs, columns=['predicted_sales'])

    return prediction_data['predicted_sales']


# Set up sidebar
st.sidebar.header('Navigation')
menu = ['Home', 'About']
choice = st.sidebar.selectbox("Select an option", menu)
# Home section
if choice == 'Home':
    st.image(gif_url, use_column_width=True)
    st.markdown("<h1 style='text-align: center;'>Welcome</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>This is a Sales Forecasting App.</p>", unsafe_allow_html=True)
    
    # Set Page Title
    st.title('SEER- A Sales Forecasting APP')
    st.markdown('Enter the required information to forecast sales:')

    
    # Input form
    col1, col2 = st.columns(2)

    Stores = ['Store_' + str(i) for i in range(1, 55)]
    Stores1 = ['Store_' + str(i) for i in range(0, 5)]
    cities = ['city_' + str(i) for i in range(22)]
    clusters = ['cluster_' + str(i) for i in range(17)]
    categories = ['Category_' + str(i) for i in range(33)]

    with col1:
        date = st.date_input("Date")
        # Convert the date to datetime format
        date = pd.to_datetime(date)
        onpromotion = st.number_input("How many products are on promotion?", min_value=0, step=1)
        selected_category = st.selectbox("Category", categories)


    with col2:
        selected_store = st.selectbox("Store_type", Stores)
        selected_store1 = st.selectbox("Store_id", Stores1)
        selected_city = st.selectbox("City", cities)
        selected_cluster = st.selectbox("Cluster", clusters)

    # Call getDateFeatures() function on sales_data (replace sales_data with your DataFrame)
    sales_data = pd.DataFrame({
        'date': [date],
        'store_id': [selected_store],
        'category_id': [selected_category],
        'onpromotion': [onpromotion],
        'city' :[selected_city],
        'store_type': [selected_store1],
        'cluster':[selected_cluster]
        })
    print(sales_data)
    print(sales_data.info())



if st.button('Predict'):
    sales = predict(sales_data)
    formatted_sales = [round(s, 2) for s in sales]  # Round each prediction to 2 decimal places

    for i, s in enumerate(formatted_sales):
        week_number = i + 1
        st.write(f"Total sales for week {week_number} is: #{s}")



# About section
elif choice == 'About':
    # Load the banner image
    banner_image_url = "https://raw.githubusercontent.com/Gilbert-B/Forecasting-Sales/0d7b869515bdf5551672f71b6e1f62be9902e3dc/app/seer.png"
    banner_image = Image.open(requests.get(banner_image_url, stream=True).raw)

    # Display the banner image
    st.image(banner_image, use_column_width=True)
    st.markdown('''
            <p style='font-size: 20px; font-style: italic;font-style: bold;'>
            SEER is a powerful tool designed to assist businesses in making accurate 
            and data-driven sales predictions. By leveraging advanced algorithms and 
            machine learning techniques, our app provides businesses with valuable insights 
            into future sales trends. With just a few input parameters, such as distance and 
            average speed, our app generates reliable sales forecasts, enabling businesses
            to optimize their inventory management, production planning, and resource allocation. 
            The user-friendly interface and intuitive design make it easy for users to navigate 
            and obtain actionable predictions. With our Sales Forecasting App, 
            businesses can make informed decisions, mitigate risks, 
            and maximize their revenue potential in an ever-changing market landscape.
            </p>
            ''', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>This Sales Forecasting App is developed using Streamlit and Python.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>It demonstrates how machine learning can be used to predict sales for the next 8 weeks based on historical data.</p>", unsafe_allow_html=True)
