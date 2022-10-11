
# python program to play Rock, Paper, Scissors with your computer

import random

print("********************************************************************")

print("\nHow to play.")
print("-----------\n")
print("1. r = rock, p = paper and s = scissors\n")
print("2. use small letters.\n")
print("3. Enjoy\n")
print("********************************************************************\n")

start = input("So lets start the game? (yes/no): ")

if start == "yes":

    
    nameOfPlayer = input("\nWhat should I call you? : ")

    while start != "no":
        totalScore = int(input("\nTell me the max score to win: "))
        print("\n********************************************************************")
        myScore = 0
        yourScore = 0
        scoreBoard = "\nScore Board : {}'s score = {} and My score = {} (Max score = {}).\n"
        listOfOptions = ["rock", "paper", "scissors"]

        while myScore<totalScore or yourScore <totalScore:
            
            userOption = input("\nEnter your choice, {} (r/p/s): ".format(nameOfPlayer))
            randomChoice = "My choice : {}"

            luckyNumber = random.randrange(3)
            myChoice = listOfOptions[luckyNumber]

            if userOption == "p":
                print("\n{}'s choice : paper".format(nameOfPlayer))
            if userOption == "s":
                print("\n{}'s choice : scissors".format(nameOfPlayer))
            if userOption == "r":
                print("\n{}'s choice : rock".format(nameOfPlayer))
            

            print(randomChoice.format(myChoice))

            if myChoice[0] == userOption:
                print("\nThis round is a draw. No points awarded to neither of us.\n")
                print(scoreBoard.format(nameOfPlayer, yourScore , myScore, totalScore))
                print("********************************************************************")

            elif myChoice == "rock" and userOption == "p":
                yourScore +=1   
                print(scoreBoard.format(nameOfPlayer, yourScore , myScore, totalScore))
                print("********************************************************************")

            elif myChoice == "rock" and userOption == "s":
                myScore += 1
                print(scoreBoard.format(nameOfPlayer, yourScore , myScore, totalScore))
                print("********************************************************************")

            elif myChoice == "paper" and userOption == "r":
                myScore += 1
                print(scoreBoard.format(nameOfPlayer, yourScore , myScore, totalScore))
                print("********************************************************************")

            elif myChoice == "paper" and userOption == "s":
                yourScore +=1
                print(scoreBoard.format(nameOfPlayer, yourScore , myScore, totalScore))
                print("********************************************************************")

            elif myChoice == "scissors" and userOption == "p":
                myScore +=1
                print(scoreBoard.format(nameOfPlayer, yourScore , myScore, totalScore))
                print("********************************************************************")

            elif myChoice == "scissors" and userOption == "r":
                yourScore += 1
                print(scoreBoard.format(nameOfPlayer, yourScore , myScore, totalScore))
                print("********************************************************************")

            else:
                print("\nYou made a mistake while typing, try again.")
                print(scoreBoard.format(nameOfPlayer, yourScore , myScore, totalScore))
                print("********************************************************************")

            if myScore == totalScore:
                print(scoreBoard.format(nameOfPlayer, yourScore , myScore, totalScore))
                print("You lost, its ok, better luck next time.\n")    
                break
            if yourScore == totalScore:
                print(scoreBoard.format(nameOfPlayer, yourScore , myScore, totalScore))
                print("You won, Congratulations!! Have a nice day :)\n")    
                break   
        
        start = input("Shall we play again? (yes/no) : ")
else:
    print("\nOk, we will play later.")