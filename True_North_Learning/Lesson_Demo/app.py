import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="AI-Powered Learning Platform",
    layout="centered",
    initial_sidebar_state="auto"
)

# Custom utility to log student progress
from utils.progress import log_progress

# Lesson imports (only import what you need for now)
from lessons.pythagorean_theorem import render_pythagorean_lesson
from lessons.linear_equations import render_linear_equations_lesson

# Sidebar for lesson selection
st.sidebar.title("📚 Select a Lesson")
lesson = st.sidebar.radio(
    "Choose a lesson:",
    ("Pythagorean Theorem", "Linear Equations and Functions")
)

# Placeholder for student ID or name
student_name = st.sidebar.text_input("Enter student name to track progress:")

# Main content area
if lesson == "Pythagorean Theorem":
    st.title("📐 Proving and Applying the Pythagorean Theorem")
    render_pythagorean_lesson(student_name)
    if student_name:
        log_progress(student_name, "Pythagorean Theorem", "Lesson Started")

elif lesson == "Linear Equations and Functions":
    st.title("📊 Linear Equations and Functions")
    render_linear_equations_lesson(student_name)
    if student_name:
        log_progress(student_name, "Linear Equations", "Lesson Started")

# Future expansion:
# - Add avatar engagement
# - Whiteboard tools
# - Mastery dashboards
# - Parent/Admin view


