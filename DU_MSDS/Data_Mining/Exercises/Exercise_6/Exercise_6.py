# Student: Duncan Ferguson <br>
# Student Id: 871641260 <br>
# Class: Comp 4431-1 <br>
# Assignment: Exercise 5 <br>
# Date: 10/16/2021 <br>
# Group: Name: Broken Toe <br>
# Group Members: Emma Bright, Mike Santoro <br>

import pandas as pd
import random
from sklearn.tree import export_graphviz
import graphviz

def create_tuples():
    """This Function goes through and creates"""
    random.seed(50)

    # Creating a list of 12 Random GPAS
    GPA = [round(random.uniform(1, 4), 2) for _ in range(12)]  # Creating List of Random GPA

    # Setting up quasi random Ranking
    RANK = []
    for grade in GPA:
        if grade > 3.5:
            RANK.append(round(random.uniform(.9, 1), 2))
        elif grade > 3:
            RANK.append(round(random.uniform(.8, .9), 2))
        elif grade > 2.5:
            RANK.append(round(random.uniform(.7, .8), 2))
        elif grade > 2:
            RANK.append(round(random.uniform(.6, .7), 2))
        else:
            RANK.append(round(random.uniform(0, .6), 2))

    # Setting up Random Work 0 did not work 1 did, Scalling it toward working have lower GPA
    WORKED = []
    for num in enumerate(GPA):
        if num[1] > 2:
            rand_work = random.randint(0, 60)
            if rand_work > 50:
                WORKED.append(1)
            else:
                WORKED.append(0)
        else:
            rand_work = random.randint(30, 100)
            if rand_work > 50:
                WORKED.append(1)
            else:
                WORKED.append(0)

    #  Setting up if they Graduated College
    for num in enumerate(GPA):
        if num[1] > 2:
            if random.randint(0, 60) > 50:
                WORKED.append(1)
            else:
                WORKED.append(0)
        else:
            if random.randint(30, 100) > 50:
                WORKED.append(1)
            else:
                WORKED.append(0)

    print("GPA", GPA)
    print("RANK", RANK)
    print("WORKED", WORKED)

    # List of lists
    list_o_lists = []
    for num in enumerate(GPA):
        list_o_lists.append([GPA[num[0]], RANK[num[0]], WORKED[num[0]]])

    return list_o_lists

def main():
    """Main Function for running the code"""
    list_o_list = create_tuples()
    print(list_o_list)


if __name__ == '__main__':
    main()

