import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"guess an numbre betweeen 1 and {x}: "))
        if guess < random_number:
            print("sorry. guess again , too low")
        elif guess > random_number:
            print("sorry. guess again , too high")

    print(f"yeey , congrats you have guessd the number {random_number}")   


guess(10)           