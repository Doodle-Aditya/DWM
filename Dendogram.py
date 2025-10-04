import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import load_iris

iris = load_iris()
Z = linkage(iris.data, method="ward")  # linkage matrix

plt.title("Hierarchical Clustering Dendrogram (Iris)")
dendrogram(Z, truncate_mode="level", p=3)
plt.xlabel("Sample index or cluster size")
plt.ylabel("Distance")
plt.show()
