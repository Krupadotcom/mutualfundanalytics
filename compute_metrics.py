import sqlite3
import pandas as pd
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "bluestock_mf.db"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Connect to SQLite
# -----------------------------
conn = sqlite3.connect(DB_PATH)

# Read performance table
df = pd.read_sql("SELECT * FROM fact_performance", conn)

conn.close()

# -----------------------------
# Compute summary metrics
# -----------------------------
summary = pd.DataFrame({
    "Metric": [
        "Average 1-Year Return (%)",
        "Average 3-Year Return (%)",
        "Average 5-Year Return (%)",
        "Average Alpha",
        "Average Beta",
        "Average Sharpe Ratio",
        "Average Sortino Ratio",
        "Average Annual Std Dev (%)",
        "Average Max Drawdown (%)",
        "Average Expense Ratio (%)",
        "Average AUM (Crore)"
    ],
    "Value": [
        df["return_1yr_pct"].mean(),
        df["return_3yr_pct"].mean(),
        df["return_5yr_pct"].mean(),
        df["alpha"].mean(),
        df["beta"].mean(),
        df["sharpe_ratio"].mean(),
        df["sortino_ratio"].mean(),
        df["std_dev_ann_pct"].mean(),
        df["max_drawdown_pct"].mean(),
        df["expense_ratio_pct"].mean(),
        df["aum_crore"].mean()
    ]
})

# Save CSV
output_file = OUTPUT_DIR / "performance_metrics.csv"
summary.to_csv(output_file, index=False)

print("\nPerformance Metrics Summary:\n")
print(summary)

print(f"\nSummary saved to: {output_file}")