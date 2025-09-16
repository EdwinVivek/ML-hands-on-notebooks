import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import adjusted_rand_score

# --- Example data (replace X with your dataset) ---
X, _ = make_blobs(n_samples=50000, centers=5, cluster_std=[1.0, 2.5, 0.5, 1.2, 0.8], random_state=42)



results = {}

# --- 1. Equal Variance ---
variances = []
for i in np.unique(labels):
    cluster_points = X[labels == i]
    var = np.var(cluster_points, axis=0).mean()  # mean variance across features
    variances.append(var)
results['cluster_variances'] = variances
results['variance_ratio'] = max(variances) / min(variances)

# --- 2. Similar Densities ---
densities = []
for i in np.unique(labels):
    cluster_points = X[labels == i]
    if cluster_points.shape[0] > 1:
        # Mean distance of points to centroid as density proxy
        dists = np.linalg.norm(cluster_points - centroids[i], axis=1)
        density = cluster_points.shape[0] / (dists.mean() + 1e-6)
    else:
        density = 0
    densities.append(density)
results['cluster_densities'] = densities
results['density_ratio'] = max(densities) / (min(densities) + 1e-6)

# --- 3. Same Size ---
cluster_sizes = [np.sum(labels == i) for i in np.unique(labels)]
results['cluster_sizes'] = cluster_sizes
results['size_ratio'] = max(cluster_sizes) / min(cluster_sizes)

# --- Put into DataFrame for readability ---
summary = pd.DataFrame({
    'Cluster': list(range(len(cluster_sizes))),
    'Variance': variances,
    'Density': densities,
    'Size': cluster_sizes
})

print("--- Cluster Summary ---")
print(summary)
print("\nVariance Ratio (max/min):", results['variance_ratio'])
print("Density Ratio (max/min):", results['density_ratio'])
print("Size Ratio (max/min):", results['size_ratio'])



# --- Stability Check Parameters ---
n_runs = 20  # how many times to re-run KMeans
n_clusters = 5

# Store labels from multiple runs
all_labels = []
for seed in range(n_runs):
    km = KMeans(n_clusters=n_clusters, random_state=seed, n_init=10)
    labels = km.fit_predict(X)
    all_labels.append(labels)

# --- Compute stability (pairwise adjusted rand index between runs) ---
stability_scores = []
for i in range(n_runs):
    for j in range(i + 1, n_runs):
        score = adjusted_rand_score(all_labels[i], all_labels[j])
        stability_scores.append(score)

avg_stability = np.mean(stability_scores)

print("Average stability across runs (ARI):", avg_stability)

# --- Track how often each point is assigned to the same cluster ---
all_labels = np.array(all_labels)
consistency = []
for idx in range(X.shape[0]):
    # most common label for this point across runs
    vals, counts = np.unique(all_labels[:, idx], return_counts=True)
    consistency.append(np.max(counts) / n_runs)

consistency = np.array(consistency)

print("\nOverall mean point consistency:", consistency.mean())
print("Fraction of points with >90% consistent assignment:", np.mean(consistency > 0.9))

# --- Inspect small cluster stability ---
final_kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10).fit(X)
final_labels = final_kmeans.labels_

smallest_cluster = np.argmin([np.sum(final_labels == i) for i in range(n_clusters)])
small_cluster_points = np.where(final_labels == smallest_cluster)[0]
small_consistency = consistency[small_cluster_points]

print("\nSmallest cluster size:", len(small_cluster_points))
print("Smallest cluster mean consistency:", small_consistency.mean())
