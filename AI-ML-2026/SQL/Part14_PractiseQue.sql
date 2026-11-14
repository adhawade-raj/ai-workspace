-- left exclusibve join
select * 
from customers as A
LEFT Join orders as B
ON A.customer_id=B.customer_id
Where b.customer_id is NULL;


-- right exclusibve join
select * 
from customers as A
Right Join orders as B
ON A.customer_id=B.customer_id
Where a.customer_id is NULL;