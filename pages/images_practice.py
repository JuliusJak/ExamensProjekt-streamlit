import streamlit as st
from components.navBar import navBar
from streamlit_image_coordinates import streamlit_image_coordinates
from authentication import authentication


st.set_page_config(
    page_title="Image practice",
    page_icon=None,
    layout="wide"
)
authentication()
navBar()
st.title("Image practice")
with st.container(border=True):
    st.subheader("Click on the battery")
    value = streamlit_image_coordinates("images/car_engine.jpg")

    if value:
        x, y = value["x"], value["y"]
        if 710 <= x <= 910 and 315 <= y <= 455:
            st.success("Correct! The coordinates are within the specified range.")
        else:
            st.error("Incorrect. The coordinates are outside the specified range.")
        st.write(f"Clicked coordinates: x={x}, y={y}")
    else:
        st.write("Click on the image to get coordinates.")