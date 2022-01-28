# python3 DataPreparation.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Ann-Kathrin Jauk
# Description: Reads in data from csv/json files, converts datatypes where needed (e.g.
# with date string to datetime), drops columns/nan-values and returns pandas dataframe
# ===========================================================================================

import numpy as np

import DataProcessing.DataGenerators as dg
import pandas as pd

import DataProcessing.DataPreparation as dp


def prepareWeatherData():
    '''
    Reads weather data from csv, drops unnecessary columns, returns dataframe

    :return: weather: (pandas.dataframe)
                prepared weather data
    '''
    # columnnames:   date, tavg (average temperature), tmin (min. temp.), tmax (max. temp.),
    #               prcp (overall precipitation/Gesamtniederschlag), snow, wdir (wind direction),
    #               wspd (wind speed), wpgt (wind peak/Spitzenboe), pres (pressure/Luftdruck),
    #               tsun (time of sunshine)

    print("Preparing Weather Data")

    weather = dg.gWeather.generateWeatherData()
    # drop all columns except date, tavg, tmin and tmax
    weather = weather.drop(columns=['prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun'])

    print("Finished")
    return weather


def prepareArticlesData():
    '''
    Reads articles data from csv, replaces empty values with NaN, returns dataframe

    :return: articles: (pandas.dataframe)
                prepared articles data
    '''
    print("Preparing Articles Data")

    # get ArticlesData (without parameter: use already generatedData
    articles = dg.gArticles.generateArticlesData()

    # replace empty/blank spaced values with NaN
    articles = articles.replace(r'^s*$', np.nan, regex=True)
    print("Finished")

    return articles


def prepareStockArticlesData():
    '''
    Reads stockarticles data from csv, merges with articles for calculation of Best-By-Date,
    drops articles with NaN Best-By-Period, returns dataframe

    :return: stock: (pandas.dataframe)
                prepared stockarticles data
    '''
    print("Preparing Stockarticles Data")
    # get stockArticles and ArticlesData (without parameter: use already generatedData, else True)
    stockArticles = dg.gStockarticles.generateStockArticles(False)
    articles = dg.gArticles.generateArticlesData()

    # print(stockArticles)
    # print(articles)

    #drop and rename columns
    articles = articles.drop(columns=['Article', 'Unit'])
    articles = articles.rename(columns={'ID':'articleID'})

    # merge on ArticleID
    merged = pd.merge(stockArticles, articles, left_on='articleID', right_on='articleID')
    merged = merged.rename(columns={'ID': 'stockarticleID'})

    # drop nan a.k.a articles without Best By Period
    merged = merged.dropna()

    # calculate Best By Date
    merged['productionDate'] = pd.to_datetime(merged['productionDate'])
    merged['BestByDate'] = merged['productionDate'] + pd.to_timedelta(merged['Best By Period'], unit='d')
    merged = merged.drop(columns=['Best By Period'])
    merged = merged.sort_values(["articleID", "productionDate"]).reset_index(drop=True)

    print("Finished")

    # workaround for sums not being treated as objects but as numeric values
    merged.to_csv('../Datasets/Stockarticles/stockarticles_prepared.csv', index=False)
    stock = pd.read_csv('../Datasets/Stockarticles/stockarticles_prepared.csv', parse_dates=['productionDate',
                                                                                             'BestByDate'])
    return stock


def prepareSalesData():
    '''
    Reads sales data from json, sums sales quantities per article per day, returns dataframe

    :return: sales: (pandas.dataframe)
                prepared sales data
    '''
    print("Preparing Sales Data")

    #get SalesData (without parameter: use already generatedData
    sales = dg.gSales.generateSalesData(False)

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
                if pd.isna(value):
                    value = np.nan
                preparedSales.iloc[row, key] = value
        row += 1

    #changing article id columnnames to include "articleId_"
    for index, name in enumerate(columnNames):
        if type(name) == int:
            columnNames[index] = 'articleId_' + str(name)

    preparedSales.columns = columnNames

    print("Finished")

    # workaround for sums not being treated as objects but as numeric values
    preparedSales.to_csv('../Datasets/Sales/sales_prepared.csv', index=False)
    sales = pd.read_csv('../Datasets/Sales/sales_prepared.csv', parse_dates=['date'])

    return sales