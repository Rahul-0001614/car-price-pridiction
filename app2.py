import streamlit as st
import pandas as pd
import joblib

loaded_pipe = joblib.load('pipeline_LinearRegression.pkl') 

st.title("Car Price Prediction App")

with st.form("input_form"):
    st.write("Enter the car details:")
    year = st.number_input("Year")
    make = st.text_input("Make")
    model = st.text_input("Model")
    trim = st.text_input("Trim")
    body = st.text_input("Body Type")
    transmission = st.selectbox("Transmission", ["Automatic", "Manual"])
    condition = st.number_input("Condition")
    odometer = st.number_input("Odometer")
    color = st.text_input("Color")
    interior = st.text_input("Interior Color")
    mmr = st.number_input("MMR")
    day = st.number_input("Day", min_value=1, max_value=31, value=1)
    day_name = st.selectbox("Day Name", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    month_name = st.selectbox("Month Name", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    year1 = st.number_input("Year 1", min_value=2000, max_value=2100, value=2023)


    submitted = st.form_submit_button("Submit")

    if submitted:
        columns = ['year', 'make', 'model', 'trim', 'body', 'transmission',
                       'condition', 'odometer', 'color', 'interior', 'mmr',
                       'day', 'day_name', 'month_name', 'year1']
            
        input_data = pd.DataFrame([[
                year, make, model, trim, body, transmission, condition,
                odometer, color, interior, mmr, day, day_name, month_name, year1
            ]], columns=columns)
    
        prediction = loaded_pipe.predict(input_data)

        st.success(f"Prediction : {prediction[0]}")
