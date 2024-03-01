# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 08:53:08 2023

@author: shrik
"""

# Assignment 1 -----------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load crime data and display basic information
cd = pd.read_csv('c:/Data_sets/crime_data.csv')
cd.columns
cd.shape
cd.dtypes

# Drop the 'Unnamed: 0' column as it appears to be unnecessary
cd.drop(['Unnamed: 0'], axis=1, inplace=True)

# Display basic summary statistics of the data
cd.describe()

# Normalize the data to ensure all features are on a similar scale (0 to 1)
def normalize(i):
    x = (i - i.min()) / (i.max() - i.min())
    return x

cd_norm = normalize(cd)
cd_norm.describe()

# Visualize the hierarchical clustering of the crime data
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

cd1 = linkage(cd_norm, method='complete', metric='euclidean')
plt.figure(figsize=(10, 5))
plt.title("Crime data in hierarchical clustering")
sch.dendrogram(cd1, leaf_rotation=0, leaf_font_size=10)
plt.show()

# Apply agglomerative clustering to the normalized data
from sklearn.cluster import AgglomerativeClustering
crime = AgglomerativeClustering(n_clusters=4, linkage='complete', affinity='euclidean').fit(cd_norm)
crime.labels_
cluster_labels = pd.Series(crime.labels_)
cd_norm['Cluster'] = cluster_labels
res = cd_norm.groupby(cd_norm.Cluster).mean()

# Save the clustered data to a CSV file
cd_norm.to_csv("Crimes_cluster.csv", encoding='utf-8')

# Change the working directory to the current directory
import os
os.getcwd()


# Assignment 2-----------------------------------------------------------------

# Load airline data and display basic information
import pandas as pd
import matplotlib.pyplot as plt

air = pd.read_excel('c:/Data_sets/EastWestAirlines.xlsx')
air.dtypes
air.shape
air.columns

# Drop the 'ID#' column as it appears to be unnecessary
air.drop(['ID#'], axis=1, inplace=True)

# Display basic summary statistics of the data
al = air.describe()

# Normalize the data to ensure all features are on a similar scale (0 to 1)
def normalize(i):
    x = (i - i.min()) / (i.max() - i.min())
    return x

air_norm = normalize(air)
al_des = air_norm.describe()

# Visualize the hierarchical clustering of the airline data
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

airline = linkage(air_norm, method='complete', metric='euclidean')
plt.figure(figsize=(15, 8))
plt.title("Clustering on Airline Data")
sch.dendrogram(airline, leaf_rotation=0, leaf_font_size=10)
plt.show()

# Apply agglomerative clustering to the normalized data
from sklearn.cluster import AgglomerativeClustering
air1 = AgglomerativeClustering(n_clusters=10, linkage='complete', affinity='euclidean').fit(air_norm)
air1.labels_
cluster_labels = pd.Series(air1.labels_)
air_norm['Cluster'] = cluster_labels
r1 = air_norm.groupby(air_norm.Cluster).mean()

# Save the clustered data to a CSV file
air_norm.to_csv("Airlines_cluster.csv", encoding='utf-8')

# Change the working directory to the current directory
import os
os.getcwd()

