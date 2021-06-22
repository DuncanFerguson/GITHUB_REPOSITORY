# Duncan Ferguson
# Comp 3005

def rotate(list,k):
    '''This Function rotates the list one to the right list k amount of spots'''
    i = 0
    newOrder = list
    while i < k:
        frontList = [newOrder[0]]
        backList = newOrder[1:]
        newOrder = backList + frontList
        i += 1
    return newOrder

list = [1,4,7,13,9]

k = int(input("How Many spots would you like to rotate the list? "))
print("New Order: ", rotate(list,k))
print("Original List: ", list)

#https://www.geeksforgeeks.org/python-ways-to-rotate-a-list/
# look at this for moving the list a few more