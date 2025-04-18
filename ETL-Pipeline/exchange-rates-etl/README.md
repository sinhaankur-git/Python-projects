# 💱 Exchange Rates ETL Pipeline

## 📌 Overview
This project demonstrates a full ETL pipeline to extract live foreign exchange rates using the [Frankfurter API](https://www.frankfurter.app/), transform the data, load it into a MySQL database, and perform basic analysis with SQL queries. This is a great beginner-friendly project for learning API integration and SQL-based analytics.

---

## ⚙️ Tech Stack
- Python (`requests`, `pandas`, `mysql-connector-python`)
- MySQL
- Jupyter Notebook
- Frankfurter API (no API key required)

---

## 🔄 ETL Workflow

| Step       | Description                                  |
|------------|----------------------------------------------|
| Extract    | Pulls live exchange rates from Frankfurter API |
| Transform  | Converts JSON to tabular format with timestamp |
| Load       | Inserts data into a structured MySQL table    |
| Analyze    | Runs SQL queries to find trends and compare currencies |

---

## 🧱 Database Table: `exchange_rates`
```sql
CREATE TABLE exchange_rates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    base_currency VARCHAR(10),
    target_currency VARCHAR(10),
    rate FLOAT,
    timestamp DATETIME,
    UNIQUE (base_currency, target_currency, timestamp)
);
```

---

## 📊 Key Queries
- Highest exchange rate vs USD
- All exchange rates greater than 1
- Compare USD to EUR, GBP, INR, JPY

---

## 📁 Project Structure
```
exchange-rates-etl/
├── data/
│   └── usd_vs_major_currencies.csv
├── notebooks/
│   └── exchange_rates_etl_pipeline.ipynb
├── db/
    └── exchange_rates_db.sql     # (Optional SQL schema backup)
├── README.md

```

---

## ▶️ How to Run
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Make sure MySQL is running and `exchange_db` is created
4. Open and run `exchange_rates_etl_pipeline.ipynb` step-by-step

---

## 📌 Notes
- API source: [Frankfurter.app](https://www.frankfurter.app/)
- Project shows complete ETL logic in one Jupyter Notebook
- Easily extendable to use historical or custom date ranges

