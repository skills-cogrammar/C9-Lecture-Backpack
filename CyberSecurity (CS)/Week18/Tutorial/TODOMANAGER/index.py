'''
1. View all the tasks
2. Add new tasks
3. Delete tasks
'''

def display_menu():
    print('''
    To Do List Manager:
          1. View tasks
          2. Add Task
          3. Delete Task
          4. Exit
    ''')

# View functionality
def view_tasks():
    try:
        results = ""
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            
            if not tasks:
                print("No tasks found!")
                results = "No tasks"
            else:
                print("These are your tasks: ")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                results = "Tasks Found"
        return results
    except FileNotFoundError:
        print("No todo file found")

# Add functionality
def add_task():
    task = input("Enter the task to add: ")

    if task:
        try:
            with open("todo.txt", "a") as file:
                file.write(f"{task}\n")
                view_tasks()
        except FileNotFoundError:
            print("File does not exist")
    else:
        print("Task cannot be empty!")
    
    



# Delete functionality
def delete_task():
    results = view_tasks()
    if results == "No tasks":
        return
    choice = int(input("Which would you want to delete?:"))
    try:

        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            len_of_todos = len(tasks)
            
            if 1 <= choice <= len_of_todos:
                deleted_task = tasks.pop(choice - 1)
                with open("todo.txt", "w") as file:
                    file.writelines(tasks)
            else:
                print("Invalid task Number")
    except FileNotFoundError:
        print("The file does not exist")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice, Please try again!")


main()