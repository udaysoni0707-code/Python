# # this code is use for create db file 
# import sqlite3

# # connect with SQLitew database file
# conn = sqlite3.connect("you.db")

# # Cursor execute SQL commands
# cursor = conn.cursor()

# print("Database connected sucessfully")

# conn.close()

# now we create table

import sqlite3

conn = sqlite3.connect("you.db")
cursor = conn.cursor()

cursor.execute('''
    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    attedence REAL,
    marks REAL,
    result TEXT
               ''')