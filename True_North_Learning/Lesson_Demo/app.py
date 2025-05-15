import streamlit as st

# ✅ MUST be the first Streamlit command
st.set_page_config(page_title="True North Learning", page_icon="🧭")

import os
from modules.student_dashboard import show_student_dashboard
from modules.lesson_handler import show_lessons
from modules.utils import log_progress, view_saved_progress

# Create a folder to store student logs if it doesn't exist
if not os.path.exists("student_logs"):
    os.makedirs("student_logs")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"
if "selected_lesson" not in st.session_state:
    st.session_state.selected_lesson = None

st.title("🧭 True North Learning")

# Simple student login / entry
student_name = st.text_input("Enter your name to begin:", key="student_name_input")

if student_name:
    page = st.session_state.page

    if page == "Dashboard":
        show_student_dashboard(student_name)

    elif page == "Lessons":
        lesson_result = show_lessons(student_name)
        if lesson_result:
            log_progress(
                student_name,
                lesson_result["lesson_name"],
                lesson_result["score"]
            )
            st.success("✅ Progress saved successfully!")

    elif page == "View Saved Progress":
        view_saved_progress(student_name)

    elif page == "Upload Data":
        st.info("📤 Upload data feature coming soon.")

else:
    st.warning("👋 Please enter your name to begin.")


