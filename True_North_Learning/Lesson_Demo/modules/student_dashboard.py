import os
import json
import streamlit as st
from datetime import datetime

def load_student_progress(student_name):
    log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")
    st.write(f"Looking for progress file at: `{log_file}`")  # Debug output

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            data = json.load(f)
        if isinstance(data, list) and all("lesson_name" in entry for entry in data):
            return data
        else:
            st.warning("Progress file found but has invalid format.")
            return []
    else:
        st.info("No saved progress found yet. Start your first lesson!")
        return []

def show_student_dashboard(student_name):
    st.header(f"📊 Welcome back, {student_name}!")
    progress_data = load_student_progress(student_name)

    if progress_data:
        last_lesson = sorted(progress_data, key=lambda x: x["timestamp"], reverse=True)[0]
        st.success(f"✅ Last completed lesson: **{last_lesson['lesson_name']}** (Score: {last_lesson['score']})")

        # Use columns for button layout
        col1, col2 = st.columns(2)

        with col1:
            if st.button("▶️ Resume Last Lesson"):
                st.session_state.selected_lesson = last_lesson["lesson_name"]
                st.session_state.page = "lesson"
                st.experimental_rerun()

        with col2:
            if st.button("📚 Explore All Lessons"):
                st.session_state.page = "explore"
                st.experimental_rerun()

        # Optional: Show full progress table
        with st.expander("📈 See Full Progress History"):
            st.table(progress_data)

    else:
        st.warning("No progress data found. Click below to begin your learning journey!")

        if st.button("📚 Start Exploring Lessons"):
            st.session_state.page = "explore"
            st.experimental_rerun()
