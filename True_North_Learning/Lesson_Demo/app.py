st.title("📘 Personalized Learning Lesson")

uploaded_file = st.file_uploader("📂 Upload your lesson CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    for _, row in df.iterrows():
        content_type = row['type'].strip().lower()
        title = row['title']
        content = row['content']

        if content_type == 'text':
            st.subheader(title)
            st.write(content)

        elif content_type == 'video-script':
            st.subheader(title)
            st.image("https://via.placeholder.com/150", width=150, caption="Instructor Avatar")
            st.info(content)

        elif content_type == 'whiteboard':
            st.subheader(title)
            st.write("📽️ Whiteboard Sketch (description):")
            st.code(content)

        elif content_type == 'quiz':
            st.subheader(title)
            answer = st.radio(content, ['A', 'B', 'C', 'D'])
            if st.button("Check Answer"):
                st.success("✅ Great job!" if answer == "A" else "❌ Try again!")

        elif content_type == 'interaction':
            st.subheader(title)
            user_input = st.text_input(content)
            if user_input:
                st.write("💬 Thanks for sharing!")

        elif content_type == 'closing':
            st.subheader(title)
            st.success(content)
else:
    st.warning("👈 Please upload a lesson CSV file to begin.")
