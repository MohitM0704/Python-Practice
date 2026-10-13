class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll, course):
        super().__init__(name,age)
        self.roll = roll
        self.course = course

class EngineeringStudent(Student):
    def __init__(self, name, age, roll, course, branch, year):
        super().__init__(name, age, roll, course)
        self.branch = branch
        self.year = year

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll No.: {self.roll}")
        print(f"Course: {self.course}")
        print(f"Branch: {self.branch}")
        print(f"Year: {self.year}")

student = EngineeringStudent("Mohit", 21, 7, "B.E.", "AIML", "2024-2027")
student.display()
