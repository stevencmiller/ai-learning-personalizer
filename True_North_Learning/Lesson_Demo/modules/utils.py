import os
import json
from datetime import datetime

def log_progress(student_name, lesson_name, score):
    log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            data = json.load(f)
    else:
        data = []

    new_entry = {
        "lesson_name": lesson_name,
        "score": score,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data.append(new_entry)

    with open(log_file, "w") as f:
        json.dump(data, f, indent=4)

def view_saved_progress(student_name):
    log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            return json.load(f)
    return []


