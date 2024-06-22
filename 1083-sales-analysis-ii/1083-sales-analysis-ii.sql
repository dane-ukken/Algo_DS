/* Write your T-SQL query statement below */


(
SELECT DISTINCT
    s.buyer_id
FROM
    Sales s
WHERE
    s.product_id = (SELECT product_id from Product WHERE product_name = 'S8')
)
EXCEPT
(
SELECT DISTINCT
    s.buyer_id
FROM
    Sales s
WHERE
    s.product_id = (SELECT product_id from Product WHERE product_name = 'iPhone')
)