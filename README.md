# 🎭 Shakespeare's Darkest and Lightest Works

This is a small dashboard that asks a playful question. Which of Shakespeare's works lean the most towards gloom, and which lean the most towards warmth? It answers by counting words, then shows the results as two bar charts you can hover over to see the exact numbers.

If you want to run the app yourself or change how it works, see [TECHNICAL.md](TECHNICAL.md).

## Using the dashboard

The page shows two charts. The black chart on the left lists the ten darkest works and the red chart on the right lists the ten lightest. On a phone the charts stack, with the dark chart first and the light chart underneath.

To see the exact numbers, move your mouse over any bar. A small label pops up with the name of the work and how many dark or light words it uses. On the dark chart the label is red, and on the light chart it is black, so it stands out against the bar. On a phone or tablet, tap a bar instead of hovering.

When you hover over a chart, a small toolbar also appears in its top right corner. You can use it to zoom in on part of the chart, reset the view, or download the chart as a picture. Double clicking anywhere on a chart takes it back to how it started.

## Where the data comes from

The words come from the public [Shakespeare sample dataset](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&t=shakespeare&page=table) hosted on [Google BigQuery](https://cloud.google.com/bigquery). That dataset lists every word in Shakespeare's works along with how many times it appears in each play or poem. For this project the top 500 words in each work were kept, tidied up, and saved as `shakespeare_clean.csv`, which sits in this folder. The file has three columns holding the name of the work, the word, and how many times that word appears in it.

Because the data is already saved as a CSV, you don't need a Google account or any BigQuery access to use the dashboard. If you'd like to explore the original data yourself, Google has a short guide on [querying public datasets](https://cloud.google.com/bigquery/public-data).

## How works are scored

Each work gets a dark score and a light score. The dark score adds up how often a work uses words such as death, blood, murder, ghost, fear, evil, kill, grave, devil and die. The light score does the same for words such as love, joy, sweet, gentle, happy, merry, fair, kind, dear, heaven, laugh, smile and grace. The ten works with the highest dark score appear in the black chart, and the ten with the highest light score appear in the red chart.

This is a simple word count rather than a deep reading of the plays, so it rewards longer works that simply have more words in them. That's why a long history like Henry VI can lead the dark chart and still come second in the light one. It's meant to be a fun starting point, not a final verdict.

## Licence

This project is shared under the terms in the `LICENSE` file in this folder.
