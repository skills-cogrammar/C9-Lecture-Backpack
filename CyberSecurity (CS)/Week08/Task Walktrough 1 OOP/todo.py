class Person:
    def __init__(self, name, surname, age, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address

    def walk(self):
        print(f"{self.name} is going for a walk!")

    def display_info(self):
        info = "Personal Information:\n"
        info += f"Name: {self.name}\nSurname: {self.surname}\n"
        info += f"Age: {self.age}\nAddress: {self.address}"
        print(info)

person1 = Person("Jack", "Peters", 23, "123 Walk Str")
person2 = Person("Tina", "Jackson", 25, "542 Main Rd")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the to-do list."""
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added.')

    def complete_task(self, task_number):
        """Marks a task as completed by its task number."""
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            print(f'Task "{self.tasks[task_number]["task"]}" marked as completed.')
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        """Deletes a task by its task number."""
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f'Task "{removed_task["task"]}" deleted.')
        else:
            print("Invalid task number.")

    def show_tasks(self):
        """Displays all tasks with their status."""
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = "✓" if task["completed"] else "✗"
                print(f'{i}. {task["task"]: <25} [{status}]')

# Challenge students to create a task class that would contain
# attributes such as title, description, is_completed etc.
# Encourage students ot be creative.

# Example usage:
to_do_list = ToDoList()
to_do_list.add_task("Buy groceries")
to_do_list.add_task("Study for exams")
to_do_list.show_tasks()
to_do_list.complete_task(0)
to_do_list.show_tasks()
to_do_list.delete_task(1)
to_do_list.show_tasks()
