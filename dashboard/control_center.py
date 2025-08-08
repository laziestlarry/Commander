import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="🎮 AutonomaX Control Center", layout="wide")
st.title("🎮 Commander Control Center")

st.sidebar.header("Agent Commands")
if st.sidebar.button("🚀 Launch Agents"):
    st.success("Agents launched at " + datetime.now().strftime("%H:%M:%S"))

if st.sidebar.button("🔁 Sync Logs"):
    st.info("Sync initiated...")

if st.sidebar.button("📈 View Revenue Tracker"):
    st.switch_page("revenue_tracker.py")

if st.sidebar.button("🧠 Strategy Visualizer"):
    st.switch_page("strategy_visualizer.py")

st.markdown("### 🧠 Latest Summary Logs")
try:
    logs = pd.read_csv("data/revenue_log.csv")
    st.dataframe(logs.tail(10))
except:
    st.warning("No logs found yet.")