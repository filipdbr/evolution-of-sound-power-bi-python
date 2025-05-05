import json
import os

"""
Helper script to create a JSON structure for playlist IDs from multiple countries and years.
Definitely faster than doing it all by hand 😉
"""

# Output path relative to this script's location
output_path = os.path.join(os.path.dirname(__file__), "playlists.json")

# Define years
years = range(2015, 2025)

# Create structured dictionary
playlists = {
    "global":   {str(year): f"playlist_id_{year}_global" for year in years},
    "usa":      {str(year): f"playlist_id_{year}_usa" for year in years},
    "france":   {str(year): f"playlist_id_{year}_fr" for year in years},
    "poland":   {str(year): f"playlist_id_{year}_poland" for year in years},
    "china":    {str(year): f"playlist_id_{year}_china" for year in years},
    "india":    {str(year): f"playlist_id_{year}_india" for year in years}
}

# Write to JSON file
with open(output_path, "w") as f:
    json.dump(playlists, f, indent=4)

print(f"The JSON was successfully written to {output_path}")
