"""
Student Manager.

Tasks:
- Add a new student and their grades.
- Update a student's grade.
- Calculate the average grade for each student
- Find the student with the highest average.
"""


# Dictionary -> Relation (Student: [Grades])

# Create/Initialise an empty gradebook
gradebook = {
    "Walobwa" : [40, 50, 80, 100],
    "Armand" : [10, 50, 100, 400]
}


# Add a new student to the gradebook
def add_student():
    print("User asked to create a student")

    # Prompt the user about the student's name. Removed all leading and trailing white spaces
    student_name = input("Enter a student's name: ").strip()

    # Check if the name is already existing
    if student_name in gradebook:
        print(f"{student_name} already exists in the gradebook")
    else:
        try:
            # Curate a list of grades from the user's answers using built-in functions/methods
            grades = list(map(int, input("Enter the student's grades separated by spaces as numbers: ").split()))
            gradebook[student_name] = grades
            print(f"{student_name} has been added with grades: {grades}.")
        except ValueError:
            print("Invalid input. Please insert the student's grades separated by spaces as numbers")
    



# Update a student's grade
def updates_student_grade():

    # Display all students
    for student in gradebook.keys():
        print(student)
    student_name = input("Which student would you like to update?").strip()

    #Check if the students exist
    if student_name in gradebook:
        try:
            
            new_grades = list(map(int, input("Enter the student's grades separated by spaces as numbers: ").split()))
            # Update the student's grades by adding onto the existing list
            gradebook[student_name].extend(new_grades)
            print(f"Updated grades for {student_name}: {gradebook[student_name]}")
        except ValueError:
            print("Invalid input. Enter the student's grades separated by spaces as numbers")
    else:
        print(f"{student_name} not found in gradebook.")




# Calculate the average grade for each student
def get_average_grade(student_name):

    grades = gradebook.get(student_name)
    if grades:
        results =  sum(grades) / len(grades)

        '''
        From the tutorial. The problem was with the return statement. We used print instead of return
        '''
        print(f"{student_name}'s average grade is: {results:.2f}")
        return results
    else:
        return None






# Find the student with the highest average.
def find_student_with_highest_average():

    if gradebook:
        highest_student = max(gradebook, key=get_average_grade)
        highest_average = get_average_grade(highest_student)

        print(f"The student with the highest average is {highest_student} with {highest_average}")
    else: 
        print("The gradebook is empty.")
    
            
    
            





# Prompt the user
main_question = '''
    What action would you want to perform?
    1. Add a new student and their grades.
    2. Update a student's grade.
    3. Calculate the average grade for each student
    4. Find the student with the highest average.
    5. Exit
'''


while True:
    print(main_question)
    choice = input("Enter a number (1-5)")

    if choice == "1":
        add_student()
    elif choice == "2":
        updates_student_grade()
    elif choice == "3":
        for student in gradebook.keys():
            print(student)
        student = input("Which student would you want to get the average for? ").strip()

        get_average_grade(student)
    elif choice == "4":
        find_student_with_highest_average()
    elif choice == "5":
        break
    else:
        print("Invalid choice selected. Please enter a number between 1 and 5")

    
