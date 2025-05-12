import streamlit as st
from datetime import datetime

def run_lesson(student_name: str = ""):
    # keep the same content
    st.title("📈 Understanding Linear Equations and Functions")
    st.write("Let’s learn how linear equations can help us model real-world problems!")

    st.subheader("🔍 Discover")
    st.markdown("A **linear equation** can be written as: ")
    st.latex(r"y = mx + b")
    st.markdown("Where **m** is the slope and **b** is the y-intercept.")

    st.subheader("🧠 Think")
    st.markdown("**Try this:** What is the slope of the line given by the equation y = 2x + 3?")

    user_answer = st.number_input("Your answer for slope (m):", step=0.1)
    submitted = st.button("Check Answer")

    if submitted:
        correct_answer = 2
        if abs(user_answer - correct_answer) < 0.1:
            st.success("✅ That’s correct! The slope is 2.")
            score = 100
        else:
            st.error("❌ Not quite. The correct slope is 2.")
            score = 0

        st.subheader("📊 Lesson Summary")
        st.markdown(f"**Score:** {score}/100")

        return {
            "student_name": student_name,
            "lesson_name": "Linear Equations and Functions",
            "standard_id": "8.F.B.4",
            "score": score,
            "completion_status": "completed",
            "timestamp": datetime.now()
        }
    return None


