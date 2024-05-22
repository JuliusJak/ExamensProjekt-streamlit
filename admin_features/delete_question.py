import streamlit as st
from api_requests.study_questions import delete_question

def admin_delete_question():

    with st.form("Delete Question", clear_on_submit=True):

        user_id = st.number_input("Select Question Id",min_value=0)

        if st.form_submit_button("Delete Question"):
            response = delete_question(user_id)
            st.write(response)