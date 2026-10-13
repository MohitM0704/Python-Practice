import random

number = random.randint(1,100)
attempts = 0

guess = int(input("Enter a number from 1 to 100: "))

while guess != number:
    attempts +=1
    if guess<number:
        print("Too Low! Try a Higher number")
    else:
        print("Too High! Try a Lower number")
    guess = int(input("Enter a number: "))

attempts += 1
print("Congratulations! \n You've guessed the correct number")
print(f"Attempts taken: {attempts}")

