import streamlit as st
from components.navBar import navBar
from api_requests.users_api import create_new_user

st.set_page_config(
    page_title="Main Menu",
    page_icon=None
)
navBar()

with st.container(border=True):


    st.subheader("Practice")
    st.page_link(page="pages/study_material.py",label="Study Material")
    st.page_link(page="pages/study_questions.py",label="Study Questions")
    st.page_link(page="pages/images.py",label="Images")

    st.subheader("Tests")