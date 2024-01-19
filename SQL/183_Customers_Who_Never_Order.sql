-- Description
-- LeetCode solution to 183. Customers Who Never Order

-- @author: Jw

SELECT Customers.name AS Customers
FROM Customers
LEFT JOIN Orders ON Customers.id = Orders.customerId
-- Select name of customers where their Order customerId is NULL
WHERE Orders.CustomerId IS NULL;