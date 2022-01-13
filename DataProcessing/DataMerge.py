import pandas as pd
import DataPreparation as dp

def mergeData():
    ## 1st: Merging weather and sales on date
    weather = dp.prepareWeatherData()
    sales = dp.prepareSalesData()

    merged = pd.merge(weather, sales, left_on='date', right_on='date')
    print(merged)

    ## 2nd: Merging new df with stockarticles
    # stockarticles = dp.prepareStockArticlesData()
    # print(stockarticles)
    # merged2 = pd.merge(merged, stockarticles, left_on='date', right_on='BestByDate')
    # print(merged2)

mergeData()