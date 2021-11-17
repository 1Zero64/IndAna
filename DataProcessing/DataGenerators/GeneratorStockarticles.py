# author Kevin Hilzinger
# version 1
# function to create stock article data
# assumption:   production dates are within 14 days prior to 1 day prior to current date
#               lower and upper quantity limit is same for every article

import pandas as pd
from datetime import date, timedelta
import random


def generateStockArticles():

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
    # dates = pd.date_range(start=today-14, end=today-1)
    dates = pd.date_range(date.today() - timedelta(days=14), date.today() - timedelta(days=2))
    print()
    print("creating new dataframe")

    # set dataframe columns
    columns = ['ID', 'ProductionDate', 'Quantity']
    stock = pd.DataFrame(columns=columns)

    print("creating data")

    # writing data frame
    for i in range(len(articles)):

        productionDate = dates[random.randint(0, len(dates) - 1)]
        quantity = random.randint(0, 20)
        stock[i] = [i, productionDate.strftime("%y-%m-%d"), quantity]

    return stock
