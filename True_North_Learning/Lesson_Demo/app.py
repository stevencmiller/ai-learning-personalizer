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
from dashboard import show_dashboard

# Streamlit page setup
st.set_page_config(page_title="True North Learning", page_icon="🧭")
st.title("🧭 True North Learning")
st.write("Welcome to your personalized learning journey!")

# User input
student_name = st.text_input("Enter your name:")

# Navigation between pages
page = st.sidebar.radio("📚 Navigate", ["Lesson", "View Saved Progress", "Dashboard"])

# Page 1: Lesson
if page == "Lesson":
    lesson = st.selectbox("Choose a lesson:", [
        "Prove and Apply the Pythagorean Theorem",
        "Understanding Linear Equations and Functions"
    ])

    if lesson == "Prove and Apply the Pythagorean Theorem":
        result = run_pythagorean_lesson()
        if result:
            st.session_state.lesson_result = result

    elif lesson == "Understanding Linear Equations and Functions":
        result = run_linear_lesson(student_name)
        if result:
            st.session_state.lesson_result = result

    if "lesson_result" in st.session_state and student_name:
        lesson_result = st.session_state.lesson_result

        if st.button("📥 Save Progress"):
            log_progress(
                student_name,
                lesson_result["lesson_name"],
                lesson_result["score"]
            )
            st.success("✅ Progress saved successfully!")

# Page 2: View Raw Progress (Dev Tool)
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

# Page 3: Dashboard
elif page == "Dashboard":
    if student_name:
        show_dashboard(student_name)
    else:
        st.warning("Please enter your name to view your dashboard.")



