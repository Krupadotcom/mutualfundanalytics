import pandas as pd

# Load data
funds = pd.read_csv("data/processed/processed_01_fund_master.csv")
sharpe = pd.read_csv("data/processed/sharpe_ratio.csv")

# Merge
data = funds.merge(sharpe, on="amfi_code")


# User input
risk = input("Enter Risk Appetite (Low/Moderate/High): ").strip().lower()

risk_map = {
    "low": ["Low"],
    "moderate": ["Moderate"],
    "high": ["High", "Very High"]
}

filtered = data[data["risk_category"].isin(risk_map.get(risk, []))]

recommendations = (
    filtered.sort_values("Sharpe_Ratio", ascending=False)
    .head(3)[["scheme_name_x", "risk_category", "Sharpe_Ratio"]]
)

recommendations = recommendations.rename(
    columns={"scheme_name_x": "scheme_name"}
)

print("\nTop 3 Recommended Funds\n")
print(recommendations.to_string(index=False))