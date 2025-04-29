# app/models.py

from sqlalchemy import Column, Integer, String, Date, Enum, DECIMAL
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"
    
    emp_id = Column(Integer, primary_key= True, index= True, autoincrement= True, nullable= False)
    first_name = Column(String(50), nullable = False)
    last_name = Column(String(50), nullable = False)
    departments = Column(String(100))
    positions = Column(String(100))
    salary = Column(DECIMAL(10,2))
    hire_date = Column(Date)
    gender = Column(Enum("M","F", name = "gender_enum"))
    email = Column(String(100), unique = True)
    phone = Column(String(15))
    
class DeletedEmployee(Base):
    __tablename__ = "deleted_employees"
    
    emp_id = Column(Integer, primary_key= True, index= True,  autoincrement= True, nullable= False)
    first_name = Column(String(50), nullable = False)
    last_name = Column(String(50), nullable = False)
    departments = Column(String(100))
    positions = Column(String(100))
    salary = Column(DECIMAL(10,2))
    hire_date = Column(Date)
    gender = Column(Enum("M","F", name = "gender_enum"))
    email = Column(String(100), unique = True)
    phone = Column(String(15))