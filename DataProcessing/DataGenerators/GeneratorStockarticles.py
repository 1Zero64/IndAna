# author Kevin Hilzinger
# Version 1.0
# Generates stock articles data and writes it into a csv document. Returns dataframe of stockarticles.
# This csv document is located in ../Datasets/StockArticles/stockarticles.csv

import pandas as pd

def generateStockarticlesData(dataToGenerate=5000):
    columns = ['articleId', 'productionDate', 'quantity']
    stockarticlesDataFrame = pd.DataFrame(columns=columns)

    # WIP

    stockarticlesDataFrame.to_csv('../Datasets/Articles/stockarticles.csv')

    return stockarticlesDataFrame