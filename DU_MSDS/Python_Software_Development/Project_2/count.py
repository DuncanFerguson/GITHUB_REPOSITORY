# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3006-2; Assignment 2: Counting Characters
# Date: 2/4/2021
# Teacher: dalton.crutchfield@du.edu
# TA: sunny.shrestha@du.edu


import sys
import string


def dict_2_csv_format(d):
    """This function takes a dictionary "d" and returns it in csv format as "csv" for saving files or printing"""
    csv = ""
    for key, value in sorted(d.items()):
        csv = csv + "'" + key + "'," + str(value) + "\n"
    return csv


def add_frequencies(d, file, remove_case):
    """This function goes through a "file", counts all the ascii characters then stores and returns the values in
    a dictionary, "d". If "remove_case" is True, it will count everything as lowercase. Elif "remove_case" is
     false both upper and lower case ascii characters will be counted. """

    # Opening file and storing characters as list per line
    filetext = []
    with open(file, mode='r', encoding='UTF-8') as f:
        for line in f:
            filetext.append(line.rstrip('\n'))

    ## Counting characters in the file
    for line in filetext:
        for char in line:
            if char.isalnum() == True:  # Making sure that the char is a ascii character
                if remove_case == True:  # Only counting lower case. So Switching all file chars lower
                    char = char.lower()
                    if char in d:
                        d[char] += 1
                    else:
                        d[char] = 1
                elif remove_case == False:  # No case distinction. Add char count to dictionary
                    if char in d:
                        d[char] += 1
                    else:
                        d[char] = 1
    return d


def searchflags(args):
    """This Function Searches for flags '-z', '-c', '-l'. If there is a -z flag the dictionary returns 0 for
    every value that does not have a count. -c Counts both upper and lower cases. -l only counts characters that are
    given in the argument statement. .txt are the files that will be read. .csv files will not be considered.
    Any string that does not start with - or end with .txt .cvs will be considered the l flags counting list"""

    ## Setting the alphabet, and defaults for remove cases and z flag print zeros
    upper_lower_chars = string.ascii_letters
    remove_case = True
    print_zeroes = False

    ## Creating Flag List, files to read, and l flag characters to print
    flaglist = []
    readfiles = []
    savefile = ""
    only_chars = ""

    ## Looping through args to parse through the flaglists, .txt files and .csv files. If there is an l flag, and a
    ## If '-l' is in the flags and the arg item does not end with '.txt' or '.csv' it will only count those characters
    for arg in args:
       if arg[0] == "-":
          if len(arg) == 2:
             flaglist.append(arg[1])
          elif len(arg) >= 2:
             for char in arg:
                if char != "-" and arg not in flaglist:
                   flaglist.append(char)
       elif arg[-4:] == ".txt":  # Adding file names to list
            readfiles.append(arg)
       elif arg[-4:] == ".csv":  # This is just a catch incase the a .csv file for saving gets pass through
          savefile = arg
       elif arg[-3:] != ".py" and "l" or "L" in flaglist:
          only_chars += arg

    ## Parsing through the -c flag
    if "c" in flaglist:
        remove_case = False

    ## Changing z flag setting
    if "z" in flaglist:
        print_zeroes = True

    ## Creating Dictionary
    d ={}

    ## Calling Add Frequencies to count ascii letter in files and return as dictionary
    for file in readfiles:
        d = add_frequencies(d, file, remove_case)

    ## Parsing through -l flag
    if "l" in flaglist:
        l_d = {}
        for key, value in sorted(d.items()):
            if key in only_chars:
               l_d[key] = value
        d = l_d

    ## Parsing through -z flag
    if print_zeroes == True:
        for letter in upper_lower_chars:
            letter = letter.lower()
            if letter not in d:
                d[letter] = 0

    # Parsing throuch -zc flag combo
    if print_zeroes == True and "c" in flaglist:
        for letter in upper_lower_chars:
            if letter not in d:
                d[letter] = 0

    return d


def main():
    """This main function allows the code to be run through the command line. It will also print out the dictionary
    that is returned from search flags in csv format"""
    args = sys.argv[1:]
    d = searchflags(args)
    print(dict_2_csv_format(d))

## If the name is main. Run the main Function
if __name__ == "__main__":
    main()

