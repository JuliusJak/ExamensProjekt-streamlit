import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
from api_requests.images_api import get_image_questions

def load_image_question(image_question):
    with st.container(border=True):

        if "selectbox_index" not in st.session_state:
            st.session_state["selectbox_index"] = 0

        
        st.subheader(image_question["question"])

        width = 700
        height = width * 0.667
        value = streamlit_image_coordinates(f"images/{image_question['name']}.jpg",height,width)

        if value:
            x, y = value["x"], value["y"]
            
            min_x = min(image_question["firstXValue"], image_question["secondXValue"])
            max_x = max(image_question["firstXValue"], image_question["secondXValue"])
            min_y = min(image_question["firstYValue"], image_question["secondYValue"])
            max_y = max(image_question["firstYValue"], image_question["secondYValue"])

            if min_x <= x <= max_x and min_y <= y <= max_y:
                return True
            else:
                return None
            