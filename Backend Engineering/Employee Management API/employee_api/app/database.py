# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#Update with your actual MySQL credentials
DATABASE_URL = "mysql+mysqlconnector://root:yourpassword@localhost/employee_db"

#Create engine
engine = create_engine(DATABASE_URL)

#Create Session Factory
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind= engine)
 
# Base class for models
Base = declarative_base()

#Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()