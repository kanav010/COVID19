import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

table = pd.read_csv("State.csv")
print(table)

X = table.Active.values
Y = table.Deaths.values


plt.scatter(X, Y)
plt.show()

X = X.reshape(len(X), 1)
Y = Y.reshape(len(Y), 1)


model = LinearRegression()
