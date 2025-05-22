import streamlit as st
import requests

st.set_page_config(page_title="AI Prompt Styles", layout="wide")

user_id = "abc123"

st.title("🧠 AI Tone Switcher")
query = st.text_area("Enter your question or topic:", height=100)

if st.button("Generate") and query:
    with st.spinner("Generating responses..."):
        res = requests.post("http://localhost:8000/generate", json={"user_id": user_id, "query": query})
        print("RESULT:",res)
        data = res.json()

        st.subheader("🎉 Casual Style")
        st.write(data["casual_response"])

        st.subheader("📘 Formal Style")
        st.write(data["formal_response"])

st.sidebar.header("📜 History")
res = requests.get(f"http://localhost:8000/history?user_id={user_id}")
history = res.json()
for item in history:
    with st.sidebar.expander(item["query"]):
        st.markdown(f"**Casual:** {item['casual_response']}")
        st.markdown(f"**Formal:** {item['formal_response']}")
