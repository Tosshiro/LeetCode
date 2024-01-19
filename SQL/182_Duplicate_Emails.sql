-- Description
-- LeetCode solution to 182. Duplicate Emails

-- @author: Jw

SELECT email
FROM Person AS Email
GROUP BY email
-- HAVING applys condition, in this case whether there are duplicated emails
HAVING COUNT(*) > 1;