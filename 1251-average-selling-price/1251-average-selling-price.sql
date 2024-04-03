/* Write your T-SQL query statement below */
select
    p.product_id,
    ROUND(
        CASE
            WHEN SUM(us.units) IS NULL
            THEN 0.00
            ELSE CAST(SUM(p.price * us.units) AS FLOAT) / CAST(SUM(us.units) AS FLOAT)
        END
    , 2) 
    AS average_price
        
from
    Prices p
    LEFT JOIn UnitsSold us 
        ON p.product_id = us.product_id 
        AND us.purchase_date >= p.start_date
        AND us.purchase_date <= p.end_date
GROUP BY
    p.product_id