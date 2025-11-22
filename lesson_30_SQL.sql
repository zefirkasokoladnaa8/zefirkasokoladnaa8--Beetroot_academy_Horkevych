-- **************************************************************************************
-- Task 1
-- 1. Create table
CREATE TABLE flowers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    color TEXT,
    price INTEGER
);

-- 2. Rename table
ALTER TABLE flowers RENAME TO warehouse;

-- 3. Add column
ALTER TABLE warehouse ADD COLUMN amount INTEGER;

-- 4. Insert rows
INSERT INTO warehouse (name, color, price, amount) VALUES 
('Rose', 'Red', 100, 50),
('Tulip', 'Yellow', 40, 200),
('Orchid', 'White', 300, 10);

-- 5. Update
UPDATE warehouse 
SET price = 120 
WHERE name = 'Rose';

-- 6. Delete
DELETE FROM warehouse 
WHERE name = 'Tulip';

-- ******************************************************************************************
-- Task 2

-- 1. Display names with aliases "First Name", "Last Name"
-- Використовуємо AS для перейменування стовпчиків у виводі
SELECT first_name AS "First Name", last_name AS "Last Name"
FROM employees;

-- 2. Get unique department ID
-- DISTINCT прибирає дублікати, залишаючи лише унікальні ID відділів
SELECT DISTINCT department_id
FROM employees;

-- 3. Get all employee details ordered by first name, descending
-- DESC означає сортування від Z до A (спадання)
SELECT *
FROM employees
ORDER BY first_name DESC;

-- 4. Get names, salary, PF (12% of salary)
-- Ми можемо робити математику прямо в запиті: salary * 0.12
SELECT first_name, last_name, salary, salary * 0.12 AS PF
FROM employees;

-- 5. Get maximum and minimum salary
-- Використовуємо агрегатні функції MAX та MIN
SELECT MAX(salary), MIN(salary)
FROM employees;

-- 6. Get monthly salary (round 2 decimal places)
-- Ділимо річну зарплату на 12 і округлюємо до 2 знаків функцією ROUND
SELECT first_name, last_name, ROUND(salary / 12.0, 2) AS Monthly_Salary
FROM employees;
