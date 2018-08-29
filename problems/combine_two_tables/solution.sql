# Write your MySQL query statement below
SELECT FirstName, LastName, City, State from Person left join Address on Address.PersonId = Person.PersonId