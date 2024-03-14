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
DROP TABLE 

-- 9. Intermediate: Given a table `students_courses` with columns `student_id`, `course_id`, `course_name`, `credits`, and `instructor`, identify the potential partial dependencies.

 

-- 10. Intermediate: Convert the table `students_courses` described above to third normal form (3NF).

 

-- 11. Advanced: Given a table `customers_orders` with columns `customer_id`, `order_id`, `order_date`, `product_id`, `product_name`, `quantity`, and `total_price`, identify the transitive dependencies.

 

-- 12. Advanced: Convert the table `customers_orders` described above to third normal form (3NF).

 

-- 13. Advanced: Given a table `books_authors` with columns `book_id`, `title`, `author_id`, `author_name`, and `author_bio`, identify the potential partial dependencies.

 

-- 14. Advanced: Convert the table `books_authors` described above to third normal form (3NF).

 

-- 15. Advanced: Given a denormalized table `invoices` with columns `invoice_id`, `customer_name`, `customer_address`, `customer_phone`, `order_id`, `order_date`, `product_id`, `product_name`, `quantity`, and `total_price`, identify the functional dependencies.

 

-- 16. Advanced: Convert the table `invoices` described above to third normal form (3NF).

 

-- 17. Expert: Given a table `university_courses` with columns `course_id`, `course_name`, `instructor`, `department_id`, `department_name`, `building`, and `room_number`, identify the functional dependencies.

 

-- 18. Expert: Convert the table `university_courses` described above to third normal form (3NF).

 

-- 19. Expert: Given a denormalized table `employees_projects` with columns `employee_id`, `employee_name`, `project_id`, `project_name`, `start_date`, and `end_date`, identify the functional dependencies.



-- 20. Expert: Convert the table `employees_projects` described above to third normal form (3NF).

