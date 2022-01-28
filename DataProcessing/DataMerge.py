# python3 DataMerge.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Ann-Kathrin Jauk
# Description: Merges data into one dataframe
# ===========================================================================================

import pandas as pd
import DataProcessing.DataPreparation as dp

def mergeData():
    '''
    Merges data into one dataframe,
    Step 1: weather and sales,
    Step 2: weather, sales, stockarticles

    :return: merged: (pandas.dataframe)
                merged data
    '''
    ## 1st: Merging weather and sales on date
    weather = dp.prepareWeatherData()
    sales = dp.prepareSalesData()

    merged = pd.merge(weather, sales, left_on='date', right_on='date')
    pd.set_option('display.max_columns', None)
    # print(merged)
    merged.to_csv('../Datasets/merged1.csv', index=False)

    ## 2nd: Merging new df with stockarticles on date and BestByDate
    # stockarticles = dp.prepareStockArticlesData()
    # stockarticles = stockarticles.rename(columns={'ID': 'stockarticleID'})
    # print(stockarticles)
    #
    # merged = pd.merge(merged, stockarticles, left_on='date', right_on='BestByDate')
    # pd.set_option('display.max_columns', None)
    # print(merged)

    return merged