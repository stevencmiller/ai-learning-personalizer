import os
import sys
import streamlit as st
from datetime import datetime

# Ensure module path includes the current subfolder (Lesson_Demo/modules)
current_dir = os.path.dirname(os.path.abspath(__file__))
modules_dir = os.path.join(current_dir, 'modules')
sys.path.insert(0, modules_dir)

# Imports from the modules package
from modules.progress import log_progress
from modules.lesson_linear import run_lesson as run_linear_lesson
from modules.lesson_pythagorean import run_lesson as run_pythagorean_lesson

# Streamlit page setup
st.set_page_config(page_title="True North Learning", page_icon="🧭")
st.title("🧭 True North Learning")
st.write("Welcome to your personalized learning journey!")

# User input
student_name = st.text_input("Enter your name:")

# Lesson selector
lesson = st.selectbox("Choose a lesson:", [
    "Prove and Apply the Pythagorean Theorem",
    "Understanding Linear Equations and Functions"
])

# Lesson execution
lesson_result = None
if lesson == "Prove and Apply the Pythagorean Theorem":
    lesson_result = run_pythagorean_lesson()
elif lesson == "Understanding Linear Equations and Functions":
    lesson_result = run_linear_lesson()

# Save progress
if lesson_result and student_name:
    if st.button("📥 Save Progress"):
        log_progress(
            student_name,
            lesson_result["lesson_name"],
            lesson_result["score"]
        )
        st.success("✅ Progress saved successfully!")

 # ✅ DEVELOPMENT TOOL: Show saved log for this student
        log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")
        if os.path.exists(log_file):
            if st.checkbox("📂 View My Saved Progress (dev tool)"):
                with open(log_file, "r") as f:
                    progress_data = json.load(f)
                st.json(progress_data)
        else:
            st.info("No saved progress found yet.")


