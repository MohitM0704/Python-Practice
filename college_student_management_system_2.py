class Student:
    def __init__(self, name, rollno, branch, marks):
        self.name = name
        self.rollno = rollno
        self.branch = branch
        self.marks = marks

    def display(self):
        print("Name: ", self.name)
        print("Roll No.: ", self.rollno)
        print("Branch: ", self.branch)
        print("Marks: ", self.marks)

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
            print("Status: Pass")
        else:
            print("Status: Fail")

student1 = Student("Mohit", 7, "AIML", 86)
student2 = Student("Om", 5, "AIML", 71)
student3 = Student("Rudra", 10, "CS", 94)

students = [student1, student2, student3]

for student in students:
    student.display()
    student.grade()
    student.status()
    print("------------")