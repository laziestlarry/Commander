import streamlit as st
import json
import os

MEMORY_FILE = "data/strategy_memory.json"
SCORE_FILE = "data/agent_scores.json"

st.set_page_config(page_title="Agent Scoreboard", layout="centered")

st.title("🏆 Commander Agent Scoreboard")

if os.path.exists(SCORE_FILE):
    with open(SCORE_FILE) as f:
        scores = json.load(f)
else:
    scores = {}

if scores:
    st.bar_chart(scores)
else:
    st.warning("No agent scores yet. Run a mission to collect data.")

st.header("🧠 Recent GPT Strategy Memory")
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE) as f:
        memory = json.load(f)
    for m in memory[-5:]:
        st.markdown(f"### Topic: {m['topic']}")
        st.code(m["strategy"])
else:
    st.info("No memory log yet.")