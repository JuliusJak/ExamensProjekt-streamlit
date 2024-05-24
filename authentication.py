import streamlit as st
import time

def countdown(seconds: int):

    countdown_placeholder = st.empty()

    while seconds:
        countdown_placeholder.warning(f"You are not logged in. You will be returned to the login page in {seconds} seconds.")
        time.sleep(1)
        seconds -= 1

def authentication():
    if "current_user" not in st.session_state or st.session_state.current_user == None:
        countdown(15)
        st.switch_page("app.py")