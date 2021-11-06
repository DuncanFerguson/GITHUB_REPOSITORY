# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4431-1
# Assignment: Exercise 8
# Date: 11/5/2021
# Group: Name: Broken Toe
# Group Members: Emma Bright, Mike Santoro

from sklearn.cluster import KMeans
import pandas as pd

import pandas as pd
from sklearn.cluster import KMeans

X = pd.read_csv('exercise8_infile1.csv')

kmeans_model = KMeans(n_clusters = 3, random_state = 0).fit(X)
X['kmean'] = kmeans_model.labels_

with open('sklearnOut.txt', 'w') as file:
    file.write('Centroid 0: ' + str(kmeans_model.cluster_centers_[0]) + '\n')
    file.write('Number of Points: ' + str(len(X[X.kmean == 0])) + '\n')
    file.write('Cluster 0:\n')
    for point in X[X.kmean == 0][['d1', 'd2', 'd3']].values.tolist():
        file.write(str(point) + "\n")
    file.write('Centroid 1: ' + str(kmeans_model.cluster_centers_[1]) + '\n')
    file.write('Number of Points: ' + str(len(X[X.kmean == 1])) + '\n')
    file.write('Cluster 1:\n')
    for point in X[X.kmean == 1][['d1', 'd2', 'd3']].values.tolist():
        file.write(str(point) + "\n")
    file.write('Centroid 2: ' + str(kmeans_model.cluster_centers_[2]) + '\n')
    file.write('Number of Points: ' + str(len(X[X.kmean == 2])) + '\n')
    file.write('Cluster 2:\n')
    for point in X[X.kmean == 2][['d1', 'd2', 'd3']].values.tolist():
        file.write(str(point) + "\n")

file.close()

print(f'Using the clustering model to predict clusters now:\n{kmeans_model.predict([ [8,8,8], [19,19,19], [31,31,31]])}')