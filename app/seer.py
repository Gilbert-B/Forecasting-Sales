import streamlit as st
import pandas as pd
import numpy as np
import datetime
from sklearn.linear_model import LinearRegression
from PIL import Image
import requests
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from bokeh.models import HoverTool

# Set Page Configurations
st.set_page_config(page_title="ETA Prediction App", page_icon="fas fa-chart-line", layout="wide", initial_sidebar_state="auto")

# Loading GIF
gif_url = "https://raw.githubusercontent.com/Gilbert-B/Forecasting-Sales/main/app/salesgif.gif"

# Set up sidebar
st.sidebar.header('Navigation')
menu = ['Home', 'About']
choice = st.sidebar.selectbox("Select an option", menu)


# Home section
if choice == 'Home':
    st.image(gif_url,use_column_width=True)
    st.markdown("<h1 style='text-align: center;'>Welcome</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>This is a Sales Forecasting App.</p>", unsafe_allow_html=True)
# Set Page Title
    st.title('SEER- A Sales Forecasting  APP')
    st.markdown('Enter the required information to forecast sales:')

    # Input form
    col1, col2 = st.beta_columns(2)

    with col1:
        store_id = st.text_input("Store ID")
        previous_sales = st.number_input("Previous Week's Sales", min_value=0, step=1)
        advertising_expenditure = st.number_input("Advertising Expenditure", min_value=0.0, step=0.01)

    # Make predictions using the loaded machine learning model
    prediction_inputs = [[store_id, previous_sales, advertising_expenditure]]
    predicted_weekly_sales = model.predict(prediction_inputs)

    # Display forecast results
    st.subheader('Sales Forecast Results')
    st.write("Predicted Number of Products Purchased per Week:")
    for i, prediction in enumerate(predicted_weekly_sales):
        st.write(f"Week {i+1}: {prediction}")

    # Convert the predicted weekly sales to a list
    predicted_sales_list = predicted_weekly_sales.tolist()

# Line Chart
    plt.figure(figsize=(10, 6))
    weeks = range(1, 9)
    plt.plot(weeks, predicted_sales_list, marker='o')
    plt.xlabel('Week')
    plt.ylabel('Predicted Sales')
    plt.title('Predicted Number of Products Purchased per Week')
    st.pyplot(plt)

# Convert the predicted weekly sales to a list
    predicted_sales_list = predicted_weekly_sales.tolist()

# Create the interactive line chart
    p = figure(title='Predicted Number of Products Purchased per Week', x_axis_label='Week', y_axis_label='Predicted Sales')
    p.line(weeks, predicted_sales_list, line_width=2)
    p.circle(weeks, predicted_sales_list, fill_color='white', size=8)

    hover = HoverTool(tooltips=[('Week', '@x'), ('Predicted Sales', '@y')])
    p.add_tools(hover)

    st.bokeh_chart(p)



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
            and maximize their revenue potential in an ever-changing market landscape..
            </p>
            ''',unsafe_allow_html=True)


