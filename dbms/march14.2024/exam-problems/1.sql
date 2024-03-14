-- 1. Problem: Write a SQL query to retrieve all records from the `employees` table. 
DROP TABLE IF EXISTS employees CASCADE;
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary int
);
SELECT * FROM employees;
-- 2. Problem: Write a SQL query to insert a new employee record into the `employees` table with values for `name`, `department`, and `salary`.
INSERT INTO employees (name, department, salary) VALUES ('John Doe', 'Sales', 50000);
-- 3. Problem: Write a SQL query to update the `salary` of an employee with `id` 1 to 60000. 
UPDATE TABLE employees SET salary = 60000 WHERE id = 1;
-- 4. Problem: Write a SQL query to delete an employee record from the `employees` table with `id` 2.
INSERT INTO employees (name, department, salary) VALUES ('Jane Doe', 'Marketing', 60000);
DELETE FROM employees WHERE id = 2;
-- 5. Problem: Write a SQL query to retrieve all unique departments from the `employees` table.
SELECT DISTINCT department FROM employees;
-- 6. Problem: Write a SQL query to insert a new record into the `departments` table with values for `name` and `location`.
DROP TABLE IF EXISTS departments CASCADE;
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name TEXT,
    location TEXT
);
INSERT INTO departments (name, location) VALUES ('Sales', 'New York');
-- 7. Problem: Write a SQL query to update the `location` of a department with `id` 1 to 'New Location'.
UPDATE TABLE departments SET location = 'New Location' WHERE id = 1;
-- 8. Problem: Write a SQL query to delete a department record from the `departments` table with `id` 2.
INSERT INTO departments (name, location) VALUES ('Marketing', 'Los Angeles');
DELETE FROM departments WHERE id = 2;
-- 9. Problem: Write a SQL query to retrieve the total number of employees in each department
INSERT INTO employees (name, department, salary) VALUES ('Jane Doe', 'Marketing', 60000);
INSERT INTO employees (name, department, salary) VALUES ('Elon Must', 'IT', 60000);
INSERT INTO employees (name, department, salary) VALUES ('Jenna Doe', 'Sales', 50000);
INSERT INTO employees (name, department, salary) VALUES ('Robert Black', 'Sales', 500000);
SELECT department, COUNT(*) FROM employees GROUP BY department;
-- 10. Problem: Write a SQL query to retrieve the highest salary from the `employees` table.
SELECT MAX(salary) FROM employees;

-- DROPPING ALL THE TABLES
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS departments CASCADE;