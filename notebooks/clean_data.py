import pandas as pd

print("Starting data cleaning...")

# =========================
# 1. NAV HISTORY
# =========================

df = pd.read_csv("data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"], errors="coerce")

df = df.sort_values(["amfi_code", "date"])

df = df.drop_duplicates()

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

df = df[df["nav"] > 0]

df.to_csv("data/processed/nav_history_clean.csv", index=False)

print("Nav cleaned")


# =========================
# 2. INVESTOR TRANSACTIONS
# =========================

df2 = pd.read_csv("data/raw/08_investor_transactions.csv")

df2["transaction_date"] = pd.to_datetime(df2["transaction_date"], errors="coerce")

df2["transaction_type"] = df2["transaction_type"].astype(str).str.upper().str.strip()

df2["amount_inr"] = pd.to_numeric(df2["amount_inr"], errors="coerce")

df2 = df2[df2["amount_inr"] > 0]

df2 = df2[df2["kyc_status"].isin(["Verified", "Pending", "Rejected"])]

df2.to_csv("data/processed/investor_transactions_clean.csv", index=False)

print("Transactions cleaned")


# =========================
# 3. SCHEME PERFORMANCE
# =========================

df3 = pd.read_csv("data/raw/07_scheme_performance.csv")

cols = ["return_1yr_pct", "return_3yr_pct", "return_5yr_pct", "expense_ratio_pct"]

for c in cols:
    df3[c] = pd.to_numeric(df3[c], errors="coerce")

df3 = df3.dropna(subset=cols)

df3 = df3[(df3["expense_ratio_pct"] >= 0.1) & (df3["expense_ratio_pct"] <= 2.5)]

df3.to_csv("data/processed/scheme_performance_clean.csv", index=False)

print("Performance cleaned")