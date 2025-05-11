import os
import json
from datetime import datetime

def log_progress(student_name, lesson_name, score):
    progress_entry = {
        "student_name": student_name,
        "lesson_name": lesson_name,
        "score": score,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    log_folder = "student_logs"
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, f"{student_name.replace(' ', '_')}_progress.json")

    # Append or create log
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(progress_entry)

    with open(log_file, "w") as f:
        json.dump(data, f, indent=4)
