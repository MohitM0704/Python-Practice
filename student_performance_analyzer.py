name = input("Enter your name: ")
maths = int(input("Enter marks in math: "))
physics = int(input("Enter marks in physics: "))
chemistry = int(input("Enter marks in chemistry: "))
biology = int(input("Enter marks in biology: "))
computer = int(input("Enter marks in computer: "))

total = maths + physics + chemistry + biology + computer
average = total/5

high_score = 0
low_score = 0

if maths>75:
    high_score += 1
if maths<35:
    low_score +=1

if physics>75:
    high_score += 1
if physics<35:
    low_score +=1

if chemistry>75:
    high_score += 1
if chemistry<35:
    low_score +=1

if biology>75:
    high_score += 1
if biology<35:
    low_score +=1

if computer>75:
    high_score += 1
if computer<35:
    low_score +=1

if low_score>1:
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
    grade = "E"

print("\n----- Student Report -----")
print(f"Student Name: {name}")
print(f"Total Marks: {total}")
print(f"Percentage: {average}%")
print(f"Grade: {grade}")
print(f"Result: {result}")
print(f"High Scoring Subjects (>75): {high_score}")
print(f"Failed Subjects (<35): {low_score}")