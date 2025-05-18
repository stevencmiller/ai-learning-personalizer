import os
import json

# Absolute path to the student_logs folder, relative to this utils.py file
LOG_DIR = os.path.join(os.path.dirname(__file__), "../student_logs")

# Make sure the directory exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def get_log_path(student_name):
    safe_name = student_name.replace(" ", "_").lower()
    path = os.path.join(LOG_DIR, f"{safe_name}_log.json")
    # print(f"DEBUG: Log path resolved to: {os.path.abspath(path)}")  # or use st.write if in Streamlit app
    return path


def log_progress(student_name, progress):
    """Appends a new progress entry to the student's log file."""
    log_path = get_log_path(student_name)
    
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(progress)

    with open(log_path, "w") as f:
        json.dump(logs, f, indent=2)

def view_saved_progress(student_name):
    """Returns the saved progress data for the student, or empty list if none."""
    log_path = get_log_path(student_name)
    
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            return json.load(f)
    return []


