# 🌦️ OpenWeather ETL Pipeline

## 📌 Overview
This project extracts current weather data from the [OpenWeather API](https://openweathermap.org/api), transforms it into structured format, and loads it into a MySQL database for analysis. It demonstrates a full ETL workflow using Python.

---

## ⚙️ Tech Stack
- Python (`requests`, `pandas`, `mysql-connector-python`)
- MySQL (database)
- Jupyter Notebook

---

## ⭮️ ETL Workflow

| Step       | Description                                |
|------------|--------------------------------------------|
| Extract    | Fetches live weather data for selected cities |
| Transform  | Parses JSON, selects key fields (e.g., temp, humidity) |
| Load       | Inserts data into MySQL, handling duplicates |
| Analyze    | SQL queries for max temp, average humidity, wind stats |

---

## 🗃️ MySQL Table Structure

```sql
CREATE TABLE weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    temperature FLOAT,
    humidity INT,
    weather VARCHAR(100),
    wind_speed FLOAT,
    timestamp DATETIME,
    UNIQUE (city, timestamp)
);
```

---

## 📊 Sample Queries

- Cities with highest temperatures
- Average humidity across locations
- Windy cities (wind speed > 5 m/s)

---

## 📁 Project Structure
```
openweather-etl/
├── data/
    └── weather_analysis.csv
├── sql_db/
    └── weather_db.sql
├── notebooks/
│   └── openweather_etl_pipeline.ipynb
├── README.md
├── requirements.txt

```

---

## 📌 How to Run
1. Clone the repo
2. Create a `weather_db` database in MySQL
3. Add your API key in the notebook
4. Run all cells step-by-step in `openweather_etl_pipeline.ipynb`

