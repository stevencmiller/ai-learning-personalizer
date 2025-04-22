import streamlit as st
import json
import csv

# Streamlit App: Literacy Diagnostic Scoring
st.set_page_config(page_title="📚 Literacy Diagnostic Scoring Tool", layout="centered")
st.title("📖 Literacy Diagnostic Scoring Tool")
st.write("Enter student scores (0–100) for each literacy strand to assess mastery levels.")

# Input form
with st.form("literacy_form"):
    reading = st.slider("Reading Comprehension", 0, 100, 75)
    vocabulary = st.slider("Vocabulary Acquisition", 0, 100, 75)
    writing = st.slider("Writing Mechanics", 0, 100, 75)
    text_structure = st.slider("Text Structure & Purpose", 0, 100, 75)
    literary = st.slider("Literary Analysis", 0, 100, 75)
    grammar = st.slider("Grammar & Usage", 0, 100, 75)
    submitted = st.form_submit_button("Submit")

# Mastery function
def assess_literacy_mastery_by_strand(scores_dict):
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
        "Reading Comprehension": reading,
        "Vocabulary Acquisition": vocabulary,
        "Writing Mechanics": writing,
        "Text Structure & Purpose": text_structure,
        "Literary Analysis": literary,
        "Grammar & Usage": grammar
    }
    results = assess_literacy_mastery_by_strand(scores)

    st.subheader("📋 Mastery Results")
    for strand, level in results.items():
        st.write(f"**{strand}**: {level}")

    # Export to JSON
    json_file = json.dumps(results, indent=4)
    st.download_button("⬇️ Download Results as JSON", data=json_file, file_name="literacy_results.json", mime="application/json")

    # Export to CSV
    csv_data = "Strand,Mastery Level\n" + "\n".join([f"{s},{l}" for s, l in results.items()])
    st.download_button("⬇️ Download Results as CSV", data=csv_data, file_name="literacy_results.csv", mime="text/csv")
