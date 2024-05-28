import streamlit as st
from api_requests.users_api import create_new_user
import time

st.title("Sign up page")

with st.form("sign in form",clear_on_submit=True):

    username = st.text_input("Username")
    password = st.text_input("Password",type="password")

    sign_in_button = st.form_submit_button("Sign in")
    if sign_in_button:

        with st.spinner("Confirming account details"):

            new_user = create_new_user(username,password)

            if isinstance(new_user, str):
                st.warning(new_user)
            else:
                st.session_state.current_user = new_user
                time.sleep(1)
                st.switch_page("pages/main_menu.py")