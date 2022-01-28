# python3 LinearRegression.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Niko Kauz
# Description: Creates a Linear Regression Model and predicts the sales
# ===========================================================================================

from sklearn.linear_model import LinearRegression
import pandas as pd
import datetime as dt

import MachineLearning.MLEvalutation as eval
import MachineLearning.MLPreparation as mlprep

def linearRegression(articleId):
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
                identifier of a article
        :return:
            articleName: (string)
                name of the retrieved article
        '''
        articles = mlprep.prepareArticlesData()
        articleName = articles.loc[articles['ID'] == articleId]['Article'][articleId-1]
        return articleName

    # prepare column name for right article
    articleColumn = "articleId_" + str(articleId)

    # read merged data frame
    sales, X_train, X_test, y_train, y_test = mlprep.prepareForML()

    # Get last years for training
    year = 2
    sales = sales.tail(year * 365)

    # Make sales copy
    salesMod = sales.copy(deep=True)

    # Convert date to numeric
    salesMod['date'] = pd.to_datetime(salesMod['date'])
    salesMod['date'] = salesMod['date'].map(dt.datetime.toordinal)

    # Split copied data frame in features (X) and label (y)
    X = salesMod[['date', 'tavg']]
    y = salesMod[articleColumn]

    X = X[['date', 'tavg']].fillna(0)
    y = y.fillna(0)

    # Create and fit linear regression
    linModel = LinearRegression()
    linModel.fit(X, y)

    # Make sales predictions on data
    predictions = linModel.predict(X)

    # Get name for the article with ID from articles
    articleName = getArticleName(articleId)

    # Evaluation of the model
    eval.evaluateLinearRegression(realData=y, predictions=predictions, articleName=articleName)

    # Prediction for the next day
    nextDay = X.iloc[-1]['date']
    predNextDay = linModel.predict([[nextDay, 5]])[0]
    print("Prediction for next day (2021-11-01):", round(predNextDay))

    # Convert date in original data frame to object for plotting
    sales['date'] = sales['date'].astype(object)

    # Prepare data for return for last year
    sales = sales.tail(365)
    y = y[-365:]
    predictions = predictions[-365:]

    # return series and names
    return sales, y, predictions, articleName
