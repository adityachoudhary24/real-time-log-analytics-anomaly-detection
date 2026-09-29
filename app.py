
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Real-Time Log Analytics",
    layout="wide"
)

st.title("Real-Time Log Analytics Dashboard")

# Load processed logs
df = pd.read_csv("processed_logs (1).csv")

# Basic metrics
total_requests = len(df)
successful_requests = len(df[df["status_code"].isin([200, 201])])
error_requests = len(df[df["status_code"] >= 400])
error_rate = (error_requests / total_requests) * 100

# Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Requests", total_requests)
col2.metric("Successful Requests", successful_requests)
col3.metric("Error Requests", error_requests)
col4.metric("Error Rate", f"{error_rate:.2f}%")

st.subheader("Requests by Endpoint")

endpoint_counts = df["endpoint"].value_counts()

st.bar_chart(endpoint_counts)

st.subheader("HTTP Status Code Distribution")

status_counts = df["status_code"].value_counts().sort_index()

st.bar_chart(status_counts)

st.subheader("Response Time Analysis")

st.write(
    f"Average Response Time: {df['response_time_ms'].mean():.2f} ms"
)

st.write(
    f"Maximum Response Time: {df['response_time_ms'].max()} ms"
)

st.subheader("Detected Anomalies")

anomalies = df[
    (df["response_time_ms"] > 1000) |
    (df["status_code"] == 500)
]

st.dataframe(anomalies)
