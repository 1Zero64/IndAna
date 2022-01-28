# python3 2 - MA.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Niko Kauz
# Description: Visualisation and testing of the Moving Average (MA) model
# ===========================================================================================
# https://www.geeksforgeeks.org/how-to-calculate-moving-averages-in-python/

from statsmodels.graphics.tsaplots import plot_predict
from statsmodels.tsa.arima.model import ARIMA
from matplotlib import pyplot as plt
import pandas as pd

def movingAverage(articleId):
    '''
        Calculates and plots the moving average of the sales for a article

        :param articleId: (int)
                identifier of a article
        '''
    articleColumn = "articleId_" + str(articleId)

    salesDF = pd.read_csv('../../DataProcessing/Datasets/merged1.csv')
    salesDF.date = pd.to_datetime(salesDF.date)
    salesDF = salesDF[['date', articleColumn]]
    salesDF = salesDF.set_index("date", drop=True, append=False, inplace=False, verify_integrity=False)
    salesDF = salesDF.fillna(0)

    # Fit a MA model for the sales data
    mod = ARIMA(salesDF, order=(2, 0, 2), trend="n")
    res = mod.fit()

    # Print out summary information on the fit
    print(res.summary())

    # Print out the estimate for the constant and for theta
    print("When the true theta=-0.9, the estimate of theta (and the constant) are:")
    print(res.params)

    fig, ax = plt.subplots(figsize=(10, 8))
    fig = plot_predict(res, start="2020-01-01", end="2021-10-31", ax=ax)
    legend = ax.legend(loc="upper left")
    plt.show()


    salesList = salesDF[articleColumn].tolist()

    windowSize = 7

    # Convert array of integers to pandas series
    numbers_series = pd.Series(salesList)

    # Get the window of series
    # of observations of specified window size
    windows = numbers_series.rolling(windowSize)

    # Create a series of moving
    # averages of each window
    moving_averages = windows.mean()

    # Convert pandas series back to list
    moving_averages_list = moving_averages.tolist()

    # Remove null entries from the list
    final_list = moving_averages_list[windowSize - 1:]

    print(final_list)
    plt.plot(final_list)
    plt.show()


if __name__ == '__main__':
    whishedArticleId = 1
    movingAverage(whishedArticleId)