import streamlit as st
from modules.lesson_handler import show_lessons
from modules.student_dashboard import show_student_dashboard
from modules.utils import log_progress

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

# Get or prompt for student name
if not st.session_state.student_name:
    st.title("🎓 Welcome to True North Learning")
    student_name = st.text_input("Enter your name to begin:")
    if student_name:
        st.session_state.student_name = student_name
        st.experimental_rerun()
else:
    student_name = st.session_state.student_name

    st.sidebar.title("📌 Navigation")
    if st.sidebar.button("🏠 Dashboard"):
        st.session_state.page = "Dashboard"
    if st.sidebar.button("📚 Explore Lessons"):
        st.session_state.page = "Lessons"

    st.sidebar.markdown("---")
    if st.sidebar.button("🔄 Restart"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()

    # Show appropriate page
    if st.session_state.page == "Dashboard":
        show_student_dashboard(student_name)
    elif st.session_state.page == "Lessons":
        progress = show_lessons(student_name)
        if progress:
            log_progress(student_name, progress)
            st.success("✅ Your progress has been saved!")
            if st.button("⬅️ Back to Dashboard"):
                st.session_state.page = "Dashboard"
                st.experimental_rerun()



