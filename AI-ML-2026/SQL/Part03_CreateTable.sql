Create Database if not exists instagram;

use instagram;
Create Table user (
id int,
age int,
name varchar(30) NOT NULL,
email varchar(50) unique,
followers int DEFAULT 0,
following int,
CONSTRAINT age_check CHECK(age>=13)
);