
students = [
    {"name": "Rahul", "marks": 85, "course": "AIML"},
    {"name": "Om", "marks": 45, "course": "Data Science"},
    {"name": "Harsh", "marks": 72, "course": "AIML"},
    {"name": "Aditya", "marks": 91, "course": "Cyber Security"},
    {"name": "Riya", "marks": 64, "course": "Data Science"}
]

# Q1. Display students
def display_students(students):
    for student in students:
        print(student["name"], "-", student["marks"])


# Q2. Calculate average
def calculate_average(students):
    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)
    return average


# Q3. Find highest scorer
def highest_scorer(students):
    highest = students[0]

    for student in students:
        if student["marks"] > highest["marks"]:
            highest = student

    return highest["name"]


# Q4. Return passed students
def get_passed_students(students):
    passed = []

    for student in students:
        if student["marks"] >= 50:
            passed.append(student)

    return passed


# Q5. Get unique courses
def get_unique_courses(students):
    courses = set()

    for student in students:
        courses.add(student["course"])

    return courses


# Q6. Count failed students
def count_failed(students):
    count = 0

    for student in students:
        if student["marks"] < 50:
            count += 1

    return count


# Display results
print("All Students:")
display_students(students)

print("\nAverage Marks:", calculate_average(students))
print("Highest Scorer:", highest_scorer(students))
print("Passed Students:", get_passed_students(students))
print("Unique Courses:", get_unique_courses(students))
print("Failed Students:", count_failed(students))
