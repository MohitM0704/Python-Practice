class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll, branch, marks):
        super().__init__(name,age)
        self.roll = roll
        self.branch = branch
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            print("Grade: A")
        elif self.marks >= 80:
            print("Grade: B")
        elif self.marks >= 60:
            print("Grade: C")
        elif self.marks >= 40:
            print("Grade: D")
        else:
            print("Grade: F")

    def display_role(self):
        print("Role: Student")

    def display_student(self):
        print(f"Roll No.: {self.roll}")
        print(f"Branch: {self.branch}")
        print(f"Marks: {self.marks}")

class Professor(Person):
    def __init__(self, name, age, empid, subject, salary):
        super().__init__(name, age)
        self.empid = empid
        self.subject = subject
        self.salary = salary

    def display_role(self):
        print("Role: Professor")

    def display_professor(self):
        print(f"Employee id: {self.empid}")
        print(f"Subject: {self.subject}")
        print(f"Salary: {self.salary}")

student1 = Student("Mohit", 21, 7, "AIML", 86)
student2 = Student("Rudra", 20, 5, "CS", 94)
student3 = Student("Daksh", 21, 10, "ENTC", 71)

professor1= Professor("Disha", 40, 1, "Data Science", 65000)
professor2 = Professor("Bharti", 35, 2, "DMW", 35000)

people = [student1, student2, student3, professor1, professor2]
for person in people:
    person.display_person()
    person.display_role()
    print("----------------")