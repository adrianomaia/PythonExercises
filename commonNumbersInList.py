''' Take two lists, say for example these two and write a
program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.'''

import random

firstList = random.sample(range(30),5)
secondList = random.sample(range(30),8)

equalNumber =[]

for first in firstList:
    for second in secondList:
        if first == second:
            equalNumber.append(first)

print("First List -->",(firstList))
print("First List -->",(secondList))
print("List with equal numbers -->",(equalNumber))
