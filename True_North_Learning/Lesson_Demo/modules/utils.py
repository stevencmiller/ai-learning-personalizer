import os
import json

LOG_DIR = "student_logs"

def get_log_path(student_name):
    """Returns the file path for a student's progress log."""
    safe_name = student_name.replace(" ", "_").lower()
    return os.path.join(LOG_DIR, f"{safe_name}_log.json")

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


