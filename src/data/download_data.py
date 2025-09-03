import pandas as pd
import os


# download Jeff Sackman's tennis data and save into ...data/raw/, for years 1998-2024
def download_and_save_data(year):
    url = f"https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_matches_{year}.csv"
    df = pd.read_csv(url)
    raw_dir = os.path.join("../../data/raw/")
    os.makedirs(raw_dir, exist_ok=True)
    df.to_csv(f"{raw_dir}atp_matches_{year}.csv", index=False)
    print(f"Data for year {year} downloaded and saved.")
    return

for year in range(1998, 2025):
    download_and_save_data(year)
