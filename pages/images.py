import streamlit as st
from components.navBar import navBar
from streamlit_image_coordinates import streamlit_image_coordinates

navBar()

value = streamlit_image_coordinates("images\cute_cat1.jpg")

st.write(value)