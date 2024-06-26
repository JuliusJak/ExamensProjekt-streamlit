import streamlit as st
from api_requests.study_questions import get_questions
from components.load_question import load_question
from api_requests.test_score_api import add_test_score
from authentication import authentication

authentication()
if "question_index" not in st.session_state:
    st.session_state["question_index"] = 0

if "test_score" not in st.session_state:
    st.session_state["test_score"] = 0

if "regular_test_score_submitted" not in st.session_state:
    st.session_state["regular_test_score_submitted"] = False
    
questions = get_questions()

if st.session_state["question_index"] >= len(questions):

    st.write(f"Your Final Score Is: {st.session_state["test_score"]}/{len(questions)}")
    st.write("Something something better then previous score...")

    if not st.session_state["regular_test_score_submitted"]:
        test_score = {
            "username": st.session_state["current_user"]["username"],
            "testType": "regular_test",
            "amountOfTestQuestions": len(questions),
            "correctAnswers": st.session_state["test_score"]
        }
        add_test_score(test_score)
        st.session_state["regular_test_score_submitted"] = True

    if st.button("Restart"):
        st.session_state["question_index"] = 0
        st.session_state["test_score"] = 0  
        st.session_state["regular_test_score_submitted"] = False
        st.rerun()
    
    if st.button("Return To Main Menu"):
        st.switch_page("pages/main_menu.py")
        

else:

    if st.toggle("Start Test"):   

        question_response = load_question(questions[st.session_state["question_index"]])
        
        if question_response:
            st.session_state["test_score"] += 1
            st.session_state["question_index"] += 1
            st.rerun()

        elif question_response is False:
            st.session_state["question_index"] += 1
            st.rerun()
