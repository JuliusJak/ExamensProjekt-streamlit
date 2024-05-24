import streamlit as st
from components.navBar import navBar

st.set_page_config(
    page_title="Main Page",
    page_icon=None,
)

if "main_page_content" not in st.session_state:
    st.session_state.main_page_content = None

st.title("WELCOME :)")

with st.container(border=True):

    #Use columns to center the page_links
    col1,col2,col3 = st.columns([1,0.8,1])
    with col2:

        sign_in = st.page_link(page="pages/sign_in.py", label="Sign In",use_container_width=True)
        sign_up = st.page_link(page="pages/sign_up.py", label="Sign Up",use_container_width=True)

        #TODO this will just go to the different optoins menu immidietly but user won't be logged in
        continue_as_guest = st.page_link(page="pages/main_menu.py", label="Continue As Guest",use_container_width=True)
