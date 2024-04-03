/* Write your T-SQL query statement below */

WITH SalaryRanking AS
(
    SELECT
        salary,
        departmentId, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rank
    FROM
        Employee
)
SELECT
    d.name as Department,
    e.name as Employee,
    e.salary as Salary
 FROM
    Employee e
    JOIN Department d ON e.departmentId = d.id
    JOIN SalaryRanking sr ON sr.departmentId = d.id and sr.salary = e.salary
WHERE  
    sr.rank <=3
GROUP BY
    d.name, e.name, e.salary

/*
SELECT
    d.name as Department,
    e.name as Employee,
    e.salary as Salary
FROM
    Employee e
    JOIN Department d ON e.departmentId = d.id
WHERE
    e.salary IN (
        SELECT
            TOP 3 DISTINCT salary
        FROM
            Employee
        GROUP BY departmentId
    )
*/