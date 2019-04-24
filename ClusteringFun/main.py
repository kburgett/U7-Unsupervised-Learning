import numpy as np
import pandas as pd

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

if __name__ == "__main__":
    main()