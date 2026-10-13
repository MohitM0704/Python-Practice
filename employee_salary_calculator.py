def input_employee():
    name = input("Enter your name: ")
    salary = int(input("Enter your monthly salary: "))
    return name, salary

def calculate_annual_salary(salary):
    annual = salary * 12
    return annual

def calculate_bonus(annual):
    if annual>500000:
        bonus = 0.10 * annual
        print(f"Bonus is 10% of salary: {bonus}")
        return bonus
    else:
        print("No bonus")
    return 0

def display_summary(name, salary, annual, bonus):
    print("\n--------Employee Salary---------")
    print(f"Name: {name}")
    print(f"Monthly salary: {salary}")
    print(f"Annual Salary: {annual}")
    print(f"Bonus: {bonus}")

name, salary = input_employee()

annual = calculate_annual_salary(salary)

bonus = calculate_bonus(annual)

display_summary(name, salary, annual, bonus)



