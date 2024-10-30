# Get list of student and calualte avrages and get max average 
# swap += to =+ so averages are incorrect

def get_max_student_average(students):
    averages = []
    for student in students:
        total = 0
        for grade in students[student]:
            total =+ grade
        average = total/len(students)
        averages.append(average)
    
    max_average = max(averages)
    max_index = averages.index(max_average)

    student = students[max_index]

    print(f"Max Average\nStudent: {student}\nAverage: {max_average}")

students = {
    "James": [55, 76, 67, 68],
    "Jesicca": [60, 65, 70, 72],
    "Blake": [70, 75, 72, 71],
    "John": [65, 60, 77, 66]
}
get_max_student_average(students)