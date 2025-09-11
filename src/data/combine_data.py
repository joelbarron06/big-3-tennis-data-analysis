import pandas as pd
import os

# combine the data from each year into one csv
raw_dir = "../../data/raw/"
all_files = []

for file in os.listdir(raw_dir):
    if file.endswith(".csv"):
        all_files.append(file)

combined_df = pd.DataFrame()
for file in all_files:
    year_df = pd.read_csv(os.path.join(raw_dir, file))
    combined_df = pd.concat([combined_df, year_df], ignore_index=False)

combined_df.to_csv("../../data/processed/combined_ATP_results.csv", index=True)