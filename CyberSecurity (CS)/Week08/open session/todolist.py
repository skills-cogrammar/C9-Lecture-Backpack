class Task:
    def __init__(self, description, due_date, completed=False):
        self.description = description
        self.due_date = due_date

class TodoList:
    def __init__(self):
        self.tasks = [] # empty list to store tasks

    def add_task(self, task):
        self.tasks.append(task)
        print(f"{task} has been added!!")

    def view_tasks(self):
        for task in self.tasks:
            print(task.description)

task1 = Task("cleaning", "Monday")
my_todolist = TodoList()

my_todolist.add_task(task1)
my_todolist.view_tasks()


class Library:
    pass

class Book:
    pass

class Member:
    pass

# using object oriented approach, represent a school management system
