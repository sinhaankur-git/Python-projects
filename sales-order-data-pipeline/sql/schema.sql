-- Ecommerce Sales & Order Pipeline --

create database if not exists sales_orders_db;
use sales_orders_db;

-- Customer Table
create table customers(
	customer_id varchar(15) primary key ,
    customer_name varchar (100) not null,
    email varchar (100) unique not null,
    country varchar (100),
    registered_date date
    );
    
-- Product Table    
create table products(
	product_id varchar(15) primary key ,
    product_name varchar (100) not null,
    category varchar (100),
    unit_price decimal (10,2) not null,
    quantity int default 0 
    );

-- Orders Table
create table orders(
	order_id varchar(15) primary key ,
    customer_id varchar(15),
    order_date date not null,
    total_price decimal(10,2),
    status ENUM('Placed','Shipped','Delieverd','Cancelled') Default ('Placed'),
    foreign key (customer_id) references customers(customer_id)
    );
   
-- Order Item Table    
create table order_items(
	item_id varchar(15) primary key,
    order_id varchar(15),
    product_id varchar(15),
    quantity int not null,
    unit_price decimal(10,2) not null,
    foreign key (order_id) references orders(order_id),
    foreign key (product_id) references products(product_id)
    );
 
-- Payment table
create table payments(
	payment_id varchar(15) primary key,
    order_id varchar(15),
    customer_id varchar(15),
    payment_method ENUM('Credit Card','Debit Card','Net Banking','PayPal','UPI'),
    total_price decimal(10,2) not null,
    foreign key (order_id) references orders(order_id),
    foreign key (customer_id) references customers(customer_id)
    );
    drop table payments;
