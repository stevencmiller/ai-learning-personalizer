# 🧮 Streamlit App: Math Diagnostic

import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Math Diagnostic", layout="wide")

st.title("🧠 Math Diagnostic Assessment")

# Simulated diagnostic input
st.subheader("📋 Enter Strand Scores")

strands = [
    "Expressions & Equations",
    "Ratios & Proportions",
    "Geometry",
    "Statistics"
]

scores = {}
for strand in strands:
    scores[strand] = st.slider(f"{strand} Score", 0, 100, 75)

# Scoring function
def assess_mastery_by_strand(scores_dict):
    mastery_results = {}
    for strand, score in scores_dict.items():
        if score >= 90:
            mastery_results[strand] = "Mastered"
        elif score >= 70:
            mastery_results[strand] = "In Progress"
        else:
            mastery_results[strand] = "Not Yet Mastered"
    return mastery_results

# Load pathway logic from JSON
@st.cache_data
def load_pathways():
    try:
        with open("curriculum/pathway_logic_math.json") as f:
            return json.load(f)
    except:
        return {}

pathways = load_pathways()

# Compute and display results
if st.button("Evaluate Mastery"):
    results = assess_mastery_by_strand(scores)
    st.subheader("📊 Mastery Results")
    for strand, level in results.items():
        st.markdown(f"**{strand}**: {level}")
        suggestion = pathways.get(strand, {}).get(level, "No recommendation available.")
        st.markdown(f"→ Suggested Path: {suggestion}")

    # Generate downloadable CSV string
    csv_data = "Strand,Mastery Level\n" + "\n".join([f"{s},{l}" for s, l in results.items()])
    st.download_button(
        label="📥 Download Results as CSV",
        data=csv_data,
        file_name="math_diagnostic_results.csv",
        mime="text/csv"
    )
