# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3006-2; Assignment 1: Counting Characters
# Date: 9/28/2021
# Teacher: dalton.crutchfield@du.edu
# TA: sunny.shrestha@du.edu

# This program counts the number of letters in a txt file. There are a few variations. Including

# Only counting certain characters, like vowels. Indicated by the -l followed by a string of letters to only count
# Ignoring case, so that 'a' and 'A' are counted as different letters. Indicated by -c
# Counting characters in multiple files.
# Printing out lines for characters with a frequency of zero. Indicated by -z
import sys


def add_frequencies(d, file, remove_case):
    """This def reads a file or files and counts the occurences of letters.
     if the remove case is TRUE the function counts lowercase. If remove case is False the function counts upper
     and lower case characters"""

    # Opening file and storing characters as list per line
    filetext = []
    with open(file, mode='r', encoding='UTF-8') as f:
        for line in f:
            filetext.append(line.rstrip('\n'))

    # Running through each line in the file. Going through the characters and adding them to a dictionary
    for line in filetext:
        for char in line:
            if char.isalnum() == True:  # Making sure it is a letter
                if remove_case == True:  # Turning all cases into lower
                    char = char.lower()
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1
    return d


def main():
    """This functions creates a upper and lower case alphabet. It then goes through and parses the command line
    arguments -c (case sensitive), -l letter (only count letters listed), -z (display dictionary of 0 counts)."""
    # creating list of all possible letters in the alphabet
    lowerletter_list = []
    upperletter_list = []
    alpha = 'a'
    for i in range(0, 26):
        lowerletter_list.append(alpha)
        upperletter_list.append(alpha.upper())
        alpha = chr(ord(alpha) + 1)

    # 1. Parse the command line arguments -c, -l, -z
    list = []
    for val in sys.argv:
        list.append(val)

    filenames = []  # a list of file names to loop through
    flaglist = []  # a list of flags
    only_chars = ""  # a stromg of characters to count

    #Searching for the flags "-" as a leading indicator
    for num in list:
        if num[0] == "-":
            if len(num) == 2:  # For a single flag, i.e. -c
                flaglist.append(num[1])
            elif len(num) >=2:  # For multiple flags, ie. -lc or -lcz
                for letter in num:
                    if letter != "-" and letter not in flaglist:
                        flaglist.append(letter)
        elif num[-4:] == ".txt":  #Adding file names to list
            filenames.append(num)
        elif num[-3:] != ".py":  #Adding specific characters to count
            only_chars += num

    # 2. Create an empty dictionary
    d = {}

    #flag '-c':  remove cases sensitivity
    if "c" in flaglist:
        remove_case = False
        letters_list = lowerletter_list + upperletter_list  # Making a letter dictionary for upper and lower case
    else:
        remove_case = True
        letters_list = lowerletter_list  # Making a letter dictionary for the lower case alphabet

    # 3. Add the frequencies for each file in the argument list to that dictionary
    for file in filenames:
        d = add_frequencies(d, file, remove_case)


    #l flag dictionary filter
    if "l" in flaglist:
        ldict = {}
        for letter in d:
            if "c" not in flaglist:  # -c is the case flag. This way we are only counting lower letters.
                only_chars = only_chars.lower()
                if letter in only_chars:
                    ldict[letter] = d[letter]
            else:
                if letter in only_chars:
                    ldict[letter] = d[letter]
        d = ldict

    #z flag. Add the corresponding library
    if "z" in flaglist:
        for letter in letters_list:
            if letter not in d:
                d[letter] = 0

    # 4. Print out the elements of that dictionary in CSV format
    csv = ""
    for key, value in sorted(d.items()):
        csv = csv + '"' + key + '"' + "," + str(value) + "\n"
    print(csv)


main()

