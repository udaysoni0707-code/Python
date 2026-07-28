import sqlite3

conn = sqlite3.connect("Try.db")

cursor = conn.cursor()
print("Database Connected Successfully!")

# CREATE TABLE
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS try(
#         id INTEGER,
#         name TEXT,
#         marks INTEGER
#     )
#                """)

# # INSERT TABLE : Define the dataset as a list of tuples
# data = [
#     (1,'Uday',89),
#     (2,'Aman',75),
#     (3,'Rahul',95),
#     (4,'Mohit',65)
# ]

# # Use executemany with ? placeholders
# query = "INSERT INTO try(id, name, marks) VALUES (?, ?, ?)"
# cursor.executemany(query, data)

cursor.execute("SELECT * FROM try WHERE name = 'Rahul'")
data = cursor.fetchall()
print(data)

# update marks
cursor.execute("""
               UPDATE try
               SET marks = 98
               WHERE id = 3;
               """)

# delete row 
cursor.execute("""
               DELETE FROM try
               WHERE name = 'Mohit';
               """)
print("delete row successfully ..")


# show table 
cursor.execute("SELECT * FROM try")

data = cursor.fetchall()

for row in data:
    print(row)
# Commit the changes and close
conn.commit()

print(f"Successfully inserted {cursor.rowcount} rows!")

conn.close()