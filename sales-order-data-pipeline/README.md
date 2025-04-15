# Ecommerce Sales & Orders Data Pipeline System

## 📌 Overview
This project simulates a real-world ecommerce data pipeline using Python and MySQL. It demonstrates the end-to-end process of data engineering—from data ingestion to SQL-based analytics and business intelligence.

## 🚀 Objectives
- Ingest raw data from CSV
- Clean and transform the data using Python (Pandas)
- Load the cleaned data into a MySQL database
- Run analytical SQL queries to extract business insights
- Visualize the results using Matplotlib and Seaborn

## 🧱 Database Schema
The database is composed of the following tables:
- `customers`
- `products`
- `orders`
- `order_items`
- `payments`

The schema and view definitions were created in MySQL Workbench and saved as:
- `schema.sql`
- `views.sql`
- `business-&-sql-queries.sql`

## 📥 Data Ingestion
Source data: `ecom-sales-data1.csv`
- Loaded using Pandas
- Data cleaning includes type conversions, date formatting, and comma removal from numeric strings

## 🧹 Data Cleaning & Transformation
- Converted string numbers with commas to float
- Transformed date columns to `datetime` objects
- Prepared the dataset for relational table insertion

## 🗃️ Database Operations
- MySQL database: `sales_orders_db`
- Connection via MYSQL.Connections/SQLAlchemy for Pandas compatibility
- Data inserted into MySQL tables manually or via script (not included here for brevity)

## 📊 Analytical Queries
A range of business-focused queries were executed:
- Top 5 customers by spending
- Best Selling Products 
- Revenue by product category
- Monthly Spend
- Orders Without Payments
- Average Order per Country

Queries are saved in `business-&-sql-queries.sql`.

## 📈 Visualizations
Generated using Matplotlib and Seaborn:
- Line chart for monthly revenue trend
- Bar charts for:
  - Orders without payments 
  - Top 5 customers by total spend
  - Top 5 Best Selling Products
  - Revenue by Product Category
  - Average Order per Country

## 🧾 Tools Used
- Python (Pandas, Matplotlib, Seaborn, SQLAlchemy)
- MySQL & MySQL Workbench
- Jupyter Notebook

## 📁 File Structure
```
├── ecom-sales-orders-data-pipeline.ipynb      # Final notebook
├── ecom-sales-data1.csv                       # Source CSV file
├── schema.sql                                 # SQL table creation
├── views.sql                                  # SQL views
├── business-&-sql-queries.sql
└── ER Diagram.png                             # EEr Diagram png file
└── README.md                                  # This file
```

## ✅ Conclusion
This project demonstrates a complete data engineering workflow. It's ideal for showcasing practical skills in data cleaning, SQL database design, query writing, and business analysis.

---
Feel free to clone, customize, or extend this project for your portfolio!

