import pandas as pd
import numpy as np

def loadGraph(edgeFilename):
    """ 2). This function reads in the file of edge data.
     This function should return an adjacency list representation of the corresponding undirected graph
     A list of vertex Ids is not explicitly given but instead can be inferred from the edge data"""
    df = pd.read_csv(edgeFilename, sep=" ", header=None)  # Importing the txt file into a dataframe
    # rows = df.values.tolist()  # Turning Dataframe into list of lists
    nodes = np.unique(df)
    nodes.tolist()
    adj_dict = dict.fromkeys(nodes, [])



    # for row in df:
    #     # adj_dict[]
    #
    #     print(df[0][row], "Gap")


    print(adj_dict)
    print(nodes)
    # adj_dict = dict()
    # nodesValues = set(nodes.values())
    # print("Uniqi vals", nodesValues)


    # for key in nodes:
    #     adj_dict[key] = []
    #
    # s= dict(val for )


    # for row in df[0]
    # print(df[0][1])
    # for row in df[0][1]:
    #     print(row)
    # for row in df[0]:
    #     adj_dict[row[0]] == 0

    # print(adj_dict)
        # print("Edge")
        # adj_dict[row[0]].append([row[1]])

    # for row in df1[]


    # print(nodes)


    print(df)

    # # Produces a dictionary with the node and the adjacency of the lists next to it
    # # TODO Maybe look at making this a bit quicker
    graph = dict()
    # for row in range(len(rows)):
    #     if rows[row][0] not in graph.keys():
    #         graph[rows[row][0]] = [rows[row][1]]
    #     elif rows[row][0] in graph.keys():
    #         graph[rows[row][0]].append(rows[row][1])
    #
    # for row in range(len(rows)):
    #     if rows[row][1] not in graph.keys():
    #         graph[rows[row][1]] = [rows[row][0]]
    #     elif rows[row][1] in graph.keys():
    #         graph[rows[row][1]].append(rows[row][0])
    #     else:
    #         print("\n \n \n \n \n BREAK \n \n \n \n \n")  # Should never get to here
    #
    # # Sorting the Graph Dictionary
    # sorted_dict = dict()
    # for i in sorted(graph.keys()):
    #     sorted_dict[i] = sorted(graph[i])
    #
    # # Convert to List of Lists
    # adj_list = []
    # for key in sorted_dict:
    #     adj_list.append(sorted_dict[key])

    # return adj_list

def test():
    """Testing code that prints out the final distribution dictionary"""
    graphit = loadGraph('edges.txt')
    # graphit = loadGraph('edgesshort.txt')
    # distanceDistribution(graphit)

def main():
    """Standard Main pointing to test queue"""
    test()

if __name__ == '__main__':
    main()