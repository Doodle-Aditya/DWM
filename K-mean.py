l = list(map(int, input("Numbers (comma-separated): ").split(",")))
k = int(input("Enter K: "))

# Initialize centroids as the first k elements
centroids = l[:k]

while True:
    # Create empty clusters
    clusters = [[] for _ in range(k)]
    
    # Assign each point to the nearest centroid
    for val in l:
        idx = min(range(k), key=lambda i: abs(val - centroids[i]))
        clusters[idx].append(val)
    
    # Recompute centroids
    new_centroids = [
        sum(c)/len(c) if c else centroids[i]
        for i, c in enumerate(clusters)
    ]
    
    # Stop if centroids don't change
    if new_centroids == centroids:
        break
    
    centroids = new_centroids

print("Final Clusters:", clusters)
print("Centroids:", centroids)
