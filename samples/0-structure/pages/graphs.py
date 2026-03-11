import streamlit as st
import numpy as np
import pandas as pd

st.title("Graphs")

np.random.seed(42)

tab_line, tab_bar, tab_area = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])

dates = pd.date_range("2025-01-01", periods=30, freq="D")
df = pd.DataFrame(
    np.random.randn(30, 3).cumsum(axis=0),
    index=dates,
    columns=["Series A", "Series B", "Series C"],
)

with tab_line:
    st.line_chart(df)

with tab_bar:
    st.bar_chart(df.tail(10))

with tab_area:
    st.area_chart(df)
