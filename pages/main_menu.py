import streamlit as st
from components.navBar import navBar
from api_requests.create_user import create_new_user

st.set_page_config(
    page_title="Main Menu",
    page_icon=None
)
navBar()

with st.container(border=True):

    st.page_link("pages/study_material.py")