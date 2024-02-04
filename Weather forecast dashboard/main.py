import streamlit as st
import plotly.express as px
from functions import get_data

st.header("Weather forecast for next few days")
place = st.text_input("Enter Place : ")
value = st.slider("Forecast Days", min_value=1, max_value=5,
                  help="Select Number of days to forecast")
option = st.selectbox("Which data you want to view",
                       ("Temperature", "Sky"))
st.subheader(f"{option} for next {value} days in {place} is : ")

d, t = get_data(place, value, option)
figure = px.line(x=[1,2,3], y=[1,2,3], labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)