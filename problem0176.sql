select max(Salary) as SecondHighestSalary from 
(select Salary from Employee where Salary not in (select max(Salary) from Employee)) X
