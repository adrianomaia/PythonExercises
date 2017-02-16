'''Write a program (using functions!) that asks the user for a
long string containing multiple words.
Print back to the user the same string,
except with the words in backwards order
'''
import sys

def getInput(): # get message from user
    message = input("Write a message: ")
    return message


def messageBackward():
    message = getInput()
    messageSplit = message.split()
    backwardMessage = messageSplit[::-1]
    for i in backwardMessage:
        sys.stdout.write(i)
        sys.stdout.write(" ")

messageBackward()
