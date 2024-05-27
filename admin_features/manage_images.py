import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
from api_requests.images_api import save_image_question

def admin_upload_image_question():

    images = ["car_engine","cute_cat1"]

    image_question = st.text_input("Write The Question Here")

    selected_image = st.selectbox("Select the image to make a question to",images,index=None)

    if selected_image is not None:
        width = 700
        height = int(width * 0.667)
        
        coords_list = []
        if "coords" not in st.session_state:
            st.session_state["coords"] = []
        
        coords = streamlit_image_coordinates(f"images/{selected_image}.jpg", height, width)
        
        if coords and len(st.session_state["coords"]) < 2:
            st.session_state["coords"].append(coords)
        
        if len(st.session_state["coords"]) == 2:
            st.write("First click coordinates:", st.session_state["coords"][0])
            st.write("Second click coordinates:", st.session_state["coords"][1])
        else:
            st.write("Click on the image to get coordinates. You need to click twice.")

        if st.button("Create New Image Question"):

            formatted_image_question ={
                "name": selected_image,
                "question": image_question,
                "firstXValue": st.session_state["coords"][0]["x"],
                "secondXValue": st.session_state["coords"][1]["x"],
                "firstYValue": st.session_state["coords"][0]["y"],
                "secondYValue": st.session_state["coords"][1]["y"]
            }

            save_image_question(formatted_image_question)
            st.session_state["coords"] = []
            st.rerun()

