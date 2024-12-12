import sqlite3

# Connect to the database
db = sqlite3.connect('index.db')

# Create a cursor for command execution
cursor = db.cursor()

# Execute the commands needed
cursor.execute('''
               CREATE TABLE members (
               ID INT PRIMARY KEY, 
               email VARCHAR(50)
               )
            ''')

# Saving changes to the Database
db.commit()

# Close the connection to the database
db.close()