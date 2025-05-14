# parent_dashboard.py

import os
import json
import streamlit as st

def show_parent_dashboard():
    st.subheader("👨‍👩‍👧 Parent Dashboard")

    student_name = st.text_input("Enter your child's name to view progress:")

    if student_name:
        log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")

        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                data = json.load(f)

            total_lessons = len(data)
            average_score = round(sum(entry['score'] for entry in data) / total_lessons, 2)

            st.markdown(f"**Total Lessons Completed by {student_name}:** {total_lessons}")
            st.markdown(f"**Average Score:** {average_score}%")

            st.markdown("---")
            st.markdown("### 📘 Lesson History")
            for entry in reversed(data):
                st.markdown(f"- **{entry['lesson_name']}** — Score: {entry['score']}% on {entry['timestamp']}")

            st.success("💡 Tip: Encourage your child to reflect on what they’re learning. Ask: *What was the hardest part of today’s lesson?*")

        else:
            st.warning("No progress found for that student.")
