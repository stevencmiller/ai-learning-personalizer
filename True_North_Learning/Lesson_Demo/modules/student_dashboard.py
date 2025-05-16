import streamlit as st
from modules.utils import view_saved_progress

def show_student_dashboard(student_name):
    st.header(f"📊 Welcome back, {student_name}!")

    progress_data = view_saved_progress(student_name)

    if progress_data:
        # Sort by latest timestamp
        last_lesson = sorted(progress_data, key=lambda x: x["timestamp"], reverse=True)[0]

        st.success(f"✅ Last completed lesson: **{last_lesson['lesson_name']}** (Score: {last_lesson['score']})")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("▶️ Resume Last Lesson"):
                st.session_state.selected_lesson = last_lesson["lesson_name"]
                st.session_state.page = "Lessons"
                st.experimental_rerun()

        with col2:
            if st.button("📚 Explore All Lessons"):
                st.session_state.page = "Lessons"
                st.experimental_rerun()

        with st.expander("📈 See Full Progress History"):
            st.table(progress_data)

    else:
        st.warning("No progress data found yet. Click below to begin your learning journey!")

        if st.button("📚 Start Exploring Lessons"):
            st.session_state.page = "Lessons"
            st.experimental_rerun()

