import streamlit as st
from components.navBar import navBar
from admin_features import create_new_user, create_new_question, search_for_user, update_user, delete_user,delete_question
from authentication import authentication


#NOTE Needs more authenitcation since it's admin
authentication()
navBar()
st.title("Admin page")

with st.container(border=True):
    if st.checkbox("Search For User"):
        search_for_user.admin_search_for_user()

    if st.checkbox("Create User"):
        create_new_user.admin_new_user()

    if st.checkbox("Update User Information"):
        update_user.admin_update_user()

    if st.checkbox("Delete User"):
        delete_user.admin_delete_user()

with st.container(border=True):
    if st.checkbox("Create New Question"):
        create_new_question.admin_new_question()
    if st.checkbox("Delete Question"):
        delete_question.admin_delete_question()
        
with st.container(border=True):
    if st.checkbox("Create New Study Material*"):
        pass