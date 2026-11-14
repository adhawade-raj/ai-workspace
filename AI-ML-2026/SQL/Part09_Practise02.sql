Create table student (
rollNo INT Primary Key,
name varchar(30),
city varchar(50),
marks INT
);

Insert Into student
(rollNo, name, city, marks)
values
(110, "adam", "Delhi", 76),
(108, "bob", "Mumbai", 65),
(124, "casey", "Pune", 94),
(112, "duke", "Pune", 80);

select * from student;

select * from student where marks>=75;

select distinct(CITY) from student;
Select city from student GROUP BY City;

select city, max(marks) from student GROUP BY City;
select avg(marks) from student;

Alter table student
ADD column grade varchar(5);

Update student set Grade = "o" where marks>=80;
Update student set Grade = "A" where marks>=70;
Update student set Grade = "B" where marks Between 50 and 69;


