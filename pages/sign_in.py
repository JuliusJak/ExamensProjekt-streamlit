import streamlit as st
from api_requests.users_api import get_user
import time

st.title("Sign in Page")

with st.form("sign in form",clear_on_submit=True):

    username = st.text_input("Username")
    password = st.text_input("Password",type="password")

    sign_in_button = st.form_submit_button("Sign in")
    if sign_in_button:

        with st.spinner("Confirming account details"):
            user = get_user(username=username,password=password)

            if user == []:
                st.warning("No User With That Username And/Or Password Could Be Found")
            else:
                user = user[0]

                if user != None:
                    #Save users info to the session state as "current_user"
                    st.session_state["current_user"] = user

                time.sleep(1)
                st.switch_page(page="pages/main_menu.py")

