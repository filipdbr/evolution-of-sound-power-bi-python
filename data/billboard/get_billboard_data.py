import kagglehub
import pandas as pd
import os

# Define path to kaggle JSON
os.environ["KAGGLE_CONFIG_DIR"] = os.path.abspath("../../config")

# Get data from kaggle - dataset containing top 100 songs each year from 1958
path = kagglehub.dataset_download("dhruvildave/billboard-the-hot-100-songs")
print("Dataset downloaded to:", path)

# Read CSV
csv_path = os.path.join(path, "charts.csv")
df = pd.read_csv(csv_path)

# Save CSV
output_path = "billboard_data_2015_2024.csv"
df.to_csv(output_path, index=False)
print("Billboard data saved to:", output_path)
