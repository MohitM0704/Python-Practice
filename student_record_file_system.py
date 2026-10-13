def get_student_details():
    name = input("Enter your name: ")
    roll = int(input("Enter your roll no.: "))
    branch = input("Enter your branch: ")
    marks = int(input("Enter your marks: "))
    return name, roll, branch, marks

def add_student(name, roll, branch, marks):
    with open("student_record_file_system.txt", "a") as file:
        file.write(f"Name   : {name}\n")
        file.write(f"Roll   : {roll}\n")
        file.write(f"Branch : {branch}\n")
        file.write(f"Marks  : {marks}\n")
        file.write("--------------------------\n")

def display_students():
    with open("student_record_file_system.txt", "r") as file:
        data = file.read()
        print("\n-----Student Record-------")
        print(data)

name, roll, branch, marks = get_student_details()

add_student(name, roll, branch, marks)

display_students()

choice = input("Do you want to add another student? (Yes/No): ")

if choice.lower() == "yes":
    name, roll, branch, marks = get_student_details()
    add_student(name, roll, branch, marks)

print("\nUpdated Student Records:")
display_students()


