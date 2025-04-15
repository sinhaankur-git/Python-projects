-- 1. Business & Analytical SQL Queries --

use sales_orders_db;
select
	c.customer_name,
    sum(o.total_price) as total_spent
from customers c
join orders o on c.customer_id = o.customer_id
group by c.customer_name
order by total_spent desc
limit 5 ;

---------------------------------------------------
-- 2. Best Selling Products 

select
	p.product_name,
    p.category,
	sum(oi.quantity) as total_sold
from
	products p
join order_items oi on p.product_id = oi.product_id
group by p.product_name,p.category
order by total_sold desc
limit 5;

---------------------------------------------------

-- 3. Revenue by product category

select
	p.category,
    sum(oi.quantity * oi.unit_price ) as total_revenue
from products p
join order_items oi on p.product_id = oi.product_id
group by p.category
order by total_revenue desc;

---------------------------------------------------

-- 4. monthly spend

select
	date_format(order_date, '%Y-%m') as month,
	count(order_id) as total_orders,
    sum(total_price) as revenue
from orders
group by month
order by month;	

---------------------------------------------------

-- 5. Orders without payments

select
	o.order_id,
    c.customer_name,
    o.order_date,
    o.total_price
from orders o
join customers c on o.customer_id = c.customer_id
left join payments p on o.order_id = p.order_id
where p.payment_id is null;

----------------------------------------------------

-- 6. Average Order by Country

select
    c.country,
    count(o.order_id) as total_orders,
    sum(o.total_price) as total_revenue,
    round(avg(o.total_price),2) as avd_order_value
from customers c
join orders o on c.customer_id = o.customer_id
group by c.country
order by total_revenue desc;