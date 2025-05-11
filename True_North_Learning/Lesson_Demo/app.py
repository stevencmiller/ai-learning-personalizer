import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


import sys
import os
import streamlit as st
from datetime import datetime

# ✅ Add parent directory to system path so utils can be imported

from Utils.progress import log_progress
from lessons.pythagorean import run_pythagorean_lesson
from lessons.linear_equations import run_linear_equations_lesson

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

