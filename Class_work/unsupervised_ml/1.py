# from sklearn.cluster import KMeans 
# import pandas as pd


# data ={
#     "income" : [10,12,15,50,60,75,22,33,43,70]
# }
# df =pd.DataFrame(data)
# k_means =KMeans(n_clusters=4,random_state=42)

# df['cluster']=k_means.fit_predict(df)

# print(df)
# print("centroid :",k_means.cluster_centers_)  # centroid 

from sklearn.cluster import KMeans 
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "income" : [10,12,15,50,60,75,22,33,43,70]
}
df = pd.DataFrame(data)

# 1. The Loop: Calculate WCSS for K=1 through K=9
wcss = []
for i in range(1, 10):
    # n_init='auto' silences a common scikit-learn warning
    kmeans = KMeans(n_clusters=i, random_state=42, n_init='auto')
    kmeans.fit(df[['income']])
    wcss.append(kmeans.inertia_)

# 2. Plot the Elbow Graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, 10), wcss, marker='o', linestyle='--')
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS (Inertia)')
plt.grid(True)
plt.show()