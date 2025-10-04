import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("Iris.csv")

# Encode species into numbers
species_map = {'Iris-setosa': 1, 'Iris-versicolor': 2, 'Iris-virginica': 3}
df['Species'] = df['Species'].map(species_map)

# Features and target
X = df.iloc[:, 1:5].values   # SepalLength, SepalWidth, PetalLength, PetalWidth
Y = df['Species'].values     # Encoded species (1, 2, 3)

# Train Multiple Linear Regression model
model = LinearRegression()
model.fit(X, Y)

# Predict for new flower
new_flower = [[5.4, 3.2, 1.2, 0.1]]
pred_value = model.predict(new_flower)[0]

# Round to nearest class
pred_class = int(round(pred_value))
pred_species = {1: "Iris-setosa", 2: "Iris-versicolor", 3: "Iris-virginica"}.get(pred_class, "Unknown")

print("Raw prediction (continuous):", pred_value)
print("Predicted Species:", pred_species)
