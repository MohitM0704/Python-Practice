first = input("Enter your first name: ")
last = input("Enter your last name: ")
year = input("Enter your birth year: ")

username = f"{first.lower()}_{last.lower()}_{year}"

print(f"Generated username: {username}")

if len(username)<20:
    print("Username Available")
else:
    print("Username too long")