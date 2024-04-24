-- Randomness
-- Write a SQL query to select a random record from the `products` table. Create Products table with random records.
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2)
);
INSERT INTO products (name, price) VALUES ('Apple', 1.00);
INSERT INTO products (name, price) VALUES ('Banana', 0.50);
INSERT INTO products (name, price) VALUES ('Cherry', 2.00);
INSERT INTO products (name, price) VALUES ('Date', 3.00);
INSERT INTO products (name, price) VALUES ('Elderberry', 4.00);
INSERT INTO products (name, price) VALUES ('Fig', 5.00);
INSERT INTO products (name, price) VALUES ('Grape', 6.00);
INSERT INTO products (name, price) VALUES ('Honeydew', 7.00);
INSERT INTO products (name, price) VALUES ('Jackfruit', 8.00);

SELECT * FROM products ORDER BY RANDOM() LIMIT 1;
-- Write a SQL query to generate a random IP address.
SELECT CONCAT(
    ROUND(RANDOM() * 256), '.', 
    ROUND(RANDOM() * 256), '.', 
    ROUND(RANDOM() * 256), '.', 
    ROUND(RANDOM() * 256)
) AS ip_address;
-- Write a SQL query to generate a random email address.
SELECT CONCAT(
    SUBSTRING('abcdefghijklmnopqrstuvwxyz', CAST(FLOOR(RANDOM() * 26) + 1 as INTEGER), 1),
    SUBSTRING('abcdefghijklmnopqrstuvwxyz0123456789', CAST(FLOOR(RANDOM() * 26) + 1 as INTEGER), 1),
    SUBSTRING('abcdefghijklmnopqrstuvwxyz0123456789', CAST(FLOOR(RANDOM() * 26) + 1 as INTEGER), 1),
    SUBSTRING('abcdefghijklmnopqrstuvwxyz0123456789', CAST(FLOOR(RANDOM() * 26) + 1 as INTEGER), 1),
    SUBSTRING('abcdefghijklmnopqrstuvwxyz0123456789', CAST(FLOOR(RANDOM() * 26) + 1 as INTEGER), 1),
    SUBSTRING('abcdefghijklmnopqrstuvwxyz0123456789', CAST(FLOOR(RANDOM() * 26) + 1 as INTEGER), 1),
    SUBSTRING('abcdefghijklmnopqrstuvwxyz0123456789', CAST(FLOOR(RANDOM() * 26) + 1 as INTEGER), 1),
    SUBSTRING('abcdefghijklmnopqrstuvwxyz0123456789', CAST(FLOOR(RANDOM() * 26) + 1 as INTEGER), 1),
    '@',
    SUBSTRING('abcdefghijklmnopqrstuvwxyz', CAST(FLOOR(RANDOM() * 26) + 1 as INTEGER), 1),
    SUBSTRING('abcdefghijklmnopqrstuvwxyz', CAST(FLOOR(RANDOM() * 26) + 1 as INTEGER), 1),
    SUBSTRING('abcdefghijklmnopqrstuvwxyz', CAST(FLOOR(RANDOM() * 26) + 1 as INTEGER), 1),
    SUBSTRING('abcdefghijklmnopqrstuvwxyz', CAST(FLOOR(RANDOM() * 26) + 1 as INTEGER), 1),
    '.com'
) AS email;
-- Write a SQL query to generate a random price between a 50,000 and 65,000 value.
SELECT ROUND((RANDOM() * (65000 - 50000) + 50000) * 100) / 100 AS price;
-- Write a SQL query to generate a random latitude and longitude.
SELECT 
    ROUND((RANDOM() * 180 - 90) * 1000000) / 1000000 AS latitude, 
    ROUND((RANDOM() * 360 - 180) * 1000000) / 1000000 AS longitude;
