/* Write your T-SQL query statement below */

select
    m.name
from
    employee e
    join employee m on e.managerId = m.id
group by
    m.name, m.id    
having
    COUNT(e.id) >= 5