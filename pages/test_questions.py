import streamlit as st
from api_requests.study_questions import get_questions
from components.load_question import load_question

#TODO add more filtering for how the questions are selected
if "question_index" not in st.session_state:
    st.session_state["question_index"] = 0

if "test_score" not in st.session_state:
    st.session_state["test_score"] = 0
    
st.write("You will have 1 minute to complete this test")
st.write(st.session_state["question_index"])

questions = get_questions()

if st.session_state["question_index"] >= len(questions):

    st.write(f"Your Final Score Is: {st.session_state["test_score"]}/{len(questions)}")
    st.write("Something something better then previous score...")
    #TODO Save score to users profile
    if st.button("Restart"):
        st.session_state["question_index"] = 0
        st.session_state["test_score"] = 0  
        st.rerun()
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
