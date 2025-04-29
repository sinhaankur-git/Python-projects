# app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas

# Add employee
def add_employee(db: Session, employee: schemas.EmployeeCreate):
    new_employee = models.Employee(**employee.model_dump())   #(Pydantic V1 supports dict(), and v2 supports model_dump())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

# Get all employees
def get_all_employees(db: Session):
    return db.query(models.Employee).all()

# Get all employees by id
def get_employee_by_id(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.emp_id == emp_id).first()

# Update employee
def updated_employee(db:Session, emp_id:int, update_data: schemas.EmployeeUpdate):
    employee = get_employee_by_id(db, emp_id)
    if not employee:
        return None
    for key, value in update_data.model_dump().items():
        setattr(employee,key, value)
    db.commit()
    db.refresh(employee)
    return employee

#archieve employee before deletion
def archive_employee(db:Session, employee: models.Employee):
    archived = models.DeletedEmployee(
        emp_id=employee.emp_id,
        first_name=employee.first_name,
        last_name=employee.last_name,
        departments=employee.departments,
        positions=employee.positions,
        salary=employee.salary,
        hire_date=employee.hire_date,
        gender=employee.gender,
        email=employee.email,
        phone=employee.phone,
    )
    db.add(archived)
    db.commit()

# Delete employee and archieve
def delete_employee(db:Session, emp_id:int):
    print(f"Attempting to delete emp_id = {emp_id}")
    employee = get_employee_by_id(db, emp_id)
    if not employee:
        return None
    archive_employee(db,employee)
    db.delete(employee)
    db.commit()
    return employee

# Get all deleted employees
def get_all_deleted_employees(db:Session):
    return db.query(models.DeletedEmployee).all()

#Delete archieve employee
def delete_archived_employee(db: Session, emp_id: int):
    archived = db.query(models.DeletedEmployee).filter(models.DeletedEmployee.emp_id == emp_id).first()
    if not archived:
        return None
    db.delete(archived)
    db.commit()
    return archived



    

