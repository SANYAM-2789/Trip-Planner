import streamlit as st
from datetime import date
import json
import subprocess
import requests
import pandas as pd

st.set_page_config(page_title="Trip Planner", page_icon="🌍", layout="centered")
st.title("🚀WELCOME to Départly!!")
st.write("NEW TO TRAVEL to your WHERE TO NOW moment, this is your all-in-one runaway to wanderlust ✈️🥤")
st.markdown("Fill in your travel details and get personalized trip plans instantly!")

with st.form("trip_form"):

    st.header(" Personal Information")
    name = st.text_input("Name", placeholder="Enter your name")

    st.header("✈️ Basic Information")
    Departure_Place = st.text_input("Departure_Place(s) (e.g., Paris, Tokyo)", placeholder="Enter city or country names")
    destinations = st.text_input("Destination(s) (e.g., Paris, Tokyo)", placeholder="Enter city or country names")
    start_date = st.date_input("Start Date", min_value=date.today())
    end_date = st.date_input("End Date", min_value=start_date)
    purpose = st.selectbox(
    "Purpose of Trip",
    ["Leisure", "Business", "Honeymoon", "Family Visit", "Adventure", "Cultural Exploration", "Medical", "Educational", "Other"])

    num_travelers = st.number_input("Number of Travelers", min_value=1, step=1)
    if_elders_and_children = st.selectbox("Elders and Children", ["Yes", "No"])
    
    st.header("💰 Budget & Currency")
    budget = st.number_input("Total Budget", min_value=100.0, step=100.0)
    currency = st.selectbox("Preferred Currency", ["USD", "EUR", "INR", "GBP", "JPY", "CAD", "AUD", "Other"])

    st.header("🎯 Interests & Preferences")
    activities = st.multiselect(
        "Preferred Activities",
        ["Adventure", "Sightseeing", "Shopping", "Food", "History", "Nature", "Relaxation"]
    )
    pace = st.radio("Preferred Travel Pace", ["Relaxed", "Balanced", "Packed"])
    must_visit = st.text_area("Must-Visit Attractions (Optional)")

    st.header("🏨 Accommodation")
    stay_type = st.selectbox("Type of Stay", ["Hotel", "Hostel", "Resort", "Airbnb", "Other"])
    star_rating = st.slider("Preferred Star Rating", 1, 5, 3)
    # location_pref = st.selectbox("Preferred Location", ["Central", "Near Beach", "Near Airport", "No Preference"])

    st.header("🚗 Transportation")
    transport_modes = st.multiselect("Preferred Transport", ["Flight", "Train", "Car Rental", "Public Transit"])
    travel_class = st.selectbox("Travel Class", ["Economy", "Business", "First", "No Preference"])

    st.header("🍽️ Meals & Dietary Needs")
    meal_type = st.multiselect("Meal Preferences", ["Vegetarian", "Vegan", "Halal", "Gluten-Free", "No Restrictions"])

    # st.header("🌡️ Weather Preference")
    # weather_pref = st.radio("Preferred Climate", ["Warm", "Mild", "Cold", "No Preference"])

    st.header("🛂 Visa & Citizenship Info")
    citizenship = st.text_input("Country of Citizenship")
    # visa_info = st.text_area("Travel History / Visa Notes (Optional)")

    # st.header("🌐 Language Preference")
    # language_pref = st.radio("Preferred Language for Communication", ["English", "Local Language", "No Preference"])

    st.header(" Insurance and Guide")
    insurance = st.selectbox("Insurance", ["Yes", "No"])
    guide = st.selectbox("Guide", ["Yes", "No"])

    st.header("📝 Additional Notes")
    notes = st.text_area("Other Needs (e.g., honeymoon, business trip, wheelchair access)")

    submitted = st.form_submit_button("Submit Trip Details")

    if submitted:

        # accessing the booking dataset and returnuing the appropriate data

        # df = pd.read_csv('booking.csv')

        # filtered_hotels = df[
        #     (df[]
        # ]


        # calling weather api then sending it o ollama

        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': destinations,
            'appid': "bc80b1bf94d3cd15828e2d32231df",
            'units': 'metric'
        }
        response = requests.get(base_url, params=params)
        data_weather = response.json()

        user_data = {
            "name": name,
            "departure_place": Departure_Place,
            "destinations": destinations,
            "dates": {"start": str(start_date), "end": str(end_date)},
            "purpose": purpose,
            "num_travelers": num_travelers,
            "weather" : data_weather,
            "if_elders_and_children": if_elders_and_children,
            "budget": budget,
            "currency": currency,
            "activities": activities,
            "pace": pace,
            "must_visit": must_visit,
            "stay_type": stay_type,
            "star_rating": star_rating,
            "transport_modes": transport_modes,
            "travel_class": travel_class,
            "meal_type": meal_type,
            "citizenship": citizenship,
            "insurance": insurance,
            "guide": guide,
            "notes": notes
        }




        with open("trip_data.json", "w") as f:
            json.dump(user_data, f)

        st.success("✅ Trip details submitted successfully!")
        st.write("Here's what you entered:")
        st.json(user_data)

    # 👉 Run gpt_prompt.py and get output
        result = subprocess.run(
            ["python3", "gpt_prompt.py"],
            capture_output=True,
            text=True
        )

        st.header("🧠 Trip Suggestion by LLaMA 3.2")
    st.markdown(result.stdout)  

#ollama
#llama 3.2
#data from ollama
#openweather api
#stream input output
#611


