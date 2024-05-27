import streamlit as st

def load_question(question):
    st.subheader(question["question"])
    
    col1, col2 = st.columns(2)

    option_a = col1.button(question["optionA"], use_container_width=True)
    option_b = col1.button(question["optionB"], use_container_width=True)
    option_c = col2.button(question["optionC"], use_container_width=True)
    option_d = col2.button(question["optionD"], use_container_width=True)

    if option_a:
        return question["correctOption"] == question["optionA"]
    elif option_b:
        return question["correctOption"] == question["optionB"]
    elif option_c:
        return question["correctOption"] == question["optionC"]
    elif option_d:
        return question["correctOption"] == question["optionD"]
    
    # If no button has been pressed, return None
    return None
