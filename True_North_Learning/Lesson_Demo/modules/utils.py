import os
import json

def get_last_lesson(student_name):
    log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")
    if not os.path.exists(log_file):
        return None
    with open(log_file, "r") as f:
        data = json.load(f)
    if not data:
        return None
    last_entry = data[-1]
    return last_entry.get("lesson_name")

def get_next_suggested_lesson(student_name, all_lessons):
    log_file = os.path.join("student_logs", f"{student_name.replace(' ', '_')}_progress.json")
    completed = set()
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            data = json.load(f)
            completed = {entry["lesson_name"] for entry in data}
    for lesson in all_lessons:
        if lesson not in completed:
            return lesson
    return None  # all done!
