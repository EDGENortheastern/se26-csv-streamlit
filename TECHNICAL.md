# Technical Documentation

This file is for anyone who wants to run, change or deploy the dashboard. For what the dashboard shows and how to use it, see [README.md](README.md).

## How it's built

The whole app lives in `app.py`. It uses [Streamlit](https://streamlit.io) to turn a Python script into a web page, [pandas](https://pandas.pydata.org) to read the CSV and add up the word counts, and [Plotly Express](https://plotly.com/python/plotly-express/) to draw the interactive bar charts.

The look follows the Northeastern University colours of black, red (`#C8102E`) and white. All the styling lives in its own file, `style.css`, which `app.py` loads when the page starts with `st.html(Path("style.css"))`.

## Running it on your own computer

You'll need [Python](https://www.python.org/downloads/) 3.9 or newer. Open a terminal in this folder and create a virtual environment, so the libraries for this project are kept separate from the rest of your computer.

```bash
python3 -m venv .venv
```

Activate it. On macOS or Linux run this.

```bash
source .venv/bin/activate
```

On Windows run this instead.

```bash
.venv\Scripts\activate
```

Your terminal prompt should now start with `(.venv)`. Install the three libraries the app depends on.

```bash
pip install streamlit pandas plotly
```

Then start the app.

```bash
streamlit run app.py
```

Streamlit will open the dashboard in your browser, usually at `http://localhost:8501`. If you edit `app.py` while it's running, press R on the page to reload it with your changes. The [Streamlit getting started guide](https://docs.streamlit.io/get-started) is a good place to look if anything goes wrong.

When you're finished, stop the app with Ctrl+C and leave the virtual environment.

```bash
deactivate
```

Next time you only need to activate the environment again and run `streamlit run app.py`. The `.venv` folder is already listed in `.gitignore`, so it won't be committed.

## Styling and responsive layout

`style.css` uses [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries), which let a page change its layout depending on how wide the screen is. The breakpoint is 768px, a common width for the edge between tablets and laptops.

```css
@media (min-width: 769px) { ... }
@media (max-width: 768px) { ... }
```

On screens wider than 768px, the block that `st.columns(2)` creates (`[data-testid="stHorizontalBlock"]`) is forced into a single row with `flex-direction: row` and `flex-wrap: nowrap`, with a `2rem` gap. Each column is set to `width: 50%` and `flex: 1 1 0`, so the two charts share the space equally and sit side by side.

On screens 768px or narrower, the same block switches to `flex-direction: column` and each column takes `width: 100%`, so the charts stack one under the other with the dark chart first. The title shrinks from `2.4rem` to `1.7rem` and the intro text from `1.05rem` to `0.95rem` so they fit on a phone.

The rules target both `[data-testid="column"]` and `[data-testid="stColumn"]` because different Streamlit versions use different names for the column element. `!important` is needed to override Streamlit's own built-in column styles.

The charts themselves are made responsive by `st.plotly_chart(..., use_container_width=True)`, which stretches each chart to fill whatever width its column has.

To check the responsive layout, open the app in your browser, open the developer tools and switch on the device toolbar, then drag the width either side of 768px.

## Sharing it online

The easiest way to put the dashboard on the web is [Streamlit Community Cloud](https://streamlit.io/cloud), which is free. You connect it to this GitHub repository, point it at `app.py`, and it gives you a public link. It will also want a `requirements.txt` file listing `streamlit`, `pandas` and `plotly` so it knows what to install. With your virtual environment active you can create one with `pip freeze > requirements.txt`.

## Changing the word lists

If you'd like to try your own idea of dark and light, open `app.py` and edit the `dark_words` and `light_words` lists. Any word you add will be counted as long as it appears in the CSV. Save the file, reload the page, and the charts will update straight away.
