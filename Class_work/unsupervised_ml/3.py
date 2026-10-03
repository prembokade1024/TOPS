"""import  pandas as pd 
import numpy as np 
from sklearn.cluster  import DBSCAN
from sklearn.decomposition import PCA 
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler 
import matplotlib.pyplot as plt


df = pd.read_csv("Mall_Customers.csv")
# print(df.head())

# feature selection:
X=df[['Age','Annual Income (k$)','Spending Score (1-100)']]

# sclae the data :

scaler = StandardScaler()
x_scaled = scaler.fit_transform(X)

# apply pca :
pca = PCA(n_components=2)
X_pca = pca.fit_transform(x_scaled)

# explain the variance :

pca_variance = pca.explained_variance_ratio_
sum_explained_variance = np.sum(pca_variance)
print(sum_explained_variance)

# datafram  of the  pca : 

df_pca = pd.DataFrame(
    X_pca,
    columns=['PCA1', 'PCA2']
    
)
print(df_pca) 

# plot pca 1 ,pca 2 :

plt.figure(figsize=(8, 5))
plt.scatter(
    df_pca['PCA1'],
    df_pca['PCA2'],
    c=df['Spending Score (1-100)'],
    s=100
)
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('PCA')
plt.show()

neighbours = NearestNeighbors(n_neighbors=6).fit(x_scaled)
distances, indices = neighbours.kneighbors(x_scaled)

print(distances,indices)
k_distance =distances[:,2]
k_distance = np.sort(k_distance)

plt.figure(figsize=(10,10))
plt.plot(k_distance)
plt.title("neighboring points")
plt.grid(True)
plt.show()


db = DBSCAN(eps=0.7, min_samples=6).fit(X_pca) 

df['cluster'] = db.labels_

# display the cluster labels :
print(df['cluster'].values)
noise_points = df[df["cluster"] == -1]
print(noise_points)


# graph DBSCAN Clusters
plt.figure(figsize=(8, 5))
plt.scatter(
    x_scaled[:, 0],
    x_scaled[:, 1],
    c=df["cluster"],
    s=100
)
plt.xlabel("Income (Scaled)")
plt.ylabel("Spending Score (Scaled)")
plt.title("DBSCAN Clustering")
plt.show()

# hightlight  Noise Points
plt.figure(figsize=(8, 5))
plt.scatter(
    x_scaled[df["cluster"] != -1, 0],
    x_scaled[df["cluster"] != -1, 1],
    c=df.loc[df["cluster"] != -1, "cluster"],
    s=100
)
# Plot noise points separately
plt.scatter(
    x_scaled[df["cluster"] == -1, 0],
    x_scaled[df["cluster"] == -1, 1],
    marker="x",
    s=150,
    label="Noise"
)
plt.xlabel("Income (Scaled)")
plt.ylabel("Spending Score (Scaled)")
plt.title("DBSCAN - Clusters and Noise")
plt.legend()
plt.show()

"""

import pandas as pd  
import numpy as np  
from sklearn.cluster import DBSCAN 
from sklearn.decomposition import PCA  
from sklearn.neighbors import NearestNeighbors 
from sklearn.preprocessing import StandardScaler  
import matplotlib.pyplot as plt 
 
 
df = pd.read_csv("Mall_Customers.csv") 
# print(df.head()) 
 
# feature selection: 
X = df[['Age','Annual Income (k$)','Spending Score (1-100)']] 
 
# scale the data : 
 
scaler = StandardScaler() 
x_scaled = scaler.fit_transform(X) 
 
# apply pca : 
pca = PCA(n_components=2) 
X_pca = pca.fit_transform(x_scaled) 
 
# explain the variance : 
 
pca_variance = pca.explained_variance_ratio_ 
sum_explained_variance = np.sum(pca_variance) 
print(sum_explained_variance) 
 
# dataframe of the pca :  
 
df_pca = pd.DataFrame( 
    X_pca, 
    columns=['PCA1', 'PCA2'] 
) 

print(df_pca)  
 
# plot pca 1 ,pca 2 : 
 
plt.figure(figsize=(8, 5)) 
plt.scatter( 
    df_pca['PCA1'], 
    df_pca['PCA2'], 
    c=df['Spending Score (1-100)'], 
    s=100 
) 

plt.xlabel('PCA1') 
plt.ylabel('PCA2') 
plt.title('PCA') 
plt.show() 
 
# ------------------------------------------------
# CHANGED: use X_pca because DBSCAN is applied
# on X_pca
# ------------------------------------------------

neighbours = NearestNeighbors(n_neighbors=6).fit(X_pca) 

distances, indices = neighbours.kneighbors(X_pca) 
 
# CHANGED: 6th nearest neighbour
# index 5 because indexing starts from 0

k_distance = distances[:,5] 
k_distance = np.sort(k_distance) 
 
plt.figure(figsize=(10,10)) 
plt.plot(k_distance) 

plt.title("neighboring points") 
plt.grid(True) 
plt.show() 
 
 
db = DBSCAN(eps=0.7, min_samples=6).fit(X_pca)  
 
df['cluster'] = db.labels_ 
 
# display the cluster labels : 
print(df['cluster'].values) 

# ------------------------------------------------
# ADDED: find number of clusters
# -1 represents noise, so exclude it
# ------------------------------------------------

n_clusters = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)

print("Number of clusters:", n_clusters)

# ADDED: count noise points

n_noise = list(db.labels_).count(-1)

print("Number of noise points:", n_noise)

# ADDED: number of customers in each cluster

print("Customers in each cluster:")
print(df['cluster'].value_counts().sort_index())


noise_points = df[df["cluster"] == -1] 
print(noise_points) 
 
 
# graph DBSCAN Clusters 

# CHANGED: X_pca instead of x_scaled
# because DBSCAN was applied on X_pca

plt.figure(figsize=(8, 5)) 

plt.scatter( 
    X_pca[:, 0], 
    X_pca[:, 1], 
    c=df["cluster"], 
    s=100 
) 

plt.xlabel("PCA1") 
plt.ylabel("PCA2") 
plt.title("DBSCAN Clustering") 
plt.show() 
 
 
# highlight Noise Points 

# CHANGED: X_pca instead of x_scaled

plt.figure(figsize=(8, 5)) 

plt.scatter( 
    X_pca[df["cluster"] != -1, 0], 
    X_pca[df["cluster"] != -1, 1], 
    c=df.loc[df["cluster"] != -1, "cluster"], 
    s=100 
) 

# Plot noise points separately 

plt.scatter( 
    X_pca[df["cluster"] == -1, 0], 
    X_pca[df["cluster"] == -1, 1], 
    marker="x", 
    s=150, 
    label="Noise" 
) 

plt.xlabel("PCA1") 
plt.ylabel("PCA2") 
plt.title("DBSCAN - Clusters and Noise") 
plt.legend() 
plt.show()