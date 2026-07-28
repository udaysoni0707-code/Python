import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()
print("Database Connected Successfully!")

cursor.execute("""
    CREATE TABLE IF NOT EXIST student(
        id INTEGER
        name TEXT
        marks INTEGER
)
 """)

# INSERT TABLE 
cursor.execute("""
    INSERT INTO student
    VALUES (1, 'Uday', 89)           
               """)
# save changes
conn.commit()

# read data 
cursor.execute("SELECT * FROM student")

data = cursor.fetchall()

for row in data:
    print(row)
    
# close connection
conn.close()