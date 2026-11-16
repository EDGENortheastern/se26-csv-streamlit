# 🎭 Shakespeare's Darkest and Lightest Works

This is a small dashboard that asks a playful question. Which of Shakespeare's works lean the most towards gloom, and which lean the most towards warmth? It answers by counting words, then shows the results as two bar charts you can hover over to see the exact numbers.

## Where the data comes from

The words come from the public [Shakespeare sample dataset](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&t=shakespeare&page=table) hosted on [Google BigQuery](https://cloud.google.com/bigquery). That dataset lists every word in Shakespeare's works along with how many times it appears in each play or poem. For this project the top 500 words in each work were kept, tidied up, and saved as `shakespeare_clean.csv`, which sits in this folder. The file has three columns holding the name of the work, the word, and how many times that word appears in it.

Because the data is already saved as a CSV, you don't need a Google account or any BigQuery access to run the dashboard. If you'd like to explore the original data yourself, Google has a short guide on [querying public datasets](https://cloud.google.com/bigquery/public-data).

## How works are scored

Each work gets a dark score and a light score. The dark score adds up how often a work uses words such as death, blood, murder, ghost, fear, evil, kill, grave, devil and die. The light score does the same for words such as love, joy, sweet, gentle, happy, merry, fair, kind, dear, heaven, laugh, smile and grace. The ten works with the highest dark score appear in the black chart, and the ten with the highest light score appear in the red chart.

This is a simple word count rather than a deep reading of the plays, so it rewards longer works that simply have more words in them. That's why a long history like Henry VI can lead the dark chart and still come second in the light one. It's meant to be a fun starting point, not a final verdict.

## How it's built

The whole app lives in `app.py`. It uses [Streamlit](https://streamlit.io) to turn a Python script into a web page, [pandas](https://pandas.pydata.org) to read the CSV and add up the word counts, and [Plotly Express](https://plotly.com/python/plotly-express/) to draw the interactive bar charts.

The look follows the Northeastern University colours of black, red (`#C8102E`) and white. All the styling lives in its own file, `style.css`, which `app.py` loads when the page starts. That CSS centres the text and controls the layout, so the two charts sit side by side on a laptop or desktop screen and stack one under the other on a phone. The CSS uses [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries), which let a page change its layout depending on how wide the screen is.

## Running it on your own computer

You'll need [Python](https://www.python.org/downloads/) 3.9 or newer. Open a terminal in this folder and install the three libraries the app depends on.

```bash
pip install streamlit pandas plotly
```

Then start the app.

```bash
streamlit run app.py
```

Streamlit will open the dashboard in your browser, usually at `http://localhost:8501`. If you edit `app.py` while it's running, press R on the page to reload it with your changes. The [Streamlit getting started guide](https://docs.streamlit.io/get-started) is a good place to look if anything goes wrong.

## Sharing it online

The easiest way to put the dashboard on the web is [Streamlit Community Cloud](https://streamlit.io/cloud), which is free. You connect it to this GitHub repository, point it at `app.py`, and it gives you a public link. It will also want a `requirements.txt` file listing `streamlit`, `pandas` and `plotly` so it knows what to install.

## Changing the word lists

If you'd like to try your own idea of dark and light, open `app.py` and edit the `dark_words` and `light_words` lists. Any word you add will be counted as long as it appears in the CSV. Save the file, reload the page, and the charts will update straight away.

## Licence

This project is shared under the terms in the `LICENSE` file in this folder.
