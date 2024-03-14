-- 1. Beginner: Write a SQL query to create a table `students` with a primary key `student_id`.
DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name TEXT,
    age INT
);
-- 2. Beginner: Write a SQL query to add a primary key `product_id` to an existing table `products`.
DROP TABLE IF EXISTS products CASCADE;
CREATE TABLE products (
    name TEXT,
    dateofmanufacture TIMESTAMP DEFAULT NOW()
);

ALTER TABLE products ADD COLUMN product_id SERIAL PRIMARY KEY;
-- 3. Beginner: Write a SQL query to create a table `books` with a composite primary key `isbn` and `edition`.
DROP TABLE IF EXISTS books CASCADE;
CREATE TABLE books (
    name TEXT,
    edition TEXT,
    isbn TEXT,
    PRIMARY KEY(isbn, edition)
);
-- 4. Beginner: Write a SQL query to add a foreign key `department_id` to an existing table `employees` referencing the `id` column of the `departments` table.
DROP TABLE IF EXISTS departments CASCADE;
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name TEXT
);

DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT
);

ALTER TABLE employees ADD COLUMN department_id INT REFERENCES departments(id);
-- 5. Beginner: Write a SQL query to create a table `orders` with a primary key `order_id` and a foreign key `customer_id` referencing the `id` column of the `customers` table.
DROP TABLE IF EXISTS customers CASCADE;
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT
);
DROP TABLE IF EXISTS orders CASCADE;
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id)
);

-- 6. Intermediate: Write a SQL query to add a unique constraint on the `email` column of the `users` table.
DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    unique (email)
);
-- 7. Intermediate: Write a SQL query to add a composite unique constraint on the `first_name` and `last_name` columns of the `employees` table.
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    unique(first_name, last_name)
);
-- 8. Intermediate: Write a SQL query to create a table `transactions` with a primary key `transaction_id` and a foreign key `product_id` referencing the `id` column of the `products` table.
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT
);

DROP TABLE IF EXISTS transactions CASCADE;
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id)
);
-- 9. Intermediate: Write a SQL query to add a unique constraint on the `isbn` column of the `books` table.
DROP TABLE IF EXISTS books CASCADE;
CREATE TABLE books (
    name TEXT,
    isbn TEXT,
    unique(isbn)
);
-- 10. Intermediate: Write a SQL query to create a table `invoices` with a primary key `invoice_id` and a foreign key `order_id` referencing the `id` column of the `orders` table.
DROP TABLE IF EXISTS orders CASCADE;
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    name TEXT
);

DROP TABLE IF EXISTS invoices CASCADE;
CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id)
);
-- 11. Advanced: Write a SQL query to add a check constraint to the `age` column of the `students` table to ensure that the age is greater than 18.
DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT,
    age int,
    CHECK (AGE >= 18)
);
-- 12. Advanced: Write a SQL query to create a table `sales` with a primary key `sale_id` and a foreign key `customer_id` referencing the `id` column of the `customers` table, and a foreign key `product_id` referencing the `id` column of the `products` table.
DROP TABLE IF EXISTS products CASCADE;
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT
);

DROP TABLE IF EXISTS customers CASCADE;
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT
);

DROP TABLE IF EXISTS sales CASCADE;
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    customer_id int REFERENCES customers(id),
    product_id int REFERENCES products(id)
);
-- 13. Advanced: Write a SQL query to add a check constraint to the `salary` column of the `employees` table to ensure that the salary is greater than 0.
DROP TABLE IF EXISTS employees CASCADE;
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT,
    salary int,
    CHECK (salary > 0)
);
-- 14. Advanced: Write a SQL query to create a table `payments` with a primary key `payment_id` and a foreign key `order_id` referencing the `id` column of the `orders` table, and a foreign key `customer_id` referencing the `id` column of the `customers` table.
DROP TABLE IF EXISTS customers CASCADE;
CREATE TABLE customers (
    id SERIAL primary key,
    name TEXT
);

DROP TABLE IF EXISTS orders CASCADE;
CREATE TABLE orders (
    id SERIAL PRIMARY key,
    name TEXT
);

DROP TABLE IF EXISTS payments CASCADE;
CReate Table payments (
    id serial primary key,
    order_id int REFERENCES orders(id),
    customer_id int REFERENCES customers(id)
);
-- 15. Advanced: Write a SQL query to add a check constraint to the `quantity` column of the `products` table to ensure that the quantity is greater than or equal to 0.
DROP TABLE IF EXISTS products CASCADE;
create table products (
    id serial primary key,
    name TEXT,
    quantity int,
    check (quantity >= 0)
);
-- 16. Expert: Write a SQL query to create a table `reviews` with a primary key `review_id` and a foreign key `product_id` referencing the `id` column of the `products` table, and a foreign key `customer_id` referencing the `id` column of the `customers` table, and a check constraint to ensure that the rating is between 1 and 5. 
DROP TABLE if EXISTS customers CASCADE;
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT
);
DROP TABLE IF EXISTS products CASCADE;
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT
);
DROP TABLE IF EXISTS reviews CASCADE;
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    customer_id INT REFERENCES customers(id),
    rating INT,
    CHECK (rating BETWEEN 1 AND 5)
);
-- 17. Expert: Write a SQL query to add a check constraint to the `total_amount` column of the `orders` table to ensure that the total amount is greater than 0.
DROP TABLE IF EXISTS orders CASCADE;
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    total_amount INT
);
ALTER TABLE orders ADD CHECK (total_amount > 0);
-- 18. Expert: Write a SQL query to create a table `subscriptions` with a primary key `subscription_id` and a foreign key `customer_id` referencing the `id` column of the `customers` table, and a foreign key `product_id` referencing the `id` column of the `products` table, and a check constraint to ensure that the start date is before the end date.
DROP TABLE IF EXISTS customers CASCADE;
CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    name TEXT
);

DROP TABLE IF EXISTS products CASCADE;
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT
);

DROP TABLE IF EXISTS subscriptions CASCADE;
CREATE TABLE subscriptions (
    id SERIAL PRIMARY KEY,
    customer_id int REFERENCES customers(id),
    product_id int REFERENCES products(id),
    start_date DATE,
    end_date DATE,
    CHECK (start_date < end_date)
);
-- 19. Expert: Write a SQL query to add a check constraint to the `quantity` column of the `order_details` table to ensure that the quantity is greater than 0.
DROP TABLE IF EXISTS order_details CASCADE;
CREATE TABLE order_details (
    id SERIAL PRIMARY KEY,
    quantity int,
    CHECK (quantity >= 0)
);
-- 20. Expert: Write a SQL query to create a table `attendances` with a primary key `attendance_id` and a foreign key `student_id` referencing the `id` column of the `students` table, and a foreign key `class_id` referencing the `id` column of the `classes` table, and a check constraint to ensure that the attendance status is either 'Present' or 'Absent'.
DROP TABLE IF EXISTS classes CASCADE;
CREATE TABLE classes (
    id serial primary key,
    name TEXT
);

DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students (
    id serial primary key,
    name text
);

drop table if EXISTS attendances CASCADE;
create table attendances (
    id serial primary key,
    name text,
    student_id int REFERENCES students(id),
    class_id int REFERENCES classes(id),
    status text,
    check (status = 'Present' OR status = 'Absent')
);

-- DROPPING ALL TABLES
DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS artist CASCADE;
DROP TABLE IF EXISTS attendances CASCADE;
DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS category CASCADE;
DROP TABLE IF EXISTS classes CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS departments CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS invoices CASCADE;
DROP TABLE IF EXISTS iso CASCADE;
DROP TABLE IF EXISTS order_details CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS payments CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS region CASCADE;
DROP TABLE IF EXISTS reviews CASCADE;
DROP TABLE IF EXISTS sales CASCADE;
DROP TABLE IF EXISTS state CASCADE;
DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS subscriptions CASCADE;
DROP TABLE IF EXISTS track CASCADE;
DROP TABLE IF EXISTS track_raw CASCADE;
DROP TABLE IF EXISTS tracktoartist CASCADE;
DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS unesco CASCADE;
DROP TABLE IF EXISTS unesco_raw CASCADE;
