name = input("Enter your name: ")
age = int(input("Enter your age: "))
college = input("Enter college: ")
branch = input("Enter branch: ")
percentage = float(input("Enter percentage: "))
print(name)
print(age)
print(college)
print(branch)
print(percentage)
if percentage>=75:
    print("Eligible for scholarship")
else:
    print("Keep Working Hard!")