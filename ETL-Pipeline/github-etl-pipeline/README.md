# 🎨 GitHub ETL Pipeline

## 📄 Overview
This project builds a full ETL pipeline to extract public repository and user profile data from the GitHub API for a given username. The data is transformed and stored in a MySQL database, and key statistics are analyzed using SQL.

---

## ⚙️ Tech Stack
- Python (`requests`, `pandas`, `mysql-connector-python`)
- GitHub REST API
- MySQL
- Jupyter Notebook

---

## 🔄 ETL Workflow
| Step     | Description                                          |
|----------|------------------------------------------------------|
| Extract  | Fetch user info and repositories from GitHub API     |
| Transform| Normalize and clean the data into structured format  |
| Load     | Insert data into MySQL (`github_users`, `github_repos`) |
| Analyze  | Run SQL queries to extract insights from the data     |

---

## 📊 Database Tables

### `github_users`
```sql
CREATE TABLE github_users (
    login VARCHAR(100) PRIMARY KEY,
    name VARCHAR(100),
    company VARCHAR(100),
    location VARCHAR(100),
    followers INT,
    public_repos INT,
    created_at DATETIME
);
```

### `github_repos`
```sql
CREATE TABLE github_repos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(100),
    repo_name VARCHAR(100),
    description TEXT,
    language VARCHAR(100),
    stars INT,
    forks INT,
    updated_at DATETIME,
    FOREIGN KEY (login) REFERENCES github_users(login)
);
```

---

## 🔢 Key SQL Queries
- Most starred repository
- Most forked repository
- Most used programming languages
- Recently updated repositories

CSV Outputs:
- `data/top_starred_repo.csv`
- `data/top_forked_repo.csv`
- `data/language_stats.csv`
- `data/recently_updated_repos.csv`

---

## 📁 Project Structure
```
github-etl/
├── data/
│   ├── top_starred_repo.csv
│   ├── top_forked_repo.csv
│   ├── language_stats.csv
│   └── recently_updated_repos.csv
├── notebooks/
│   └── github_etl_pipeline.ipynb
├── sql_db/                       # (Optional backup or schema)
    └── github_db.sql
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run
1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Start MySQL and create the `github_db` database
4. Open `github_etl_pipeline.ipynb` and follow the steps

---

## 📅 Notes
- Rate limit for unauthenticated GitHub API: 60 requests/hour
- Extendable to track stars/forks over time or across users

