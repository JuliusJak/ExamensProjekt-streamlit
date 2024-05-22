import streamlit as st
from api_requests.users_api import update_user

def admin_update_user():

    with st.form("Update user", clear_on_submit=True):

        user_id = st.text_input("Select User By Id")
        new_username = st.text_input("Enter New Username")
        new_password = st.text_input("Enter New Password")
        new_role = st.selectbox("Select New Role",["USER","ADMIN"])
        
        if st.form_submit_button("UPDATE"):
            
            result = update_user(user_id,new_username,new_password,new_role)

            st.write(result)