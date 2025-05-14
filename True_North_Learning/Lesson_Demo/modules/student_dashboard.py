# student_dashboard.py

import os
import json
import streamlit as st
from modules.utils import get_last_lesson, get_next_suggested_lesson  # Make sure this exists

def show_student_dashboard(student_name):
    st.subheader(f"📊 {student_name}'s Progress Dashboard")

    log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            data = json.load(f)

        total_lessons = len(data)
        average_score = round(sum(entry['score'] for entry in data) / total_lessons, 2)

        st.markdown(f"**Total Lessons Completed:** {total_lessons}")
        st.markdown(f"**Average Score:** {average_score}%")

        st.markdown("---")
        st.markdown("### 📚 Lesson History")
        for entry in reversed(data):
            st.markdown(f"- **{entry['lesson_name']}** — Score: {entry['score']}% on {entry['timestamp']}")

    else:
        st.info("No saved progress found yet. Start your first lesson!")

    st.markdown("---")
    st.markdown("🎯 What would you like to do next?")

    col1, col2 = st.columns(2)

    all_lessons = [
        "Prove and Apply the Pythagorean Theorem",
        "Understanding Linear Equations and Functions"
    ]

    with col1:
        if st.button("📘 Resume Last Lesson"):
            last = get_last_lesson(student_name)
            if last:
                st.session_state.selected_lesson = last
                st.session_state.page = "Lessons"
                st.rerun()
            else:
                st.warning("No saved lessons found to resume.")

    with col2:
        if st.button("🚀 Start Next Suggested Lesson"):
            next_lesson = get_next_suggested_lesson(student_name, all_lessons)
            if next_lesson:
                st.session_state.selected_lesson = next_lesson
                st.session_state.page = "Lessons"
                st.rerun()
            else:
                st.success("🎉 You've completed all available lessons!")

