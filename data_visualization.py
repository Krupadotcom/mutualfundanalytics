import pandas as pd
import os
import matplotlib.pyplot as plt

os.makedirs("reports", exist_ok=True)

processed_path = "data/processed"
files = os.listdir(processed_path)

file_path = os.path.join(processed_path, files[0])
df = pd.read_csv(file_path)

numeric_cols = df.select_dtypes(include=['number']).columns
col = numeric_cols[0]

plt.figure()
df[col].plot(kind='bar')
plt.title("Bar Chart")

# ✅ SAVE FIRST (IMPORTANT)
plt.savefig("reports/bar_chart.png")

# optional: show graph
plt.show()

print("Graph saved in reports folder")