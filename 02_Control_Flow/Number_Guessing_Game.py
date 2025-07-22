# Descrption: 

# This Number guessing game project is based on python concepts : Control flow (if-else, loops)

import random

secret_number = random.randint(1,100)

while True:
    try:
        guess = int(input("Enter your Guess:"))
        if guess == secret_number:
            print("🎉Congratulations! You won game")
            break
        elif guess > secret_number:
            print("Your guess is greater than secret number ")
        else:
            print("Your guess is lesser than secret number ")
    except ValueError:
        print("Ouch! Please Enter valid Number.")
    