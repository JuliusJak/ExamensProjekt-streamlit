import streamlit as st
from api_requests.study_questions import create_question, delete_question

def admin_new_question():
    with st.container(border=True):

        question = st.text_input("Write Question Here")

        col1,col2 = st.columns(2)
        with col1:
            option_a = st.text_input("Write Option A Here",placeholder="OptionA")
            option_c = st.text_input("Write Option C Here",placeholder="OptionC")
            category_id = st.radio("Select The Propper Category For This Question", [1,2,3],horizontal=True)

        with col2:
            option_b = st.text_input("Write Option B Here",placeholder="OptionB")
            option_d = st.text_input("Write Option D Here",placeholder="OptionD")
            correct_option = st.radio("Select The Correct Option",[option_a,option_b,option_c,option_d],horizontal=True)

        if st.button("Create New Question"):

            question_body = {
                "question": question,
                "optionA": option_a,
                "optionB": option_b,
                "optionC": option_c,
                "optionD": option_d,
                "correctOption": correct_option,
                "categoryId": category_id
            }

            st.write(create_question(question_body))


def admin_delete_question():

    with st.form("Delete Question", clear_on_submit=True):

        user_id = st.number_input("Select Question Id",min_value=0)

        if st.form_submit_button("Delete Question"):
            response = delete_question(user_id)
            st.write(response)