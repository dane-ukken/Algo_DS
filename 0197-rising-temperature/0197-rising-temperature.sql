/* Write your T-SQL query statement below */
select
    t.id
from
    Weather t
    join Weather y ON t.recordDate = DATEADD(day, 1, y.recordDate)
where
    t.temperature > y.temperature