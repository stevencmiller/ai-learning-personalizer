import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

st.set_page_config(
    page_title="True North Learning",
    page_icon="📘",
    layout="wide"
)

# -----------------------------
# Log Progress Function
# -----------------------------
def log_progress(student_name, lesson_name, mastery_score):
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "student_name": student_name,
        "lesson_name": lesson_name,
        "mastery_score": mastery_score
    }

    log_file = os.path.join(log_folder, f"{student_name}_progress.json")

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(log_entry)

    with open(log_file, "w") as f:
        json.dump(data, f, indent=2)


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

# Final section of your app — AFTER quiz or review
st.subheader("Lesson Summary")

student_name = st.text_input("Enter your name to track progress:", key="student_name")

if student_name:
    mastery_score = 90  # Replace this with real quiz score if available
    if st.button("Save My Progress"):
        log_progress(student_name, "Pythagorean Theorem", mastery_score)
        st.success("✅ Your progress has been logged!")

