# QUIZ

## Files

1. diagram.png - is visual representation of the the database

2. sql code.sql - is the sql code to recreate the database

3. README.md - is the file you are reading now

4. WinterAthletesSampleData.csv - is the sample data for the database

5. load.py - is the python script to load the data into the database

6. requirements.txt - is the file with the required python packages

How to start load.py:
1. Install the required packages from requirements.txt

```bash
pip install -r requirements.txt
```

2. Make sure you have a running postgresql server and you have the credentials to access it

3. Change the credentials in the load.py file

4. Run the load.py script

```bash
python load.py
```

## What the load.py does:
1. Read the content of sql code.sql and runs it to delete the database and then recreate it
2. Read the content of WinterAthletesSampleData.csv and loads it into the database
