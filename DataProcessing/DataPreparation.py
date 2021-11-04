# Gathering data from data generators, add derived features, etc.

import DataGenerators as dg
import pandas as pd
import numpy as np

def prepareWeatherData():     
    df = dg.gWeather.generateWeatherData()
    df['date'] = pd.to_datetime(df['date'])
    return df

def prepareArticlesData():
    df = dg.gArticles.generateArticlesData()
    df = df.replace(r'^s*$', float('NaN'), regex = True)
    return df