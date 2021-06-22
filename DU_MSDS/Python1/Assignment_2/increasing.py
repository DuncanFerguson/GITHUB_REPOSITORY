# Duncan Ferguson
# Class: COMP-3005-2
# Assignment 2: Increasing

#Links Used https://pynative.com/python-accept-list-input-from-user/#:~:text=Use%20a%20input()%20function,loop%20and%20range()%20function.
def strictlyIncreasing(howMany):
    '''This definition returns TRUE if all the numbers are increasing in order. It returns false if they are not
    there is some sas in my descriptions if you get it false.'''

    # Just in Case they only put one number in
    if howMany == 1:
        return print("FALSE")
    count = 0
    list = []
    while count < howMany:
        input_num = int(input("Enter Number: "))
        list.append(input_num)
        count += 1
        if count == 1:
            continue
        elif list[count-1] <= list[count -2]:
            print("FALSE")
            return
    return print("TRUE")

howMany = int(input("Input how many numbers you are you going to input: "))
strictlyIncreasing(howMany)



