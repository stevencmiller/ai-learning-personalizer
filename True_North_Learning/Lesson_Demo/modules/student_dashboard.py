import os
import json
import streamlit as st
import pandas as pd
from modules.utils import get_log_path

def load_student_progress(student_name):
    log_file = get_log_path(student_name)
    
    st.write(f"📁 Debug: Looking for file at `{log_file}`")  # Add debug output

    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                data = json.load(f)
            if isinstance(data, list) and all("lesson_name" in entry for entry in data):
                return data
            else:
                st.warning("⚠️ Progress file exists but has unexpected format.")
                return []
        except Exception as e:
            st.error(f"❌ Error reading progress: {e}")
            return []
    else:
        st.info("ℹ️ No saved progress found yet. Start your first lesson!")
        return []

