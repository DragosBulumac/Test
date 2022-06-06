import sqlite3

# create database
connection = sqlite3.connect("company.db")

# create a database table
cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS employee
([employer_id] INTEGER PRIMARY KEY, [first_name] TEXT, [last_name] TEXT, [age] INTEGER, [job] TEXT, [salary] INTEGER,
 [bonus] INTEGER) """
)

cursor.execute("""ALTER TABLE employee add column total_salary as (bonus + salary)""")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS department
([department_id] INTEGER PRIMARY KEY, [name] TEXT, [users] BLOB) """
)

connection.commit()


