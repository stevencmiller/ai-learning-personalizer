# 🎯 Streamlit App: True North Student Goal Setting

import streamlit as st

st.set_page_config(page_title="Student Goal Setting | True North", layout="wide")

st.title("🎯 True North Student Goal Setting")

st.subheader("Step 1: Reflect on Last Week")
proud = st.text_input("What did you accomplish last week that you’re proud of?")
improve = st.text_input("What is something you want to keep improving?")

st.subheader("Step 2: Set This Week’s Goals")
academic_goal = st.text_input("Academic Goal (e.g., Master fractions, complete essay)")
passion_project_goal = st.text_input("Passion Project Goal (e.g., Research a podcast topic)")
soft_skill_goal = st.text_input("Soft Skills/Social Goal (e.g., Practice teamwork)")

st.subheader("Step 3: Personal Encouragement")
quote_or_verse = st.text_input("Favorite quote or Bible verse this week")
inspiring_word = st.selectbox(
    "Pick a word that inspires you this week",
    ["Courage", "Perseverance", "Curiosity", "Kindness", "Focus", "Joy"]
)

st.subheader("Step 4: Progress Check (End of Week)")
met_goal = st.radio("Did you meet your goals?", ["Yes", "No", "Partially"])
reflection = st.text_area("Short reflection: What helped you succeed? What obstacles did you face?")

# Submit Button
if st.button("✅ Submit My Weekly Goals"):
    st.success("Goals saved! Great job setting your path forward!")
