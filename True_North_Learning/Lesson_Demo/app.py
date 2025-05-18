import streamlit as st
from modules.lesson_handler import show_lessons
from modules.student_dashboard import show_student_dashboard
from modules.utils import log_progress

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

# Prompt for name if not entered yet
if not st.session_state.student_name:
    st.title("🎓 Welcome to True North Learning")
    student_name_input = st.text_input("Enter your name to begin:")
    if student_name_input:
        st.session_state.student_name = student_name_input.strip()
        st.rerun()

else:
    student_name = st.session_state.student_name

    # Sidebar navigation
    with st.sidebar:
        st.header(f"👋 Hello, {student_name}!")
        
        # Use radio buttons for navigation (safer and more stable)
        st.session_state.page = st.radio(
            "Navigate", ["Dashboard", "Lessons"], index=0 if st.session_state.page == "Dashboard" else 1
        )

        st.markdown("---")
        if st.button("🔁 Restart"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()  # restart app cleanly

    # Route between pages
    if st.session_state.page == "Dashboard":
        show_student_dashboard(student_name)

    elif st.session_state.page == "Lessons":
        progress = show_lessons(student_name)
        if progress:
            log_progress(student_name, progress)
            st.success("✅ Your progress has been saved!")

        if st.button("⬅️ Back to Dashboard"):
            st.session_state.page = "Dashboard"





