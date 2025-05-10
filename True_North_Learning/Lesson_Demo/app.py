import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

log_progress(
    student_name=st.session_state.get("student_name", "anonymous"),
    lesson_title="Pythagorean Theorem",
    concept="Apply the Pythagorean Theorem",
    status="Completed"
)

from lessons.pythagorean import run_pythagorean_lesson
from lessons.linear_equations import run_linear_equations_lesson

# --- Logging Function ---
def log_progress(data: dict, filepath="learning_log.csv"):
    df = pd.DataFrame([data])
    if os.path.exists(filepath):
        df.to_csv(filepath, mode='a', header=False, index=False)
    else:
        df.to_csv(filepath, mode='w', header=True, index=False)

# --- Sidebar Navigation ---
st.sidebar.title("Lesson Navigation")
lesson_choice = st.sidebar.selectbox(
    "Choose a lesson:",
    ["Select", "Pythagorean Theorem", "Linear Equations & Functions"]
)

# --- Lesson Dispatcher ---
if lesson_choice == "Pythagorean Theorem":
    results = run_pythagorean_lesson()
    if results:
        log_progress(results)

elif lesson_choice == "Linear Equations & Functions":
    results = run_linear_equations_lesson()
    if results:
        log_progress(results)

display_lesson(sample_lesson)

if st.button("Show Sample Lesson"):
    display_lesson(sample_lesson)
