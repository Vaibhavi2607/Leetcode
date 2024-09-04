# Write your MySQL query statement below
select customer_id, count(v.visit_id) as count_no_trans 
from Visits v
left join Transactions t ON v.visit_id = t.visit_id
WHERE transaction_id is NULL
GROUP BY customer_id