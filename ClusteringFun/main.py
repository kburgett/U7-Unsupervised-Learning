import numpy as np
import pandas as pd
# scipy is a library for scientific computing
import scipy.spatial.distance as distance

def main():
    # k means clustering
    # 1. pick a value of k
    # 2. select k instances to serve as the k initial centroids
    # 3. assign each instance to its "nearest" cluster
    # 4. re-calculate the centroids
    # 5. repeat steps 3 and 4 until the centroids no longer "move"

    # the instances chosen for initial centroids can affect
    # the set of final clusters
    # k means clustering is a greedy algorithm
    # choose the "nearest" cluster... this is choosing
    # local optima, not a global optima
    # will get a local optimal solution (set of clusters)
    # but not guaranteed to give you a global optimal solution
    # so... run k means multiple times for each k

    # what happens if k = 1? "one giant cluster" original dataset
    # what happens if k = n? one cluster per instance original dataset
    # why cluster? data exploration/visualization
    # data reduction, data prediction

    # pandas
    # pandas is data analysis library built on numpy
    # numpy is a numerical computing library
    # beauty of pandas: data structures and advanced (label) indexing
    # 1D: Series
    # 2D: Dataframe
    # 3D: Panel

    ser = pd.Series(["a", "b", "c"], index=["att1", "att2", "att3"])
    print(ser)
    print(ser.index)

    # lets read in our shirt_sizes.csv into a dataframe
    df = pd.read_csv("shirt_sizes.csv")
    print(df)
    print(df.index)
    print(df.columns)
    # remove the leading whitespace on the header names
    df.columns = df.columns.str.strip()
    print(df.columns)

    # indexing
    # use loc for label based indexing
    # iloc for integer based indexing
    print(df.loc[0, :]) # first row
    print(df.loc[:, "weight(kg)"]) # weight column
    print(df.describe())
    stats_df = df.describe()
    print(stats_df)
    # task: print out max weight (68)
    print(stats_df.loc["max", "weight(kg)"]) 

    # lets get rid of the size column
    # cluster on weight and height
    df = df.drop("size(t-shirt)", axis=1) # 1 is for columns
    print(df)

    k = 2
    clusters = perform_k_means_clustering(df, k)

def perform_k_means_clustering(df, k):
    # 1. pick a value of k
    # done!!

    # 2. select k instances to serve as the k initial centroids
    # lets add a column for the cluster number
    df["cluster"] = np.nan # broadcasted
    print(df)
    rand_df = df.sample(k, replace=False)
    print(rand_df)
    for i in range(k):
        row = rand_df.iloc[i, :]
        print(row.name)
        # task: update the cluster number appropriately
        df.loc[row.name, "cluster"] = i
    print(df)
    # task: calculate the centroids
    centroids = compute_centroids(df, k)

    # 3. assign each instance to its "nearest" cluster
    # for each instance in df
    for index in df.index:
        instance = df.loc[index, :]
        nearest_centroid_index = find_nearest_centroid(instance, centroids)

    # 4. re-calculate the centroids
    # 5. repeat steps 3 and 4 until the centroids no longer "move"

def find_nearest_centroid(instance, centroids):
    dists = []
    for i in range(len(centroids)):
        dist = distance.euclidean(instance.iloc[:-1], centroids[i])
        dists.append(dist)
    #print(dists)
    return dists.index(min(dists))

def compute_centroids(df, k):
    centroids = []
    # for each value of k
    # grab a subset of df with cluster equal to k value
    # compute the average of that subset
    for i in range(k):
        # boolean indexing
        #print(df["cluster"] == i)
        cluster = df[df["cluster"] == i]
        print(cluster)
        centroids.append(cluster.iloc[:,:-1].mean())
    #print(centroids)

    return centroids



if __name__ == "__main__":
    main()