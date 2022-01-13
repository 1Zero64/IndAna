# Gathering data from data generators, add derived features, etc.
import json

import numpy as np

import DataGenerators as dg
import pandas as pd
import flatten_json

def prepareWeatherData(loadingMode='old'):
    # columnnames:   date, tavg (average temperature), tmin (min. temp.), tmax (max. temp.),
    #               prcp (overall precipitation/Gesamtniederschlag), snow, wdir (wind direction),
    #               wspd (wind speed), wpgt (wind peak/Spitzenboe), pres (pressure/Luftdruck),
    #               tsun (time of sunshine)

    weather = dg.gWeather.generateWeatherData()
    weather['date'] = pd.to_datetime(weather['date'])
    weather = weather.drop(columns=['prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun'])
    return weather


def prepareArticlesData():
    # get ArticlesData (without parameter: use already generatedData
    articles = dg.gArticles.generateArticlesData()
    articles = articles.replace(r'^s*$', np.nan, regex=True)
    return articles


def prepareStockArticlesData():
    # get stockArticles and ArticlesData (without parameter: use already generatedData)
    stockArticles = dg.gStockarticles.generateStockArticles()
    articles = prepareArticlesData()
    articles = articles.drop(columns=['Article', 'Unit'])
    articles = articles.rename(columns={'ID':'ArticleID'})

    # merge on ArticleID
    merged = pd.merge(stockArticles, articles, left_on='ArticleID', right_on='ArticleID')

    # drop nan which are articles without Best By Period
    merged = merged.dropna()

    # calculate Best By Date
    dateformat = '%y-%m-%d'
    merged['ProductionDate'] = pd.to_datetime(merged['ProductionDate'], format=dateformat)
    merged['BestByDate'] = merged['ProductionDate'] + pd.to_timedelta(merged['Best By Period'], unit='d')
    merged = merged.drop(columns=['Best By Period'])
    return merged

def prepareSalesData():
    #get SalesData (without parameter: use already generatedData
    sales = dg.gSales.generateSalesData()

    #Get unique dates of sales dataframe
    dates = pd.unique(sales['date'])

    #Returns list of unique articleIDs of a sales dataframe
    def getIdListOf(df):
        idList = []
        for articles in df['soldArticles']:
            for article in articles:
                id = article['articleId']
                if id not in idList:
                    idList.append(id)
        return idList

    #returns sums of quantities grouped by articleId
    def getSumPerArticleOfDay(salesDay, idList):
        articleQuantity = {}
        for id in idList:
            articleQuantity[id] = 0

        for id in idList:
            for articles in salesDay['soldArticles']:
                for article in articles:
                    if id == article['articleId']:
                        articleQuantity[id] += article['quantity']
        return articleQuantity

    #idList of all sales
    idListSales = getIdListOf(sales)
    idListSales.sort()

    ##preparing prepared sales dataframe
    #columnNames are date and all unique articleIDs
    columnNames = ['date']
    for id in idListSales:
        columnNames.append(id)

    #initializing new dataframe
    preparedSales = pd.DataFrame(columns=columnNames)

    #using unique dates for 'date' column
    preparedSales['date'] = dates

    #mapping sales summed per day on new dataframe with unique dates
    row = 0
    for date in dates:
        df = sales.loc[(sales['date'] == date)]
        idList = getIdListOf(df)
        articleQuantity = getSumPerArticleOfDay(df, idList)
        for key, value in articleQuantity.items():
            if preparedSales['date'][row] == date:
                preparedSales.loc[row, key] = value
        row += 1

    #changing article id columnnames to include "articleId_"
    for index, name in enumerate(columnNames):
        if type(name) == int:
            columnNames[index] = 'articleId_' + str(name)

    preparedSales.columns = columnNames

    #converting date string to datetime
    preparedSales['date'] = pd.to_datetime(preparedSales['date'])
    return preparedSales