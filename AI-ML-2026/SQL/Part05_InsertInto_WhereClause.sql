insert into user
(id, age, name, email, followers, following)
values
(1,14, "adam", "adam@yahoo", 123, 145),
(2,16, "steve", "steveid@yahoo", 402, 201);

select id, name from user;
select * from user;
select distinct(age) from user;
select * from user where age >=15;

Select age, followers from user where age >=15;
Select age, followers from user where age Between 15 AND 16;

Select age, email from user where email IN("adam@yahoo", "raj@gmail.com");
Select age, email from user where age IN(14,16);

Select age, email from user where age NOT IN(14,16);

Select age, email from user where age!=14 Limit 2;

Select name, age, followers from user Order BY followers ASC;
Select name, age, followers from user Order BY followers DESC;

select max(followers) from user;
select min(followers) from user;
select count(age) from user where age>=20;
select sum(followers) from user;

-- Group by
select age, count(id) from user GROUP BY age;

-- Having clause
select age, count(id) from user GROUP BY age Having max(followers)>500;



