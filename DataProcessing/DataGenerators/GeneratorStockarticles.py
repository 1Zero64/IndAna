# author Kevin Hilzinger
# version 1.1
# function to create stock article data
# assumption:   production dates are within 5 days prior to 1 day prior to current date
#               lower and upper quantity limit is same for every article

import pandas as pd
from datetime import date, timedelta
import random


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
        dates = pd.date_range('01/09/2020'-'01/11/2021')
        print()
        print("creating new dataframe")

        # set dataframe columns
        columns = ['ArticleID', 'ProductionDate', 'Quantity']
        stock = pd.DataFrame(columns=columns)

        print("creating data")

        # writing data frame
        for i in range(900):

            #generating attributes
            articleId = int(articles.iloc[random.randint(0, articles.shape[0]-1)]["ID"])
            productionDate = dates[random.randint(0, len(dates) - 1)]
            quantity = random.randint(1, 20)

            #creating rows
            stock.loc[i] = [articleId,productionDate.strftime("%y-%m-%d"), quantity]

        print("Sorting entries")
        # sort values by articleId -> Date
        stock = stock.sort_values(articleId, productionDate).reset_index(drop=True)


        stock.to_csv('../Datasets/Stockarticles/stockarticles.csv', index_label='ID')
    else:
        stock = pd.read_csv('../Datasets/Stockarticles/stockarticles.csv', index_col=False)
    return stock


if __name__ == '__main__':
    generateStockArticles(True)