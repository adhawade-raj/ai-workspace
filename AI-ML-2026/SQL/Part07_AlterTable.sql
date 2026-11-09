alter table user ADD column CITY varchar(50) Default "Pune";
SELECT * from user;

alter table USER Drop column CITY;
SELECT * from user;

Alter table user1 Rename to instaUser;
SELECT * from user1;
SELECT * from instaUser;

ALTER table user change column CITY City  varchar(50) Default "Pune";
SELECT * from user;

Alter Table user modify followers INT Default 10;
insert into user (id, name, email, following, city) values (6, 'Sanket', 'sanket@gmail.com', 512, 'Mumbai');


-- Truncate Table
Select * from instaUser;
Drop table Post;
Truncate table instaUser;
Select * from Post;
Select * from instaUser;