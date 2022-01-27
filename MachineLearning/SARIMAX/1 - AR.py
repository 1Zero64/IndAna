# python3 1 - AR.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Niko Kauz
# Description: Visualisation and testing of the Auto Regression (AR) model
# ===========================================================================================

from pandas.plotting import autocorrelation_plot
from pandas.plotting import lag_plot
from pandas import DataFrame
from pandas import concat
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.ar_model import AutoReg
from math import sqrt
import pandas as pd


# AutoRegression for sales to test

def autoRegression(articleId):
    '''
        Calculates and plots the auto regression of the sales for a article

        :param articleId: (int)
                identifier of a article
        '''
    articleColumn = "articleId_" + str(articleId)

    salesDF = pd.read_csv('../../DataProcessing/Datasets/merged1.csv')
    salesDF.date = pd.to_datetime(salesDF.date)
    salesDF = salesDF[['date', articleColumn]]
    salesDF = salesDF.set_index("date", drop=True, append=False, inplace=False, verify_integrity=False)
    salesDF = salesDF.fillna(0)

    lag_plot(salesDF)
    pyplot.show()

    salesDF.plot()
    pyplot.show()

    values = DataFrame(salesDF.values)
    print(values.shift(1))
    dataFrame = concat([values.shift(1), values], axis=1)
    dataFrame.columns = ['t-1', 't+1']
    result = dataFrame.corr()
    print(result)
    autocorrelation_plot(salesDF)
    pyplot.show()

    plot_acf(salesDF, lags=20)
    pyplot.show()

    # create lagged dataset
    values = DataFrame(salesDF.values)
    dataFrame = concat([values.shift(1), values], axis=1)
    dataFrame.columns = ['t-1', 't+1']
    # split into train and test sets

    X = dataFrame.values
    train, test = X[1:len(X) - 100], X[len(X) - 100:]
    train_X, train_y = train[:, 0], train[:, 1]
    test_X, test_y = test[:, 0], test[:, 1]

    #  persistence model
    def model_persistence(x):
        return x

    # walk-forward validation
    predictions = list()
    for x in test_X:
        yhat = model_persistence(x)
        predictions.append(yhat)
    test_score = mean_squared_error(test_y, predictions)
    print('Test MSE: %.3f' % test_score)
    # plot predictions vs expected
    pyplot.plot(test_y)
    pyplot.plot(predictions, color='red')
    pyplot.show()

    # train autoregression
    X = salesDF.values
    train, test = X[1:len(X) - 100], X[len(X) - 100:]
    model = AutoReg(train, lags=20)
    model_fit = model.fit()
    print('Coefficients: %s' % model_fit.params)
    # make predictions
    predictions = model_fit.predict(start=len(train), end=len(train) + len(test) - 1, dynamic=False)

    rmse = sqrt(mean_squared_error(test, predictions))
    print('Test RMSE: %.3f' % rmse)
    # plot results
    pyplot.plot(test)
    pyplot.plot(predictions, color='red')
    pyplot.show()

    # split dataset
    # train autoregression
    window = 20
    model = AutoReg(train, lags=20)
    model_fit = model.fit()
    coef = model_fit.params
    # walk forward over time steps in test
    history = train[len(train) - window:]
    history = [history[i] for i in range(len(history))]
    predictions = list()
    for t in range(len(test)):
        length = len(history)
        lag = [history[i] for i in range(length - window, length)]
        yhat = coef[0]
        for d in range(window):
            yhat += coef[d + 1] * lag[window - d - 1]
        obs = test[t]
        predictions.append(yhat)
        history.append(obs)
        # print('predicted=%f, expected=%f' % (yhat, obs))
    rmse = sqrt(mean_squared_error(test, predictions))
    print('Test RMSE: %.3f' % rmse)
    # plot
    pyplot.plot(test)
    pyplot.plot(predictions, color='red')
    pyplot.show()

    window = 20
    model = AutoReg(train, lags=20)
    model_fit = model.fit()
    coef = model_fit.params
    # walk forward over time steps in test
    history = train[len(train) - window:]
    history = [history[i] for i in range(len(history))]
    predictions = list()
    for t in range(len(test)):
        length = len(history)
        lag = [history[i] for i in range(length - window, length)]
        yhat = coef[0]
        for d in range(window):
            yhat += coef[d + 1] * lag[window - d - 1]
        obs = test[t]
        predictions.append(yhat)
        history.append(obs)
        # print('predicted=%f, expected=%f' % (yhat, obs))

    rmse = sqrt(mean_squared_error(test, predictions))
    print('Test RMSE: %.3f' % rmse)
    # plot
    pyplot.plot(test)
    pyplot.plot(predictions, color='red')
    pyplot.show()


if __name__ == '__main__':
    wishedArticleId = 1
    autoRegression(wishedArticleId)


# 	Auto Regression for weather to test.
#	Comment out to see results
"""
weatherDF = read_csv('../../DataProcessing/Datasets/Weather/weather_012016-102021.csv', index_col=0)
weatherDF = weatherDF.loc[:, "tavg"]

print(weatherDF.head())
print(weatherDF.dtypes)

lag_plot(weatherDF)
pyplot.show()

weatherDF.plot()
pyplot.show()

values = DataFrame(weatherDF.values)
print(values.shift(1))
dataFrame = concat([values.shift(1), values], axis=1)
dataFrame.columns = ['t-1', 't+1']
result = dataFrame.corr()
print(result)
autocorrelation_plot(weatherDF)
pyplot.show()

plot_acf(weatherDF, lags=20)
pyplot.show()

# create lagged dataset
values = DataFrame(weatherDF.values)
dataFrame = concat([values.shift(1), values], axis=1)
dataFrame.columns = ['t-1', 't+1']
# split into train and test sets
X = dataFrame.values
train, test = X[1:len(X) - 7], X[len(X) - 7:]
train_X, train_y = train[:, 0], train[:, 1]
test_X, test_y = test[:, 0], test[:, 1]


#  persistence model
def model_persistence(x):
    return x


# walk-forward validation
predictions = list()
for x in test_X:
    yhat = model_persistence(x)
    predictions.append(yhat)
test_score = mean_squared_error(test_y, predictions)
print('Test MSE: %.3f' % test_score)
# plot predictions vs expected
pyplot.plot(test_y)
pyplot.plot(predictions, color='red')
pyplot.show()

# train autoregression
X = weatherDF.values
train, test = X[1:len(X) - 7], X[len(X) - 7:]
model = AutoReg(train, lags=20)
model_fit = model.fit()
print('Coefficients: %s' % model_fit.params)
# make predictions
predictions = model_fit.predict(start=len(train), end=len(train) + len(test) - 1, dynamic=False)
for i in range(len(predictions)):
    print('predicted=%f, expected=%f' % (predictions[i], test[i]))
rmse = sqrt(mean_squared_error(test, predictions))
print('Test RMSE: %.3f' % rmse)
# plot results
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()

# split dataset
train, test = X[1:len(X) - 7], X[len(X) - 7:]
# train autoregression
window = 20
model = AutoReg(train, lags=20)
model_fit = model.fit()
coef = model_fit.params
# walk forward over time steps in test
history = train[len(train) - window:]
history = [history[i] for i in range(len(history))]
predictions = list()
for t in range(len(test)):
    length = len(history)
    lag = [history[i] for i in range(length - window, length)]
    yhat = coef[0]
    for d in range(window):
        yhat += coef[d + 1] * lag[window - d - 1]
    obs = test[t]
    predictions.append(yhat)
    history.append(obs)
    print('predicted=%f, expected=%f' % (yhat, obs))
rmse = sqrt(mean_squared_error(test, predictions))
print('Test RMSE: %.3f' % rmse)
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()


train, test = X[1:len(X) - 100], X[len(X) - 100:]
window = 20
model = AutoReg(train, lags=20)
model_fit = model.fit()
coef = model_fit.params
# walk forward over time steps in test
history = train[len(train) - window:]
history = [history[i] for i in range(len(history))]
predictions = list()
for t in range(len(test)):
    length = len(history)
    lag = [history[i] for i in range(length - window, length)]
    yhat = coef[0]
    for d in range(window):
        yhat += coef[d + 1] * lag[window - d - 1]
    obs = test[t]
    predictions.append(yhat)
    history.append(obs)
    print('predicted=%f, expected=%f' % (yhat, obs))

rmse = sqrt(mean_squared_error(test, predictions))
print('Test RMSE: %.3f' % rmse)
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()
"""
