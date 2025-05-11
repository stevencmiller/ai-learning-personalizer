import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from utils.progress import log_progress
from lessons.pythagorean_theorem import run_pythagorean_lesson
from lessons.linear_equations import render_linear_equations_lesson

st.set_page_config(page_title="AI-Powered Math Coach", layout="centered")

st.title("🎯 AI-Powered Personalized Learning")
st.markdown("Welcome to your learning dashboard! Choose a lesson to begin:")

# Student name input (shared across lessons)
student_name = st.text_input("Enter your name to track progress:")

# Lesson selection
lesson_options = {
    "Prove and Apply the Pythagorean Theorem": run_pythagorean_lesson,
    "Linear Equations and Functions": render_linear_equations_lesson
}

lesson_choice = st.selectbox("Select a lesson:", list(lesson_options.keys()))

if student_name:
    lesson_function = lesson_options[lesson_choice]
    result = lesson_function(student_name=student_name)

    if result:
        # Centralized logging call
        log_progress(
            student_name=result["student_name"],
            lesson_name=result["lesson_name"],
            score=result["score"]
        )
        st.success("✅ Your progress has been logged!")
else:
    st.warning("👤 Please enter your name to begin.")
