import os
import sys
import streamlit as st
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

# Initialize session state variables if not present
if "page" not in st.session_state:
    st.session_state["page"] = "Lessons"  # Default page

if "selected_lesson" not in st.session_state:
    st.session_state["selected_lesson"] = None

# User Role & Page Selection
role = st.sidebar.selectbox("Who is using the app?", ["Student", "Parent"])

if role == "Student":
    student_name = st.sidebar.text_input("👤 Enter your name:")

    # Sync sidebar navigation with session state page
    page = st.sidebar.radio(
        "📚 Navigate",
        ["Lessons", "Dashboard", "View Saved Progress", "Upload Data"],
        index=["Lessons", "Dashboard", "View Saved Progress", "Upload Data"].index(st.session_state["page"])
    )
    st.session_state["page"] = page  # Update page in session_state if changed

    if student_name.strip() == "":
        st.warning("Please enter your name to proceed.")
    else:
        if page == "Lessons":
            # If a lesson is preselected (from resume last lesson), use it
            lesson_options = [
                "Prove and Apply the Pythagorean Theorem",
                "Understanding Linear Equations and Functions"
            ]

            default_index = 0
            if st.session_state.selected_lesson in lesson_options:
                default_index = lesson_options.index(st.session_state.selected_lesson)

            lesson = st.selectbox("Choose a lesson:", lesson_options, index=default_index)

            # Save the currently selected lesson to session_state
            st.session_state.selected_lesson = lesson

            if lesson == "Prove and Apply the Pythagorean Theorem":
                result = run_pythagorean_lesson()
                if result:
                    st.session_state.lesson_result = result

            elif lesson == "Understanding Linear Equations and Functions":
                result = run_linear_lesson(student_name)
                if result:
                    st.session_state.lesson_result = result

            if "lesson_result" in st.session_state:
                lesson_result = st.session_state.lesson_result

                if st.button("📥 Save Progress"):
                    log_progress(
                        student_name,
                        lesson_result["lesson_name"],
                        lesson_result["score"]
                    )
                    st.success("✅ Progress saved successfully!")

        elif page == "Dashboard":
            show_student_dashboard(student_name)

        elif page == "View Saved Progress":
            log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")
            if os.path.exists(log_file):
                if st.checkbox("📂 View My Saved Progress (dev tool)"):
                    with open(log_file, "r") as f:
                        progress_data = json.load(f)
                    st.json(progress_data)
            else:
                st.info("No saved progress found yet.")

        elif page == "Upload Data":
            st.info("📤 Upload data feature coming soon.")

elif role == "Parent":
    show_parent_dashboard()
