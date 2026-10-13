class Employee:
    def __init__(self, name, id, department, salary):
        self.name = name
        self.id = id
        self.department = department
        self.salary = salary

    def display_details(self):
        print("Name: ", self.name)
        print("ID: ", self.id)
        print("Department: ", self.department)
        print("Salary: ", self.salary)

    def annual_salary(self):
        annualsalary = self.salary * 12
        print("Annual Salary: ", annualsalary)

employee1 = Employee("Pranav", 1, "DA", 40000)
employee2 = Employee("Mrudul", 2, "HW", 20000)
employee3 = Employee("Rudra", 3, "SD", 50000)
employee4 = Employee("Uday", 4, "DS", 45000)
employee5 = Employee("Om", 5, "DA", 30000)

employees = [employee1, employee2, employee3, employee4, employee5]

for employee in employees:
    employee.display_details()
    print("-------------")

highest_employee = employees[0]
for employee in employees:
    if employee.salary > highest_employee.salary:
        highest_employee = employee

print("Highest Salary Employee:", highest_employee.name)
print("Salary:", highest_employee.salary)

total_salary = 0
for employee in employees:
    total_salary = total_salary + employee.salary

average_salary = total_salary / 5
print("Average Salary: ", average_salary)

department = input("Enter department: ")

for employee in employees:
    if employee.department == department:
        employee.display_details()