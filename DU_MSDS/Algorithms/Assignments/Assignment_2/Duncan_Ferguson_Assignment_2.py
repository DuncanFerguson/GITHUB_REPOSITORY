# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Assignment 2
# Date 7/ # TODO Day/2021

import pandas as pd

def find_stock(file, symbol):
    stock = file[file['symbol'] == symbol]
    print(stock)
    MaxStockProfit(stock)


def MaxStockProfit(stock):
    print(type(stock))
    stock.sort_values(['close'], ascending=True)
    # print(stock)




def main():
    """Running the main code"""
    psa = pd.read_csv("prices-split-adjusted.csv")
    print(psa.head())
    stock = psa['symbol'].unique()
    find_stock(psa, 'AAPL')


    # print(stock)
    # Laptop to main


if __name__ == '__main__':
    main()

