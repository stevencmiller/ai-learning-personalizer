import os
import streamlit as st
from modules.student_dashboard import show_student_dashboard
from modules.lesson_handler import show_lessons
from modules.utils import log_progress, view_saved_progress

# Ensure student_logs folder exists
if not os.path.exists("student_logs"):
    os.makedirs("student_logs")

st.title("🎓 True North Learning")

# Simple login: enter student name
student_name = st.text_input("Enter your name to continue:")

if student_name:
    # Show dashboard by default
    page = st.session_state.get("page", "Dashboard")

    # Sidebar navigation
    with st.sidebar:
        st.header(f"Hello, {student_name}!")
        if st.button("📊 Dashboard"):
            st.session_state.page = "Dashboard"
            page = "Dashboard"
        if st.button("📘 Explore Lessons"):
            st.session_state.page = "Lessons"
            page = "Lessons"

    if page == "Dashboard":
        show_student_dashboard(student_name)

    elif page == "Lessons":
        # show_lessons returns progress dict or None
        result = show_lessons(student_name)
        if result:
            log_progress(student_name, result)
            st.success("✅ Progress saved! Return to dashboard to see your progress.")
else:
    st.info("Please enter your name to begin learning.")


