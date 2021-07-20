# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Assignment 2
# Date 7/ # TODO Day/2021

import pandas as pd

def main():
    """Running the main code"""
    psa = pd.read_csv("prices-split-adjusted.csv")
    print(psa.head())
    stock = psa['symbol'].unique()
    print(stock)
    # Pushing Testing From Main Computer


if __name__ == '__main__':
    main()

