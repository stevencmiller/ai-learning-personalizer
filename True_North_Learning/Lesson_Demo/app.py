import streamlit as st
import os
from modules.student_dashboard import show_student_dashboard
from modules.lesson_handler import show_lessons
from modules.utils import log_progress, view_saved_progress

# Create a folder to store student logs if it doesn't exist
if not os.path.exists("student_logs"):
    os.makedirs("student_logs")

# Sidebar: User Role Selection
st.sidebar.title("True North Learning")
role = st.sidebar.selectbox("Who are you?", ["Student", "Parent", "Educator"])

# Sidebar: Enter name if student
if role == "Student":
    student_name = st.sidebar.text_input("Enter your name:")
    if student_name:
        st.sidebar.success(f"Welcome, {student_name}!")
        page = st.sidebar.radio("Navigate", ["Dashboard", "Lessons"])

        st.session_state.page = page  # Store current page

        if page == "Dashboard":
            show_student_dashboard(student_name)

        elif page == "Lessons":
            result = show_lessons(student_name)
            if result:
                log_progress(student_name, result["lesson_name"], result["score"])
                st.success("Progress saved!")
    else:
        st.warning("Please enter your name to continue.")

else:
    st.info(f"{role} features coming soon! Check back later.")



