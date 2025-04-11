-- csv to mySql data pipeline --

create database employee_db;

use employee_db;

create table employees (
	emp_id int primary key,
    first_name varchar(50),
    last_name varchar(50),
    departments varchar(100),
    positions varchar(100),
	salary decimal (10,2),
    hire_date date,
    gender ENUM('M', 'F'),
    email varchar(100),
    phone varchar(15)
);    


