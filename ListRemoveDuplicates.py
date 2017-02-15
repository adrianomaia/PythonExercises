'''Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.'''

import random

def  defineSet(y):
    l = set(y)
    print(l)

def getDuplicates(list):
    newList = []
    for i in list:
        if i not in newList:
            newList.append(i)
    print (newList)

list = [0,1,1,1,2,3,4,5,6,6,2,2]
defineSet(list)
getDuplicates(list)

# without a function
# two ways:
# first

'''list  = [1,3,4,5,6,2,2,3,5,6]
duplicateNumb = set(list)
print(duplicateNumb)'''

# second way
'''list  = [1,3,4,5,6,2,2,3,5,6]
newList = []
for i in list:
    if i not in newList:
        newList.append(i)
print(newList)'''

#print(list)
