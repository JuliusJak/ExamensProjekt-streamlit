import streamlit as st
from components.navBar import navBar
from admin_features import manage_images, manage_questions, manage_users
from authentication import authentication


st.set_page_config(
    page_title="Admin Page",
    layout="wide"
)

#NOTE Needs more authenitcation since it's admin
authentication(True)
navBar()
st.title("Admin page")

with st.container(border=True):
    if st.checkbox("Search For User"):
        manage_users.admin_search_for_user()

    if st.checkbox("Create User"):
        manage_users.admin_new_user()

    if st.checkbox("Update User Information"):
        manage_users.admin_update_user()

    if st.checkbox("Delete User"):
        manage_users.admin_delete_user()

with st.container(border=True):
    if st.checkbox("Create New Question"):
        manage_questions.admin_new_question()
    if st.checkbox("Delete Question"):
        manage_questions.admin_delete_question()
        
with st.container(border=True):
    if st.checkbox("Create New Study Material*"):
        pass

with st.container(border=True):
    if st.checkbox("Upload New Image Question"):
        manage_images.admin_upload_image_question()

        