#####################
## Exercise 8
## Emma Bright
##
## Group: Broken Toes
## Group Members: Mike Santoro, Duncan Ferguson

import pandas as pd
from statistics import mean
import math


def distance(p1, p2):
    '''function takes in two point tuples and returns the distance'''
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return dist

def newCentroid(records):
    x = []
    y = []
    z = []
    for i in records:
        x_temp, y_temp, z_temp = i
        x.append(x_temp)
        y.append(y_temp)
        z.append(z_temp)
    return (mean(x), mean(y), mean(z))


df = pd.read_csv('./exercise8_infile1.csv')
records = df.to_records(index=False)

centroidCurrent = df.sample(n=3, replace=False).to_records(index=False).tolist()
print(centroidCurrent)
centroidNew = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
count = 0
while centroidCurrent != centroidNew:
    if count > 0:
        centroidCurrent = centroidNew
    cluster0 = []
    cluster1 = []
    cluster2 = []
    for point in records:
        d_c0 = distance(point, centroidCurrent[0])
        d_c1 = distance(point, centroidCurrent[1])
        d_c2 = distance(point, centroidCurrent[2])
        minDist = min([d_c0, d_c1, d_c2])
        if minDist == d_c0:
            cluster0.append(point)
        elif minDist == d_c1:
            cluster1.append(point)
        elif minDist == d_c2:
            cluster2.append(point)
    centroid0 = newCentroid(cluster0)
    centroid1 = newCentroid(cluster1)
    centroid2 = newCentroid(cluster2)
    centroidNew = [centroid0, centroid1, centroid2]
    count += 1

print(centroidCurrent)
print(len(cluster0))
print(len(cluster1))
print(len(cluster2))


# These are created in the "opposite" order of the SKMeans algorithm, 
# so cluster 2 is cluster 0 and vise versa
# with open('handCodedOut.txt', 'w') as file:
#     file.write('Centroid 0: ' + str(centroidNew[2]) + '\n')
#     file.write('Number of Points: ' + str(len(cluster2)) + '\n')
#     file.write('Cluster 0:\n')
#     for point in cluster2:
#         file.write(str(point) + "\n")
#     file.write('\nCentroid 1: ' + str(centroidNew[1]) + '\n')
#     file.write('Number of Points: ' + str(len(cluster1)) + '\n')
#     file.write('Cluster 1:\n')
#     for point in cluster1:
#         file.write(str(point) + "\n")
#     file.write('\nCentroid 2: ' + str(centroidNew[0]) + '\n')
#     file.write('Number of Points: ' + str(len(cluster0)) + '\n')
#     file.write('Cluster 2:\n')
#     for point in cluster0:
#         file.write(str(point) + "\n")
#
# file.close()
