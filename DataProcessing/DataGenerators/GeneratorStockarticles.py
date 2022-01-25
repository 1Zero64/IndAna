# author Kevin Hilzinger
# version 1.2
# function to create stock article data
# generated production dates between Jan 2020 and Sept 2021
# outcome article volume influenced by seasonality as introduced in def getseason

import pandas as pd
import random
from matplotlib import pyplot as plt

import DataProcessing.DataGenerators.Configuration.Season as seas

def generateStockArticles(hasToBeGenerated=True):
    random.seed(42)

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
        dates = pd.date_range(start="2016-01-01", end="2021-09-30").date
        print()
        print("creating new dataframe")

        # set dataframe columns
        columns = ['articleID', 'productionDate', 'Quantity']
        stock = pd.DataFrame(columns=columns)

        print("creating data")

        # writing data frame
        for i in range(1000):

            #generating attributes
            articleId = int(articles.iloc[random.randint(0, articles.shape[0]-1)]["ID"])
            productionDate = dates[random.randint(0, len(dates) - 1)]
            # execute seasonality determination

            randomQuantity = random.randint(5, 20)
            seasonweight = seas.getSeason(productionDate, articleId)
            quantity = int(randomQuantity + randomQuantity * seasonweight)

            #creating rows
            stock.loc[i] = [articleId,productionDate, quantity]

        print("Sorting entries")
        # sort values by articleId -> Date
        stock = stock.sort_values(["productionDate", "articleID"]).reset_index(drop=True)
        stock.plot('productionDate', y='Quantity')
        plt.show()

        stock.to_csv('../Datasets/Stockarticles/stockarticles.csv', index_label='ID')
    else:
        stock = pd.read_csv('../Datasets/Stockarticles/stockarticles.csv', index_col=False)
    return stock

if __name__ == '__main__':
    generateStockArticles(False)