from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

data = pd.read_json("../../DataProcessing/Datasets/Sales/salestest.json")

dictionary = {}

for i in range(data.shape[0]):
    #date = to_integer(pd.Timestamp(data.iloc[i][0]).date())
    date = pd.Timestamp(data.iloc[i][0]).date()
    if date not in dictionary:
        dictionary[date] = 0
    for j in range(len(data.iloc[i][1])):
        if data.iloc[i][1][j]["articleId"] == 1:
            dictionary[date] = dictionary[date] + data.iloc[i][1][j]["quantity"]

columns = ["date", "quantity"]
data_items = dictionary.items()
data_list = list(data_items)
dataFrame = pd.DataFrame(data_list, columns=columns)
dataFrame.date = pd.to_datetime(dataFrame.date)


print(dataFrame)


X = dataFrame.date.values.reshape(-1, 1)
Y = dataFrame["quantity"].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

linear_regressor = LinearRegression().fit(X,Y)  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_predictions = ["2021-11-01", "2021-11-02"]
Y_pred = linear_regressor.predict(dataFrame.date.values.astype(float).reshape(-1, 1))  # make predictions

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.show()

