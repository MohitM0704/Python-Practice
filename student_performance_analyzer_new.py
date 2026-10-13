students = [
    {"name": "Rahul", "marks": 85, "course": "AIML"},
    {"name": "Om", "marks": 45, "course": "Data Science"},
    {"name": "Harsh", "marks": 72, "course": "AIML"},
    {"name": "Aditya", "marks": 91, "course": "Cyber Security"},
    {"name": "Riya", "marks": 64, "course": "Data Science"}
]
def display_students(students):
    for student in students:
        print(student["name"], "-", student["marks"])
def count_passed(students):
    count = 0
    for student in students:
        if student["marks"]>=50:
            count += 1
    return count
def calculate_average(students):
    total = 0
    for student in students:
        total += student["marks"]
    average = total/len(students)
    return average
def highest_scorer(students):
    highest = students[0]
    for student in students:
        if student["marks"]>highest["marks"]:
           highest = student
    return highest["name"]
def get_courses(students):
    courses = set()
    for student in students:
        courses.add(student["course"])
    return courses

display_students(students)
print("Passed:", count_passed(students))
print("Average:", calculate_average(students))
print("Highest Scorer:", highest_scorer(students))
print("Courses:", get_courses(students))

             