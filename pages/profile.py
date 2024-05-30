from authentication import authentication
import streamlit as st
from api_requests.test_score_api import get_users_test_scores
import matplotlib.pyplot as plt
from components.navBar import navBar

st.set_page_config(
    page_title="Profile",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def calculate_average_score(test_data):
    
    total_correct = 0
    total_questions = 0

    for test in test_data:
        total_correct += test["correctAnswers"]
        total_questions += test["amountOfTestQuestions"]

    if total_questions == 0:
        return 0

    average_score = (total_correct / total_questions) * 100
    average_score = round(average_score, 2)

    return average_score

def generate_line_chart(data):

    if data is None:
        return "Could Not Generate a Graph with 0 Tests Taken"
    
    test_numbers = [test["id"] for test in data]
    scores = [test["correctAnswers"] for test in data]

    fig, ax = plt.subplots()
    ax.plot(test_numbers, scores, marker='o', linestyle='-')
    
    ax.set_xlabel('Amount of Tests')
    ax.set_ylabel('Score')
    ax.set_title('Image Test Scores')
    
    return fig

def profile_page():
    test_scores = get_users_test_scores(st.session_state["current_user"]["username"])
    image_tests = []
    regular_test = []

    if test_scores is not None or test_scores == []:
        for score in test_scores:
            if score["testType"] == "image_test":
                image_tests.append(score)
            elif score["testType"] == "regular_test":
                regular_test.append(score)

    col1,col2,col3 = st.columns([1,2,1])
    with col2:

        st.title(f"Profile Page - {st.session_state["current_user"]["username"]}")

        with st.container(border=True):
            st.subheader("Regular Tests")
            st.write(f"Regular Tests taken: {len(regular_test)}")

            with st.expander("See All Regular Tests Taken"):
                for test in regular_test:
                    st.write(test)

            averige_score = calculate_average_score(regular_test)
            if averige_score <= 30:
                st.error(f"Averige regular test score: {averige_score}%")
            elif averige_score <= 54:
                st.warning(f"Averige regular test score: {averige_score}%")
            elif averige_score > 54:
                st.success(f"Averige regular test score: {averige_score}%")

            with st.expander("Show Graph of Your Test history"):
                st.write(generate_line_chart(regular_test))

        with st.container(border=True):
            st.subheader("Image Tests")
            st.write(f"Image Tests taken: {len(image_tests)}")

            with st.expander("See All Image Tests Taken"):
                for test in image_tests:
                    st.write(test)

            averige_score = calculate_average_score(image_tests)
            if averige_score <= 30:
                st.error(f"Averige regular test score: {averige_score}%")
            elif averige_score <= 54:
                st.warning(f"Averige regular test score: {averige_score}%")
            elif averige_score > 54:
                st.success(f"Averige regular test score: {averige_score}%")
            
            with st.expander("Show Graph of Your Test history"):
                st.write(generate_line_chart(image_tests))


        sign_out = st.button("Sign Out",type="primary")

        if sign_out:
            st.session_state.current_user = None
            st.switch_page("app.py")

authentication()
navBar()
if st.session_state["current_user"]["role"] == "GUEST":
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.warning("Current page is not available to guests. Please log in to use this page")
        col1,col2,col3 = st.columns([1,2,1])
        with col2:
            if st.button("Sign In",use_container_width=True):
                st.switch_page("pages/sign_in.py")
            if st.button("Sign Up",use_container_width=True):
                st.switch_page("pages/sign_up.py")
else:
    profile_page()