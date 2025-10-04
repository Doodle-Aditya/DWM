import pandas as pd


df = pd.read_csv("dataset.csv")

age = input("Age: ")
income = input("Income: ")
student = input("Student (yes/no): ")
credit = input("Credit rating: ")


subset = df[
    (df['age'] == age) &
    (df['income'] == income) &
    (df['student'] == student) &
    (df['credit_rating'] == credit)
]

if not subset.empty:
    pred_class = subset['class'].mode()[0] 
else:
    pred_class = df['class'].mode()[0]   

print("Predicted class:", pred_class.upper())
