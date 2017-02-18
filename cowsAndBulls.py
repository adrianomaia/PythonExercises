'''
Create a program that will play the “cows and bulls” game with the user.
The game works like this:
Randomly generate a 4-digit number.
Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct
place, they have a “cow”. For every digit the user guessed
correctly in the wrong place is a “bull.” Every time the
user makes a guess, tell them how many “cows” and “bulls”
they have. Once the user guesses the correct number,
the game is over. Keep track of the number of guesses the
user makes throughout teh game and tell the user at the end.
'''
import random
from random import randint

def randomNumber():
    r = str(random.randint(0000, 9999))
    return r

def cowsOrBulls(x,y):
    cowbull = [0,0]
    for z in range(len(y)):
        if x[z] == y[z]:
            cowbull[0] += 1 #cow
        elif x[z] in y:
            cowbull[1] += 1 #bull
    return cowbull


if __name__ == "__main__":

    tries = 0
    game = True
    numRandom = randomNumber()
    print(numRandom)
    while game:
        numberUser = userGuess = str(input("Guess the number (the number contains four digit, to exit write 0): "))
        if numberUser == 0:
            break
        countBullCow = cowsOrBulls(numberUser,numRandom)
        tries += 1

        print("You have " + str(countBullCow[0]) + " cows, and " + str(countBullCow[1]) + " bulls.")

        if countBullCow[0] == 4:
            game = False
            print("You Win with " + str(tries) + " tries and the number was " + str(numRandom) + "")
        else:
            print("Try again until you win, never give up")
