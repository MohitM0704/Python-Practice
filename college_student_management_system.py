class Student:
    def __init__(self, name, roll, branch, marks):
        self.name = name
        self.roll = roll
        self.branch = branch
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.roll}")
        print(f"Branch: {self.branch}")
        print(f"Marks: {self.marks}")

    def grade(self):
        if self.marks>=90:
            print("Grade A")
        elif self.marks>=80:
            print("Grade B")
        elif self.marks>=60:
            print("Grade C")
        elif self.marks>=40:
            print("Grade D")
        else:
            print("Fail")

    def status(self):
        if self.marks>=40:
            print("Student Pass")
        else:
            print("Student Fail")

student1 = Student("Mohit Musale",7, "AIML",86)
student2 = Student("Om Pathare",9, "AIML", 71)
student3 = Student("Pranav Dudhe",14, "AIML", 92)

students = [student1, student2, student3]
for student in students:
    student.display()
    student.grade()
    student.status()
    print("-------------")
                   

    
    