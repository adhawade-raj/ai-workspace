Create Database if not exists instagram;

use instagram;
Create Table user1 (
id int primary key,
age int,
name varchar(30) NOT NULL,
email varchar(50) unique,
followers int DEFAULT 0,
following int
);

Create Table post(
id int,
content varchar(50),
user_id int,
foreign key (user_id) references user1(id)
);