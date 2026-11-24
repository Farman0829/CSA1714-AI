import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


X, y = make_blobs(
    n_samples=100,
    centers=3,
    cluster_std=1.0,
    random_state=42
)


kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

kmeans.fit(X)


labels = kmeans.labels_
centroids = kmeans.cluster_centers_


print("Cluster Labels:")
print(labels)

print("\nCluster Centroids:")
print(centroids)

print("\nNumber of Clusters:", kmeans.n_clusters)


plt.scatter(
    X[:, 0], X[:, 1],
    c=labels,
    cmap='viridis',
    s=50
)

plt.scatter(
    centroids[:, 0], centroids[:, 1],
    color='red',
    marker='X',
    s=200,
    label='Centroids'
)

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
