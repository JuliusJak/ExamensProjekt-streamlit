import streamlit as st
from api_requests.users_api import create_new_user, get_user, delete_user, update_user

def admin_new_user():

    with st.container(border=True):
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

def admin_search_for_user():

    with st.container(border=True):

        id_search = st.text_input("Search By Id")
        username_search = st.text_input("Search By Username")
        role_search = st.selectbox("Search By Role",["USER","ADMIN"])
        
        result = get_user(username=username_search,id=id_search,role=role_search,password=None)

        st.write(result)

def admin_delete_user():

    with st.form("Delete User", clear_on_submit=True):

        user_id = st.number_input("Select User Id",min_value=0)

        if st.form_submit_button("Delete User"):
            response = delete_user(user_id)
            st.write(response)


def admin_update_user():

    with st.form("Update user", clear_on_submit=True):

        user_id = st.text_input("Select User By Id")
        new_username = st.text_input("Enter New Username")
        new_password = st.text_input("Enter New Password")
        new_role = st.selectbox("Select New Role",["USER","ADMIN"])
        
        if st.form_submit_button("UPDATE"):
            
            result = update_user(user_id,new_username,new_password,new_role)

            st.write(result)