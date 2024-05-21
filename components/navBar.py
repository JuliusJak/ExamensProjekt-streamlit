import streamlit as st



def navBar():

    pages = ["app","main_menu","admin","profile"]

    col1,col2,col3,col4 = st.columns(len(pages))

    with col1:
        st.page_link("app.py")    
    
    with col2:
        st.page_link("pages/main_menu.py")
    
    with col3:
        st.page_link("pages/admin.py")

    with col4:
        st.page_link("pages/profile.py")