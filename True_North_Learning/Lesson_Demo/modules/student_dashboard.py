# student_dashboard.py
import os
import json
import streamlit as st

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

    if st.button("Resume Last Lesson"):
        # Safely get the last lesson from data if it exists
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                data = json.load(f)
            if data:
                last_lesson_name = data[-1]['lesson_name']
                # Save to session_state for navigation and preselection
                st.session_state.selected_lesson = last_lesson_name
                st.session_state.page = 'Lessons'
                st.experimental_rerun()
            else:
                st.warning("No lessons found to resume.")
        else:
            st.warning("No saved progress found yet.")

    if st.button("Explore All Lessons"):
        st.session_state.page = 'Lessons'
        st.experimental_rerun()
