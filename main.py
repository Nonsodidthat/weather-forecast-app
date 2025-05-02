import streamlit as st
st.title("Weather Forecast App")
city = st.text_input("Enter City Name")
slider = st.slider("Select number of days", min_value=1, max_value=5,
                   help="select the number of days you want weather forecast data for")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"Here is the {option} in {city} for the next {slider} days")