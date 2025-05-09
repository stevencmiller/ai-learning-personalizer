import streamlit as st
import pandas as pd
import os

# Paste this into app.py
def display_lesson(lesson):
    
    st.markdown(f"## {lesson.get('title', 'Untitled Lesson')}")
    st.markdown(f"**Objective:** {lesson.get('objective', '')}")
    st.markdown("---")
    if 'warm_up' in lesson:
        st.subheader("Warm-Up")
        st.markdown(lesson['warm_up'])
    if 'instruction' in lesson:
        st.subheader("Direct Instruction")
        st.markdown(lesson['instruction'])
    if 'examples' in lesson:
        st.subheader("Examples")
        st.markdown(lesson['examples'])
    if 'student_practice' in lesson:
        st.subheader("Student Practice")
        st.markdown(lesson['student_practice'])
    if 'assessment' in lesson:
        st.subheader("Assessment")
        st.markdown(lesson['assessment'])
    if 'reflection' in lesson:
        st.subheader("Reflection")
        st.markdown(lesson['reflection'])
    st.markdown("---")
    st.success("Lesson Complete! Great job thinking deeply and working hard.")


st.title("📘 Personalized Learning Lesson")

uploaded_file = st.file_uploader("📂 Upload your lesson CSV", type=["csv"])

if uploaded_file is not None:
   df = pd.read_csv(uploaded_file, encoding='latin1')


   for _, row in df.iterrows():
        content_type = row['type'].strip().lower()
        title = row['title']
        content = row['content']

        if content_type == 'text':
            st.subheader(title)
            st.write(content)

        elif content_type == 'video-script':
            st.subheader(title)
            st.image("https://via.placeholder.com/150", width=150, caption="Instructor Avatar")
            st.info(content)

        elif content_type == 'whiteboard':
            st.subheader(title)
            st.write("📽️ Whiteboard Sketch (description):")
            st.code(content)

        elif content_type == 'quiz':
            st.subheader(title)
            answer = st.radio(content, ['A', 'B', 'C', 'D'])
            if st.button("Check Answer"):
                st.success("✅ Great job!" if answer == "A" else "❌ Try again!")

        elif content_type == 'interaction':
            st.subheader(title)
            user_input = st.text_input(content)
            if user_input:
                st.write("💬 Thanks for sharing!")

        elif content_type == 'closing':
            st.subheader(title)
            st.success(content)
else:
    st.warning("👈 Please upload a lesson CSV file to begin.")

# Sample lesson to test the display
sample_lesson = {
    "title": "Understanding Fractions as Parts of a Whole",
    "objective": "Students will recognize and model fractions using shapes and real-world examples.",
    "warm_up": "Draw a circle and divide it into 4 equal parts. Shade one part. What fraction is shaded?",
    "instruction": "Fractions represent parts of a whole. A numerator is the top number...",
    "examples": "- 1/2 of a pizza means one of two equal slices.\n- 3/4 of a chocolate bar...",
    "student_practice": "1. Color 2/3 of a triangle\n2. Solve: What fraction is left if you eat 3/8 of a cake?",
    "assessment": "Q1: What does the numerator represent?\nQ2: Draw and label 2/5 of a rectangle.",
    "reflection": "What was easy or hard about working with fractions today?"
}

# Call the function
display_lesson(sample_lesson)

if st.button("Show Sample Lesson"):
    display_lesson(sample_lesson)
