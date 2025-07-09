import streamlit as st
import requests

st.set_page_config(page_title="Xaprise AI Agent Demo", layout="centered")

st.title("🤖 Xaprise AI Agent")
st.subheader("Try chatting with our AI agent below")

user_input = st.text_input("Your Message")

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            response = requests.post(
                "https://api-link.com/agent/",  # Replace this with your real API
                json={"user_input": user_input}
            )
            if response.status_code == 200:
                st.success("Agent Reply:")
                st.write(response.json().get("response", "No reply field in response."))
            else:
                st.error(f"Error: {response.status_code}")
