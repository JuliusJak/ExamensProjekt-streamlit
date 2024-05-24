import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates

def admin_upload_image_question():

    pass
#TODO User selects an image from a the image directory. Either with the select image library or simple select_box
#Then the image is loaded with streamlit_image_coordinates
#Then it will take the first and second x/y coord and save them together with the image name.
#Then it will use the api to send a dict with the image_name, image_question and 4 coords. This will be saved in the DB
#Then when a quesstion is called. The api will return the name of the image and the 4 coords. Then do the same as already done in images_practice
