import time
import pandas as pd
import streamlit as st

st.title("Caching Example")

@st.cache_data
def load_data(url):
    # This function is slow...
    # Due to streamlit's inner workings, this function is executed 
    # every time the script is run. So we use caching to avoid this.
    df = pd.read_csv(url)
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

# Clicking this button will cause the script to re-run
st.button("Do something else")

