# Spotify Top 100 Songs Analysis (2015–2024)

This project analyzes how popular music has evolved over the past decade by extracting the top 100 songs for each year (2015–2024) using Spotify's Web API. The dataset includes audio features like danceability, energy, valence, and tempo — enabling an exploration of trends in mood, genre, and sound over time.

## Author  
Filip Dąbrowski*

## Project Objectives

- Extract Spotify's top 100 songs per year (2015–2024)
- Analyze changes in song characteristics and popularity across time
- Visualize audio feature trends and genre shifts using Power BI

## Data Collection

- Source: Spotify Web API
- Method: Python script using the Spotipy library
- Playlists: Yearly "Top 100" or "Top Hits" playlists curated by Spotify
- Collected fields:
  - Track name, artist, release year, popularity
  - Audio features: danceability, energy, valence, tempo, and more

## Tools and Technologies

- Python (with Spotipy) for data extraction
- Power BI for modeling and visualization
- Git and GitHub for version control and documentation

## Project Structure

```plaintext
spotify-top-100-analysis/                     # Raw and clean dataset
├── data/
│   ├── clean/
│   └── raw/
│
├── scripts/
│
├── visuals/
│
├── dashboard/
│   └── spotify_trends_dashboard.pbix         # Power BI dashboard file
│
├── assets/
│   └── cover.png                             # Optional cover/banner image for GitHub
│
├── LICENSE                                   # MIT license
├── README.md                                 # Project documentation
└── .gitignore                                # Files to ignore in Git
