# 🎓 Streamlit App: True North Student Dashboard

import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Student Dashboard | True North", layout="wide")

st.title("📊 True North Personalized Student Dashboard")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["📈 Overview", "📁 Upload Scores"])

# Load diagnostic results
@st.cache_data
def load_results():
    try:
        return pd.read_csv("Mock Student Data.csv")
    except:
        return pd.DataFrame()

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
         # Ensure 'data' directory exists before saving
        import os
        os.makedirs("data", exist_ok=True)
        df.to_csv("data/diagnostic_results.csv", index=False)
        st.success("Scores uploaded successfully! Switch to 'Overview' tab to view data.")
         # 🔄 Reload data to reflect upload
        df = load_results()
