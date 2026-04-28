import streamlit as st
from src.compare import compare_banks

st.set_page_config(page_title="Bank AI Risk Dashboard")

st.title("🏦 MultiBank Risk Intelligence Dashboard")

st.write("AI-powered comparison of major banks")

df = compare_banks()

st.dataframe(df)

st.bar_chart(df.set_index("Bank")["Risk Score"])

st.bar_chart(df.set_index("Bank")["Sentiment"])