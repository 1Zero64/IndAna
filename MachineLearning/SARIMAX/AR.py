# https://vitalflux.com/autoregressive-ar-models-with-python-examples/
import pandas as pd
from statsmodels.tsa.ar_model import AutoReg as AR
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_pacf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

weatherDF = pd.read_csv("../../DataProcessing/Datasets/Weather/weather_012016-102021.csv")

weatherDF['date'] = pd.to_datetime(weatherDF['date'], format='%Y-%m-%d')
weatherDF['date'] = (weatherDF['date'] - weatherDF['date'].min())  / np.timedelta64(1,'D')

weatherStationaryTest = adfuller(weatherDF['tavg'], autolag='AIC')

print("P-Value: ", weatherStationaryTest[1])

X = weatherDF.values

trainData = X[:int(len(X)*0.8)]
testData = X[int(len(X)*0.8)+1:]

arModel = AR(trainData, lags=12).fit()
print(arModel.summary())


predictions = arModel.predict(start=len(trainData)+1, end=len(weatherDF)-1, dynamic=False)

for i in range(len(testData)):
	print('predicted=%f, expected=%f' % (predictions.values[i], testData.values[i]))
rmse = sqrt(mean_squared_error(testData, predictions))
print(rmse)


plt.plot(testData)
plt.plot(predictions, color='red')

plt.show()