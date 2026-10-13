first = input("Enter your first name: ")
last = input("Enter your last name: ")
year = input("Enter your birth year: ")
username = f"{first}_{last}_{year}"
length = len(username)

print(f"Lenghth of username: {length}")
if length<=20:
    print("Username available")
    print(username.lower())
else:
    print("Username too long")
