# Music Industry Trends Analysis (2015–2024)

This project explores how the global music industry has evolved over the past decade. It combines data from Spotify's Top 100 charts and Billboard Hot 100 with additional context to uncover trends in genres, song characteristics, artist dynamics, release formats, and globalization of popular music.

*While Python scripts were used for initial data collection, the focus of this project is on Power BI analysis and visualization, with data cleaning performed directly in the BI tool.*

## Author  
Filip Dąbrowski

## Project Objectives

- Analyze top songs from 2015–2024 to understand broader trends in music
- Explore changes in genre popularity, song mood, and structure
- Track the evolution of artists and the growing internationalization of music
- Visualize and interpret the data through interactive Power BI dashboards

## Data Collection

### **Primary Sources**:
1. [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
2. [Billboard Hot 100 Songs (Kaggle)](https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs)

### **Data Download**:
- **Spotify**: Python script using `Spotipy` library (yearly "Top 100" playlists)
- **Billboard**: Kaggle dataset downloaded via `kagglehub` with JSON API key

### Configuration for Kaggle:
The Billboard data is already included in this repository as a CSV, so **you don't need to configure Kaggle or download it**.

However, if you ever need to download data from Kaggle here's the config:

1. Install dependencies:  
   ```bash
   pip install -r requirements.txt

2. Get the API key from your Kaggle Account → settings
3. Configure Kaggle API:
Add your JSON key to:
`~/config/kaggle.json`

    ```File structure should look like this: 
    evolution-of-sound-power-bi/
    ├── config/
    │   └── kaggle.json
    └── .env
   ```

3. Download data:
```bash
# Billboard data
python data/billboard/get_billboard_data.py
```

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