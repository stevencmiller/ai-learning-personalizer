import streamlit as st
import json
import csv

# Streamlit App: Math Diagnostic Scoring
st.set_page_config(page_title="🧠 Math Diagnostic Scoring Tool", layout="centered")
st.title("📊 Math Diagnostic Scoring Tool")
st.write("Enter student scores (0–100) for each math strand to assess mastery levels.")

# Input form
with st.form("math_form"):
    expressions = st.slider("Expressions & Equations", 0, 100, 75)
    ratios = st.slider("Ratios & Proportions", 0, 100, 75)
    geometry = st.slider("Geometry", 0, 100, 75)
    statistics = st.slider("Statistics", 0, 100, 75)
    number_sense = st.slider("Number Sense & Operations", 0, 100, 75)
    submitted = st.form_submit_button("Submit")

# Mastery function
def assess_math_mastery_by_strand(scores_dict):
    mastery_results = {}
    for strand, score in scores_dict.items():
        if score >= 90:
            mastery_results[strand] = "Mastered"
        elif score >= 70:
            mastery_results[strand] = "In Progress"
        else:
            mastery_results[strand] = "Not Yet Mastered"
    return mastery_results

# Output + Export
if submitted:
    scores = {
        "Expressions & Equations": expressions,
        "Ratios & Proportions": ratios,
        "Geometry": geometry,
        "Statistics": statistics,
        "Number Sense & Operations": number_sense
    }
    results = assess_math_mastery_by_strand(scores)

    st.subheader("📋 Mastery Results")
    for strand, level in results.items():
        st.write(f"**{strand}**: {level}")

    # Export to JSON
    json_file = json.dumps(results, indent=4)
    st.download_button("⬇️ Download Results as JSON", data=json_file, file_name="math_results.json", mime="application/json")

    # Export to CSV
    csv_data = "Strand,Mastery Level\n" + "\n".join([f"{s},{l}" for s, l in results.items()])
    st.download_button("⬇️ Download Results as CSV", data=csv_data, file_name="math_results.csv", mime="text/csv")
