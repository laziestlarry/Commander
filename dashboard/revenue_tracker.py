import streamlit as st
import pandas as pd

st.set_page_config(page_title="💸 Revenue Tracker", layout="wide")
st.title("💸 Revenue-Driven Outcomes")

df = pd.read_csv("data/revenue_log.csv")  # Automatically populated from commands

col1, col2 = st.columns(2)
col1.metric("💰 Total Revenue", f"${df['revenue'].sum():,.2f}")
col2.metric("🚀 Success Count", df[df['status'] == 'success'].shape[0])

st.line_chart(df[["timestamp", "revenue"]].set_index("timestamp"))
st.dataframe(df)