import os
import json
import streamlit as st

def show_student_dashboard(student_name):
    st.subheader(f"📊 {student_name}'s Progress Dashboard")

    log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")
    st.write(f"Looking for progress file at: {log_file}")

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            data = json.load(f)
        st.write(f"Loaded progress data: {data}")

        total_lessons = len(data)
        average_score = round(sum(entry['score'] for entry in data) / total_lessons, 2)

        st.markdown(f"**Total Lessons Completed:** {total_lessons}")
        st.markdown(f"**Average Score:** {average_score}%")

        st.markdown("---")
        st.markdown("### 📚 Lesson History")
        for entry in reversed(data):
            st.markdown(f"- **{entry['lesson_name']}** — Score: {entry['score']}% on {entry['timestamp']}")

        st.markdown("---")
        st.markdown("🎯 What would you like to do next?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("▶️ Resume Last Lesson"):
                st.session_state['selected_lesson'] = data[-1]['lesson_name']
                st.experimental_rerun()
        with col2:
            if st.button("📖 Explore All Lessons"):
                st.session_state['selected_lesson'] = None
                st.experimental_rerun()

    else:
        st.info("No saved progress found yet. Start your first lesson!")

