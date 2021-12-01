import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import cross_val_score

def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

data = pd.read_json("../../DataProcessing/Datasets/Sales/salestest.json")

dictionary = {}

for i in range(data.shape[0]):
    #date = to_integer(pd.Timestamp(data.iloc[i][0]).date())
    date = pd.Timestamp(data.iloc[i][0])
    if date not in dictionary:
        dictionary[date] = 0
    for j in range(len(data.iloc[i][1])):
        if data.iloc[i][1][j]["articleId"] == 1:
            dictionary[date] = dictionary[date] + data.iloc[i][1][j]["quantity"]

columns = ["date", "quantity"]
data_items = dictionary.items()
data_list = list(data_items)
dataFrame = pd.DataFrame(data_list, columns=columns)
dataFrame["date"] = dataFrame["date"].dt.date

X = np.arange(dataFrame['date'].size)
#X = dataFrame["date"].values
Y = dataFrame["quantity"].values

degree = 12
fit = np.polyfit(X, Y, deg=degree)
fit_function = np.poly1d(fit)

plt.scatter(dataFrame["date"], Y, s=5, label="Verkaufsmenge am Tag")
plt.plot(dataFrame["date"], fit_function(X), color='red', label='Trend')
plt.title("Verkaufsverlauf für das Produkt Apfel mit Grad {}".format(degree))
plt.xlabel("Datum")
plt.ylabel("Verkaufsmenge")
plt.legend(loc="best")

plt.show()
