# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4431-1
# Assignment: Exercise 8
# Date: 11/5/2021
# Group: Name: Broken Toe
# Group Members: Emma Bright, Mike Santoro

import pandas as pd
import numpy as np

def Euclidean_D(point1, point2):
    """This Function Finds the distance between two 3d points"""
    dist = (((point2[0]-point1[0])**2) + ((point2[1]-point1[1])**2) + ((point2[2]-point1[2])**2))**(1/2)
    return dist

def assign_clusters(centroids, df, k):
    """This Assigns Clusters to closest centroid"""
    np.random.shuffle(df)
    divided_clusters = {i:np.empty([0, k]) for i in range(k)}
    for row in df:
        d0 = Euclidean_D(centroids[0], row)
        d1 = Euclidean_D(centroids[1], row)
        d2 = Euclidean_D(centroids[2], row)
        if min(d0, d1, d2) == d0:
            divided_clusters[0] = np.append(divided_clusters[0], [row], axis=0)
        elif min(d0, d1, d2) == d1:
            divided_clusters[1] = np.append(divided_clusters[1], [row], axis=0)
        elif min(d0, d1, d2) == d2:
            divided_clusters[2] = np.append(divided_clusters[2], [row], axis=0)
        else:
            print("Error")
    return divided_clusters

def cluster_out(centroids, clusters, k):
    """This function saves the centroids and the clusters in to a txt file"""
    for i in range(k):
        print("centroid ", i, ":", centroids[i])
        print("number of points in cluster = ", len(clusters[i]))
        print(clusters[i])
        with open("handCodedOut.txt", "w+") as file:

            file.write("centroid: 0 \n")
            file.write("number of points in cluser = " + str(len(clusters[0])) + "\n")
            file.write(str(clusters[0]) + "\n")

            file.write("centroid 1 \n")
            file.write("number of points in cluser = " + str(len(clusters[1])) + "\n")
            file.write(str(clusters[1]) + "\n")

            file.write("centroid 2 \n")
            file.write("number of points in cluser = " + str(len(clusters[2]))+  "\n")
            file.write(str(clusters[2]) + "\n")
            file.close()


def main():
    """This is the main Code that Runs the hand coded version of the K-means"""

    # Importing the Data
    df = pd.read_csv("exercise8_infile1.csv")
    df = df.values
    k = 3  # Number of Clusters

    # Selecting a k random clusters
    centroids = df[np.random.choice(df.shape[0], k, replace=False)]


    # Initializing the base case for the three clusters
    clusters = assign_clusters(centroids, df, k)
    for l in range(k):
        centroids[l] = np.mean(clusters[l], axis=0)

    # Could have used the while loop that we had with the group from mikes code
    # Just wanted to rip through the algorithm knowing this way can work if you set the iterations to a high number
    # That way it can be used later on larger data sets if I dont want to go through too many times
    iterations = 10000
    for _ in range(iterations):
        clusters = assign_clusters(centroids, df, k)
        for l in range(k):
            centroids[l] = np.mean(clusters[l], axis=0)

    # Sending the centroids and the clusters out to get outputted to a file
    cluster_out(centroids, clusters, k)


if __name__ == "__main__":
    main()
