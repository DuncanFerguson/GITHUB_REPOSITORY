# Student: Duncan Ferguson <br>
# Student Id: 871641260 <br>
# Class: Comp 4431-1 <br>
# Assignment: Exercise 5 <br>
# Date: 10/16/2021 <br>
# Group: Name: Broken Toe <br>
# Group Members: Emma Bright, Mike Santoro <br>

import pandas as pd
from sklearn.tree import export_graphviz
import graphviz


def main():
    """Main Function for running the code"""
    df = pd.read_csv("Table_8_1.csv", index_col="RID")
    dot_data =tree.export_graphviz(clf2, node_ids="true", class_names="true")
    graph = graphviz(dot_data)
    print(graph)
    # print(df)





if __name__ == '__main__':
    main()

