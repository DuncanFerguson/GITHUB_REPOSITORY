import random


def writefile(a, b, c):
    """This Function writes a txt file named 'randomnumbers.txt' with c amount of numbers inbetween a and b"""
    with open('RandomNumbers.txt', mode='w', encoding='UTF-8') as f:
        i = 0
        while i < c:  # Looping through c amount of times: Choosing Random number, writing num \n then repeating
            randomnum = str(random.randint(a,b))  # choosing random number, making it a string
            f.write(randomnum)  #Writing the Random Number i on to the txt file
            f.write('\n')  # Bumping down a line
            i += 1


lowerBound = 1  # Lower Bound of the Random Number
upperBound = 10  # Upper Bounder of the Random Number
numberOfNumbers = 100  # This is the amount of random numbers that we want to write

writefile(lowerBound, upperBound, numberOfNumbers)  # Writing a txt file with random numbers from a to b
print("Your File of ",numberOfNumbers," numbers inbetween", lowerBound, " and ", upperBound, " has been created")