# Mutual Fund Analytics

## Project Overview

The Mutual Fund Analytics project is a data analytics solution built using Python, SQLite, SQL, Jupyter Notebook, and Power BI. It analyzes mutual fund performance, investor transactions, NAV history, and portfolio holdings to generate meaningful insights and investment recommendations.

---

## Objectives

- Perform ETL (Extract, Transform, Load) on mutual fund datasets.
- Store processed data in SQLite.
- Analyze fund performance using Python.
- Generate investment performance metrics.
- Build a recommendation engine.
- Visualize insights using Power BI.

---

## Project Structure

```
mutualfundanalytics/
│
├── dashboard/
│   └── bluestock_mf.pbix
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── reports/
│
├── scripts/
│   ├── compute_metrics.py
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── bluestock_mf.db
├── data_ingestion.py
├── data_cleaning.py
├── data_visualization.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Jupyter Notebook
- Power BI
- Matplotlib

---

## Key Features

- Data ingestion and preprocessing
- ETL pipeline automation
- SQLite database integration
- Exploratory Data Analysis (EDA)
- Mutual fund performance analytics
- Performance metrics computation
- Recommendation engine
- Interactive Power BI dashboard

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

### Run the Recommendation Engine

```bash
python scripts/recommender.py
```

---

## Dashboard

The Power BI dashboard provides insights into:

- Fund performance
- NAV trends
- Investor transactions
- Portfolio holdings
- Risk analysis

---

## Author

**Krupa**

Capstone Project – Mutual Fund Analytics