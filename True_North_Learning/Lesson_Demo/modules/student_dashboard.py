import streamlit as st
import os
import pandas as pd

def get_progress_file_path(student_name):
    return os.path.join("student_logs", f"{student_name}_progress.csv")

def show_student_dashboard(student_name):
    st.header(f"📊 {student_name}'s Progress Dashboard")

    file_path = get_progress_file_path(student_name)

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)

        if not df.empty:
            st.subheader("Lesson History")
            st.dataframe(df)

            avg_score = df["score"].mean()
            st.metric("Average Score", f"{avg_score:.2f}")
        else:
            st.info("No progress recorded yet.")
    else:
        st.info("No progress recorded yet. Try completing a lesson!")


        if st.button("📚 Start Exploring Lessons"):
            st.session_state.page = "Lessons"
            st.experimental_rerun()

