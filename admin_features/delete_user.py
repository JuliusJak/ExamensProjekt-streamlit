import streamlit as st
from api_requests.users_api import delete_user

def admin_delete_user():

    with st.form("Delete User", clear_on_submit=True):

        user_id = st.number_input("Select User Id",min_value=0)

        if st.form_submit_button("Delete User"):
            response = delete_user(user_id)
            st.write(response)