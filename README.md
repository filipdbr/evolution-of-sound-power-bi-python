# Music Industry Trends Analysis (2015–2024)

This project explores how the global music industry has evolved over the past decade. It combines data from Spotify's Top 100 charts with additional context to uncover trends in genres, song characteristics, artist dynamics, release formats, and globalization of popular music.

While Spotify serves as the primary data source for top tracks and audio features, the analysis aims to provide broader insights into music consumption and production patterns from 2015 to 2024.

## Author  
Filip Dąbrowski*

## Project Objectives

- Analyze top songs from 2015–2024 to understand broader trends in music
- Explore changes in genre popularity, song mood, and structure
- Track the evolution of artists and the growing internationalization of music
- Visualize and interpret the data through interactive Power BI dashboards

## Data Collection

- **Primary Source**: [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- **Method**: Python script using the `Spotipy` library
- **Playlists**: Yearly "Top 100" or "Top Hits" curated by Spotify

Additional sources may be integrated to enrich context (e.g., lyrics, geography, album metadata)

## Tools and Technologies

- Python (with Spotipy) for data extraction
- Power BI for modeling and visualization
- Git and GitHub for version control and documentation

## Power BI Report Overview
The report includes the following thematic pages:

### 1. 📈 Music Trends Over Time  
Genre share, mood evolution, song tempo and duration

### 2. 👑 Top Artists and Style Evolution  
Artist dominance, stylistic shifts, collaborations

### 3. 🌍 Music Globalization  
Artist origin, rise of regional genres, language share

### 4. 🔍 What Makes a Hit?  
Feature comparison between Top 10 vs. Top 100

### 5. 💿 Singles, Albums, and Formats  
Shift from albums to singles, track count, song length

Status

- [x] Spotify data extracted  
- [ ] Power BI model designed  
- [ ] Final dashboard in development

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
```

## License

MIT License