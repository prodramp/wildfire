import streamlit as st

def create_mapbox_graph(df):
    st.map(df, use_container_width=True)
