#app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from app.database import engine, get_db
from .schemas import EmployeeCreate, EmployeeOut

#create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Create employee
@app.post("/employees", response_model=schemas.EmployeeOut)
def create_employee(employee:schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.add_employee(db,employee)   

#Read all employees
@app.get("/employees", response_model=list[EmployeeOut])
def read_employees(db: Session = Depends(get_db)):
    return crud.get_all_employees(db)

#Read employee by ID
@app.get("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def read_employee(emp_id: int, db: Session= Depends(get_db)):
    employee = crud.get_employee_by_id(db,emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee Not Found")
    return employee

#Update employee
@app.put("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session= Depends(get_db)):
    updated = crud.update_employee(db, emp_id, employee)
    if updated is None:
       raise HTTPException(status_code=404, detail="Employee Not Found")
    return updated

# Delete and archieve employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session= Depends(get_db)):
    delete = crud.delete_employee(db, emp_id)
    if delete is None:
       raise HTTPException(status_code=404, detail="Employee Not Found")
    return {"message": f"Employee {emp_id} deleted and archieved"}

# Get deleted employees
@app.get("/deleted-employees", response_model=list[schemas.DeletedEmployeeOut])
def get_deleted_employees(db: Session= Depends(get_db)):
    return crud.get_all_deleted_employees(db)

#Permanently delete from archieve
@app.delete("/deleted-employees/{emp_id}")
def permanently_delete_archived_employee(emp_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_archived_employee(db, emp_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Archived Employee Not Found")
    return deleted