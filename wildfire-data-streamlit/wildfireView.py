import streamlit as st


def show_wildfire_map(df):
    st.map(df)