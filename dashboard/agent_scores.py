import streamlit as st
import pandas as pd

st.set_page_config(page_title="🏅 Agent Scoring Center", layout="wide")
st.title("🏅 CUA Agent Performance Scores")

scores = pd.read_csv("data/agent_scores.csv")  # Assumes external log feed

st.metric("🧠 Total Agents", len(scores))
st.bar_chart(scores.set_index("agent_name")["score"])

st.dataframe(scores)