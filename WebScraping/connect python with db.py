# an example
import sqlite3

# establish a connection and a cursor
connection = sqlite3.connect("Data.db")
cursor = connection.cursor()

# Query all data
cursor.execute("SELECT * FROM events WHERE Date='2023.10.14'")
rows = cursor.fetchall()
print(rows)

# Query some data
cursor.execute("SELECT 'Band Name', Date FROM events WHERE 'City Name'='City 1'")
rows = cursor.fetchall()
print(rows)

# insert new rows
#  create list of tuples for inserting multiple rows
new_rows = [('Band 2', 'City 2', '2023.6.11'), ('Band 3', 'City 3', '2023.6.12')]

cursor.executemany("INSERT INTO events Values(?,?,?)", new_rows)
connection.commit() # same as write changes in GUI data base

# Query all data without any condition
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)