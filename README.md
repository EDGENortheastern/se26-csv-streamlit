# 🎭 Shakespeare's Darkest and Lightest Works

This is a small dashboard that asks a playful question. Which of Shakespeare's works lean the most towards gloom, and which lean the most towards warmth? It answers by counting words, then shows the results as two bar charts you can hover over to see the exact numbers.

**[Open the live dashboard](https://se26-csv-app-6fntkryv53se65pgveq2x8.streamlit.app/)**, no installation needed.

This README has two parts. The [User Guide](#user-guide) explains what the dashboard shows and how to use it. The [Technical Documentation](#technical-documentation) explains how to get the code, run it on your own computer, how it is built, and how the responsive layout works.

---

## User Guide

### What you see

Open the [live dashboard](https://se26-csv-app-6fntkryv53se65pgveq2x8.streamlit.app/) in any browser. When the page opens you'll see a title, a short introduction explaining where the words came from, and a heading that reads **Darkness vs Light**. Underneath are two bar charts.

- The **black chart** on the left, *💀 Shakespeare's Darkest Works*, lists the ten works that use the most gloomy words.
- The **red chart** on the right, *🌹 Shakespeare's Lightest Works*, lists the ten works that use the most warm words.

Each bar is one play or poem. The longer the bar, the more dark or light words that work uses. The name of the work is on the left of each bar and the number of words is along the bottom.

### Seeing the exact numbers

Move your mouse over any bar. A small label pops up with the name of the work and how many dark or light words it uses. On the dark chart the label is red, and on the light chart it is black, so it stands out against the bar.

On a phone or tablet there is no mouse, so tap a bar instead. Tap somewhere else on the chart to hide the label again.

### Zooming and downloading

When you hover over a chart, a small toolbar appears in its top right corner. From it you can

- **zoom in** by choosing the zoom tool and dragging a box over the part of the chart you want to look at more closely,
- **pan** around a zoomed-in chart by choosing the pan tool and dragging,
- **reset** the chart back to how it started with the home or reset button,
- **download** the chart as a PNG picture with the camera button, which is handy for slides or reports.

Double clicking anywhere on a chart also takes it back to how it started.

### Using it on a phone

The dashboard works on any screen size. On a laptop or desktop the two charts sit side by side. On a phone, or any window narrower than 768 pixels, the charts stack one under the other, with the dark chart first and the light chart underneath. Scroll down to see the second chart. The title and introduction also get a little smaller so they fit comfortably.

### Where the data comes from

The words come from the public [Shakespeare sample dataset](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&t=shakespeare&page=table) hosted on [Google BigQuery](https://cloud.google.com/bigquery). That dataset lists every word in Shakespeare's works along with how many times it appears in each play or poem. For this project the top 500 words in each work were kept, tidied up, and saved as `shakespeare_clean.csv`, which sits in this folder. The file has three columns holding the name of the work (`play`), the word (`word`), and how many times that word appears in it (`word_count`).

Because the data is already saved as a CSV, you don't need a Google account or any BigQuery access to use the dashboard. If you'd like to explore the original data yourself, Google has a short guide on [querying public datasets](https://cloud.google.com/bigquery/public-data).

### How works are scored

Each work gets a dark score and a light score.

- The **dark score** adds up how often a work uses the words *death, blood, murder, ghost, fear, evil, kill, grave, devil* and *die*.
- The **light score** adds up how often a work uses the words *love, joy, sweet, gentle, happy, merry, fair, kind, dear, heaven, laugh, smile* and *grace*.

The ten works with the highest dark score appear in the black chart, and the ten with the highest light score appear in the red chart.

This is a simple word count rather than a deep reading of the plays, so it rewards longer works that simply have more words in them. That's why a long history like Henry VI can lead the dark chart and still come second in the light one. It's meant to be a fun starting point, not a final verdict.

---

## Technical Documentation

This part is for anyone who wants to run, change or deploy the dashboard.

### Project files

| File | What it does |
| --- | --- |
| `app.py` | The whole app. Reads the CSV, scores each work and draws the two charts. |
| `style.css` | All the styling, including the colours and the responsive layout. |
| `shakespeare_clean.csv` | The word counts the charts are built from. |
| `requirements.txt` | The exact library versions the app needs. |
| `LICENSE` | The terms the project is shared under. |

### How it's built

The app uses [Streamlit](https://streamlit.io) to turn a Python script into a web page, [pandas](https://pandas.pydata.org) to read the CSV and add up the word counts, and [Plotly Express](https://plotly.com/python/plotly-express/) to draw the interactive bar charts.

`app.py` works from top to bottom.

1. It sets up the page with `st.set_page_config`, using the wide layout so there's room for two charts.
2. It loads the styling with `st.html(Path("style.css"))`.
3. It writes the title and introduction with `st.markdown`, using CSS classes such as `nu-title` and `nu-intro` that are defined in `style.css`.
4. It reads `shakespeare_clean.csv` into a pandas DataFrame.
5. It keeps only the rows whose word is in `dark_words`, groups them by play, adds up the counts and takes the ten largest with `nlargest(10)`. It then does the same with `light_words`.
6. It draws each result as a horizontal bar chart with `px.bar`, and sets the hover label text and colours with `update_traces`.
7. It splits the page into two columns with `st.columns(2)` and puts one chart in each.

The look follows the Northeastern University colours of black, red (`#C8102E`) and white. In `style.css` these are stored once as CSS variables, so they only need changing in one place.

```css
:root {
    --nu-red: #C8102E;
    --nu-black: #000000;
    --nu-white: #FFFFFF;
}
```

### Getting the code

You'll need [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/) 3.10 or newer. You can check what you have by running `git --version` and `python3 --version` in a terminal.

Clone the repository and move into its folder.

```bash
git clone https://github.com/EDGENortheastern/se26-csv-streamlit.git
cd se26-csv-streamlit
```

If you have an SSH key set up with GitHub you can use `git@github.com:EDGENortheastern/se26-csv-streamlit.git` instead.

### Setting up a virtual environment

A virtual environment keeps the libraries for this project separate from the rest of your computer. Create one inside the project folder.

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

Your terminal prompt should now start with `(.venv)`. The `.venv` folder is already listed in `.gitignore`, so it won't be committed.

### Installing the libraries

Install the exact versions listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

This installs Streamlit, pandas and Plotly along with everything they depend on.

### Running the app

Start the app.

```bash
streamlit run app.py
```

Streamlit will open the dashboard in your browser, usually at `http://localhost:8501`. If you edit `app.py` or `style.css` while it's running, press R on the page to reload it with your changes. The [Streamlit getting started guide](https://docs.streamlit.io/get-started) is a good place to look if anything goes wrong.

When you're finished, stop the app with Ctrl+C and leave the virtual environment.

```bash
deactivate
```

Next time you only need to `cd` into the folder, activate the environment again and run `streamlit run app.py`.

### Responsive design

The dashboard changes its layout to suit the screen. On a laptop or desktop the two charts sit side by side, and on a phone they stack one under the other. This is done in `style.css` with [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries).

#### What a media query is

A media query is a block of CSS that only applies when a condition about the screen is true. The CSS inside the curly brackets is ignored unless the condition matches.

```css
@media (min-width: 769px) {
    /* only applies when the window is 769px wide or wider */
}

@media (max-width: 768px) {
    /* only applies when the window is 768px wide or narrower */
}
```

The two conditions meet at 768px, which is a common width for the edge between tablets and laptops. Because one starts at 769px and the other stops at 768px, exactly one of them is active at any width, so they never fight each other.

#### Which elements are being styled

`st.columns(2)` in `app.py` creates HTML that looks roughly like this.

```html
<div data-testid="stHorizontalBlock">      <!-- the row holding both columns -->
    <div data-testid="stColumn">...</div>  <!-- chart_left, the dark chart -->
    <div data-testid="stColumn">...</div>  <!-- chart_right, the light chart -->
</div>
```

The CSS selects these with attribute selectors such as `[data-testid="stHorizontalBlock"]`. The `>` in `[data-testid="stHorizontalBlock"] > [data-testid="stColumn"]` means "a column that sits directly inside the row". The rules list both `[data-testid="column"]` and `[data-testid="stColumn"]` because older and newer versions of Streamlit use different names for the column element, and listing both means the layout works on either.

The row is a [flexbox](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox), a layout where the children are lined up in a row or a column. The media queries change which direction that is.

#### Wide screens, charts side by side

```css
@media (min-width: 769px) {
    [data-testid="stHorizontalBlock"] {
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 2rem;
    }

    [data-testid="stHorizontalBlock"] > [data-testid="column"],
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
        width: 50% !important;
        flex: 1 1 0 !important;
        min-width: 0 !important;
    }
}
```

- `flex-direction: row` lines the two columns up left to right.
- `flex-wrap: nowrap` stops the second chart from dropping onto a new line, even if the window is only just over 768px.
- `gap: 2rem` puts a space between the two charts.
- `width: 50%` gives each column half of the row.
- `flex: 1 1 0` is short for grow, shrink and starting size. Both columns start from zero and grow by the same amount, so they always end up exactly the same width.
- `min-width: 0` lets a column shrink below the width of its contents. Without it a long play name could push its column wider than half.

#### Narrow screens, charts stacked

```css
@media (max-width: 768px) {
    [data-testid="stHorizontalBlock"] {
        flex-direction: column !important;
    }

    [data-testid="stHorizontalBlock"] > [data-testid="column"],
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
        width: 100% !important;
        flex: 1 1 100% !important;
        min-width: 100% !important;
    }

    .nu-title {
        font-size: 1.7rem;
    }

    .nu-intro {
        font-size: 0.95rem;
    }
}
```

- `flex-direction: column` lines the two columns up top to bottom instead. They appear in the same order as in `app.py`, so the dark chart comes first.
- `width: 100%`, `flex: 1 1 100%` and `min-width: 100%` make each column take the full width of the screen, so a chart never gets squashed next to the other one.
- `.nu-title` shrinks from `2.4rem` to `1.7rem` and `.nu-intro` shrinks from `1.05rem` to `0.95rem`, so the heading and introduction fit on a small screen without wrapping onto lots of lines.

#### Why `!important` is needed

Streamlit ships with its own CSS for columns. Normally the browser would use Streamlit's rules over ours, because they are more specific. Adding `!important` tells the browser that our rule wins, so the layout changes actually take effect.

#### How the charts resize

The CSS only controls how wide each column is. The charts themselves fill whatever space they're given because of `use_container_width=True` in `app.py`.

```python
with chart_left:
    st.plotly_chart(dark_fig, use_container_width=True)
```

So when the media query makes a column half the screen or the full screen, the chart inside it stretches to match.

#### Testing the layout

Open the app in your browser and open the developer tools (F12, or Cmd+Option+I on a Mac). Switch on the device toolbar (Ctrl+Shift+M, or Cmd+Shift+M on a Mac) and drag the width either side of 768px. You should see the charts jump between side by side and stacked. You can also pick a phone such as an iPhone from the device list to see how it looks there.

### Changing the word lists

If you'd like to try your own idea of dark and light, open `app.py` and edit the `dark_words` and `light_words` lists. Any word you add will be counted as long as it appears in the CSV. Save the file, reload the page, and the charts will update straight away.

### Sharing it online

The easiest way to put the dashboard on the web is [Streamlit Community Cloud](https://streamlit.io/cloud), which is free.

1. Push your copy of the project to GitHub.
2. Sign in to Streamlit Community Cloud with your GitHub account.
3. Choose **Create app**, pick this repository and branch, and set the main file to `app.py`.
4. Choose **Deploy**. After a minute or two you'll get a public link you can share.

The current version of this project is already live at <https://se26-csv-app-6fntkryv53se65pgveq2x8.streamlit.app/>.

Streamlit Community Cloud reads `requirements.txt` to know which libraries to install. If you add a new library, install it in your virtual environment and update the file with `pip freeze > requirements.txt`.

### Licence

This project is shared under the terms in the `LICENSE` file in this folder.
