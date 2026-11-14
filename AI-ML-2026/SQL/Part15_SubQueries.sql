use college;
Select * from orders
where amount > (
Select Avg(amount) from orders
);


Select name, (
Select Count(*)
from orders o
where o.customer_id=c.customer_id
) AS order_count
From Customers c;



Select summary.customer_id, summary.avg_amount
from ( Select customer_id, avg(amount) as avg_amount
from orders 
group BY customer_id
) as summary;