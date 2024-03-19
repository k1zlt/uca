-- Problems
-- 1. Beginner: Write a SQL query to calculate the square root of a number.
DROP TABLE IF EXISTS numbers;
CREATE TABLE numbers (
    id SERIAL PRIMARY KEY,
    a INT,
    b INT,
    c float,
    result INT
);

INSERT INTO numbers (a, b) VALUES (4, NULL);
UPDATE numbers SET result = SQRT(a) WHERE id = 1;
-- 2. Beginner: Write a SQL query to calculate the absolute value of a number.
INSERT INTO numbers (a, b) VALUES (-4, NULL);
UPDATE numbers SET result = ABS(a) WHERE id = 2;
-- 3. Beginner: Write a SQL query to calculate the ceiling of a number (round up to the nearest integer).
INSERT INTO numbers (c, b) VALUES (4.1, NULL);
UPDATE numbers SET result = CEIL(c) WHERE id = 3;
-- 4. Beginner: Write a SQL query to calculate the floor of a number (round down to the nearest integer).
INSERT INTO numbers (c, b) VALUES (4.1, NULL);
UPDATE numbers SET result = FLOOR(c) WHERE id = 4;
-- 5. Beginner: Write a SQL query to calculate the power of a number (e.g., 2 raised to the power of 3).
INSERT INTO numbers (a, b) VALUES (2, 3);
UPDATE numbers SET result = POW(a, b) WHERE id = 5;
-- 6. Intermediate: Write a SQL query to calculate the average of a set of numbers.
INSERT INTO numbers (a) VALUES 
    (1),
    (2),
    (3),
    (4),
    (5),
    (6),
    (7),
    (8),
    (9),
    (10);
SELECT AVG(a) FROM numbers;
-- 7. Intermediate: Write a SQL query to calculate the sum of a set of numbers.
SELECT SUM(a) FROM numbers;
-- 8. Intermediate: Write a SQL query to calculate the minimum value in a set of numbers.
SELECT MIN(a) FROM numbers;
-- 9. Intermediate: Write a SQL query to calculate the maximum value in a set of numbers.
SELECT MAX(a) FROM numbers;
-- 10. Intermediate: Write a SQL query to calculate the standard deviation of a set of numbers.
SELECT STDDEV(a) FROM numbers;
-- 11. Advanced: Write a SQL query to calculate the factorial of a number.
UPDATE numbers SET result = factorial(a) where a > 0;
SELECT a, result FROM numbers order by a;
-- 12. Advanced: Write a SQL query to calculate the logarithm of a number.
SELECT LOG(a) FROM numbers where a > 0;
-- 13. Advanced: Write a SQL query to calculate the trigonometric sine of an angle.
SELECT SIN(90);
-- 14. Advanced: Write a SQL query to calculate the trigonometric cosine of an angle.
SELECT COS(90);
-- 15. Advanced: Write a SQL query to calculate the trigonometric tangent of an angle.
SELECT TAN(90);
-- 16. Expert: Write a SQL query to calculate the hyperbolic sine of a number.
SELECT SINH(90);
-- 17. Expert: Write a SQL query to calculate the hyperbolic cosine of a number.
SELECT COSH(90);
-- 18. Expert: Write a SQL query to calculate the hyperbolic tangent of a number.
SELECT TANH(90);
-- 19. Expert: Write a SQL query to calculate the greatest common divisor (GCD) of two numbers.
SELECT GCD(4, 6);
-- 20. Expert: Write a SQL query to calculate the least common multiple (LCM) of two numbers
SELECT LCM(4, 6);
