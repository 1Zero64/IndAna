from unittest.mock import inplace

import inline as inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy



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

print(data.isna().sum())

#separate articles via new dataframe
#articledata = {}
#for x in range(len(articles)-1):
#    globals()['string%s' % x] = data.loc[data['articleID'] == x]
#    globals()['string%s' % x] = globals()['string%s' % x].drop(columns=['articleID'])

#print(articledata)

#data0 = data.loc[data['articleID'] == 0]
#data0.drop(columns=['articleID'], inplace=True)
#data0.groupby('productionDate').sum()
#print(data0)

#create pivot from dataframe to separate
print("create pivot table with articles as column")
pivot0 = pd.pivot_table(data, values='Quantity', index='productionDate', columns='articleID', dropna=True, fill_value=0, aggfunc=np.sum)
pivot0.reset_index(inplace=True)
#pivot0.set_index('productionDate')
pivot0.index = pivot0['productionDate']
pivot0.drop(columns=['productionDate'], inplace=True)
#data0.drop(columns=['articleID'], inplace=True)
print(pivot0)


#for x in range(len(pivot0.columns)):
 #   df = pd.DataFrame(pivot0[0])
 #   print(df)





#from statsmodels.tsa.seasonal import seasonal_decompose
#pd.DataFrame(pivot0, columns=['productionDate'])
#decompose_data = seasonal_decompose(pivot0, model="additive", period=10)
#print(decompose_data)
#decompose_data.plot()

fig, ax = plt.subplots(figsize=(8,6))
#ax = pivot0.plot(secondary_y=['0', '1', '2'])
data.groupby(data['articleID']).plot()
#print(data.groupby(data['articleID']).head())
#data.groupby(data['articleID']).plot(x='productionDate', y='Quantity')
#data.plot(ax=ax)
#pivot0.plot(ax=ax)
plt.show()