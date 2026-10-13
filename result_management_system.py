name = input("Enter your name: ")
rollno = int(input("Enter your rollno.: "))
math = int(input("Marks in math: "))
physics = int(input("Marks in physics: "))
chemistry = int(input("Marks in chemistry: "))
biology = int(input("Marks in biology: "))
computer = int(input("Marks in computer: "))
total = math + physics + chemistry + biology + computer
print(total)
percentage = total/5
print(percentage)
if math<35 or physics<35 or chemistry<35 or biology<35 or computer<35:
    print("Result:Fail")
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=60:
    print("Grade C")
elif percentage>=50:
    print("Grade D")
elif percentage>=40:
    print("Grade E")
else:
    print("Fail")