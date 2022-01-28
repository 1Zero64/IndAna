# python3 DataExploration.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Ann-Kathrin Jauk
# Description: Explores data
# ===========================================================================================

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import DataProcessing.DataGenerators as dg
import DataProcessing.DataPreparation as dp

def exploreWeather():
    '''
    Run different statistical and visual exploration on weather data
    '''
    print("Explore Weather")
    # columnnames:   date, tavg (average temperature), tmin (min. temp.), tmax (max. temp.),
    #               prcp (overall precipitation/Gesamtniederschlag), snow, wdir (wind direction),
    #               wspd (wind speed), wpgt (wind peak/Spitzenboe), pres (pressure/Luftdruck),
    #               tsun (time of sunshine)

    # get data
    weather = dg.gWeather.generateWeatherData()
    print(weather)

    ''' Descriptive Statistics '''
    print(weather.describe().T)
    print(weather.info())

    ##dropping wind peak: no non-null values
    weather = weather.drop(columns=["wpgt"])

    ''' Plots/Visualization '''
    ## plotting all features with x-axis on date
    # weather.plot()
    # plt.xlabel('date')
    # plt.grid()
    # plt.show()

    ## histograms for all features
    # fig = plt.figure()
    # plt.hist(weather)
    # plt.show()

    ## histogram for single feature
    fig = plt.figure()
    weather['prcp'].hist()
    plt.xlabel('prcp')
    plt.show()

    ## Scatterplot for two features
    # weather.plot(kind='scatter', x='tavg', y='date')
    # plt.show()

    ## Scatterplot for two features with labels
    # weather.plot(kind='scatter', x='tavg', y='prcp')
    # plt.xlabel('Average Temperature')
    # plt.ylabel('Overall Precipitation')
    # plt.show()

    ## Scatterplot for two features, colored by another feature
    weather.plot(kind='scatter', x='tavg', y='date', c='tsun', cmap='viridis')
    plt.xlabel('Average Temperature')
    plt.show()

    ## scattermatrix for all features
    # pd.plotting.scatter_matrix(weather)
    # plt.show()

    ## line plot for three temperature features, color coded
    # fig = plt.figure()
    # plt.plot(weather['date'], weather['tavg'], 'g', label='Average Temperature')
    # plt.plot(weather['date'], weather['tmin'], 'b', label='Min. Temperature')
    # plt.plot(weather['date'], weather['tmax'], 'r', label='Max. Temperature')
    # plt.legend()
    # plt.show()


def exploreSales():
    '''
    Run different statistical and visual exploration on weather data
    '''
    print("Explore Sales")

    # get prepared data
    sales = dp.prepareSalesData()
    print(sales)

    ''' Descriptive Statistics '''
    print(sales.info())
    salesWithoutDates = sales.drop(columns=['date'])
    print(salesWithoutDates.describe().T)

    ''' Plots/Visualization '''
    ## scattermatrix for all features
    # pd.plotting.scatter_matrix(sales)
    # plt.show()

    ## Scatterplot for two features
    # sales.plot(kind='scatter', x='articleId_1', y='date')
    # plt.show()

    ## histogram for single feature
    fig = plt.figure()
    sales['articleId_8'].hist()
    plt.xlabel('Sales Eggs')
    plt.ylabel('Days')
    plt.show()


def exploreStockArticles():
    '''
    Run different statistical and visual exploration on weather data
    '''
    print("Explore StockArticles")

    # get prepared data
    stockarticles = dp.prepareStockArticlesData()
    print(stockarticles)

    ''' Descriptive Statistics '''
    print(stockarticles.info())
    pd.set_option('display.max_columns', None)
    print(stockarticles.describe().T)

    ''' Plots/Visualization '''
    ## scattermatrix for all features
    # pd.plotting.scatter_matrix(stockarticles)
    # plt.show()

    ## Scatterplot for two features
    # stockarticles.plot(kind='scatter', x='articleID', y='Quantity')
    # plt.show()

    ## Scatterplot for two features, colored by another feature
    stockarticles2016 = stockarticles[stockarticles.productionDate <= np.datetime64('2017-01-01')]
    print(stockarticles2016)
    stockarticles2016.plot(kind='scatter', x='productionDate', y='Quantity', c='articleID', cmap='viridis')
    plt.show()

    ## histogram for single feature
    # fig = plt.figure()
    # stockarticles['articleId_6'].hist()
    # plt.xlabel('Stock Ginger Bread')
    # plt.show()


def explore():
    exploreWeather()
    exploreSales()
    exploreStockArticles()