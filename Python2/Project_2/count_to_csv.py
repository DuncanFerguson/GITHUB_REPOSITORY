# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3006-2; Assignment 2: Using Modules with Character Counting
# Date: 2/4/2021
# Teacher: dalton.crutchfield@du.edu
# TA: sunny.shrestha@du.edu

import count
import sys


def save_csv(args):
    """This takes the argument string. Passes it through count. It then saves the file to what ever has
    .csv on the back"""

    ##Parsing through command line to find name of .csv to be written and saved
    savefile = ""
    for item in args:
        if item[-4:] == ".csv":
            savefile = item

    return_d = count.searchflags(args)
    data_2_save = count.dict_2_csv_format(return_d)
    with open(savefile, mode="w") as f:
        f.write(data_2_save)
    print("File Saved")


def main():
    """Reading the CMD argument lines"""
    args = sys.argv[1:]
    save_csv(args)


if __name__ == "__main__":
    main()


