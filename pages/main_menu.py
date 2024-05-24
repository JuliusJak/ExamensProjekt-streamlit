import streamlit as st
from components.navBar import navBar
from api_requests.users_api import create_new_user
from authentication import authentication

st.set_page_config(
    page_title="Main Menu",
    page_icon=None
)
authentication()

navBar()
#NOTE Temporary
st.write("Current User:",st.session_state.current_user)

with st.container(border=True):


    st.subheader("Practice")
    st.page_link(page="pages/study_material_practice.py",label="Study Material")
    st.page_link(page="pages/study_questions_practice.py",label="Study Questions")
    st.page_link(page="pages/images_practice.py",label="Images")

    st.subheader("Tests")