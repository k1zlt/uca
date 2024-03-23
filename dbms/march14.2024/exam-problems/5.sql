-- 1. Problem: Write a SQL query to concatenate the `first_name` and `last_name` columns of the `employees` table, separated by a space.
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
);
INSERT INTO employees (first_name, last_name) VALUES 
    ('John', 'Doe'),
    ('Anna', 'Smith'),
    ('Peter', 'Jones');
SELECT first_name || ' ' || last_name FROM employees;
DROP TABLE IF EXISTS numbers;
-- 2. Problem: Write a SQL query to convert the `name` column values of the `products` table to uppercase.
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
INSERT INTO products (name) VALUES 
    ('Apple'),
    ('Banana'),
    ('Orange');
SELECT UPPER(name) FROM products;
DROP TABLE IF EXISTS products;
-- 3. Problem: Write a SQL query to extract the domain name from an email address stored in the `email` column of the `users` table.
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100)
);
INSERT INTO users (email) VALUES 
    ('firuz.azizbekov18@gmail.com'),
    ('firuz.k1zlt@mail.ru'),
    ('firuz.azizbekov_2026@ucentralasia.org');
SELECT SUBSTRING(email, POSITION('@' IN email) + 1) FROM users;
DROP TABLE IF EXISTS users;
-- 4. Problem: Write a SQL query to replace all occurrences of 'Mr.' with 'Ms.' in the `salutation` column of the `customers` table.
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    salutation VARCHAR(100)
);
INSERT INTO customers (salutation) VALUES 
    ('Mr. John Doe'),
    ('Ms. Anna Smith'),
    ('Mr. Peter Jones');
SELECT REPLACE(salutation, 'Mr.', 'Ms.') FROM customers;
DROP TABLE IF EXISTS customers;
-- 5. Problem: Write a SQL query to calculate the length of the `description` column values in the `products` table.
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    description TEXT
);
INSERT INTO products (description) VALUES 
    ('This is a product description.'),
    ('This is another product description.'),
    ('This is a longer product description.');
SELECT LENGTH(description) FROM products;
DROP TABLE IF EXISTS products;
-- 6. Problem: Write a SQL query to pad the `id` column values of the `orders` table with zeros to a length of 5 characters. 
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    order_number INT
);
INSERT INTO orders (order_number) VALUES 
    (123),
    (456),
    (789);
SELECT LPAD(id::TEXT, 5, '0') FROM orders;
DROP TABLE IF EXISTS orders;
-- 7. Problem: Write a SQL query to trim leading and trailing spaces from the `city` column values of the `addresses` table. 
DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100)
);
INSERT INTO addresses (city) VALUES 
    (' New York '),
    (' Los Angeles '),
    (' San Francisco ');
SELECT TRIM(city) FROM addresses;
DROP TABLE IF EXISTS addresses;
-- 8. Problem: Write a SQL query to extract the first 3 characters from the `zipcode` column values of the `addresses` table.
DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
    id SERIAL PRIMARY KEY,
    zipcode VARCHAR(100)
);
INSERT INTO addresses (zipcode) VALUES 
    ('10001'),
    ('90001'),
    ('94101');
SELECT SUBSTRING(zipcode, 0, 4) FROM addresses;
DROP TABLE IF EXISTS addresses;
-- 9. Problem: Write a SQL query to convert the `phone_number` column values of the `contacts` table to a standard format (e.g., '+1-555-123-4567').
DROP TABLE IF EXISTS contacts;
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    phone_number VARCHAR(100),
    result VARCHAR(100)
);
INSERT INTO contacts (phone_number) VALUES 
    ('5551234567'),
    ('555-123-4567'),
    ('+1 (555) 123-4567');
UPDATE contacts SET result = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(phone_number, '(', ''), ')', ''), '-', ''), ' ', ''), '+1', '');
UPDATE contacts SET result = '+1-' || SUBSTRING(result, 1, 3) || '-' || SUBSTRING(result, 4, 3) || '-' || SUBSTRING(result, 7, 4);
SELECT result FROM contacts;
DROP TABLE IF EXISTS contacts;
-- 10.  Problem: Write a SQL query to reverse the `username` column values of the `users` table.
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100)
);
INSERT INTO users (username) VALUES 
    ('john.doe'),
    ('anna.smith'),
    ('peter.jones');
SELECT REVERSE(username) FROM users;
DROP TABLE IF EXISTS users;
-- 11.  Problem: Write a SQL query to extract the last 4 digits from the `credit_card_number` column values of the `payments` table.
DROP TABLE IF EXISTS payments;
CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    credit_card_number VARCHAR(100)
);
INSERT INTO payments (credit_card_number) VALUES 
    ('1234567890123456'),
    ('9876543210987654'),
    ('1111222233334444');
SELECT SUBSTRING(credit_card_number, LENGTH(credit_card_number) - 3) FROM payments;
DROP TABLE IF EXISTS payments;
-- 12.  Problem: Write a SQL query to convert the `title` column values of the `books` table to lowercase.
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100)
);
INSERT INTO books (title) VALUES 
    ('The Great Gatsby'),
    ('To Kill a Mockingbird'),
    ('1984');
SELECT LOWER(title) FROM books;
DROP TABLE IF EXISTS books;
-- 13.  Problem: Write a SQL query to truncate the `notes` column values of the `appointments` table to 50 characters.
DROP TABLE IF EXISTS appointments;
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    notes TEXT
);
INSERT INTO appointments (notes) VALUES 
    ('This is a long note that needs to be truncated.'),
    ('This is another long note that needs to be truncated.'),
    ('This is a short note.');
SELECT SUBSTRING(notes, 0, 50) FROM appointments;
DROP TABLE IF EXISTS appointments;
-- 14.  Problem: Write a SQL query to extract the second word from the `address` column values of the `customers` table.
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    address VARCHAR(100)
);
INSERT INTO customers (address) VALUES 
    ('123 Main Street'),
    ('456 Elm Street'),
    ('789 Oak Street');
SELECT SUBSTRING(address, POSITION(' ' IN address) + 1, POSITION(' ' IN address)) FROM customers;
DROP TABLE IF EXISTS customers;
-- 15.  Problem: Write a SQL query to remove all non-alphabetic characters from the `name` column values of the `students` table.
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
INSERT INTO students (name) VALUES 
    ('John Doe'),
    ('Anna Smith'),
    ('Peter Jones');
SELECT REGEXP_REPLACE(name, '[^a-zA-Z]', '', 'g') FROM students;
DROP TABLE IF EXISTS students;
-- 16.  Problem: Write a SQL query to capitalize the first letter of each word in the `description` column values of the `products` table. 
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    description TEXT
);
INSERT INTO products (description) VALUES 
    ('this is a product description.'),
    ('this is another product description.'),
    ('this is a longer product description.');
SELECT INITCAP(description) FROM products;
DROP TABLE IF EXISTS products;
-- 17.  Problem: Write a SQL query to extract the numeric part from the `version` column values of the `software` table.
DROP TABLE IF EXISTS software;
CREATE TABLE software (
    id SERIAL PRIMARY KEY,
    version VARCHAR(100)
);
INSERT INTO software (version) VALUES 
    ('1.2.3'),
    ('4.5.6'),
    ('7.8.9');
SELECT SUBSTRING(version, POSITION('.' IN version) + 1) FROM software;
DROP TABLE IF EXISTS software;
-- 18.  Problem: Write a SQL query to remove duplicates from the `tags` column values of the `articles` table. 
DROP TABLE IF EXISTS articles;
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    tags VARCHAR(100)
);
INSERT INTO articles (tags) VALUES 
    ('science,science,technology,math,math'),
    ('technology,math,math,math,science'),
    ('math,science,science,technology,technology');
SELECT DISTINCT UNNEST(STRING_TO_ARRAY(tags, ',')) FROM articles;
DROP TABLE IF EXISTS articles;
-- 19.  Problem: Write a SQL query to convert the `url` column values of the `links` table to lowercase.
DROP TABLE IF EXISTS links;
CREATE TABLE links (
    id SERIAL PRIMARY KEY,
    url VARCHAR(100)
);
INSERT INTO links (url) VALUES 
    ('https://www.example.com'),
    ('https://www.example.com/ABOUT'),
    ('https://www.example.com/CONTACT');
SELECT LOWER(url) FROM links;
DROP TABLE IF EXISTS links;
-- 20.  Problem: Write a SQL query to extract the substring between two specified characters (e.g., '[' and ']') from the `comments` column values of the `posts` table.
DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    comments TEXT
);
INSERT INTO posts (comments) VALUES 
    ('[This is a comment]'),
    ('[This is another comment]'),
    ('[This is a longer comment]');
SELECT SUBSTRING(comments, POSITION('[' IN comments) + 1, POSITION(']' IN comments) - POSITION('[' IN comments) - 1) FROM posts;
DROP TABLE IF EXISTS posts;