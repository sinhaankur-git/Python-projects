# app/schemas

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

# Base employee schema (Shared fields for create/update)
class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    departments: Optional[str] = None
    positions: Optional[str] = None
    salary: Optional[float] = None
    hire_date: Optional[date] = None
    gender: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[int]= None
    
# For employee creation from base
class EmployeeCreate(EmployeeBase):
    pass
    
 # For employee update   
class EmployeeUpdate(BaseModel):
    pass
    
# For response   (What we send back to client)
class EmployeeOut(EmployeeBase):
    emp_id: int
    
    class Config:
        orm_mode = True

# Deleted employee schema
class DeletedEmployeeOut(EmployeeOut):
    pass    

    
    