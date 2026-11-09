update user set followers=600 where age =14;
set sql_safe_updates=0;

select * from user;

-- Delete tabel
delete from user where age=13;