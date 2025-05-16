import streamlit as st
import os
from modules.student_dashboard import show_student_dashboard
from modules.lesson_handler import show_lessons
from modules.utils import log_progress

# Create the student log folder if it doesn't exist
if not os.path.exists("student_logs"):
    os.makedirs("student_logs")

# Set page config
st.set_page_config(page_title="True North Learning", layout="wide")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "student_name" not in st.session_state:
    st.session_state.student_name = ""
if "selected_lesson" not in st.session_state:
    st.session_state.selected_lesson = None

# Sidebar
st.sidebar.title("🔹 Navigation")
st.sidebar.write("Welcome to True North Learning!")

# Student name input (top of sidebar)
student_name = st.sidebar.text_input("Enter your name:", st.session_state.student_name)
if student_name:
    st.session_state.student_name = student_name

# Navigation buttons
if student_name:
    if st.sidebar.button("🏠 Dashboard"):
        st.session_state.page = "Dashboard"
    if st.sidebar.button("📘 Lessons"):
        st.session_state.page = "Lessons"

# Main content logic
if not st.session_state.student_name:
    st.warning("Please enter your name in the sidebar to continue.")
elif st.session_state.page == "Dashboard":
    show_student_dashboard(st.session_state.student_name)
elif st.session_state.page == "Lessons":
    result = show_lessons(st.session_state.student_name)
    if result:
        log_progress(st.session_state.student_name, result)
        st.success("✅ Progress saved! You can return to the dashboard to see it.")

        else:
            st.info("No progress data available yet.")


