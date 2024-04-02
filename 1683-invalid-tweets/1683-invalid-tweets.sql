/* Write your T-SQL query statement below */
select
    t.tweet_id
from
    Tweets t
where
    len(t.content) > 15