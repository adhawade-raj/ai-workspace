CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    name VARCHAR(50),
    balance DECIMAL(10, 2),
    branch VARCHAR(50)
);

INSERT INTO accounts VALUES
(1, 'Adam', 500.00, 'Mumbai'),
(2, 'Bob', 300.00, 'Delhi'),
(3, 'Charlie', 700.00, 'Bangalore'),
(4, 'David', 1000.00, 'Noida');

create INDEX idx_branch ON accounts(branch);
show index from accounts;
select * from accounts where branch="Mumbai";

-- composite indexes
create INDEX idx2 ON accounts(branch, balance);
drop index idx2 ON accounts;