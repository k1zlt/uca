import psycopg2
import csv

db_params = {
    'dbname': 'users',
    'user': 'dbadmin',
    'password': 'password',
    'host': 'localhost',
    'port': 5433
}

def get_or_insert_country(cur, row):
    check_query = f"SELECT * FROM country WHERE country_name = '{row['Nationality']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    if fo is None:
        insert_query = f"INSERT INTO country (country_name) VALUES ('{row['Nationality']}')"
        cur.execute(insert_query)
        conn.commit()
        country_id = cur.lastrowid
    check_query = f"SELECT * FROM country WHERE country_name = '{row['Nationality']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    country_id = fo[0]
    return country_id

def get_or_insert_sports(cur, row):
    sports = row['Sport'].split(',')
    sport_ids = []
    for sport in sports:
        check_query = f"SELECT * FROM sport WHERE sport_name = '{sport}'"
        cur.execute(check_query)
        fo = cur.fetchone()
        if fo is None:
            insert_query = f"INSERT INTO sport (sport_name) VALUES ('{sport}')"
            cur.execute(insert_query)
            conn.commit()
            sport_id = cur.lastrowid
        check_query = f"SELECT * FROM sport WHERE sport_name = '{sport}'"
        cur.execute(check_query)
        fo = cur.fetchone()
        sport_id = fo[0]
        sport_ids.append(sport_id)
    return sport_ids

def get_or_create_athlete(cur, row):
    check_query = f"SELECT * FROM athlete WHERE name = '{row['Name']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    country_id = get_or_insert_country(cur, row)
    if fo is None:
        if row['Ht'] == '':
            row['Ht'] = '0'
        if row['Wt kg'] == '':
            row['Wt kg'] = '0'
        if "'" in row['Name']:
            row['Name'] = row['Name'].replace("'", '')
        insert_query = f"INSERT INTO athlete (name, age, weight, height, country_id) VALUES ('{row['Name']}', '{row['Age']}', '{row['Wt kg']}', '{row['Ht']}', '{country_id}')"
        cur.execute(insert_query)
        conn.commit()
        athlete_id = cur.lastrowid
    check_query = f"SELECT * FROM athlete WHERE name = '{row['Name']}'"
    cur.execute(check_query)
    fo = cur.fetchone()
    athlete_id = fo[0]
    return athlete_id

def insert_row(cur, row):
    sport_ids = get_or_insert_sports(cur, row)
    athlete_id = get_or_create_athlete(cur, row)

    for sport_id in sport_ids:
        insert_query = f"INSERT INTO SportAthlete (sport_id, athlete_id) VALUES ('{sport_id}', '{athlete_id}')"
    
    cur.execute(insert_query)
    conn.commit()




conn = psycopg2.connect(**db_params)
cur = conn.cursor()

with open('sql code.sql', 'r', encoding='utf-8', errors='replace') as s:
        s = s.read()
        cur.execute(s)
        conn.commit()
        print('Tables are successfully recreated.')

with open('WinterAthletesSampleData - Athletes.csv', 'r', encoding='utf-8', errors='replace') as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)
    for row in reader:
        insert_row(cur, row)

with open('show results.sql', 'r', encoding='utf-8', errors='replace') as s:
    s = s.read()
    cur.execute(s)
    conn.commit()
    print("Done.")


cur.close()
conn.close()