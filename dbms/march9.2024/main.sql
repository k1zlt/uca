DROP TABLE IF EXISTS department CASCADE;
CREATE TABLE department (
    department_id SERIAL PRIMARY KEY,
    name TEXT,
    location TEXT
);

DROP TABLE IF EXISTS employee CASCADE;
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name TEXT,
    salary INT,
    department_id INT,
    email TEXT,
    phone TEXT,
    FOREIGN KEY(department_id) REFERENCES department(department_id) ON DELETE CASCADE
);
