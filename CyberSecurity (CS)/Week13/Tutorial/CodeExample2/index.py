#1. Import sqlite3
import sqlite3

#2. Connecting to the db file
try:
    db = sqlite3.connect('index.db')
    #3. Create cursor for execution of commands
    cursor = db.cursor()
except sqlite3.Error as e:
    print(f"Error connecting to db: {e}")

#4. Create table with defined columns
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50),
                description TEXT,
                status TEXT DEFAULT 'incomplete',
                owner VARCHAR(50),
                date_created DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
except sqlite3.Error as e:
    print(f"Error creating table: '{e}'")


# Functon1: add a new task
def add_task(task_name, task_description, task_owner):
    try:
        cursor.execute('''
            INSERT INTO todo (name, description, status, owner)
            VALUES(?, ?, ?, ?)
        ''', (task_name, task_description, 'incomplete', task_owner))
        db.commit()
    except sqlite3.Error as e:
        print(f"Something went wrong: {e}")


# Function2: Display tasks
def view_tasks():
    try:
        cursor.execute("SELECT * FROM todo")
        tasks = cursor.fetchall()

        for task in tasks:
            print(task)
    except sqlite3.Error as e:
        print(f"Something went wrong: {e}")


def filter(column, value):
    try:
        cursor.execute(f'''
            SELECT * FROM todo WHERE {column} = ?
        ''', (value,))
        tasks = cursor.fetchall()
        if tasks:
            for task in tasks:
                print(task)
        else:
            print(f"No tasks found with {column} = {value}")
    except sqlite3.Error as e:
        print(f"Error filtering tasks: {e}")

 
# Function3: Marking a task as complete
def mark_complete(task_id):
    try:

        cursor.execute('''
            UPDATE todo SET status = 'complete' WHERE id = ?
        ''', (task_id))
        db.commit()
    except sqlite3.Error as e:
        print(f"Something went wrong: {e}")

# Function4: Delete
def delete(task_id):
    try:
        cursor.execute('''
            DELETE FROM todo WHERE id = ?
        ''', (task_id))
        db.commit()
    except sqlite3.Error as e:
        print(f"Something went wrong {e}")


def main():
    while True:
        choice = '''
        WELCOME TO THE TODO LIST APP, WHAT WOULD YOU LIKE TO ACHIEVE
        1. ADD A TASK.
        2. VIEW TASKS
        3. MARK A TASK AS COMPLETE
        4. DELETE A TASK
        5. EXIT THE PROGRAM
        6. FILTER TASKS
        '''
        print(choice)

        user_choice = input("Enter Your Choice: ")
        print(user_choice)

        if user_choice == "1":
            task_name = input("Enter a task name: ")
            task_description = input("Enter a task description: ")
            task_owner = input("Enter your name: ")
            add_task(task_name, task_description, task_owner)

        elif user_choice == "2":
            view_tasks()

        elif user_choice == "3":
            task_id = input("Enter the id of the task to be marked: ")
            mark_complete(task_id)

        elif user_choice == "4":
            task_id = input("Enter the id of the task to be deleted: ")
            delete(task_id)

        elif user_choice == "5":
            print("Exiting the program ...")
            break
        elif user_choice == "6":
            task_column = input("Enter the column they'd want to filter with: ")
            column_value = input("Enter the value: ")
            filter(task_column, column_value)
        else:
            print("Invalid choice, Pease try again.")


main()
db.close()