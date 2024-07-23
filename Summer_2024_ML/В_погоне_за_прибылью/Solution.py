import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Load data from file
data_path = "/Users/melodiz/projects/CodeRun/Summer_2024_ML/В_погоне_за_прибылью/data.txt"
file = open(data_path, 'r')
k, n, cost, C = list(map(int, file.readline().split()))
houses = [tuple(map(int, line.split())) for line in file]
houses_df = pd.DataFrame(houses, columns=['x', 'y'])

# Perform KMeans clustering
kmeans = KMeans(n_clusters=k)
kmeans.fit(houses_df[['x', 'y']])
houses_df['cluster'] = kmeans.labels_

# Calculate centroids of clusters
centroids = houses_df.groupby('cluster').mean()
centroids_list = centroids[['x', 'y']].to_numpy().tolist()
places_df = pd.DataFrame(centroids_list, columns=['x', 'y'])

# Function to calculate Euclidean distance
def euclidean_distance(house, centroid):
    return np.sqrt((house['x'] - centroid['x'])**2 + (house['y'] - centroid['y'])**2)

# Calculate distance between each house and its corresponding centroid
houses_df['distance'] = houses_df.apply(
    lambda house: euclidean_distance(house, centroids.loc[house['cluster']]), axis=1)

# Add cluster information to centroids DataFrame
centroids['cluster'] = centroids.index.tolist()

# Function to calculate expected profit
def calculate_expected_profit(C, cost, houses_df, k):
    total_cost = 0
    for cluster in range(k):
        cluster_houses = houses_df[houses_df['cluster'] == cluster]
        for _, house in cluster_houses.iterrows():
            distance = house['distance']
            total_cost += cost * ((distance ** (1/4)) + 1) / len(cluster_houses)
    
    expected_profit = C - total_cost
    return expected_profit

# Calculate and print total expected profit
total_expected_profit = calculate_expected_profit(C, cost, houses_df, k)
print(f"Total Expected Profit: {total_expected_profit}")