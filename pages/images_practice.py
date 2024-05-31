import streamlit as st
from components.navBar import navBar
from streamlit_image_coordinates import streamlit_image_coordinates
from authentication import authentication
from api_requests.images_api import get_image_questions

st.set_page_config(
    page_title="Image practice",
    page_icon=None,
    layout="wide"
)
authentication()
navBar()
st.title("Image practice")
with st.container(border=True):


    all_image_questions = get_image_questions()

    questions = []
    for question in all_image_questions:
        questions.append(question["question"])

    if "selectbox_index" not in st.session_state:
        st.session_state["selectbox_index"] = 0

    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        selected_image_question = st.selectbox("Select A Image Question",questions,index=st.session_state["selectbox_index"])

        image_question = get_image_questions(question=selected_image_question)
        
        st.subheader(image_question[0]["question"])

        width = 700
        height = width * 0.667
        value = streamlit_image_coordinates(f"images/{image_question[0]['name']}.jpg",height,width)

        if value:
            x, y = value["x"], value["y"]
            
            min_x = min(image_question[0]["firstXValue"], image_question[0]["secondXValue"])
            max_x = max(image_question[0]["firstXValue"], image_question[0]["secondXValue"])
            min_y = min(image_question[0]["firstYValue"], image_question[0]["secondYValue"])
            max_y = max(image_question[0]["firstYValue"], image_question[0]["secondYValue"])

            if min_x <= x <= max_x and min_y <= y <= max_y:
                st.success("Correct")
            else:
                st.error("Wrong")

        if st.button("Next Question"):
            st.session_state["selectbox_index"] += 1
            if st.session_state["selectbox_index"] >= len(questions):
                st.session_state["selectbox_index"] = 0
            st.rerun()