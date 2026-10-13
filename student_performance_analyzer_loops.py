name = input("Enter your name: ")

total = 0
high_score = 0
low_score = 0

for i in range(1,6):
    marks = int(input(f"Enter marks for subject {i}: "))
    total += marks
    if marks>=75:
        high_score += 1
    if marks<35:
        low_score += 1

average = total/5

if low_score>0:
    result = "Fail"
else:
    result = "Pass"

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D" 
else:
    grade = "F"

print("\n------ Student Report ------")
print(f"Student Name: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average: }")
print(f"Grade: {grade}")
print(f"Result: {result}")
print(f"High Scoring Subjects: {high_score}")
print(f"Failed Subjects: {low_score}")
