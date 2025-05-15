import os
import sys
import streamlit as st
from datetime import datetime
import json

# Ensure module path includes the current subfolder (Lesson_Demo/modules)
current_dir = os.path.dirname(os.path.abspath(__file__))
modules_dir = os.path.join(current_dir, 'modules')
sys.path.insert(0, modules_dir)

# Imports from the modules package
from modules.progress import log_progress
from modules.lesson_linear import run_lesson as run_linear_lesson
from modules.lesson_pythagorean import run_lesson as run_pythagorean_lesson
from modules.student_dashboard import show_student_dashboard
from modules.parent_dashboard import show_parent_dashboard

# Streamlit page setup
st.set_page_config(page_title="True North Learning", page_icon="🧭")
st.markdown("# 🧭 True North Learning\nWelcome to your personalized learning journey!")
st.write("Welcome to your personalized learning journey!")

# User Role & Page Selection
role = st.sidebar.selectbox("Who is using the app?", ["Student", "Parent"])
page = st.sidebar.radio("📚 Navigate", ["Lessons", "Dashboard", "View Saved Progress", "Upload Data"])

# --- STUDENT VIEW ---
if role == "Student":
    student_name = st.sidebar.text_input("👤 Enter your name:")

    if page == "Lessons":
        if student_name:
            # Lesson options
            lesson_options = [
                "Prove and Apply the Pythagorean Theorem",
                "Understanding Linear Equations and Functions"
            ]

            # Preselect lesson if coming from dashboard
            default_index = 0
            if "selected_lesson" in st.session_state:
                if st.session_state.selected_lesson in lesson_options:
                    default_index = lesson_options.index(st.session_state.selected_lesson)

            lesson = st.selectbox("Choose a lesson:", lesson_options, index=default_index)

            # Run selected lesson
            if lesson == "Prove and Apply the Pythagorean Theorem":
                result = run_pythagorean_lesson()
                if result:
                    st.session_state.lesson_result = result

            elif lesson == "Understanding Linear Equations and Functions":
                result = run_linear_lesson(student_name)
                if result:
                    st.session_state.lesson_result = result

            # Save Progress
            if "lesson_result" in st.session_state:
                lesson_result = st.session_state.lesson_result
                if st.button("📥 Save Progress"):
                    log_progress(
                        student_name,
                        lesson_result["lesson_name"],
                        lesson_result["score"]
                    )
                    st.success("✅ Progress saved successfully!")

        else:
            st.warning("Please enter your name to begin lessons.")

    elif page == "Dashboard":
        if student_name:
            show_student_dashboard(student_name)
        else:
            st.warning("Please enter your name to view your dashboard.")

    elif page == "View Saved Progress":
        if student_name:
            log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")
            if os.path.exists(log_file):
                if st.checkbox("📂 View My Saved Progress (dev tool)"):
                    with open(log_file, "r") as f:
                        progress_data = json.load(f)
                    st.json(progress_data)
            else:
                st.info("No saved progress found yet.")
        else:
            st.warning("Please enter your name to load your saved progress.")

    elif page == "Upload Data":
        st.info("📤 Upload data feature coming soon.")

# --- PARENT VIEW ---
elif role == "Parent":
    show_parent_dashboard()
