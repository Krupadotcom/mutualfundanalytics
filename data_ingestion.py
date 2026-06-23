import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("\n====================")
        print("File Name:", file)
        print("Rows and Columns:", df.shape)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())