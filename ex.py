import streamlit as st
import plotly.express as px
import pandas as pd

# import dataframe

df = pd.read_csv("data/happy.csv")
column_list = list(df[['happiness','gdp','generosity']].columns)
column_list = [item.title() for item in column_list]


st.title("In Search for Happines")
metric_1 = st.selectbox("Select the data for X-axis", column_list)
metric_2 = st.selectbox("Select the data for Y-axis", column_list)
st.subheader(f"{metric_1} and {metric_2}")


figure = px.scatter(df, x=metric_1.lower(), y=metric_2.lower(),
                     labels={"x" : metric_2, "y" : metric_2})
st.plotly_chart(figure)

