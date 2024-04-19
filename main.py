import streamlit as st
import plotly.express  as px
from backend import get_data
from datetime import datetime


st.title("Weather Forecast for the Next Days")
place = st.text_input ("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox("Select data to view",
                       ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place} ")

# generate plots for temperature and sky
if place:
    return_data = get_data(place, days)
    filtered_data = return_data[1]
    data_code = return_data[0]
    if data_code=='404':
        st.info("City not found")
    else:
        dates = [datetime.fromtimestamp(i["dt"]).strftime('%Y-%m-%d %H:%%M:%S') for i in filtered_data]

        match option:
            case "Temperature":
                temps = [f["main"]["temp"]/100 for f in filtered_data]
                figure =  px.line(x=dates, y=temps, labels={"x":"Date", "y": "Temperature (C)"})
                st.plotly_chart(figure)
            case "Sky":
                skys = [f["weather"][0]["main"] for f in filtered_data]
                sky_images_paths = {"Rain":"images/rain.png", "Clouds":"images/cloud.png",
                            "Snow":"images/snow.png", "Clear":"images/clear.png"}
                sky_images = [sky_images_paths[sky] for sky in skys]
                st.image(sky_images, width=200)
                # figure =  px.line(x=d, y=t, labels={"x":"Date", "y": "Temperature (C)"})
                # st.plotly_chart(figure)


