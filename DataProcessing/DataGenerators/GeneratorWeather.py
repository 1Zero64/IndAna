# python3 GeneratorWeather.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Ann-Kathrin Jauk
# Description: Reads in weather data and returns dataframe
# ===========================================================================================

import pandas as pd

def generateWeatherData():
    '''
    Reads in weather data and returns dataframe

    :return:
        weather: (pandas.dataframe)
            Dataframe with weather data, dates already parsed to datetime
    '''
    #columnnames:   date, tavg (average temperature), tmin (min. temp.), tmax (max. temp.), 
    #               prcp (overall precipitation/Gesamtniederschlag), snow, wdir (wind direction),
    #               wspd (wind speed), wpgt (wind peak/Spitzenboe), pres (pressure/Luftdruck), 
    #               tsun (time of sunshine)
    path = '../Datasets/Weather/weather_012016-102021.csv'
    weather = pd.read_csv(path, header=[0], parse_dates=['date'])
    return weather