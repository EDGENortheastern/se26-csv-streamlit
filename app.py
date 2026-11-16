import streamlit as st # for web apps in Python
import pandas as pd # for tabular data

st.title("🎭 Shakespeare's Darkest and Lovliest Works")

shakespeare_df = pd.read_csv("shakespeare_clean.csv")

st.set_page_config(page_title="Shakespeare's Dark & Light", page_icon="🎭")

