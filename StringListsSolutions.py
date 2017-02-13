'''
Ask the user for a string and print out whether this string
is a palindrome or not. A palindrome is a string that reads the
same words forwards and backwards '''

userInput = None
userInput = input("Write a word: ")
userWord = str(userInput)
#print(userWord)
wordBackwa = userWord[::-1]

if userInput == wordBackwa:
    print("This is a palindrome word")
else:
    print("This is not a palindrome word")
