import os
import json

def log_progress(student_name, progress_entry):
    log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(progress_entry)

    with open(log_file, "w") as f:
        json.dump(data, f, indent=4)

def view_saved_progress(student_name):
    log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            return json.load(f)
    return []

