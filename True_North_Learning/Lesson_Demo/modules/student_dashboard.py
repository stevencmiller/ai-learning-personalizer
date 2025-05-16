import os
import json
import streamlit as st
import pandas as pd
from modules.utils import get_log_path

def load_student_progress(student_name):
    log_file = get_log_path(student_name)
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

# Example usage in the dashboard function
def show_student_dashboard(student_name):
    progress = load_student_progress(student_name)

    if progress:
        st.write("### Your Saved Progress")
        df = pd.DataFrame(progress)
        st.table(df)
    else:
        if st.button("📚 Start Exploring Lessons"):
            st.session_state.page = "Lessons"

