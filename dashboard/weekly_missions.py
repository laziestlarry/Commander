import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="📅 Weekly Missions", layout="wide")
st.title("📅 Commander: Weekly Missions")

try:
    df = pd.read_csv("data/mission_schedule.csv")
    st.dataframe(df)
except:
    st.info("No missions scheduled yet.")

if st.button("➕ Add New Mission"):
    st.session_state["adding"] = True

if st.session_state.get("adding"):
    with st.form("new_mission"):
        task = st.text_input("Mission Title")
        date = st.date_input("Scheduled Date")
        submit = st.form_submit_button("Save")
        if submit:
            row = pd.DataFrame([[date, task]], columns=["Date", "Task"])
            try:
                df = pd.read_csv("data/mission_schedule.csv")
                df = pd.concat([df, row])
            except:
                df = row
            df.to_csv("data/mission_schedule.csv", index=False)
            st.success("Mission saved!")