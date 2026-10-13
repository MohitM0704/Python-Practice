students = [
    {"name": "Rahul", "marks": 85, "course": "AIML"},
    {"name": "Om", "marks": 45, "course": "Data Science"},
    {"name": "Harsh", "marks": 72, "course": "AIML"},
    {"name": "Aditya", "marks": 91, "course": "Cyber Security"},
    {"name": "Riya", "marks": 64, "course": "Data Science"},
    {"name": "Neha", "marks": 38, "course": "AIML"}
]
def display_students(students):
    for student in students:
        print(student["name"], "-", student["marks"], "-", student["course"])

def display_result(students):
    for student in students:
        if student["marks"]>=50:
            print(student["name"], "Passed")
        else:
            print(student["name"], "Failed")

def passed_students(students):
    count = 0
    for student in students:
        if student["marks"]>=50:
            count += 1
    return count

def average_marks(students):
    total = 0
    for student in students:
        total += student["marks"]
        average = total/len(student)
    return average

def highest_score(students):
    highest = students[0]
    for student in students:
        if student["marks"]>highest["marks"]:
            highest=student
        return highest["name"]

def get_course(students):
    courses = set()

    for student in students:
        courses.add(student["course"])

    return courses

def failed_students(students):
    failed = []
    for student in students:
        if student["marks"]<50:
            failed.append(student)
    return failed

print("----- All Students -----")
display_students(students)

print("\n----- Pass/Fail Result -----")
display_result(students)

print("\n----- Passed Students -----")
print(passed_students(students))

print("\n----- Average Marks -----")
print(average_marks(students))

print("\n----- Highest Scorer -----")
print(highest_score(students))

print("\n----- Courses -----")
print(get_course(students))

print("\n----- Failed Students -----")
print(failed_students(students))