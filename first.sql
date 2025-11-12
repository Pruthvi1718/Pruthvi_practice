--First Sql Code
mysql --version

mysql -u root -p

show databases;

create database Demo;

show databases;

use demo;

create table Student(
    S_id int,
    S_Name VARCHAR(100),
    S_Dept VARCHAR(100),
    S_Section VARCHAR(100)
);

select * from Student;

insert into Student(S_id, S_Name, S_Dept, S_section) 
values(01, 'ARU', 'CS', 'A'),
(02,'BABU','DSA','B'),
(03,'CHARU','EEE','C'),
(04,'DAS','AI','D'),
(05,'FAS','ML','E');

select * from Student;

--Filters
--WHERE
SELECT * FROM Student WHERE S_Dept = 'CS';

--LIKE
SELECT * FROM Student WHERE S_Name LIKE 'C%';

--BETWEEN
SELECT * FROM Student WHERE S_id BETWEEN 2 AND 4;

--IN
SELECT * FROM Student WHERE S_Dept IN ('AI', 'ML');

--Aggregators
--Count
SELECT COUNT(*) AS Total_Students FROM Student;

--Max
SELECT MAX(S_id) AS Max_ID FROM Student;

--Min
SELECT MIN(S_id) AS Min_ID FROM Student;

--Group by
SELECT S_Dept, COUNT(*) AS Dept_Count FROM Student GROUP BY S_Dept;

