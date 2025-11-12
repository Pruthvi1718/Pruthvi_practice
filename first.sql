INSERT INTO Customers (customer_id, first_name, last_name, age, country)
VALUES (6, 'Joe', 'Roy', 30, 'USA');

SELECT * FROM Customers;

UPDATE Customers
SET age = 32
WHERE customer_id = 1;

DELETE FROM Customers
WHERE customer_id = 5;

//filter
SELECT * FROM Customers
WHERE country = 'USA';

SELECT * FROM Customers
WHERE age BETWEEN 20 AND 30;

SELECT * FROM Customers
WHERE first_name LIKE 'J%';

SELECT * FROM Customers
WHERE country IN ('UK', 'UAE');

//aggregators
