select d.Name as Department, e.Name as Employee, e.Salary
from Employee e inner join Department D on e.DepartmentId = d.Id
inner join 
(select max(Salary) as Salary, DepartmentId from Employee group by DepartmentID) as x
on e.Salary = x.Salary and e.DepartmentId = x.DepartmentId
