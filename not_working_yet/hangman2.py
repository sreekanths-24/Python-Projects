import random
from not_working_yet.words_for_hangman import words
from not_working_yet.hangman import printRules

def selectRandomWord(words):
    word = random.choice(words)
    #if "-" or " " in word:
    #    selectRandomWord(words)
    return word

printRules()

bodyParts = ["Head", "Body", "Left Arm", "Right Arm", "Left Leg", "Right Leg"]
gallows = []
randomWord = selectRandomWord(words)
wordLength = len(randomWord)

dashedLines = wordLength * "_"
previousGuesses = set()

while (("_" in dashedLines) and (len(gallows) == 6)):
    print(randomWord)
    print(f"\nWord : {dashedLines}")
    print("Gallows : ", " ".format(gallows))
    userGuess = input("Guess : ", " ".format(previousGuesses))

    if userGuess in previousGuesses:
        print(f"\nSorry, the letter {userGuess} is already guessed, try again.")
    else:
        if userGuess not in randomWord:
            print(f"\nSorry the letter {userGuess} is not in the word. Try again.")
            gallows.append(bodyParts[0])
            previousGuesses.add(userGuess)
            bodyParts.remove(bodyParts[0])

        else:
            print("Yes, the letter you gussed is in the word.")
            previousGuesses.add(userGuess)


