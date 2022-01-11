import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics

data = pd.read_json("../../DataProcessing/Datasets/Sales/sales.json")
articleDF = pd.read_csv("../../DataProcessing/Datasets/Articles/articles.csv")

dictionary = {}
degree = 5

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
Y = dataFrame["quantity"].values

fit = np.polyfit(X, Y, deg=degree)
fit_function = np.poly1d(fit)
prediction = fit_function(X)

mse = metrics.mean_squared_error(Y, prediction)
mae = metrics.mean_absolute_error(Y, prediction)
rmse = (np.sqrt(mse))
r2_sq = metrics.r2_score(Y, prediction)

plt.scatter(dataFrame["date"], Y, s=5, label="Sold quantity in a day")
plt.plot(dataFrame["date"], prediction, color='red', label='Trend')
plt.title("Sales history for the product {} with grade {}\nMSE: {}    MAE: {}\nRMSE: {}    R-Squared: {}".format(articleDF.iloc[0]["Article"], degree, round(mse, 3), round(mae, 3), round(rmse, 3), round(r2_sq, 5)))
plt.xlabel("Date")
plt.ylabel("Sold quantity")
plt.legend(loc="best")

plt.show()
