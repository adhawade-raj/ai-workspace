create database IF NOT Exists College;
use College;

create table Teacher(
id INT Primary KEY,
name varchar(50),
subject Varchar(50),
salary INT
);

insert into College.Teacher 
(id, name, subject, salary) 
VALUES 
( 23, "ajay", "math", 50000),
(47, "bharat", "english", 60000),
(18, "chetan", "chemistry", 45000),
(9, "divya", "physics", 75000 );

Select * from teacher;
Select name from College.teacher where salary>=5000;

Alter Table teacher Change column Salary ctc INT;


update teacher set ctc = ctc+ctc*0.25;

alter table teacher add column City Varchar(50) default "Pune";


