-- 1. Beginner: Write a SQL query to retrieve all columns from the `employees` table.
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    salary INT,
    department VARCHAR(100),
    joined_date DATE
);
INSERT INTO employees (name, salary, department) VALUES 
    ('John Doe', 50000, 'Engineering'),
    ('Anna Smith', 60000, 'Marketing'),
    ('Peter Jones', 70000, 'Sales');
SELECT * FROM employees;
-- 2. Beginner: Write a SQL query to retrieve only the `name` and `salary` columns from the `employees` table.
SELECT name, salary FROM employees;
-- 3. Beginner: Write a SQL query to retrieve unique values from the `department` column of the `employees` table.
SELECT DISTINCT department FROM employees;
-- 4. Beginner: Write a SQL query to retrieve all records from the `employees` table sorted by `salary` in descending order.
SELECT * FROM employees ORDER BY salary DESC;
-- 5. Beginner: Write a SQL query to retrieve the first 5 records from the `employees` table.
SELECT * FROM employees LIMIT 5;
-- 6. Intermediate: Write a SQL query to retrieve the total number of employees in each department from the `employees` table.
SELECT department, COUNT(*) FROM employees GROUP BY department;
-- 7. Intermediate: Write a SQL query to retrieve the highest salary from the `employees` table.
SELECT MAX(salary) FROM employees;
-- 8. Intermediate: Write a SQL query to calculate the average salary of all employees in the `employees` table.
SELECT AVG(salary) FROM employees;
-- 9. Intermediate: Write a SQL query to retrieve the top 10% of employees with the highest salary from the `employees` table.
SELECT * FROM employees ORDER BY salary DESC LIMIT (SELECT COUNT(*) / 10 FROM employees);
-- 10. Intermediate: Write a SQL query to retrieve the second highest salary from the `employees` table.
SELECT DISTINCT salary FROM employees ORDER BY salary DESC OFFSET 1 LIMIT 1;
-- 11. Advanced: Write a SQL query to retrieve the names of employees who earn more than the average salary.
SELECT name FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);
-- 12. Advanced: Write a SQL query to retrieve the names of employees who do not belong to any department.
SELECT name FROM employees WHERE department IS NULL;
-- 13. Advanced: Write a SQL query to retrieve the names of employees who have the same salary as the highest salary in the `employees` table.
SELECT name FROM employees WHERE salary = (SELECT MAX(salary) FROM employees);
-- 14. Advanced: Write a SQL query to retrieve the names of employees who have joined before a specific date.
SELECT name FROM employees WHERE joined_date < '2021-01-01';
-- 15. Advanced: Write a SQL query to retrieve the names of employees who have joined after a specific date and have a salary greater than a certain amount.
SELECT name FROM employees WHERE joined_date > '2021-01-01' AND salary > 60000;
-- 16. Expert: Write a SQL query to retrieve the names of employees who have the same salary as the highest salary in their respective departments.
SELECT name FROM employees e1 WHERE salary = (SELECT MAX(salary) FROM employees e2 WHERE e1.department = e2.department);
-- 17. Expert: Write a SQL query to retrieve the names of employees who have duplicate `name` values in the `employees` table.
SELECT name FROM employees GROUP BY name HAVING COUNT(*) > 1;
-- 18. Expert: Write a SQL query to retrieve the names of employees who have a salary greater than the average salary of their respective departments.
SELECT name FROM employees e1 WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e1.department = e2.department);
-- 19. Expert: Write a SQL query to retrieve the names of employees who have the same first letter in their `name` as the department they belong to.
SELECT name FROM employees WHERE LEFT(name, 1) = LEFT(department, 1);
-- 20. Expert: Write a SQL query to retrieve the names of employees who have the same salary as the average salary of their respective departments and have joined after a specific date.
SELECT name FROM employees e1 WHERE salary = (SELECT AVG(salary) FROM employees e2 WHERE e1.department = e2.department) AND joined_date > '2021-01-01';