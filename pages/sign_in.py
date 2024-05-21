import streamlit as st
from api_requests import get_user
import time

st.title("Sign in Page")

with st.form("sign in form",clear_on_submit=True):

    username = st.text_input("Username")
    password = st.text_input("Password",type="password")

    #TODO if successfull start "loading" and then link to another page
    #TODO Also save the current user as teh "current_user" in sessoin_state
    #TODO add messages if the user missed to enter password or something. or if name or password is wrong
    sign_in_button = st.form_submit_button("Sign in")
    if sign_in_button:

        with st.spinner("Confirming account details"):
            user = get_user.get_user(username,password)
            user = user[0]

            if user != None:
                #Save users info to the session state as "current_user"
                st.session_state.current_user = user

            time.sleep(1)
            st.switch_page(page="pages/main_menu.py")

