from unittest.mock import inplace

import inline as inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from statsmodels.tsa.seasonal import seasonal_decompose



data = pd.read_csv("C:/Users/Sell-IT/PycharmProjects/IndAna/DataProcessing/Datasets/Stockarticles/stockarticlestest.csv")
articles = pd.read_csv("C:/Users/Sell-IT/PycharmProjects/IndAna/DataProcessing/Datasets/Articles/articles.csv")
data.head()

#Group by production date, consolidate quantity per articleID for each date
#data.groupby(['ProductionDate', 'ArticleID'])
data.groupby('productionDate')
#data.index = pd.to_datetime(data['ProductionDate'])
data.index = data['productionDate']
data.drop(columns='productionDate', inplace=True)
data.drop(columns='ID', inplace=True)
data = data.sort_values('productionDate')
print(data.head(30))

df_article = {}
for x in range(len(articles)):
    df_article[x] = data.loc[data['articleID'] == x+1]
    df_article[x].drop(columns='articleID', inplace=True)
    df_article[x].groupby('productionDate')['Quantity'].sum()
    print("help")
    print(df_article[x])

    #decomposing sarimax structure
    #pd.DataFrame(df_article[x], columns=['productionDate'])
    #decompose_data = seasonal_decompose(df_article[x], model="additive", period=10)
    #print(decompose_data)
    #decompose_data.plot()
    #plt.show()

    #seasonality = decompose_data.seasonal
    #seasonality.plot(color='green')
    #plt.show()

#fig, ax = plt.subplots(figsize=(8,6))
#ax = pivot0.plot(secondary_y=['0', '1', '2'])
#data.groupby(data['articleID']).plot()
#print(data.groupby(data['articleID']).head())
#data.groupby(data['articleID']).plot(x='productionDate', y='Quantity')
#data0.plot(ax=ax)
#pivot0.plot(ax=ax)
#plt.show()