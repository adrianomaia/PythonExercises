#take a list and print all the numbers less than ten


a = [1,2,4,5,6,10,11,12,13,14,15]

newList = []

for number in a:
    if number > 10:
        newList.append(number)

print(newList)
