import streamlit as st
import time

def countdown(seconds:int=10,message:str=None):

    countdown_placeholder = st.empty()

    while seconds:
        countdown_placeholder.warning(f"{message} \n\n You will be returned to the login page in {seconds} seconds.")
        time.sleep(1)
        seconds -= 1

def authentication(admin_level:bool=False):

    if "current_user" not in st.session_state or st.session_state.current_user == None:

        if st.button("Or Press here to return immidietly"):
            st.switch_page("app.py")

        countdown(message="You are not logged in.")
        st.switch_page("app.py")


    if admin_level:

        if st.session_state["current_user"]["role"] != "ADMIN":
            countdown(message="You do not have permission to use this page.")
            st.switch_page("app.py")