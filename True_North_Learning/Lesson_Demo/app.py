import streamlit as st
import pandas as pd

st.set_page_config(page_title="True North Lesson", layout="centered")
st.title("True North Math Lesson")
st.subheader("Grade 4 – Interpreting a Fraction as Division (4.NF.3b)")

lesson_file = st.file_uploader("Upload your lesson CSV", type="csv")

if lesson_file:
    df = pd.read_csv(lesson_file)

    for _, row in df.iterrows():
        section_type = row['type'].lower()
        title = row['title']
        content = row['content']

        st.markdown(f"### {title}")

        if section_type == "text":
            st.write(content)

        elif section_type == "video-script":
            st.image("assets/avatar_placeholder.png", caption="Digital Avatar Teaching Moment")
            st.info(f"**Avatar Says:** {content}")
            with st.expander("What are you thinking so far?"):
                st.text_area("Reflect here...")

        elif section_type == "whiteboard":
            st.write(content)
            st.image("https://upload.wikimedia.org/wikipedia/commons/4/42/Pizza_with_slices.png", caption="Visual Example")

        elif section_type == "interaction":
            user_input = st.text_input("Your answer:")
            if user_input:
                st.success("Great thinking! Let's reflect on that together.")

        elif section_type == "quiz":
            answer = st.radio("Choose your answer:", ["a) 1 3/4", "b) 7/4", "c) 4/7", "d) 2"])
            if answer:
                if answer == "b) 7/4":
                    st.success("Correct!")
                else:
                    st.error("Try again. Hint: a ÷ b = a/b")

        elif section_type == "closing":
            st.success(content)
            st.text_input("What did you enjoy or learn today?")
            st.selectbox("How confident do you feel now?", ["Very", "Somewhat", "Not Yet"])
else:
    st.info("Please upload a lesson CSV to begin.")
