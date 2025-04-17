# Log Analysis System for Web Server Logs

## 📌 Overview
This project analyzes raw web server logs to extract insights such as traffic patterns, most accessed pages, error codes, and IP behavior using Python. It demonstrates key data engineering steps like parsing, cleaning, aggregating, and reporting.

## ⚙️ Tech Stack
- Python (pandas, regex, matplotlib)
- Jupyter Notebook
- CSV and Log File Handling
- (Optional) MySQL or SQLite

## 📁 Project Structure
```
log-analysis-system/
├── sample_webserver.log         # Raw log file in log folder
├── parsed_log.csv              # Cleaned and structured log data in data folder
├── log_analysis_pipeline.ipynb  # Main notebook with all steps
├── daily_log_summary.csv       # Aggregated report
├── README.md
```

## 🔍 Key Features
- Parses raw Apache-style log files
- Cleans and structures log data using regex
- Aggregates traffic by day, IP, URL
- Visualizes traffic trends and error rates
- Saves summary report for further analysis

## 🧪 Analysis Highlights
- **Most requested URL**: `/index.html`, `/products`
- **Top error codes**: `404`, `500`
- **Peak traffic**: Visualized in requests per day/hour
- **Top IPs**: Identified users with most access

## 🚀 How to Run
1. Clone the repository
2. Open `log_analysis_pipeline.ipynb`
3. Run all cells step-by-step (ensure Python and Jupyter are installed)
4. Input log file: `sample_webserver.log`

## 📌 Conclusion
This project showcases how to build a lightweight, flexible log processing and reporting pipeline — a key skill in data engineering and backend development.

