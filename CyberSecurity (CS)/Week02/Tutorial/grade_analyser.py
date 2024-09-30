score = int(input("Enter your score: ")) # 90
grade = "F"

if (score > 90):
    grade = "A+"
elif (score > 80):
    grade = "A"
elif(score > 70):
    grade = "B+"
elif(score > 60):
    grade = "B"
elif (score > 50):
    grade = "B-"
else:
    print("Invalid score or Fail")

print(f"Grade: {grade}")
