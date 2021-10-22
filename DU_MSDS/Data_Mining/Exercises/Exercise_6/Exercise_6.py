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
from sklearn import tree
from sklearn.tree import export_text


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

    # print("GPA", GPA)
    # print("RANK", RANK)
    # print("WORKED", WORKED)
    #

    # List of lists
    list_o_lists = []
    for num in enumerate(GPA):
        list_o_lists.append([GPA[num[0]], RANK[num[0]], WORKED[num[0]]])

    graduate = []
    for person in enumerate(list_o_lists):
        if sum(person[1]) > 3:
            graduate.append(1)
        else:
            graduate.append(0)


    return list_o_lists, graduate

def create_tree(list_o_lists, graduate):
    """This Function goes through and creates the decision tree"""
    # X = list_o_lists
    # Y = graduate
    # clf = tree.DecisionTreeClassifier()
    # clf = clf.fit(X,Y)
    # print(type(clf))
    # print(clf)
    Xnum = list_o_lists
    classifications = graduate
    clf2 = tree.DecisionTreeClassifier(criterion="entropy")
    clf2 = clf2.fit(Xnum, classifications)

    print(type(clf2))
    print(clf2)
    treeStruct = export_text(clf2)
    print("\nNow printing export_text(clf2)")
    print(treeStruct)
    foo = clf2.apply(Xnum)  # passing in full list of training tuples
    print("clf2.apply( Xnum ):")
    print(foo)
    # now print out line by line as pair:  tuple, which leaf node
    print("\nNow printing each tuple with the decision tree node it ends up in:")
    for i in range(len(foo)):
        print(str(Xnum[i]) + "," + str(foo[i]))

    # NOTE - adding in node_ids and class_names as options to make tree viz more robust
    dot_data = tree.export_graphviz(clf2, node_ids="true",class_names=('not buy','yes buy'),out_file=None, filled=True, rounded=True, special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.formate = "png"
    graph.render("graph", view = True)


def main():
    """Main Function for running the code"""
    list_o_list, graduate = create_tuples()
    # print(list_o_list)
    create_tree(list_o_list, graduate)

if __name__ == '__main__':
    main()

