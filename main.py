import streamlit as st
import plotly.express as px
from  backend import get_data

# Build the user interface
st.title("Weather Forecast App")
city = st.text_input("Enter City Name")
days = st.slider("Select number of days", min_value=1, max_value=5,
                   help="select the number of days you want weather forecast data for")
option = st.selectbox("Select data to view", ("temperature", "sky"))
st.subheader(f"Here is how the {option} in {city} will look over the next {days} day(s)")

try:
    # Get data via API
    if city:
        filtered_data = get_data(city, days)

        # Filter data and produce output for either option
        if option == "temperature":
            dates  = [dict["dt_txt"] for dict in filtered_data]
            temperatures  = [dict["main"]["temp"] /10 for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)

        if option == "sky":
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png",
                      "Rain":"images/rain.png", "Snow": "images/snow.png" }
            sky_conditions  = [dict["weather"][0]["main"]for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
except KeyError:
    st.info("You picked a city that does not exist, try a different city")

