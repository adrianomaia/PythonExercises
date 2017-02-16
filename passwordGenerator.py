'''
Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:
    --> Ask the user how strong they want their password to be.
    For weak passwords, pick a word or two from a list.
'''

import random,string

def lenPass():
    try:
        passleng = int(input("Define a length for your password (at least equal to four and not greater thant twenty): "))
    except Exception as e:
        print("You should type an integer number")
    if passleng < 4 or passleng > 20: # I choose four and ten, you can choose your own number
        print("You have to choose a number between 4 and 20")
    else:
        return passleng

# now lets make a random password using the module string and ASCII characters

def randomPass():
    passleng = lenPass()
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    password = ''.join(random.SystemRandom().choice(chars) for _ in range(passleng))
    # use SystemRandom() for cryptographically security
    return password

randomPass()
