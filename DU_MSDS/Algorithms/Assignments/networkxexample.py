import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

A= [[0,1,1,1,0,0,0,0,0,0,0],
[1,0,1,0,1,0,0,0,0,0,0],
[1,1,0,1,1,1,0,0,0,0,1],
[1,0,1,0,0,1,0,0,0,0,0],
[0,1,1,0,0,1,0,0,0,0,0],
[0,0,1,1,1,0,1,0,0,0,0],
[0,0,0,0,0,1,0,1,0,0,0],
[0,0,0,0,0,0,1,0,1,0,0],
[0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1],
[0,0,1,0,0,0,0,0,0,1,0]]



print("adjacency matrix:\n", A)
G = nx.from_numpy_matrix(np.array(A))
print("edges: ",G.edges)
print("nodes: ",G.nodes)
print("Shortest path length: ", dict(nx.shortest_path_length(G)))  # shortest path length from each node to every other node
print("number of connections: ", G.degree())  # number of neighbors for each node
print("average neighbor degree: ",nx.average_neighbor_degree(G))  # average number of neighbors that each neighbor of node has
nx.draw(G, with_labels=True)
plt.show()

# plot out distribution of number of connections
numcon = G.degree()

distro = {}
for l in numcon:
    d = l[1]
    if d in distro:
        distro[d] += 1  # If we have already seen this distance, increment it
    else:
        distro[d] = 1 # If the first time we have seen it, init it to 1
sum = len(G.nodes)   # get number of nodes
distro = {k: v/sum*100 for k, v in distro.items()}  # divide each value by sum * 100 to get percentile       
plt.bar(list(distro.keys()), distro.values(), color='g')
plt.title("Distribution of number of connections")
plt.show()

# plot out distribution of number of shortest path
numcon = dict(nx.shortest_path_length(G))
distro = {}
for key1,value1 in numcon.items():
    for key2, value2 in value1.items():
        d = value2
        if d in distro:
            distro[d] += 1  # If we have already seen this distance, increment it
        else:
            distro[d] = 1 # If the first time we have seen it, init it to 1
sum = len(G.nodes)*len(G.nodes)  # For every vertex, there are len(A) vertex distances    
distro = {k: v/sum*100 for k, v in distro.items()}  # divide each value by sum * 100 to get percentile
plt.bar(list(distro.keys()), distro.values(), color='g')
plt.title("Distribution of shortest path length from adjacency matrix")
plt.show()

import pandas as pd

print("reading edges file\n")
df = pd.read_csv("edgesshort.txt", sep=' ', header=None, names=['source','target'])
G2 = nx.from_pandas_edgelist(df)
print("G2 Call out", G2, type(G2))


nx.draw(G2, with_labels=True)
plt.show()
# print("Shortest path length: ", dict(nx.shortest_path_length(G2)))  # shortest path length from each node to every other node
# print("number of connections: ",G2.degree())  # number of neighbors for each node
# print("average neighbor degree: ",nx.average_neighbor_degree(G2))  # average number of neighbors that each neighbor of node has

# plot out distribution of number of connections
numcon = G2.degree()
distro = {}
for l in numcon:
    d = l[1]
    if d in distro:
        distro[d] += 1  # If we have already seen this distance, increment it
    else:
        distro[d] = 1 # If the first time we have seen it, init it to 1
sum = len(G2.nodes)   # find number of nodes
distro = {k: v/sum*100 for k, v in distro.items()}  # divide each value by sum * 100 to get percentile       
plt.bar(list(distro.keys()), distro.values(), color='g')
plt.title("Distribution of number of connections from file")
plt.show()

# plot out distribution of number of shortest path
numcon = dict(nx.shortest_path_length(G2))
distro = {}
for key1,value1 in numcon.items():
    for key2, value2 in value1.items():
        d = value2
        if d in distro:
            distro[d] += 1  # If we have already seen this distance, increment it
        else:
            distro[d] = 1 # If the first time we have seen it, init it to 1
sum = len(G2.nodes) * len(G2.nodes) # normalize for number of shortest paths
distro = {k: v/sum*100 for k, v in distro.items()}  # divide each value by sum * 100 to get percentile      
plt.bar(list(distro.keys()), distro.values(), color='g')
plt.title("Distribution of shortest path length from file")
plt.show()