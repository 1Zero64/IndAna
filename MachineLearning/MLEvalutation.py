# python3 LinearRegression.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Niko Kauz
# Description: Evaluates the Machine Learning Models and their predictions and results
# ===========================================================================================

from sklearn import metrics
import numpy as np

def evaluateLinearRegression(realData, predictions, articleName="Dummy"):
    '''
        Evaluates the Linear Regression Model

        :param realData: (pandas.series)
                    series of the real data, that has to be predicted
                predictions: (pandas.series)
                    series of the predictions made by the model
                articleName: (string)
                    name of the analyzed article, for the console print
    '''
    # Evaluation of the model
    mse = metrics.mean_squared_error(realData, predictions)
    mae = metrics.mean_absolute_error(realData, predictions)
    rmse = (np.sqrt(mse))
    r2_sq = metrics.r2_score(realData, predictions)

    # print evaluations
    print("\n")
    print("Evaluation of the linear regression for the product", articleName)
    print("Mean Squarred Error:", round(mse, 2))
    print("Root Squarred Error:", round(rmse, 2))
    print("Mean Absolute Error:", round(mae, 2))
    print("R2 Squared:", round(r2_sq, 2))


def evaluatePolynomialRegression(realData, predictions, articleName="Dummy"):
    '''
        Evaluates the Polynomial Regression Model

        :param realData: (pandas.series)
                    series of the real data, that has to be predicted
                predictions: (pandas.series)
                    series of the predictions made by the model
                articleName: (string)
                    name of the analyzed article, for the console print
    '''
    # Evaluation of the model
    mse = metrics.mean_squared_error(realData, predictions)
    mae = metrics.mean_absolute_error(realData, predictions)
    rmse = (np.sqrt(mse))
    r2_sq = metrics.r2_score(realData, predictions)

    # print evaluations
    print("\n")
    print("Evaluation of the polynomial regression for the product", articleName)
    print("Mean Squarred Error:", round(mse, 2))
    print("Root Squarred Error:", round(rmse, 2))
    print("Mean Absolute Error:", round(mae, 2))
    print("R2 Squared:", round(r2_sq, 2))


def evaluateSARIMAX(realData, predictions, articleName="Dummy"):
    '''
        Evaluates the SARIMAX Model.
        ToDo

        :param realData: (pandas.series)
                    series of the real data, that has to be predicted
                predictions: (pandas.series)
                    series of the predictions made by the model
    '''


def evaluateRNN(realData, predictions, articleName="Dummy"):
    '''
        Evaluates the RNN Model.
        ToDo

        :param realData: (pandas.series)
                    series of the real data, that has to be predicted
                predictions: (pandas.series)
                    series of the predictions made by the model
    '''


