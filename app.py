import streamlit as st
from components.navBar import navBar

st.set_page_config(
    page_title="Main Page",
    page_icon=None,
)

if "main_page_content" not in st.session_state:
    st.session_state.main_page_content = None

#NOTE Only for dev
# if "current_user" not in st.session_state:
#     dev_user = {'id': 2, 'username': 'bob', 'password': '321', 'role': 'ADMIN'}
#     st.session_state.current_user = dev_user

st.title("WELCOME :smile:")

with st.container(border=True):

    #Use columns to center the page_links
    col1,col2,col3 = st.columns([1,0.8,1])
    with col2:

        sign_in = st.button("Sign In",use_container_width=True)
        if sign_in:
            st.switch_page("pages/sign_in.py")

        sign_up = st.button("Sign Up",use_container_width=True)
        if sign_in:
            st.switch_page("pages/sign_up.py")

        continue_as_guest = st.button("Continue As Guest",use_container_width=True)
        if continue_as_guest:
            st.session_state.current_user = "guest"
            st.switch_page("pages/main_menu.py")
