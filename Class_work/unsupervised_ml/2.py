import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1. Read Dataset
df = pd.read_csv("Mall_Customers.csv")

# 2. Select Features
X = df[[
    "Age",
    "Annual_Income",
    "Spending_Score"
]]

# 3. Train Test Split
X_train, X_test = train_test_split(
    X,
    test_size=0.3,
    random_state=42
)
print("Training:", X_train.shape)
print("Testing:", X_test.shape)

# 4. Standardization
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Apply PCA (Reduce to 2 Dimensions)
pca = PCA(n_components=2, random_state=42)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

print(f"\nExplained Variance Ratio by PC1 and PC2: {pca.explained_variance_ratio_}")

# 6. Create KMeans
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# 7. Train Model on PCA Data
kmeans.fit(X_train_pca)

# 8. Training Data Prediction
train_clusters = kmeans.predict(X_train_pca)
print("\nTraining Clusters:")
print(train_clusters)

# 9. Test Data Prediction
test_clusters = kmeans.predict(X_test_pca)
print("\nTest Clusters:")
print(test_clusters)

# 10. Show Test Result
test_result = X_test.copy()
test_result["Cluster"] = test_clusters
print("\nTest Result:")
print(test_result)

# 11. NEW CUSTOMER
new_customer = pd.DataFrame({
    "Age": [27],
    "Annual_Income": [32000],
    "Spending_Score": [85]
})

# Scale and apply PCA to new customer
new_customer_scaled = scaler.transform(new_customer)
new_customer_pca = pca.transform(new_customer_scaled)

# Predict cluster
new_cluster = kmeans.predict(new_customer_pca)
print("\nNew Customer:")
print(new_customer)
print("New Customer belongs to Cluster:", new_cluster[0])

# 12. Centroids (Now in 2D PCA Space)
print("\nCluster Centers (PCA Space):")
print(kmeans.cluster_centers_)

# 13. K-Means clustering graph (Using Principal Components)
plt.scatter(
    X_train_pca[:, 0],
    X_train_pca[:, 1],
    c=train_clusters,
    s=50,
    cmap="viridis",
    alpha=0.7,
    edgecolors="k"
)

# Plot Centroids
centroids = kmeans.cluster_centers_
plt.scatter(
    centroids[:, 0], 
    centroids[:, 1], 
    c='red', 
    s=200, 
    marker='X', 
    label='Centroids'
)

plt.title("K-Means Clustering with PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.show()

# 14. Silhouette Score (calculated on PCA data)
silhouette_avg = silhouette_score(X_train_pca, kmeans.labels_)
print("The average silhouette_score is:", silhouette_avg)