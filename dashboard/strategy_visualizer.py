import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="🧠 Strategy Visualizer", layout="wide")

st.title("🧠 Commander Strategy Visualizer")

strategies = pd.read_csv("data/strategy_feedback.csv")  # Assumes generated logs

fig = px.sunburst(
    strategies,
    path=['mission_group', 'objective', 'action'],
    values='score',
    color='score',
    color_continuous_scale='Blues',
    title='Strategy Success Tree'
)
st.plotly_chart(fig, use_container_width=True)
st.dataframe(strategies.sort_values(by="score", ascending=False))