balance = 10000
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
choice = int(input("Enter your choice(1/2/3): "))
if choice == 1:
    print(balance)

elif choice == 2:
    amount = int(input("Enter amount: "))
    newbalance = balance + amount
    print("New Balance is:", newbalance)

elif choice == 3:
    withdraw = int(input("Enter withdraw amount: "))
    if withdraw<=balance:
        print("Withdraw Successful")
        updatebalance = balance - withdraw
        print("Balance:", updatebalance)
    else:
        print("Not enough balance")
else:
    print("Invalid Choice")


