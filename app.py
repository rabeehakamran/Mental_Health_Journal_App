import streamlit as st
from analysis import analyze_journal
from utils import get_quote
import json
import os
from datetime import datetime


# Create data folder if not exists
if not os.path.exists("data"):
    os.makedirs("data")

st.set_page_config(page_title="Mental Health Journal", layout="centered")

st.title("🧠 Daily Mental Health Journal")

st.write("Write your thoughts below. We'll analyze your mood and offer helpful feedback.")

# Journal input
journal_text = st.text_area("✍️ What's on your mind today?", height=300)

if st.button("Analyze Entry"):
    if not journal_text.strip():
        st.warning("Please write something first.")
    else:
        result = analyze_journal(journal_text)
        st.subheader("🔍 Analysis Summary")
        st.markdown(f"**Sentiment:** `{result['sentiment']}`")
        st.markdown(f"**Keywords Detected:** `{', '.join(result['keywords'])}`")

        quote = get_quote(result['sentiment'])
        st.info(f"💬 Quote for You: *{quote}*")

        # Save to file
        today = datetime.today().strftime("%Y-%m-%d")
        entry = {
            "date": today,
            "text": journal_text,
            "sentiment": result['sentiment'],
            "keywords": result['keywords']
        }

        with open("data/journal_entries.json", "a") as f:
            f.write(json.dumps(entry) + "\n")

        st.success("Entry saved successfully.")
