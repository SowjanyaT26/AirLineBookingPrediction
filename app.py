import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("airline_booking_model.pkl")

st.set_page_config(
    page_title="Airline Booking Prediction",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ Airline Booking Prediction")
st.write("Predict whether a customer will complete a booking.")

# Inputs
num_passengers = st.number_input(
    "Number of Passengers",
    min_value=1,
    value=1
)

sales_channel = st.selectbox(
    "Sales Channel",
    ["Internet", "Mobile"]
)

trip_type = st.selectbox(
    "Trip Type",
    ["RoundTrip", "OneWay", "CircleTrip"]
)

purchase_lead = st.number_input(
    "Purchase Lead (days)",
    min_value=0,
    value=30
)

length_of_stay = st.number_input(
    "Length of Stay",
    min_value=0,
    value=5
)

flight_hour = st.slider(
    "Flight Hour",
    0,
    23,
    12
)

flight_day = st.selectbox(
    "Flight Day",
    [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ]
)

flight_duration = st.number_input(
    "Flight Duration (hours)",
    min_value=0.0,
    value=5.0
)

wants_extra_baggage = st.selectbox(
    "Extra Baggage",
    [0, 1]
)

wants_preferred_seat = st.selectbox(
    "Preferred Seat",
    [0, 1]
)

wants_in_flight_meals = st.selectbox(
    "In Flight Meals",
    [0, 1]
)

# Encoding

sales_channel_map = {
    "Internet": 0,
    "Mobile": 1
}

trip_type_map = {
    "RoundTrip": 0,
    "OneWay": 1,
    "CircleTrip": 2
}

flight_day_map = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4,
    "Sat": 5,
    "Sun": 6
}

# Prediction button
if st.button("Predict Booking"):

    input_data = pd.DataFrame({
        "num_passengers": [num_passengers],
        "sales_channel": [sales_channel_map[sales_channel]],
        "trip_type": [trip_type_map[trip_type]],
        "purchase_lead": [purchase_lead],
        "length_of_stay": [length_of_stay],
        "flight_hour": [flight_hour],
        "flight_day": [flight_day_map[flight_day]],
        "wants_extra_baggage": [wants_extra_baggage],
        "wants_preferred_seat": [wants_preferred_seat],
        "wants_in_flight_meals": [wants_in_flight_meals],
        "flight_duration": [flight_duration]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Booking Likely to be Completed")
    else:
        st.error("❌ Booking Likely NOT to be Completed")
