import streamlit as st

st.title("MLOps Dashboard")
st.write("Model Performance Metrics")

col1, col2 = st.columns(2)
col1.metric("Accuracy", "95.2%", "1.2%")
col2.metric("Latency", "23ms", "-5ms")