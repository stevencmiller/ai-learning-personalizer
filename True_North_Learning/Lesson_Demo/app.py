import streamlit as st
import os
from modules.student_dashboard import show_student_dashboard
from modules.lesson_handler import show_lessons
from modules.utils import log_progress, view_saved_progress

# Create a folder to store student logs if it doesn't exist
if not os.path.exists("student_logs"):
    os.makedirs("student_logs")

# Set Streamlit page config
st.set_page_config(page_title="True North Learning", page_icon="🌟", layout="wide")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "student_name" not in st.session_state:
    st.session_state.student_name = ""

# App title
st.title("🌟 True North Learning Platform")

# Login or name input
if st.session_state.student_name == "":
    student_name = st.text_input("Enter your name to begin:", key="student_name_input")
    if st.button("Start Learning"):
        if student_name.strip() != "":
            st.session_state.student_name = student_name.strip()
            st.experimental_rerun()
        else:
            st.warning("Please enter a valid name to continue.")
else:
    student_name = st.session_state.student_name

    # Sidebar navigation
    st.sidebar.title("🔍 Navigation")
    st.session_state.page = st.sidebar.radio("Go to:", ["Dashboard", "Lessons", "View Saved Progress"])

    page = st.session_state.page

    if page == "Dashboard":
        show_student_dashboard(student_name)

    elif page == "Lessons":
        lesson_result = show_lessons(student_name)

        if lesson_result:
            # Save progress
            log_progress(student_name, lesson_result["lesson_name"], lesson_result["score"])
            st.success("✅ Progress saved!")

    elif page == "View Saved Progress":
        st.header(f"📚 Full Progress for {student_name}")
        saved = view_saved_progress(student_name)
        if saved:
            st.table(saved)
        else:
            st.info("No progress data available yet.")


