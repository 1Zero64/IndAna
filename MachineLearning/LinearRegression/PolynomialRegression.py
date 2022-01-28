# python3 LinearRegression.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Niko Kauz
# Description: Creates a Polynomial Regression Model and predicts the sales
# ===========================================================================================

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import datetime as dt

import MachineLearning.MLEvalutation as eval
import MachineLearning.MLPreparation as mlprep

import os

def polynomialRegression(articleId):
    '''
        Generates articles data, saves them to csv file and returns dataframe

        :param articleId: (int)
                identifier of a article
        :return:
            sales: (pandas.dataframe)
                dataframe with dates and summed up sold quantities for articles
            y: (list)
                real sales data
            predictions: (list)
                predicted sales from linear regression model
            articleName: (string)
                name of the analyzed article
    '''

    def getArticleName(articleId):
        '''
        Returns the name of the article from the articles data frame with the article id

        :param articleId: (int)
                id of a article
        :return:
            articleName: (string)
                name of the retrieved article
        '''
        articles = mlprep.prepareArticlesData()
        articleName = articles.loc[articles['ID'] == articleId]['Article'][articleId - 1]
        return articleName

    print(os.getcwd())

    # Read merged data frame, prepare column name for different articles
    articleColumn = "articleId_" + str(articleId)
    sales, X_train, X_test, y_train, y_test = mlprep.prepareForML()

    # Get last years for training
    year = 2
    sales = sales.tail(year * 365)

    # fill NaN with 0
    sales = sales.fillna(0)

    # Make sales copy
    salesMod = sales.copy(deep=True)

    # Convert date to numeric
    salesMod['date'] = pd.to_datetime(salesMod['date'])
    salesMod['date'] = salesMod['date'].map(dt.datetime.toordinal)

    # Degree for polynom
    degree = 5

    # Split sales in features (X) and label (y)
    X = salesMod[['date', 'tavg']]
    y = salesMod[articleColumn]
    poly = PolynomialFeatures(degree=degree)
    polyFeatures = poly.fit_transform(X)

    polyModel = LinearRegression()
    polyModel.fit(polyFeatures, y)

    predictions = polyModel.predict(polyFeatures)

    mse = metrics.mean_squared_error(y, predictions)
    mae = metrics.mean_absolute_error(y, predictions)
    rmse = (np.sqrt(mse))
    r2_sq = metrics.r2_score(y, predictions)

    # Get article name
    articleName = getArticleName(articleId)

    # evaluations of the model
    eval.evaluatePolynomialRegression(realData=y, predictions=predictions, articleName=articleName)

    # Prediction for the next day
    nextDay = X.iloc[-1]['date']
    polyNextDay = poly.fit_transform([[nextDay, 5]])
    predNextDay = polyModel.predict(polyNextDay)[0]
    print("Prediction for next day (2021-11-01):", round(predNextDay))

    # Prepare data for return for last year
    sales = sales.tail(365)
    y = y[-365:]
    predictions = predictions[-365:]

    # return series and names
    return sales, y, predictions, articleName
