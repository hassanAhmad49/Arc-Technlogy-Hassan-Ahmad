import streamlit as st
import pickle
import numpy as np

# Load the model from dictionary
with open("housing_model12.pkl", "rb") as file:
    model_dict = pickle.load(file)
    model = model_dict['model']  # extract the model


st.title("🏡  Housing Price Prediction")

# Input fields for the 8 original features
median_income = st.number_input("Median Income", min_value=0.0, value=6.5)
house_age = st.number_input("House Age", min_value=0, value=25)
avg_rooms = st.number_input("Average Rooms", min_value=0.0, value=5.0)
avg_bedrooms = st.number_input("Average Bedrooms", min_value=0.0, value=1.0)
population = st.number_input("Population", min_value=0, value=1500)
avg_occupancy = st.number_input("Average Occupancy", min_value=0.0, value=3.0)
latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=34.0)
longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=-118.2)

# Predict button
if st.button("Predict"):
    # 1. Calculate the 3 new features from the user inputs
    # Handle division by zero for avg_rooms and avg_occupancy
    rooms_per_person = avg_rooms / avg_occupancy if avg_occupancy != 0 else 0
    bedrooms_per_room = avg_bedrooms / avg_rooms if avg_rooms != 0 else 0
    population_per_household = population / avg_occupancy if avg_occupancy != 0 else 0
    
    # 2. Create the input data array with all 11 features
    input_data = np.array([[
        median_income, house_age, avg_rooms, avg_bedrooms,
        population, avg_occupancy, latitude, longitude,
        rooms_per_person, bedrooms_per_room, population_per_household
    ]])
    
    # 3. Make the prediction
    prediction = model.predict(input_data)
    st.balloons()
    st.success(f"congratulations House Price: ${prediction[0]*100:.2f}")