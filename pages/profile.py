#TODO show personal information here
#Stuff like tests taken and scores. Best score, averige score
#Maybe a chart of how the user has improved
from authentication import authentication
import streamlit as st

authentication()

sign_out = st.button("Sign Out",type="primary")

if sign_out:
    st.session_state.current_user = None
    st.switch_page("app.py")