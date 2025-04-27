import streamlit as st
import pandas as pd
import altair as alt

# Set page config
st.set_page_config(page_title="True North Dashboard", layout="wide")

# Sample DataFrame (For example purposes, you can load real data from CSV or database)
# Example: Student diagnostic data (Mocked here)
data = {
    'Student': ['John Doe', 'Jane Smith', 'Sam Brown'],
    'Math': ['Mastered', 'In Progress', 'Not Yet Mastered'],
    'Literacy': ['In Progress', 'Mastered', 'Mastered'],
    'Science': ['Mastered', 'Mastered', 'In Progress']
}
df = pd.DataFrame(data)

# Sidebar Role Selection
role = st.sidebar.selectbox("Select your role", ["Student", "Parent", "Educator/Investor"])

# Header Title
st.title(f"📊 True North Dashboard - {role} View")

# --- Content for Student ---
if role == "Student":
    st.subheader("🎯 Your Learning Progress")
    student_name = st.selectbox("Select your name", df['Student'].tolist())
    student_data = df[df['Student'] == student_name]
    
    # Display student’s learning progress
    st.write(f"Progress for {student_name}:")  # Fixed f-string issue here
    st.dataframe(student_data)

    # Visualize progress with a bar chart
    chart = alt.Chart(student_data.melt(id_vars='Student')).mark_bar().encode(
        x='variable:N',
        y='value:N',
        color='variable'
    ).properties(width=600)
    st.altair_chart(chart, use_container_width=True)

# --- Content for Parent ---
elif role == "Parent":
    st.subheader("🎯 Child's Learning Progress")
    student_name = st.selectbox("Select your child’s name", df['Student'].tolist())
    student_data = df[df['Student'] == student_name]
    
    # Display child’s learning progress
    st.write(f"Progress for {student_name}:")  # Fixed f-string issue here
    st.dataframe(student_data)

    # Add recommendations for parents to support learning
    st.write("🔔 Recommendations:")
    st.write(f"Help {student_name} with areas marked as 'In Progress'. Consider providing additional practice in Literacy.")

    # Visualize child's progress with a bar chart
    chart = alt.Chart(student_data.melt(id_vars='Student')).mark_bar().encode(
        x='variable:N',
        y='value:N',
        color='variable'
    ).properties(width=600)
    st.altair_chart(chart, use_container_width=True)

# --- Content for Educator/Investor ---
elif role == "Educator/Investor":
    st.subheader("🎯 School-wide Learning Data")
    st.write("Here is the overall class performance.")
    # Display aggregate data for the whole class
    st.dataframe(df)

    # Aggregate performance chart (overall class trends)
    class_mastery = df.drop(columns='Student').apply(pd.Series.value_counts).T
    st.write("Class Mastery Overview:")
    st.dataframe(class_mastery)

    chart = alt.Chart(class_mastery.reset_index()).mark_bar().encode(
        x='index:N',
        y='Math',
        color='index'
    ).properties(width=600)
    st.altair_chart(chart, use_container_width=True)



