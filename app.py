import streamlit as st # for web apps in Python
import pandas as pd # for tabular data
import plotly.express as px # creates interactive charts

st.set_page_config(
    page_title="Shakespeare's Dark & Light",
    page_icon="🎭",
    layout="wide"
)

NU_RED = "#C8102E"
NU_BLACK = "#000000"

with open("style.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="nu-title">🎭 Shakespeare's <span class="accent">Darkest</span> and Lightest Works</div>
    <div class="nu-intro">The words behind these charts were pulled from the public Shakespeare
    dataset on <a href="https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&t=shakespeare&page=table" target="_blank">Google BigQuery</a>, keeping the top 500 words in each play. Each work is scored by
    how often it uses gloomy words like death and blood 💀 or warm words like love and joy 🌹,
    and the ten highest scoring works are shown for each.</div>
    """,
    unsafe_allow_html=True
)

shakespeare_df = pd.read_csv("shakespeare_clean.csv")

dark_words = [
    "death", "blood", "murder", "ghost", "fear",
    "evil", "kill", "grave", "devil", "die"
]

light_words = [
    "love", "joy", "sweet", "gentle", "happy", "merry", "fair",
    "kind", "dear", "heaven", "laugh", "smile", "grace"
]


dark_df = shakespeare_df[shakespeare_df["word"].isin(dark_words)]
darkest = dark_df.groupby("play")["word_count"].sum().nlargest(10).reset_index()

light_df = shakespeare_df[shakespeare_df["word"].isin(light_words)]
lightest = light_df.groupby("play")["word_count"].sum().nlargest(10).reset_index()

dark_fig = px.bar(darkest, x="word_count", y="play", orientation="h",
                  title="💀 Shakespeare's Darkest Works",
                  labels={"word_count": "💀 Dark Words", "play": "📜 Play"},
                  color_discrete_sequence=[NU_BLACK])
dark_fig.update_layout(title_x=0.5, title_xanchor="center")

light_fig = px.bar(lightest, x="word_count", y="play", orientation="h",
                   title="🌹 Shakespeare's Lightest Works",
                   labels={"word_count": "🌹 Light Words", "play": "📜 Play"},
                   color_discrete_sequence=[NU_RED])
light_fig.update_layout(title_x=0.5, title_xanchor="center")

st.markdown("<h3 class='nu-subheading'>Dark versus light</h3>", unsafe_allow_html=True)

chart_left, chart_right = st.columns(2)

with chart_left:
    st.plotly_chart(dark_fig, use_container_width=True)

with chart_right:
    st.plotly_chart(light_fig, use_container_width=True)
