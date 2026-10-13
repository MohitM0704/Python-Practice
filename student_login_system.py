username = input("Enter an username: ")
password = input("Enter a password: ")

if len(username)>=5 and len(password)>=8:
    print(f"Login Successful\n Welcome {username}")
else:
    print("Invalid username or password")