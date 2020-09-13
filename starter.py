import sqlite3

# establish connection
# a new database file will be created
conn = sqlite3.connect('mydatabase.db')

# create cursor object
cursor = conn.cursor()


