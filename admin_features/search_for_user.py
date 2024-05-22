import streamlit as st
from api_requests.users_api import get_user

def admin_search_for_user():

    with st.container(border=True):

        id_search = st.text_input("Search By Id")
        username_search = st.text_input("Search By Username")
        role_search = st.selectbox("Search By Role",["USER","ADMIN"])
        
        result = get_user(username=username_search,id=id_search,role=role_search,password=None)

        st.write(result)