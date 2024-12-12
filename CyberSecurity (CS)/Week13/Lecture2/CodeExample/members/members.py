'''
PRACTICAL EXAMPLE
Creates a database called (members.db)
Create a table called (members) with the columns    
    - ID (Integer)
    - Name (String)
    - Email (String)
    - Grade (String)
Insert members (rows/information) in the members table
UPDATE
DELETE
READ
'''
import sqlite3

db = sqlite3.connect("members.db")

cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        id INT PRIMARY KEY,
        name VARCHAR(50),
        email VARCHAR(50),
        grade VARCHAR(50)
    )
''')

# member_id = 2
# member_name = "Shahid"
# member_email = "shahid@gmail.com"
# member_grade = "A"

# cursor.execute('''
#     INSERT INTO members (id, name, email, grade)
#     VALUES (?, ?, ?, ?)
# ''', (member_id, member_name, member_email, member_grade))

cursor.execute('''
    SELECT * FROM members
''')


members_list = [(3, 'John', 'john@gmail.com', 'B'), (4, 'Jane', 'jane@gmail.com', 'B') ]
cursor.executemany('''
    INSERT INTO members (id, name, email, grade)
    VALUES (?, ?, ?, ?)
''', members_list)






members = cursor.fetchall()
print(type(members))

for member in members:
    print(member)

db.commit()
db.close()