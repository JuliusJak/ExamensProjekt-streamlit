import streamlit as st
from components.navBar import navBar
from api_requests.users_api import create_new_user

navBar()
st.title("Admin page")


if st.checkbox("Create User"):

    new_user_username = st.text_input("New User: Username")
    new_user_password = st.text_input("New User: Password")
    new_user_role = st.checkbox("New User: ADMIN",help="If True, new user will be set to be a ADMIN else it will default to USER")
    if new_user_role:
        new_user_role = "ADMIN"

    if st.button("Create New User"):

        result = create_new_user(
            username=new_user_username,
            password=new_user_password,
            role=new_user_role
        )

        if isinstance(result, str):
            st.warning(result)
        else:
            st.write(result)