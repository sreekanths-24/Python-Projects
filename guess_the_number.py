#python program to guess the number

import random

# user guess the number the computer has in RAM
def userGuess():
    numberRange = int(input("\nLet me choose a secret number between 1 to "))
    secretNumber = random.randint(1, numberRange)
    userGuess = 0
    numberOfSteps = 0
    while userGuess != secretNumber:
        userGuess = int(input("\nGuess the secret number: ")) 

        if userGuess < secretNumber:
            print("Sorry, try again. Too low.")
        elif userGuess > secretNumber:
            print("Sorry, try again. Too high.")
        numberOfSteps += 1
    print(f"\nCongrats you guessed the secret number {secretNumber} in {numberOfSteps} steps!!")

#the computer guess the number the user has in mind
def computerGuess():
    low = int(input("Tell me the lower limit of your secret number : "))
    high = int(input("Tell me the upper limit of your secret number : "))
    high += 1
    result = 0
    numOfSteps = 0
    
    if low == high:
        guess = low

    else:
        while result != "c":
            guess = random.randrange(low, high)
            
            result = str(input(f"\nIs the number in your mind {guess} ? too high =\"h\", too low =\"l\", correct guess =\"c\": "))

            if result == "h":
                high = guess-1
            elif result == "l":
                low = guess+1

            if low == high:
                guess = low

            if low == high:
                guess = low

            numOfSteps += 1
    print(f"The computer guessed your secret number is {guess} in {numOfSteps} steps!!")
#computerGuess()
#userGuess()