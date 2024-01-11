-- Description
-- LeetCode solution to 175. Combine Two Tables

-- @author: Jw


# Write your MySQL query statement below
SELECT Person.firstName, Person.lastName, Address.city, Address.state FROM Person
-- LEFT JOIN bcuz some cities, state are NULL. We want to include all Person's details
LEFT JOIN Address ON Address.personId = Person.personId;
-- Can use USING(personId)