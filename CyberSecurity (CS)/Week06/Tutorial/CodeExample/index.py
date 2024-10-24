'''
-Student Registration
--Students can be added by entering their name, ID, age, and courses.
--Data will be saved to a text file in a structured format.

-Search Student by ID
--Users can search for a students details using their unique ID.
--The program reads the file and displays the details if the ID exists.

-Update Student Information
--Users can update a student's information (e.g., adding a course or updating age).
--The system will load data from the file, update the necessary fields, and save it back.

-Remove Student
--A students record can be deleted by their ID.
--The file will be updated to reflect the removal.

-Display All Students
--Display all registered students with their details.

Create
Read
Update
Delete
'''
# Helper Function (To allow access of the file)
def read_helper():
    # Store the students in a list
    students = []

    with open("students.txt", "r") as file:
        for line in file:
            student_data = line.strip().split(',')
            student = {
                'id' : student_data[0].split(':')[1].strip(),
                'name': student_data[1].split(':')[1].strip(),
                'age' : student_data[2].split(':')[1].strip(),
                'course' : student_data[3].split(':')[1].strip()
            }
            students.append(student)
    return students 

# Add students (Create)
def add_student():
    student_id = input("Enter Student ID: ")
    students = read_helper()
    for student in students:
        if student["id"] == student_id:
            print(f"Student with the ID {student_id} already exists.")
            return

    name = input("Enter the student name: ")
    age = input("Enter the student age: ")
    course = input("Enter the students' courses: ")

    new_student = {
        'id' : student_id,
        'name' : name,
        'age' : age,
        'course' : course
    }

    students.append(new_student)
    save_student(students)
    print("Student added successfully")


def save_student(students):
    with open("students.txt", "w") as file:
        for student in students:
            student_record = f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}"
            file.write(student_record + '\n')


# Read all students (Read)
def read_students():
    students = read_helper()
    if not students:
        print("No student found")
        return
    for student in students:
        print(f"ID: {student["id"]}, Name: {student["name"]}")


# Update a student (Update)
def update_student():
    student_id = input("Enter the student ID to be updated.")
    students = read_helper()

    for student in students:
        if student['id'] == student_id:
            print(student)
            name = input("Enter the new name of student: ")
            age = input("Enter the new age of student")
            course = input("Enter the new course: ")

            if name:
                student['name'] = name
            if age:
                student['age'] = age
            if course:
                student['course'] = course
        
        save_student(students)
        print("Student updated successfully")
        return



# Delete a student (Delete)
def delete_student():
    student_id = input("Enter the student ID to be delete: ")
    students = read_helper()

    new_students = []
    for student in students:
        if student['id'] != student_id:
            new_students.append(student)
    
    save_student(new_students)
    print(f"Student with ID {student_id} has been deleted")
    





# Main Menu
def main():
    main_message = '''
        This is a Student Management System
        Please select a choice
        1. Add Student
        2. Display all students
        3. Update a student
        4. Delete a student
        5. Exit
    '''

    while True:
        # Prompt the user to enter a choice from 1-5
        print(main_message)
        choice = input("Enter your choice: ")

        # Perform a functionality depending with user's choice
        if choice == "1":
            add_student()
        elif choice == "2":
            read_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting the system ...")
            break
        else:
            print("Oops - incorrect input. Please try again.")
        

main()
