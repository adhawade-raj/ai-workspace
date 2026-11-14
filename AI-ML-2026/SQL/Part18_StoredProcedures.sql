USE college;
select * from accounts;

DELIMITER $$
create procedure check_balance(IN acc_id INT)
BEGIN
select balance
from accounts
where account_id = acc_id;

END $$

DELIMITER ;

CALL check_balance(2);

SHOW PROCEDURE STATUS
WHERE Db = 'college';