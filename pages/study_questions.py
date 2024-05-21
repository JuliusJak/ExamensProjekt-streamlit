import streamlit as st
from components.navBar import navBar
from api_requests.study_questions import get_questions


navBar()
st.title("Study Questions")

def all_questions():
    with st.container(border=True):

        questions_list = get_questions()

        for question in questions_list:
            
            st.subheader(question["question"])
            
            col1,col2 = st.columns(2)

            option_a = col1.button(question["optionA"],use_container_width=True)
            option_b = col1.button(question["optionB"],use_container_width=True)
            option_c = col2.button(question["optionC"],use_container_width=True)
            option_d = col2.button(question["optionD"],use_container_width=True)

            if option_a:
                if question["optionA"] == question["correctOption"]:
                    st.success("CORRECT")
                else:
                    st.error("WRONG")
            if option_b:
                if question["optionB"] == question["correctOption"]:
                    st.success("CORRECT")
                else:
                    st.error("WRONG")
            if option_c:
                if question["optionC"] == question["correctOption"]:
                    st.success("CORRECT")
                else:
                    st.error("WRONG")
            if option_d:
                if question["optionD"] == question["correctOption"]:
                    st.success("CORRECT")
                else:
                    st.error("WRONG")



if st.checkbox("All Questions"):
    all_questions()