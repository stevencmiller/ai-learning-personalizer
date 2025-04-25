# 🎓 Streamlit App: True North Student Dashboard

import streamlit as st
import pandas as pd
import altair as alt
import json
import os

st.set_page_config(page_title="Student Dashboard | True North", layout="wide")

st.title("📊 True North Personalized Student Dashboard")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["📈 Overview", "📁 Upload Scores"])

# Load diagnostic results
@st.cache_data
def load_results():
    try:
        return pd.read_csv("data/diagnostic_results.csv")
    except:
        return pd.DataFrame()

# Load pathway logic
@st.cache_data
def load_pathways():
    try:
        with open("curriculum/pathway_logic_math.json") as f:
            return json.load(f)
    except:
        return {}

df = load_results()
pathways = load_pathways()

# Overview Page
if page == "📈 Overview":
    st.subheader("🎯 Diagnostic Mastery Overview")

    if df.empty:
        st.warning("No diagnostic data found. Please upload scores to get started.")
    else:
        st.dataframe(df)

        # Count levels
        mastery_counts = df["Mastery Level"].value_counts().reset_index()
        mastery_counts.columns = ["Level", "Count"]

        chart = alt.Chart(mastery_counts).mark_bar().encode(
            x=alt.X("Level", sort=["Mastered", "In Progress", "Not Yet Mastered"]),
            y="Count",
            color="Level"
        ).properties(width=600)

        st.altair_chart(chart, use_container_width=True)

        # Display Learning Recommendations
        st.subheader("🔮 Recommended Learning Paths")
        for index, row in df.iterrows():
            strand = row["Strand"]
            level = row["Mastery Level"]
            suggestion = pathways.get(strand, {}).get(level, "No recommendation available.")
            st.markdown(f"**{strand}** ({level}): {suggestion}")

# Upload Page
elif page == "📁 Upload Scores":
    st.subheader("📤 Upload Diagnostic CSV File")
    uploaded = st.file_uploader("Choose CSV", type="csv")
    if uploaded:
        df = pd.read_csv(uploaded)
        os.makedirs("data", exist_ok=True)
        df.to_csv("data/diagnostic_results.csv", index=False)
        st.success("Scores uploaded successfully! Switch to 'Overview' tab to view data.")
        df = load_results()

results = assess_mastery_by_strand(student_scores)

    # Export to CSV
    csv_data = "Strand,Mastery Level\n" + "\n".join([f"{s},{l}" for s, l in results.items()])
    st.download_button("⬇️ Download Results as CSV", data=csv_data, file_name="math_results.csv", mime="text/csv")
