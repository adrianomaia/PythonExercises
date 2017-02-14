'''
Create a list and return another list that as only
the even elements of the previous list '''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

evenList = []

for even in a:
    if even % 2 == 0:
        evenList.append(even)

# we could also do something like this
#evenList = [even for even in a if even % 2 == 0]

print("Initial list -->",(a))
print("List with even numbers -->",(evenList))
