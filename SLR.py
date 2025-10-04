import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("salary.csv")

# Independent (X) and dependent (Y) variables
X = df.iloc[:, 0].values.reshape(-1, 1)   # reshape needed for sklearn
Y = df.iloc[:, 1].values

# Train model
model = LinearRegression()
model.fit(X, Y)

# Prediction
Exp = float(input("Enter Experience: "))
pred_salary = model.predict([[Exp]])

print("Predicted Salary:", round(pred_salary[0], 2))
