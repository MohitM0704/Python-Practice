students = []
for i in range(1,4):
    name = input("Enter your name: ")
    roll = int(input("Enter roll no.: "))
    branch = input("Enter your branch: ")
    marks = int(input("Enter your marks: "))
    student = {
    "name": name,
    "roll": roll,
    "branch": branch,
    "marks": marks
    }
    students.append(student)
for student in students:
    print("\n----- Student -----")
    print(f"Name   : {student['name']}")
    print(f"Roll   : {student['roll']}")
    print(f"Branch : {student['branch']}")
    print(f"Marks  : {student['marks']}")

highest_marks = 0
topper = {}
for student in students:
    if student["marks"]>highest_marks:
        highest_marks = student["marks"]
        topper = student
print("\n----- Topper -----")
print(f"Name   : {topper['name']}")
print(f"Roll   : {topper['roll']}")
print(f"Branch : {topper['branch']}")
print(f"Marks  : {topper['marks']}")

entered_name = input("Enter student's name: ")
for student in students:
    if student["name"] == entered_name:
        new_marks = int(input("Enter new marks: "))
        student["marks"] = new_marks
        print("Marks updated successfully!")
print("\nUpdated Student Records")
for student in students:
    print("-------------------")
    print(f"Name   : {student['name']}")
    print(f"Roll   : {student['roll']}")
    print(f"Branch : {student['branch']}")
    print(f"Marks  : {student['marks']}")




