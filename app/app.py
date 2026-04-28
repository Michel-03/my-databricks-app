import os
import streamlit as st

env = os.getenv("ENV", "dev")

st.title("Databricks App 🚀")
st.write(f"Running in prod environment triggerd by nagendra")