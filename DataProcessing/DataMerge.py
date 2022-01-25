import pandas as pd
# import os
# print (os.environ['PYTHONPATH'])
#
# import sys
# print (sys.path)

import DataProcessing.DataPreparation as dp

def mergeData():
    ## 1st: Merging weather and sales on date
    weather = dp.prepareWeatherData()
    sales = dp.prepareSalesData()

    merged = pd.merge(weather, sales, left_on='date', right_on='date')
    pd.set_option('display.max_columns', None)
    print(merged)
    merged.to_csv('../Datasets/merged1.csv', index=False)

    ## 2nd: Merging new df with stockarticles
    # stockarticles = dp.prepareStockArticlesData()
    # stockarticles = stockarticles.rename(columns={'ID': 'stockarticleID'})
    # print(stockarticles)
    #
    # merged = pd.merge(merged, stockarticles, left_on='date', right_on='BestByDate')
    # pd.set_option('display.max_columns', None)
    # print(merged)

    return merged

mergeData()