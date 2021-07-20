# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Assignment 2
# Date 7/ # TODO Day/2021

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def graph_null(data):
    sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
    plt.title("Heatmap of the null values for all numeric columns")
    plt.tight_layout()
    plt.show()


def find_stock(file, symbol):
    stock = file[file['symbol'] == symbol]
    print(stock)
    MaxStockProfit(stock)


def MaxStockProfit(stock):
    stock = stock.sort_values(['close'], ascending=True)
    stock.to_csv("AAPL_Stock.csv")
    print(stock)


def main():
    """Running the main code"""
    psa = pd.read_csv("prices-split-adjusted.csv")
    # print(psa.head())
    # stock = psa['symbol'].unique()
    find_stock(psa, 'AAPL')



if __name__ == '__main__':
    main()

