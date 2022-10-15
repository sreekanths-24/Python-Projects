import random
from words_for_hangman import words

def selectRandomWord(words):
    randomWord = random.choice(words)
    while '-' or ' ' in randomWord:
        randomWord = random.choice(words)
    return randomWord

def printRules():
    print("\nHow to play")
    print("-----------")
    print("1. Guess the word correctly, one letter at a time.")
    print("2. If the letter you guessed is worng, then one body part goes to the gallows.")
    print("3. Your body parts include head, body, arms and legs")
    print("4. If all the body parts are in the gallows you lose.")
    print("5. If you guess the word correctly, you win.")
    
    
#=====================================================================================

#print the rules
printRules()

#select a random word
bodyParts = ["head","body", "arms", "legs"]
gallows = []


print("\nLets start the game\n")
theRandomWord = selectRandomWord(words)
wordLength = len(theRandomWord)

dashedLines = wordLength * "_"
userGuesses = {}
i =0
while i == 0:
    
    print(theRandomWord)
    print(f"\nWord : {dashedLines}")
    print(f"\nGallows : {gallows}")
    print(f"\nPrevious Guesses : {userGuesses}")
    userGuess = str(input("\nGuess : "))

    
    if userGuess not in theRandomWord:
        print(f"\nSorry the letter {userGuess} is not in the word. Try again.")
        gallows.append(bodyParts[0])
        userGuesses.add(userGuess)
        bodyParts.remove(bodyParts[0])

    else:
        print("Yes, the letter you gussed is in the word.")
        userGuesses.add(userGuess)
