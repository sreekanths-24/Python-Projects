#python program to guess the number

import random

def guess():
    numberRange = int(input("\nLet me choose a secret number between 1 to "))
    secretNumber = random.randint(1, numberRange)
    userGuess = 0
    while userGuess != secretNumber:
        userGuess = int(input("\nGuess the secret number: ")) 

        if userGuess < secretNumber:
            print("Sorry, try again. Too low.")
        elif userGuess > secretNumber:
            print("Sorry, try again. Too high.")
    print(f"\nCongrats you guessed the secret number {secretNumber} correctly!!!")

guess()