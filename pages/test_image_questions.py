import streamlit as st
from api_requests.images_api import get_image_questions
from components.load_image_question import load_image_question
from api_requests.test_score_api import add_test_score

#TODO add more filtering for how the questions are selected
if "question_index" not in st.session_state:
    st.session_state["question_index"] = 0

if "test_score" not in st.session_state:
    st.session_state["test_score"] = 0

if "image_test_score_submitted" not in st.session_state:
    st.session_state["image_test_score_submitted"] = False
    
#TODO Implement the timer
st.write("You will have 1 minute to complete this test")
st.write(st.session_state["question_index"])

questions = get_image_questions()

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
else:

    if st.toggle("Start Test"):

        question_response = load_image_question(questions[st.session_state["question_index"]])
        
        if question_response:
            st.session_state["test_score"] += 1
            st.session_state["question_index"] += 1
            st.rerun()

        elif question_response is False:
            st.session_state["question_index"] += 1
            st.rerun()
