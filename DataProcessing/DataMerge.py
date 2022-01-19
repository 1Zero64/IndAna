import pandas as pd
# import os
# print (os.environ['PYTHONPATH'])
#
# import sys
# print (sys.path)

import DataPreparation as dp

def mergeData():
    ## 1st: Merging weather and sales on date
    weather = dp.prepareWeatherData()
    sales = dp.prepareSalesData()

    merged = pd.merge(weather, sales, left_on='date', right_on='date')
    print(merged)

    ## 2nd: Merging new df with stockarticles
    stockarticles = dp.prepareStockArticlesData()
    stockarticles = stockarticles.rename(columns={'ID': 'stockarticleID'})
    print(stockarticles)

    merged2 = pd.merge(merged, stockarticles, left_on='date', right_on='BestByDate')
    pd.set_option('display.max_columns', None)
    print(merged2)
    return merged

mergeData()