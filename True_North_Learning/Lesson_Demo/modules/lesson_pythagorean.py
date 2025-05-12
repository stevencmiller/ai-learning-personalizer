import streamlit as st
from datetime import datetime

def run_lesson(student_name: str = ""):
    # keep the same content
    st.write("Welcome! Let’s explore how the Pythagorean Theorem helps us solve problems involving right triangles.")
    st.subheader("🔍 Discover")
    st.latex(r"a^2 + b^2 = c^2")
    st.markdown("This formula applies to **right triangles**. The two shorter sides are *a* and *b*, and the longest side (the hypotenuse) is *c*.")

    st.subheader("🧠 Think")
    st.markdown("**Try this problem:** A right triangle has legs of length 3 and 4. What is the length of the hypotenuse?")

    user_answer = st.number_input("Your answer for c (the hypotenuse):", min_value=0.0, step=0.1, format="%.1f")
    submitted = st.button("Check Answer")

    if submitted:
        correct_answer = 5.0
        if abs(user_answer - correct_answer) < 0.1:
            st.success("✅ Great job! That’s correct.")
            score = 100
        else:
            st.error(f"❌ Not quite. The correct answer is {correct_answer}.")
            score = 0

        st.subheader("📊 Lesson Summary")
        st.markdown(f"**Score:** {score}/100")

        return {
            "student_name": student_name,
            "lesson_name": "Pythagorean Theorem",
            "standard_id": "8.G.B.6",
            "score": score,
            "completion_status": "completed",
            "timestamp": datetime.now()
        }
    return None


