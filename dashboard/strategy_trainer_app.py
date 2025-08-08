import streamlit as st
from services.strategy_gpt import generate_strategy
import json

st.set_page_config(page_title="Strategy Trainer", layout="centered")

st.title("🧠 Commander Strategy Trainer")

topic = st.text_input("Enter mission topic:")

if st.button("Generate Strategy"):
    if topic:
        strategy = generate_strategy(topic)
        st.success("✅ Strategy Generated:")
        st.code(strategy)
    else:
        st.warning("Please enter a topic first.")

st.markdown("## 📜 Strategy Memory Log")
with open("data/strategy_memory.json") as f:
    memory = json.load(f)

for item in memory[-10:]:
    st.markdown(f"### {item['topic']}")
    st.code(item["strategy"])