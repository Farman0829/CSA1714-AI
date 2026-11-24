from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


data = load_iris()
X = data.data

print("Original Dataset Shape:", X.shape)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)


print("\nReduced Dataset Shape:", X_pca.shape)

print("\nFirst 5 Rows of Reduced Data:")
print(X_pca[:5])


print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nTotal Variance Retained:",
      sum(pca.explained_variance_ratio_) * 100, "%")
