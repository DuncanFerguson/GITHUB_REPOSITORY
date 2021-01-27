# Duncan
# Comp 3005

# Initially empty contact list
names = []
numbers = []

# Should display each of the names and associated numbers
def displayContactList():
    ''' This prints the contact list '''
    for i in range(len(names)):
        print(names[i],numbers[i])

# Add the name/number pair to the lists
def addContact(name, number):
    '''This function adds name and numbers to the corresponding lists'''
    names.append(name)
    numbers.append(number)

# Return the number associated with the name, or None if name doesn't exist
def lookupNumber(name):
    ''' This function returns the number of 'name' '''
    for i in range(len(names)):
        if name == names[i]:
            return numbers[i]

# Remove the contact name/number pair from the lists.  Do nothing if name doesn't exist
def removeContact(name):
    ''' This function removes the persons phone number '''
    i = names.index(name)
    names.remove(names[i])
    numbers.remove(numbers[i])
    return

addContact("Daniel", 1234)
addContact("Alyssa", 5678)
addContact("Riley", 3456)

displayContactList()
print(lookupNumber("Alyssa"))
removeContact("Alyssa")
displayContactList()
print(lookupNumber("Alyssa"))