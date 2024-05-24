import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import Image
from io import BytesIO
import base64

# def admin_upload_image():

#     # File uploader
#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

#     if uploaded_file is not None:
#         # To read file as bytes
#         bytes_data = uploaded_file.read()
        
#         # Load the image with PIL
#         image = Image.open(BytesIO(bytes_data))
                
#         # Use the streamlit_image_coordinates function
#         coordinates = streamlit_image_coordinates(
#             source=image,
#             key="uploaded_image"
#         )
        
#         # Display the coordinates returned
#         st.write("Coordinates:", coordinates)


def admin_upload_image():

    uploaded_file = st.file_uploader("Upload An Image Here", type=["jpg","jpeg","png"])

    if uploaded_file is not None:
        st.image(uploaded_file)

        if st.button("Upload Image"):
            #TODO add api call to upload image to DB
            st.success("Image Uploaded")
            