# Employee Management System (FastAPI + Streamlit)

This project is a full-stack **Employee Management System** built using:
- 🔧 **FastAPI** for the backend REST API
- 🗄️ **MySQL** as the database
- 🌐 **Streamlit** for a clean, interactive frontend

---

## 📦 Features

| Feature                        | Description                                  |
|-------------------------------|----------------------------------------------|
| 🔍 Search by Employee ID      | Retrieve specific employee details           |
| 📋 View All Employees         | Display all employees in a table             |
| ➕ Add Employee               | Submit new employee records                  |
| ✏️ Update Employee           | Modify existing employee information         |
| ❌ Delete Employee            | Archive employee data before deletion        |
| 🕵️ View Archived Employees   | See list of soft-deleted employees           |
| 📁 Export CSV                 | Download active & archived employee data     |

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, SQLAlchemy
- **Database:** MySQL
- **Frontend:** Streamlit
- **ORM:** SQLAlchemy

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.10+
- MySQL installed & running

### 🔧 Setup Instructions

1. **Clone the Repository:**
```bash
git clone https://github.com/yourusername/employee-management-system.git
cd employee-management-system
```

2. **Create Virtual Environment & Install Dependencies:**
```bash
python -m venv venv
source venv/bin/activate   # or .\venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

3. **Start FastAPI Backend:**
```bash
uvicorn app.main:app --reload
```
FastAPI will run at `http://127.0.0.1:8000`

4. **Run Streamlit Frontend:**
```bash
streamlit run employee_ui.py
```
Streamlit will open at `http://localhost:8501`

---

## 📁 Project Structure

```
employee-management-system/
│
├── app/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── employee_ui.py         # Streamlit frontend
├── requirements.txt
└── README.md
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Ankur Sinha**  
Data Engineering & Backend Development Enthusiast

📫 [Connect with me on LinkedIn](www.linkedin.com/in/sinha-ankur-as16)
