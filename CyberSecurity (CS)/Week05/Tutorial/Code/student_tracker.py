"""
Student Manager.

Tasks:
- Add a new student and their grades.
- Update a student's grade.
- Calculate the average grade for each student.
- Find the student with the highest average.
"""

def draw_line(symbol="-", length=80):
    """
    Draws a line across the terminal.
    
    symbol : str - Symbol used to draw line.
    length : int - Length of line.
    """
    print(symbol * length)


def get_num_input(prompt):
    """
    Get numeric input from user. If non-numeric input is given user will be
    prompt to enter another value.

    prompt : str - Prompt to provide user for input.
    """
    while True:
        user_input = input(prompt)
        if user_input.lstrip("-").isnumeric():
            return int(user_input)
        print("Invalid input, please use numbers only!")


def list_data(data):
    """Print given data to terminal in list format."""
    for i, item in enumerate(data, 1):
        print(f"{i}. {item}")


def get_student_avg(student, gradebook):
    """
    Calculate average grade of given student.

    student : str - The student's average to calculate.
    gradebook : str - Gradebook to retreive student data from. 
    """
    total = 0
    for grade in gradebook[student]:
        total += grade
    total = total/len(gradebook[student])
    return total


def display_gradebook(gradebook):
    """Display all student and their grade from gradebook."""
    draw_line()
    print("Students")
    draw_line()
    for key, value in gradebook.items():
        print(f"{key} - {value}")
    draw_line()


def title(text):
    """Print the given text in a title format."""
    space = " " * ((60 - len(text))//2)
    draw_line(length=60)
    print(space + text.title())
    draw_line(length=60)


MENU = """Please select an option below:

1. Add Student
2. Update Student Grades
3. Get Student Average
4. Highest Grade Average

0. Quit
:"""

gradebook = {
    "Alice": [85, 90, 78],
    "Bob": [88, 92, 80],
    "Charlie": [70, 75, 80]
}

while True:
    display_gradebook(gradebook)
    menu_option = input(MENU)

    if menu_option == "1":
        title("Add Student")
        # Get Name
        student_name = input("Student Name: ")
        # Get grades
        print("Please provide student grades.(If all grades are provide type -1)")
        grades = []
        count = 1
        while True:
            grade = get_num_input(f"Grade {count}: ")
            if grade == -1:
                break
            grades.append(grade)
            count += 1
        # Display given data and ask user to confirm
        print(f"Student Name: {student_name}")
        print(f"Grades: {grades}")
        save = input("Are you sure you would like to save this student's data?(y/n)")
        if save == "y":
            gradebook[student_name] = grades

        print("Student Added!")
        input("Press enter to continue.")

    if menu_option == "2":
        # List students
        title("Update Student")
        print("Please select a student to edit below: ")
        list_data(gradebook.keys())
        # Get selected student and their grades
        student = get_num_input(f": ")
        student = list(gradebook.keys())[student-1]
        grades = gradebook[student]

        option = input("Would you like to add or update a grade:\n1. Add\n2. Update\n: ")
        if option == "1":
            # Adding new grade
            grade = get_num_input(f"Grade: ")
            grades.append(grade)
        elif option == "2":
            # Changing existing grade
            print("Please select a grade to edit: ")
            list_data(gradebook[student])
            while True:
                edit_grade = get_num_input(f": ")
                if 0 < edit_grade <= len(grades):
                    break
                print("Invalid option selected!")
            new_grade = get_num_input(f"New Grade: ")
            save = input("Are you sure you would like to update "
                         + f"{grades[edit_grade-1]} to {new_grade}?(y/n)\n: ")
            if save.lower() == 'y':
                grades[edit_grade-1] = new_grade
            print("Student Updated!")
            input("Press enter to continue.")
        
    elif menu_option == "3":
        title("Grade Averages")
        print("Please select a student to view their average:")
        list_data(gradebook)
        # Prompt user to select a student to get their average
        while True:
            student = get_num_input(f": ")
            if 0 < student <= len(gradebook):
                break
            print("Invalid option selected!")
        # Retrieve student and calculate average.
        student = list(gradebook.keys())[student-1]
        average = get_student_avg(student, gradebook)

        print(f"Student: {student}\nAverage: {format(average, '.2f')}%")
        input("Press enter to continue.")

    elif menu_option == "4":
        title("Highest Grade Average")
        students = list(gradebook.keys())
        # Get all student averages
        grades = []
        for student in students:
            grades.append(get_student_avg(student, gradebook))
        # Retrieve and display highest grade.
        max_grade = max(grades)
        student = students[grades.index(max_grade)]
        
        print(f"Student: {student}\nGrade Average: {max_grade}")
        input("Press enter to continue.")

    elif menu_option == "0":
        break
