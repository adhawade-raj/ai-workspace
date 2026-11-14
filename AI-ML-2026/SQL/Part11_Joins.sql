
select * from customers;
select * from orders;
-- Inner Join

Select * 
from customers c
Inner Join orders o
ON c.customer_id = o.customer_id;

-- Left Join (Outer Join)

Select * 
from customers c
LEFT Join orders o
ON c.customer_id = o.customer_id;

-- Right Join (Outer Join)

Select * 
from customers c
Right Join orders o
ON c.customer_id = o.customer_id;


-- OUTER JOIN using Union -> LEFT + UNION + RIGHT

-- Left Join (Outer Join)
Select * 
from customers c
LEFT Join orders o
ON c.customer_id = o.customer_id
UNION
-- Right Join (Outer Join)
Select * 
from customers c
Right Join orders o
ON c.customer_id = o.customer_id;


