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
    
    #Use columns to center the page_links
    col1,col2,col3 = st.columns([1,0.8,1])
    with col2:

        st.subheader("Practice")

        if st.button("Study Material",use_container_width=True):
            st.switch_page("pages/study_material_practice.py")

        if st.button("Study Questions",use_container_width=True):
            st.switch_page("pages/study_questions_practice.py")

        if st.button("Study Images",use_container_width=True):
            st.switch_page("pages/images_practice.py")

        st.subheader("Tests")