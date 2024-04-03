/* Write your T-SQL query statement below */

SELECT 
    s.user_id, 
    ROUND(AVG(CASE WHEN c.action = 'confirmed' THEN 1.0 ELSE 0.0 END), 2) AS confirmation_rate
FROM 
    Signups AS s 
LEFT JOIN 
    Confirmations AS c 
ON 
    s.user_id = c.user_id 
GROUP BY 
    s.user_id;

/*
select
    s.user_id,
    CASE
        WHEN SUM(t.confirmedCount) IS NULL
        THEN 0
        ELSE CAST(CAST(SUM(t.confirmedCount) AS float)/CAST(SUM(t.timeoutCount + t.confirmedCount) AS float) AS DECIMAL(10, 2))
    END as confirmation_rate   
from
    Signups s
    left join
    (
        select 
            user_id,
            CASE
                WHEN action = 'confirmed'
                THEN 1
                ELSE 0
            END as confirmedCount,
            CASE
                WHEN action = 'timeout'
                THEN 1
                ELSE 0
            END as timeoutCount
        from
            Confirmations
    ) t on t.user_id = s.user_id
group by
    s.user_id
*/
/*
select
    user_id,
    SUM(confirmedCount),
    SUM(timeoutCount)
from
(
    select 
        user_id,
        CASE
            WHEN action = 'confirmed'
            THEN 1
            ELSE 0
        END as confirmedCount,
        CASE
            WHEN action = 'timeout'
            THEN 1
            ELSE 0
        END as timeoutCount
    from
        Confirmations

) t
group by 
    user_id
*/

/*

    select
        s.user_id,
        SUM(t.confirmedCount)/SUM(t.timeoutCount + t.confirmedCount) as confirmation_rate
    from
        Signups s
        join
        (
            select 
                user_id,
                CASE
                    WHEN action = 'confirmed'
                    THEN 1
                    ELSE 0
                END as confirmedCount,
                CASE
                    WHEN action = 'timeout'
                    THEN 1
                    ELSE 0
                END as timeoutCount
            from
                Confirmations
        ) t on t.user_id = s.user_id
    group by
        s.user_id

*/