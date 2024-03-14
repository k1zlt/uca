import psycopg2
from faker import Faker
import random

faker = Faker()

fake_department = ['IT', 'HR', 'Finance', 'Marketing', 'Sales', 'Operations', 'Admin', 'Legal', 'R&D', 'Production']
fake_locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']

db_params = {
    'dbname': 'users',
    'user': 'dbadmin',
    'password': 'password',
    'host': 'localhost',
    'port': '5433'
}

conn = psycopg2.connect(**db_params)
cur = conn.cursor()

with open('main.sql', 'r') as file:
    cur.execute(file.read())
    conn.commit()
    print('Main sql code is executed')

for i in fake_department:
    cur.execute(f"INSERT INTO department (name, location) VALUES ('{i}', '{fake_locations[random.randint(0, len(fake_locations) - 1)]}')")
    conn.commit()

for i in range(100):
    cur.execute(f"INSERT INTO employee (name, email, phone, department_id, salary) VALUES ('{faker.name()}', '{faker.email()}', '{faker.phone_number()}', '{random.randint(1, len(fake_department))}', '{random.randint(10000, 100000)}')")
    conn.commit()

print("Fake data is inserted into the database")