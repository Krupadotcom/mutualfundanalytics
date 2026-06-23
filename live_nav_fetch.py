import pandas as pd
import os

print("Project started...")

# paths
raw_path = "data/raw"
processed_path = "data/processed"

# get files from raw folder
files = os.listdir(raw_path)
print("Files in raw folder:", files)

# check if files exist
if len(files) == 0:
    print("No CSV files found in raw folder")
else:
    # take first file
    file_name = files[0]
    file_path = os.path.join(raw_path, file_name)

    print("Reading file:", file_name)

    df = pd.read_csv(file_path)

    print("\nFirst 5 rows:")
    print(df.head())

    # create processed folder if not exists
    os.makedirs(processed_path, exist_ok=True)

    output_file = os.path.join(processed_path, "processed_" + file_name)

    df.to_csv(output_file, index=False)

    print("\nSaved processed file as:", output_file)