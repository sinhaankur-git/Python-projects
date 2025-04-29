# employee_ui

import streamlit as st
import requests
import pandas as pd

base_url = "http://127.0.0.1:8000"

st.title("Employee Management System")

# View all empoyees
if st.button("View All Employees"):
    try:
        res = requests.get(f"{base_url}/employees")
        if res.status_code == 200:
            employees = res.json()
            if employees:
                df_emp = pd.DataFrame(employees)
                st.dataframe(df_emp)
                
                #Export CSV
                csv = df_emp.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label = "Download as CSV",
                    data = csv,
                    file_name= "employees.csv",
                    mime="text/csv"
                                
                )
            
            else:
                st.info("No employee found.")
        else:
            st.error("Failed to fetch employees.")
    except requests.exceptions.ConnectionError:
        st.error("Backend not running at 127.0.0.1:8000")
        
        
# Search empoyee id
st.subheader("Search Employee by ID")
search_id = st.text_input("Enter Employee ID")
if st.button("Search"):
    if search_id:
        res = requests.get(f"{base_url}/employees/{search_id}")
        if res.status_code == 200:
            st.json(res.json())
        else:
            st.warning("Employees not found.")


# Add new employee
st.subheader("Add New Employee")
with st.form("Add Employee Form"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    departments = st.text_input("Department")
    positions = st.text_input("Position")
    salary = st.text_input("Salary")
    hire_date = st.text_input("Hire Date")
    gender = st.text_input("Gender, ['M','F']")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    submit = st.form_submit_button("Add Employee")

    if submit:
        data = {
            "first_name" : first_name,
            "last_name" : last_name,
            "departments" : departments,
            "positions" : positions,
            "salary" : salary,
            "hire_date" : str(hire_date),
            "gender" : gender,
            "email" : email,
            "phone" : phone,
        }
        res = requests.post(f"{base_url}/employees", json=data)
        if res.status_code == 200:
            st.success("Employee added succesfully!")
        else:
            st.error(f" Error : {res.json()}")
            
# Update Employee
st.subheader("Update Employee")
update_id = st.text_input("Employee ID to Update")
if update_id:
    with st.form("update_form"):
        uf_name = st.text_input("First Name (Update)")
        ul_name = st.text_input("Last Name (Update)")
        udepartments = st.text_input("Department (Update)")
        upositions = st.text_input("Position (Update)")
        usalary = st.text_input("Salary (Update)", min_value = 0.0)
        uhire_date = st.text_input("Hire Date (Update)")
        ugender = st.text_input("Gender (Update), ['M','F']")
        uemail = st.text_input("Email (Update)")
        uphone = st.text_input("Phone Number (Update)")
        submit_update = st.form_submit_button("Updated Employee")

        if submit:
            data = {
                "first_name" : uf_name,
                "last_name" : ul_name,
                "departments" : udepartments,
                "positions" : upositions,
                "salary" : usalary,
                "hire_date" : str(uhire_date),
                "gender" : ugender,
                "email" : uemail,
                "phone" : uphone,
            }
            res = requests.put(f"{base_url}/employees/{update_id}", json=data)
            if res.status_code == 200:
                st.success("Employee added succesfully!")
            else:
                st.error("Failed to update employee")

# Delete Employee
st.subheader("Delete Employee")
delete_id = st.text_input("Enter Employee ID to Delete")
if st.button("Delete"):
    res = requests.delete(f"{base_url}/employees/{delete_id}")
    if res.status_code == 200:
        st.success(f"Employee {delete_id} deleted and archieved.")
    else:
        st.warning("Employees not found or already deleted.")
        

# View Archived Employee
st.subheader("View Archived Employees")
if st.button("View Archived"):
    res = requests.get(f"{base_url}/deleted-employees")
    if res.status_code == 200:
        archived = res.json()
        if archived:
            df_archived = pd.DataFrame(archived)
            st.dataframe(df_archived)
            #CSV download
            csv = df_archived.to_csv(index=False).encode('utf-8')
            st.download_button(
                    label = "Download Archived as CSV",
                    data = csv,
                    file_name= "archived_employees.csv",
                    mime="text/csv"
            )
        else:
            st.info("No archived employees info found.")
    else:
        st.error("Failed to fetch archived employees.")