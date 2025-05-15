import os
import json
from datetime import datetime

import os

def log_progress(student_name, lesson_name, score):
    log_dir = "student_logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    # rest of your logging code here... 
    
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
