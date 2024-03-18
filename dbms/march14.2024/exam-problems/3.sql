-- 1. Beginner: Given a table `students` with columns `student_id`, `name`, `address`, `phone_number`, and `email`, identify which normal form it currently satisfies.
-- None
-- 2. Beginner: Convert the table `students` described above to first normal form (1NF).
DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students(
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(125),
    last_name VARCHAR(125),
    address TEXT,
    phone_number TEXT,
    email VARCHAR(256)
);
-- 3. Beginner: Given a table `products` with columns `product_id`, `name`, `category`, `price`, and `supplier`, identify which normal form it currently satisfies.
-- 1NF
-- 4. Beginner: Convert the table `products` described above to second normal form (2NF).
DROP TABLE IF EXISTS supplier CASCADE;
CREATE TABLE supplier (
    id SERIAL PRIMARY KEY,
    name VARCHAR(256)
);

DROP TABLE IF EXISTS category CASCADE;
CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(125)
);

DROP TABLE IF EXISTS products CASCADE;
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category_id int REFERENCES category(id),
    price int,
    supplier_id int REFERENCES supplier(id)
);
-- 5. Beginner: Given a table `orders` with columns `order_id`, `customer_id`, `product_id`, `quantity`, and `total_price`, identify which normal form it currently satisfies.
-- 2NF
-- 6. Beginner: Convert the table `orders` described above to third normal form (3NF).
DROP TABLE IF EXISTS order CASCADE;
CREATE TABLE order (
    id serial primary key,
    customer_id int
);

DROP TABLE IF EXISTS order_details CASCADE;
CREATE TABLE order_details (
    id SERIAL PRIMARY KEY,
    product_id int,
    quantity int,
    total_price int
);
-- 7. Intermediate: Given a denormalized table `employees` with columns `employee_id`, `name`, `department`, and `manager_name`, identify the functional dependencies.
-- manager_name belongs to manager which belongs to department
-- 8. Intermediate: Convert the table `employees` described above to third normal form (3NF).
DROP TABLE IF EXISTS department CASCADE;
CREATE TABLE department (
    department_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    manager_name VARCHAR(255)
);

DROP TABLE IF EXISTS employees CASCADE;
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    department_id int REFERENCES department(department_id)
);

-- 9. Intermediate: Given a table `students_courses` with columns `student_id`, `course_id`, `course_name`, `credits`, and `instructor`, identify the potential partial dependencies.
-- course_id - course_name
-- 10. Intermediate: Convert the table `students_courses` described above to third normal form (3NF).
DROP TABLE IF EXISTS course CASCADE;
CREATE TABLE course (
    course_id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

DROP TABLE IF EXISTS students_courses CASCADE;
CREATE TABLE students_courses (
    student_id int,
    course_id int REFERENCES course(course_id),
    credits int,
    instructor VARCHAR(255)
);

-- 11. Advanced: Given a table `customers_orders` with columns `customer_id`, `order_id`, `order_date`, `product_id`, `product_name`, `quantity`, and `total_price`, identify the transitive dependencies.
-- order_id - order_date
-- product_id - product_name
-- 12. Advanced: Convert the table `customers_orders` described above to third normal form (3NF).
DROP TABLE IF EXISTS order CASCADE;
CREATE TABLE order (
    id SERIAL PRIMARY KEY,
    customer_id int,
    order_date DATE
);

DROP TABLE IF EXISTS product CASCADE;
CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

DROP TABLE IF EXISTS customers_orders CASCADE;
CREATE TABLE customers_orders (
    order_id int REFERENCES order(id),
    product_id int REFERENCES product(product_id),
    quantity int,
    total_price int
);
-- 13. Advanced: Given a table `books_authors` with columns `book_id`, `title`, `author_id`, `author_name`, and `author_bio`, identify the potential partial dependencies.
-- author_id - author_name, author_bio
-- book_id - title
-- 14. Advanced: Convert the table `books_authors` described above to third normal form (3NF).
DROP TABLE IF EXISTS author CASCADE;
CREATE TABLE author (
    author_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    bio TEXT
);

DROP TABLE IF EXISTS book CASCADE;
CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255)
);

DROP TABLE IF EXISTS books_authors CASCADE;
CREATE TABLE books_authors (
    book_id int REFERENCES book(book_id),
    author_id int REFERENCES author(author_id)
);
 

-- 15. Advanced: Given a denormalized table `invoices` with columns `invoice_id`, `customer_name`, `customer_address`, `customer_phone`, `order_id`, `order_date`, `product_id`, `product_name`, `quantity`, and `total_price`, identify the functional dependencies.
-- customer_name - customer_address, customer_phone
-- order_id - order_date, customer_id, product_id
-- product_id - product_name
-- 16. Advanced: Convert the table `invoices` described above to third normal form (3NF).
DROP TABLE IF EXISTS customer CASCADE;
CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address TEXT,
    phone_number TEXT
);

DROP TABLE IF EXISTS order CASCADE;
CREATE TABLE order (
    id SERIAL PRIMARY KEY,
    customer_id int REFERENCES customer(customer_id),
    product_id int REFERENCES product(product_id),
    order_date DATE,
    quantity int,
    total_price int
);

DROP TABLE IF EXISTS product CASCADE;
CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

DROP TABLE IF EXISTS invoices CASCADE;
CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,
    order_id int REFERENCES order(id),
);
 

-- 17. Expert: Given a table `university_courses` with columns `course_id`, `course_name`, `instructor`, `department_id`, `department_name`, `building`, and `room_number`, identify the functional dependencies.
-- department_id - department_name, building
-- course_id - course_name, instructor
-- 18. Expert: Convert the table `university_courses` described above to third normal form (3NF).
DROP TABLE IF EXISTS department CASCADE;
CREATE TABLE department (
    department_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    building VARCHAR(255)
);

DROP TABLE IF EXISTS course CASCADE;
CREATE TABLE course (
    course_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    instructor VARCHAR(255),
    department_id int REFERENCES department(department_id)
);

DROP TABLE IF EXISTS university_courses CASCADE;
CREATE TABLE university_courses (
    course_id int REFERENCES course(course_id),
    department_id int REFERENCES department(department_id),
    room_number int
);
-- 19. Expert: Given a denormalized table `employees_projects` with columns `employee_id`, `employee_name`, `project_id`, `project_name`, `start_date`, and `end_date`, identify the functional dependencies.
-- employee_id - employee_name
-- project_id - project_name, start_date, end_date
-- 20. Expert: Convert the table `employees_projects` described above to third normal form (3NF).
DROP TABLE IF EXISTS employee CASCADE;
CREATE TABLE employee (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

DROP TABLE IF EXISTS project CASCADE;
CREATE TABLE project (
    project_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    start_date DATE,
    end_date DATE
);

DROP TABLE IF EXISTS employees_projects CASCADE;
CREATE TABLE employees_projects (
    employee_id int REFERENCES employee(employee_id),
    project_id int REFERENCES project(project_id)
);