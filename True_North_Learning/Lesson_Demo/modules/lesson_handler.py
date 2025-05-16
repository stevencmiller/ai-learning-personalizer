import streamlit as st
from datetime import datetime

# Sample lessons for demo purposes
LESSONS = [
    {"name": "Intro to Fractions", "content": "What is 1/2 + 1/4?", "answer": "3/4"},
    {"name": "Decimals & Percents", "content": "What is 25% of 80?", "answer": "20"},
    {"name": "Algebra Basics", "content": "Solve: 2x = 10", "answer": "5"},
]

def show_lessons(student_name):
    st.header("📚 Choose a Lesson")
    
    lesson_names = [lesson["name"] for lesson in LESSONS]
    selected_lesson = st.selectbox("Pick a lesson to begin:", lesson_names)

    lesson = next((l for l in LESSONS if l["name"] == selected_lesson), None)

    if lesson:
        st.subheader(f"Lesson: {lesson['name']}")
        user_answer = st.text_input(lesson["content"])

        if st.button("Submit Answer"):
            is_correct = user_answer.strip() == lesson["answer"]
            score = 100 if is_correct else 0

            st.write("✅ Correct!" if is_correct else f"❌ Incorrect. The correct answer was: {lesson['answer']}")
            
            return {
                "lesson_name": lesson["name"],
                "score": score,
                "timestamp": datetime.now().isoformat()
            }

    return None
