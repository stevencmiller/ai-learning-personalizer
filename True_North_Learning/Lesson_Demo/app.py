import os
import sys

# Get the current directory (Lesson_Demo/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the 'modules' subfolder to the system path
modules_dir = os.path.join(current_dir, 'modules')
sys.path.insert(0, modules_dir)

# Now imports will work
from progress import log_progress

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir))
sys.path.append(parent_dir)

# Now import after modifying path
from utils.progress import log_progress

import streamlit as st
from datetime import datetime

# ✅ Add parent directory to system path so utils can be imported

from modules.progress import log_progress
from modules.lesson_linear import run_lesson as run_linear_lesson
from modules.lesson_pythagorean import run_lesson as run_pythagorean_lesson

st.set_page_config(page_title="True North Learning", page_icon="🧭")

st.title("🧭 True North Learning")
st.write("Welcome to your personalized learning journey!")

student_name = st.text_input("Enter your name:")

lesson = st.selectbox("Choose a lesson:", [
    "Prove and Apply the Pythagorean Theorem",
    "Understanding Linear Equations and Functions"
])

lesson_result = None

if lesson == "Prove and Apply the Pythagorean Theorem":
    lesson_result = run_pythagorean_lesson()
elif lesson == "Understanding Linear Equations and Functions":
    lesson_result = run_linear_equations_lesson()

if lesson_result and student_name:
    if st.button("📥 Save Progress"):
        log_progress(
            student_name,
            lesson_result["lesson_name"],
            lesson_result["score"]
        )
        st.success("✅ Progress saved successfully!")

