
use college;

create view view1 as
Select customer_id, name from customers;

Select * from view1;

-- Join as a view
Create view view2 as
select c.customer_id, c.name, o.order_id
from customers c
Inner join orders o
ON c.customer_id = o.customer_id;

select * from view2;

drop view view3;