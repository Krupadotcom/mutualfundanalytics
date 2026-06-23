import pandas as pd
import os

raw_path = "data/raw"
processed_path = "data/processed"

files = os.listdir(raw_path)

if len(files) == 0:
    print("No files in raw folder")
else:
    file_name = files[0]
    file_path = os.path.join(raw_path, file_name)

    df = pd.read_csv(file_path)

    print("Original Data Shape:", df.shape)

    # 1. Remove duplicates
    df = df.drop_duplicates()

    # 2. Handle missing values
    df = df.fillna("Not Available")

    print("After cleaning Shape:", df.shape)

    # save cleaned file
    os.makedirs(processed_path, exist_ok=True)

    output_file = os.path.join(processed_path, "cleaned_" + file_name)
    df.to_csv(output_file, index=False)

    print("Cleaned file saved:", output_file)