import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import DataGenerators as dg

def exploreWeather():
    # columnnames:   date, tavg (average temperature), tmin (min. temp.), tmax (max. temp.),
    #               prcp (overall precipitation/Gesamtniederschlag), snow, wdir (wind direction),
    #               wspd (wind speed), wpgt (wind peak/Spitzenboe), pres (pressure/Luftdruck),
    #               tsun (time of sunshine)
    weather = dg.gWeather.generateWeatherData()
    weather['date'] = pd.to_datetime(weather['date'])
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
    # #plt.hist(weather)
    # plt.show()

    ## histogram for single feature
    # fig = plt.figure()
    # weather['tavg'].hist()
    # plt.xlabel('tavg')
    # plt.show()

    ## Scatterplot for two features
    # weather.plot(kind='scatter', x='tavg', y='date')
    # plt.show()

    ## Scatterplot for two features with labels
    # weather.plot(kind='scatter', x='tavg', y='prcp')
    # plt.xlabel('Average Temperature')
    # plt.ylabel('Overall Precipitation')
    # plt.show()

    ## Scatterplot for two features, colored by another feature
    # weather.plot(kind='scatter', x='tavg', y='date', c='tsun', cmap='viridis')
    # plt.xlabel('Average Temperature')
    # plt.show()

    ## scatttermatrix for all features
    # pd.plotting.scatter_matrix(weather)
    # plt.show()

    ## line plot for three temperature features, color coded
    fig = plt.figure()
    plt.plot(weather['date'], weather['tavg'], 'g', label='Average Temperature')
    plt.plot(weather['date'], weather['tmin'], 'b', label='Min. Temperature')
    plt.plot(weather['date'], weather['tmax'], 'r', label='Max. Temperature')
    plt.legend()
    plt.show()

exploreWeather()