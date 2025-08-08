import streamlit as st
from google.cloud import bigquery
import pandas as pd

st.set_page_config(page_title="💰 GCP Cost Dashboard", layout="wide")
st.title("📊 GCP Billing Cost Analysis")

@st.cache_data
def load_data():
    client = bigquery.Client()
    query = '''
        SELECT
          service.description as service,
          project.id as project_id,
          usage_start_time,
          cost
        FROM `propulse-autonomax.billing_export.gcp_billing_export_v1_*`
        WHERE usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
        ORDER BY usage_start_time DESC
    '''
    return client.query(query).to_dataframe()

df = load_data()
st.bar_chart(df.groupby("service")["cost"].sum().sort_values(ascending=False))
st.dataframe(df)