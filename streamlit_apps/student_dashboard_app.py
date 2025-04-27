# 🎓 Streamlit App: True North Student Dashboard (Upgraded with Pathways)

import streamlit as st
import pandas as pd
import altair as alt
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
        df = pd.read_csv("Mock Student Data.csv")
        
        # Add Personalized Pathways
        if "Recommended Pathway" not in df.columns:
            df["Recommended Pathway"] = df["Mastery Level"].apply(recommend_pathway)
        
        return df
    except:
        return pd.DataFrame()

# Pathway recommendation logic
def recommend_pathway(mastery_level):
    if mastery_level == "Mastered":
        return "🚀 Enrichment Pathway: Deeper Projects"
    elif mastery_level == "In Progress":
        return "🔧 Targeted Skills Pathway: Focus Practice"
    elif mastery_level == "Not Yet Mastered":
        return "🏗️ Intervention Pathway: Foundational Skills"
    else:
        return "🔍 Review Needed"

df = load_results()

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

# Upload Page
elif page == "📁 Upload Scores":
    st.subheader("📤 Upload Diagnostic CSV File")
    uploaded = st.file_uploader("Choose CSV", type="csv")
    if uploaded:
        df = pd.read_csv(uploaded)
        
        # Add Personalized Pathways after upload
        df["Recommended Pathway"] = df["Mastery Level"].apply(recommend_pathway)
        
        os.makedirs("data", exist_ok=True)
        df.to_csv("data/diagnostic_results.csv", index=False)
        st.success("Scores uploaded successfully! Switch to 'Overview' tab to view data.")
