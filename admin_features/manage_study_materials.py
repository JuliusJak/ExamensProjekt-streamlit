import streamlit as st
from api_requests.study_material_api import create_study_material


def admin_create_study_material():

    with st.form("Create study material form",clear_on_submit=True):
        title = st.text_input("Input The Title Of The Study Material")
        description = st.text_area("Input The Content Of The Study Material")

        if st.form_submit_button("Create New Study Material"):
            study_material = {
                "title": title,
                "description": description
            }
            response = create_study_material(study_material)
            st.success("New Study Material Has Been Created and Added")