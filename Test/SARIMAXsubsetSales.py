from unittest.mock import inplace

import inline as inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from statsmodels.tsa.seasonal import seasonal_decompose



data = pd.read_json("C:/Users/Sell-IT/PycharmProjects/IndAna/DataProcessing/Datasets/Sales/sales.json")
articles = pd.read_csv("C:/Users/Sell-IT/PycharmProjects/IndAna/DataProcessing/Datasets/Articles/articles.csv")
data.head()

print("gestartet")

colums = ["date", "articleId", "quantity"]
dataFrame = pd.DataFrame(columns=colums)

#print(data)
counter = 0

for i in range(data.shape[0]):
    date = pd.Timestamp(data.iloc[i][0]).date()
    for j in range(len(data.iloc[i][1])):
        articleId = data.iloc[i][1][j]["articleId"]
        quantity = data.iloc[i][1][j]["quantity"]
        dataFrame.loc[counter] = [date, articleId, quantity]
        counter += 1


#print(dataFrame)
#dataFrame.groupby('date')
#dataFrame.index = dataFrame['date']
#dataFrame.drop(columns='date', inplace=True)
#print(dataFrame)
dataFrame.info()
df_article = {}
for x in range(len(articles)):
    subDataFrame = pd.dataFrame.loc[dataFrame['articleId'] == x+1]
    subDataFrame = subDataFrame.loc[dataFrame['articleId'] == x+1]
    subDataFrame = subDataFrame.drop(columns='articleId', inplace=True)
    subDataFrame = subDataFrame.groupby('date')['quantity'].sum()
    print("help")
    print(subDataFrame)

print(df_article.info())

#columns = ["date", "quantity"]
#data_items = dictionary.items()
#data_list = list(data_items)
#dataFrame = pd.DataFrame(data_list, columns=columns)
#dataFrame.date = pd.to_datetime(dataFrame.date)

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