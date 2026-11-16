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
NU_WHITE = "#FFFFFF"

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


def top_works(words):
    return (
        shakespeare_df[shakespeare_df["word"].isin(words)]
        .groupby("play", as_index=False)["word_count"].sum()
        .nlargest(10, "word_count")
        .sort_values("word_count")
    )


def styled_bar(df, title, x_label, bar_colour, hover_bg, hover_font, hover_word):
    fig = px.bar(
        df,
        x="word_count",
        y="play",
        orientation="h",
        title=title,
        labels={"word_count": x_label, "play": "Work"}
    )
    fig.update_traces(
        marker_color=bar_colour,
        hovertemplate=f"<b>%{{y}}</b><br>%{{x}} {hover_word}<extra></extra>",
        hoverlabel=dict(
            bgcolor=hover_bg,
            bordercolor=hover_bg,
            font_color=hover_font,
            font_size=14
        )
    )
    fig.update_layout(
        template="plotly_white",
        height=550,
        showlegend=False,
        paper_bgcolor=NU_WHITE,
        plot_bgcolor=NU_WHITE,
        font=dict(color=NU_BLACK),
        title_font=dict(size=20, color=NU_BLACK),
        title_x=0.5,
        title_xanchor="center",
        margin=dict(l=10, r=10, t=60, b=40)
    )
    return fig


darkest = top_works(dark_words)
lightest = top_works(light_words)

dark_fig = styled_bar(
    darkest,
    title="💀 Shakespeare's Darkest Works",
    x_label="Dark Word Frequency",
    bar_colour=NU_BLACK,
    hover_bg=NU_RED,
    hover_font=NU_WHITE,
    hover_word="dark words"
)

light_fig = styled_bar(
    lightest,
    title="🌹 Shakespeare's Lightest Works",
    x_label="Light Word Frequency",
    bar_colour=NU_RED,
    hover_bg=NU_BLACK,
    hover_font=NU_WHITE,
    hover_word="light words"
)

st.markdown("<h3 class='nu-subheading'>Dark versus light</h3>", unsafe_allow_html=True)

chart_left, chart_right = st.columns(2)

with chart_left:
    st.plotly_chart(dark_fig, use_container_width=True)

with chart_right:
    st.plotly_chart(light_fig, use_container_width=True)
