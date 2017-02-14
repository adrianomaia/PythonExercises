# make a rock-paper-scissorgame versus computer
import random

listChoices = ["rock","paper","scissor"]
print("Choose rock, paper or scissor to play or write exit to leave the game")
userChoice = str.lower(input("Rock,Paper or Scissor: "))

while True:
    while userChoice not in listChoices:
        if userChoice == "exit":
            break
        print("You have to choose one of the this three options to play: rock, paper or scissor or exit to leave the game")
        userChoice = str.lower(input("Rock,Paper or Scissor: "))
    else: # if the first statetement is not reached
        pcChoice = random.choice(listChoices)
        if(userChoice == pcChoice):
            print("User Choice --> ",(userChoice))
            print("Pc Choice --> ",(pcChoice))
            print("It's a tie")
        elif ((userChoice == "rock" and pcChoice == "scissor") or (userChoice == "scissor" and pcChoice == "paper") or (userChoice == "paper" and pcChoice == "rock") ):
            print("User Choice --> ",(userChoice))
            print("Pc Choice --> ",(pcChoice))
            print("User Wins congrats!!!!! :)")
        else:
            print("User Choice --> ",(userChoice))
            print("Pc Choice --> ",(pcChoice))
            print("Pc Wins Try Again!!!!! :(")
        userChoice = None
        continue
    break
