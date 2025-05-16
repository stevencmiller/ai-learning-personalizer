import streamlit as st
import pandas as pd
from modules.utils import view_saved_progress

def show_student_dashboard(student_name):
    st.header(f"📊 {student_name}'s Progress Dashboard")

    logs = view_saved_progress(student_name)

    if logs:
        df = pd.DataFrame(logs)

        if not df.empty:
            st.subheader("Lesson History")
            st.dataframe(df)

            if "score" in df.columns:
                avg_score = df["score"].mean()
                st.metric("Average Score", f"{avg_score:.2f}")
            else:
                st.warning("No scores available in the logs yet.")
        else:
            st.info("No progress recorded yet.")
    else:
        st.info("No progress recorded yet. Try completing a lesson!")


        if st.button("📚 Start Exploring Lessons"):
            st.session_state.page = "Lessons"
            
