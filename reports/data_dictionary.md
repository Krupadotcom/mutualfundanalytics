# Data Dictionary

## 01_fund_master.csv

| Column      | Data Type | Description                |
| ----------- | --------- | -------------------------- |
| amfi_code   | Integer   | Unique fund identifier     |
| scheme_name | Text      | Name of mutual fund scheme |
| fund_house  | Text      | Asset management company   |
| category    | Text      | Mutual fund category       |

---

## 02_nav_history.csv

| Column    | Data Type | Description     |
| --------- | --------- | --------------- |
| amfi_code | Integer   | Fund identifier |
| date      | Date      | NAV date        |
| nav       | Decimal   | Net Asset Value |

---

## 07_scheme_performance.csv

| Column            | Data Type | Description                   |
| ----------------- | --------- | ----------------------------- |
| amfi_code         | Integer   | Fund identifier               |
| return_1yr_pct    | Decimal   | 1-year return percentage      |
| return_3yr_pct    | Decimal   | 3-year return percentage      |
| return_5yr_pct    | Decimal   | 5-year return percentage      |
| expense_ratio_pct | Decimal   | Fund expense ratio percentage |
| risk_grade        | Text      | Risk category of the scheme   |

---

## 08_investor_transactions.csv

| Column           | Data Type | Description                 |
| ---------------- | --------- | --------------------------- |
| investor_id      | Integer   | Unique investor identifier  |
| transaction_date | Date      | Date of transaction         |
| transaction_type | Text      | SIP, Lumpsum, or Redemption |
| amount_inr       | Decimal   | Transaction amount in INR   |
| state            | Text      | Investor state              |
| city             | Text      | Investor city               |
| kyc_status       | Text      | KYC verification status     |

---

## Source Reference

All source files are stored in:

data/raw/

Cleaned files are stored in:

data/processed/

Database:

bluestock_mf.db
