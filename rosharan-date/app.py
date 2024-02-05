import streamlit as st


st.title("Rosharan Date")

# From https://roshar.17thshard.com/#/en-US/events/kaladin-joins-bridge-four:
# 1173.7.9.3 - Kaladin joins Bridge Four

columns = st.columns(4)

with columns[0]:
    year = st.number_input(
        "Year",
        step=1,
        value=1173,
    )

with columns[1]:
    month = st.number_input(
        "Month",
        min_value=1,
        max_value=10,
        step=1,
        value=7,
    )

with columns[2]:
    week = st.number_input(
        "Week",
        min_value=1,
        max_value=10,
        step=1,
        value=9,
    )

with columns[3]:
    day = st.number_input(
        "Day",
        min_value=1,
        max_value=5,
        step=1,
        value=3,
    )
