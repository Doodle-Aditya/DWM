import pandas as pd
from math import log2

# Load dataset
df = pd.read_csv("dataset.csv")

# Entropy function
def entropy(col):
    probs = col.value_counts(normalize=True)
    return -sum(p * log2(p) for p in probs)

# Total entropy of class
total_entropy = entropy(df['class'])
print("Total Entropy:", round(total_entropy, 4))

# Info Gain for each attribute
for attr in df.drop('class', axis=1):
    weighted_entropy = 0
    for val, subset in df.groupby(attr):
        weighted_entropy += len(subset)/len(df) * entropy(subset['class'])
    ig = total_entropy - weighted_entropy
    print(f"{attr} → IG: {round(ig, 4)}")
