# author Kevin Hilzinger
# version 1.1
# function to create stock article data
# assumption:   production dates are within 5 days prior to 1 day prior to current date
#               lower and upper quantity limit is same for every article

import pandas as pd
from datetime import date, timedelta
import random

from DataProcessing.DataGenerators.Configuration.Season import getSeason


def generateStockArticles(hasToBeGenerated=True):
    if hasToBeGenerated:
        # get article list
        path = '../Datasets/Articles/articles.csv'
        articles = pd.read_csv(path, header=[0])

        # obtain total number of articles
        # articleCount = sum(1 for row in articles)

        print("fetching date information and creating possible production dates")

        # get current date
        # todayInit = date.today()
        # today = todayInit.strftime("%y-%m-%d")
        # possible production date options
        # dates = pd.date_range(start=sept 2020, end=okt 2021)
        dates = pd.date_range(start="2020-01-01", end="2021-09-30").date
        print()
        print("creating new dataframe")

        # set dataframe columns
        columns = ['articleID', 'productionDate', 'Quantity']
        stock = pd.DataFrame(columns=columns)

        print("creating data")

        # writing data frame
        for i in range(900):

            #generating attributes
            articleId = int(articles.iloc[random.randint(0, articles.shape[0]-1)]["ID"])
            productionDate = dates[random.randint(0, len(dates) - 1)]
            # execute seasonality determination
            seasonweight = getSeason(date.today(), articleId, False)
            quantity = random.randint(1, 20)

            #creating rows
            stock.loc[i] = [articleId,productionDate, quantity]

        print("Sorting entries")
        # sort values by articleId -> Date
        stock = stock.sort_values(["productionDate", "articleID"]).reset_index(drop=True)


        stock.to_csv('../Datasets/Stockarticles/stockarticles.csv', index_label='ID')
    else:
        stock = pd.read_csv('../Datasets/Stockarticles/stockarticles.csv', index_col=False)
    return stock