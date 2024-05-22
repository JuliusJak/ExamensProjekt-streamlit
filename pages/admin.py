import streamlit as st
from components.navBar import navBar
from admin_features import create_new_user, create_new_question

navBar()
st.title("Admin page")


if st.checkbox("Create User"):
    create_new_user.admin_new_user()

if st.checkbox("Create New Question"):
    create_new_question.admin_new_question()