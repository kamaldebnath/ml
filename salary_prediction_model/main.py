# packages
import pandas as pd
from sklearn.linear_model import LinearRegression
salary=pd.read_csv('salary.csv')

# split the dataset into features and target

X= salary.drop(columns=['Salary'])
y=salary['Salary']


# model setup

model = LinearRegression()
model.fit(X,y)

predictions = model.predict([[0],[11],[9.7]])
print(predictions)
