# dashboard.py

import os
import json
import streamlit as st
import pandas as pd

def load_progress(student_name):
    log_file = f"student_logs/{student_name.replace(' ', '_')}_progress.json"

    if not os.path.exists(log_file):
        st.warning("No progress data found for this student.")
        return []

    with open(log_file, "r") as f:
        data = json.load(f)

    return data

def show_dashboard(student_name):
    st.header(f"📊 {student_name}'s Progress Dashboard")
    progress_data = load_progress(student_name)

    if not progress_data:
        return

    # Convert to DataFrame for sorting/filtering
    df = pd.DataFrame(progress_data)

    # Reorder columns for clarity
    columns_order = ["lesson_name", "score", "timestamp", "completion_status", "standard_id"]
    df = df[[col for col in columns_order if col in df.columns]]

    # Format timestamp as datetime if needed
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Sort by timestamp descending
    df = df.sort_values(by="timestamp", ascending=False)

    st.dataframe(df, use_container_width=True)
