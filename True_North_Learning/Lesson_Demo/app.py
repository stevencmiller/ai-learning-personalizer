import streamlit as st
from datetime import datetime
import pandas as pd
import os

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
