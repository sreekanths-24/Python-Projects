#python program to guess the number

import random

def guess():
    numberRange = int(input("Guess a number between 1 to "))
    secretNumber = random.randint(1, numberRange)
    userGuess = 0
    while userGuess != secretNumber:
        userGuess = int(input("Guess the secret number: ")) 

        if userGuess < secretNumber:
            print("Sorry, try again. Too low.")
        elif userGuess > secretNumber:
            print("Sorry, try again. Too high.")
    print(f"Congrats you guessed the secret number {secretNumber} correctly!!!")

guess()