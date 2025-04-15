use sales_orders_db;

-- Some useful SQL views

-- View:  customer_order_summary
-- Shows each customer's total number of orders and total amount spent.

create or replace view customer_order_summary as 
select
	c.customer_id , c.customer_name,
    count(o.order_id)as total_orders,
    sum(o.total_price) as total_spent
from customers c
join orders o on c.customer_id = o.customer_id
group by c.customer_id , c.customer_name;

-- product_sales_summary
-- Description: Shows total quantity sold and revenue for each product.

create or replace view product_sales_summary as
select
	p.product_id, p.product_name,
    sum(oi.quantity) as total_quantity_sold,
    sum(oi.quantity*oi.unit_price) as total_revenue
from products as p
join order_items oi on p.product_id = oi.product_id
group by p.product_id, p.product_name;	

-- daily_sales
-- Desc: Shows total sales across all the orders.

create or replace view daily_sales as
select
	order_date,
    count(order_id) as total_orders,
    sum(total_price) as daily_revenue
from orders
group by order_date
order by order_date;	


-- payment_method_summary
-- Desc: Number and total value of payments by each method.
select* from payments;
create or replace view payment_method_summary as
select
	payment_method,
    count(payment_id) as total_payments,
    sum(total_price) as total_amount
from payments
group by payment_method;
