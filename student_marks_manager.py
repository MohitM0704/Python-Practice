name = input("Enter your name: ")
marks = []
for i in range(1,6):
    mark = int(input(f"Enter marks in subject {i}: "))
    marks.append(mark)

highest = marks[0]
for mark in marks:
    if mark>highest:
        highest = mark

lowest = marks[0]
for mark in marks:
    if mark<lowest:
        lowest = mark

total = 0
for mark in marks:
    total += mark

average = total / len(marks)

good_marks = 0
for mark in marks:
    if mark>75:
        good_marks += 1

fail = 0
for mark in marks:
    if mark < 35:
        fail += 1

print("\n---------Student Marks Manager-----------")
print(f"Name of student: {name}")
print(f"Total marks: {total}")
print(f"Average marks: {average}")
print(f"Highest mark: {highest}")
print(f"Lowest mark: {lowest}")
print(f"Outstanding Subjects: {good_marks}")
print(f"Failed Subjects: {fail}")