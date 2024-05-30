import streamlit as st
from components.navBar import navBar
from api_requests.study_material_api import study_material_search
from authentication import authentication
from gtts import gTTS
import os

def generate_tts(text, filename="output.mp3"):
    tts = gTTS(text)
    tts.save(filename)


authentication()
navBar()
st.title("Study Material")

with st.container(border=True):

    search_query = st.text_input("Search for study material")

    study_material = study_material_search(search_query)

    if study_material is not None:
        for material in study_material:
            with st.container(border=True):
                st.write(material["title"])
                st.write(material["description"])
                #TODO check if question is alredy marked as favourite
                st.checkbox("Mark as favorit",key=f"{material["title"]} mark as favourite")
                
                if st.button(f"Read Text {material['title']}"):
                    tts_filename = f"{material['title']}.mp3"
                    generate_tts(material["description"], tts_filename)
                    audio_file = open(tts_filename, "rb")
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format="audio/mp3")
                    audio_file.close()

    elif study_material is None:
        st.warning("Could not find any material matching the given search query")
