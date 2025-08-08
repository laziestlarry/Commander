
import streamlit as st
st.set_page_config(page_title="AutonomaX Control Center", layout="wide")

st.title("🧠 AutonomaX AI Commander Dashboard")
st.sidebar.header("🔧 Control Panel")
st.sidebar.page_link("pages/revenue_tracker.py", label="💰 Revenue Tracker")
st.sidebar.page_link("pages/fiverr_status.py", label="🎯 Fiverr Status")
st.sidebar.page_link("pages/shopify_status.py", label="🛒 Shopify Sync")
st.sidebar.page_link("pages/youtube_auto.py", label="📺 YouTube Automation")
st.sidebar.page_link("pages/agent_console.py", label="🤖 Agent Console")
st.sidebar.page_link("pages/logs_viewer.py", label="📜 Logs Viewer")

st.success("Welcome to AutonomaX Control Center. Use sidebar to manage operations.")
