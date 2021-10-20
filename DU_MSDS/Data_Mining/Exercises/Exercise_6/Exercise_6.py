# Student: Duncan Ferguson <br>
# Student Id: 871641260 <br>
# Class: Comp 4431-1 <br>
# Assignment: Exercise 5 <br>
# Date: 10/16/2021 <br>
# Group: Name: Broken Toe <br>
# Group Members: Emma Bright, Mike Santoro <br>

import pandas as pd
import sklearn


def main():
    """Main Function for running the code"""
    df = pd.read_csv("Table_8_1.csv", index_col="RID")
    print(df)





if __name__ == '__main__':
    main()

