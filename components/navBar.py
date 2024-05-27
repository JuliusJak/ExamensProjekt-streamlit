import streamlit as st


def navBar():

    pages = ["Main Menu","Study Material","Practice Questions","Admin","Profile"]

    col1,col2,col3,col4,col5 = st.columns(len(pages))

    with col1:
        st.page_link("pages/main_menu.py",use_container_width=True)    
    
    with col2:
        st.page_link("pages/study_material_practice.py",use_container_width=True)
    
    with col3:
        st.page_link("pages/study_questions_practice.py",use_container_width=True)
    
    with col4:
        st.page_link("pages/admin.py",use_container_width=True)

    with col5:
        st.page_link("pages/profile.py",use_container_width=True)