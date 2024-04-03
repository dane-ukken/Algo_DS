/* Write your T-SQL query statement below */

WITH SalaryRanking AS
(
    SELECT
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rank
    FROM
        Employee e
        JOIN Department d ON e.departmentId = d.id
)
SELECT
    Department, Employee, Salary
 FROM
    SalaryRanking
WHERE rank <=3

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