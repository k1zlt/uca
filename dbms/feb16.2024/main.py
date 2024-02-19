import psycopg2
import csv


def get_or_insert_job(cur, row):
    check_query = f"SELECT * FROM job WHERE job_title = '{row['Job Title']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    if fo is None:
        insert_query = f"INSERT INTO job (job_title) VALUES ('{row['Job Title']}')"
        cur.execute(insert_query)
        conn.commit()
    check_query = f"SELECT * FROM job WHERE job_title = '{row['Job Title']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    job_id = fo[0]
    return job_id

def get_or_insert_department(cur, row):
    check_query = f"SELECT * FROM department WHERE department_name = '{row['Department']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    if fo is None:
        insert_query = f"INSERT INTO department (department_name) VALUES ('{row['Department']}')"
        cur.execute(insert_query)
        conn.commit()
    check_query = f"SELECT * FROM department WHERE department_name = '{row['Department']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    department_id = fo[0]
    return department_id

def get_or_insert_business_unit(cur, row):
    check_query = f"SELECT * FROM business_unit WHERE business_unit_name = '{row['Business Unit']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    if fo is None:
        insert_query = f"INSERT INTO business_unit (business_unit_name) VALUES ('{row['Business Unit']}')"
        cur.execute(insert_query)
        conn.commit()
    check_query = f"SELECT * FROM business_unit WHERE business_unit_name = '{row['Business Unit']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    business_unit_id = fo[0]
    return business_unit_id

def get_or_insert_ethnicity(cur, row):
    check_query = f"SELECT * FROM ethnicity WHERE ethnicity_name = '{row['Ethnicity']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    if fo is None:
        insert_query = f"INSERT INTO ethnicity (ethnicity_name) VALUES ('{row['Ethnicity']}')"
        cur.execute(insert_query)
        conn.commit()
    check_query = f"SELECT * FROM ethnicity WHERE ethnicity_name = '{row['Ethnicity']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    ethnicity_id = fo[0]
    return ethnicity_id

def get_or_insert_country(cur, row):
    check_query = f"SELECT * FROM country WHERE country_name = '{row['Country']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    if fo is None:
        insert_query = f"INSERT INTO country (country_name) VALUES ('{row['Country']}')"
        cur.execute(insert_query)
        conn.commit()
        country_id = cur.lastrowid
        print(f"Inserted {row['Country']} into country table")
    check_query = f"SELECT * FROM country WHERE country_name = '{row['Country']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    country_id = fo[0]
    return country_id

def get_or_insert_location(cur, row):
    check_query = f"SELECT * FROM location WHERE city = '{row['City']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    if fo is None:
        country_id = get_or_insert_country(cur, row)
        insert_query = f"INSERT INTO location (city, country) VALUES ('{row['City']}', '{country_id}')"
        cur.execute(insert_query)
        conn.commit()
    check_query = f"SELECT * FROM location WHERE city = '{row['City']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    location_id = fo[0]
    return location_id


def insert_row(cur, row):
    eeid = row['EEID']
    full_name = row['Full Name']
    job_id = get_or_insert_job(cur, row)
    department_id = get_or_insert_department(cur, row)
    business_unit_id = get_or_insert_business_unit(cur, row)
    gender = row['Gender']
    ethnicity = get_or_insert_ethnicity(cur, row)
    age = row['Age']
    hire_date = row['Hire Date']
    annual_salary = row['Annual Salary'][1:].replace(',', '.')
    bonus = row['Bonus %'].replace('%', '')
    location_id = get_or_insert_location(cur, row)
    exit_date = row['Exit Date']

    if exit_date == '':
        exit_date = None
    
    check_query = f"SELECT * FROM employee WHERE eeid = '{eeid}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    if fo is not None:
        print(f"{eeid} already exists in employee table")
        return
    insert_query = f"INSERT INTO employee (eeid, full_name, job_id, department_id, business_unit_id, gender, ethnicity_id, age, hire_date, annual_salary, bonus, location_id, exit_date) VALUES ('{eeid}', '{full_name}', '{job_id}', '{department_id}', '{business_unit_id}', '{gender}', '{ethnicity}', '{age}', '{hire_date}', '{annual_salary}', '{bonus}', '{location_id}', '{exit_date}')"
    if exit_date is None:
        insert_query = f"INSERT INTO employee (eeid, full_name, job_id, department_id, business_unit_id, gender, ethnicity_id, age, hire_date, annual_salary, bonus, location_id, exit_date) VALUES ('{eeid}', '{full_name}', '{job_id}', '{department_id}', '{business_unit_id}', '{gender}', '{ethnicity}', '{age}', '{hire_date}', '{annual_salary}', '{bonus}', '{location_id}', NULL)"

    cur.execute(insert_query)
    conn.commit()


db_params = {
    'dbname': 'users',
    'user': 'dbadmin',
    'password': 'password',
    'host': 'localhost',
    'port': 5433
}

conn = psycopg2.connect(**db_params)
cur = conn.cursor()

with open('Employee Sample Data.csv', 'r', encoding='utf-8', errors='replace') as f:
    with open('sql table for problem 2 dbms', 'r', encoding='utf-8', errors='replace') as s:
        s = s.read()
        cur.execute(s)
        conn.commit()
    reader = csv.DictReader(f)
    print(reader.fieldnames)
    for row in reader:
        insert_row(cur, row)

cur.close()
conn.close()
