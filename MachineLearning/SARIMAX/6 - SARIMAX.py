#from unittest.mock import inplace

#import inline as inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm


data = pd.read_csv("../../DataProcessing/Datasets/Stockarticles/stockarticles.csv")
articles = pd.read_csv("../../DataProcessing/Datasets/Articles/articles.csv")
data.head()

#Group by production date, consolidate quantity per articleID for each date
#data.groupby(['ProductionDate', 'ArticleID'])
data.groupby('productionDate')
#data.index = pd.to_datetime(data['ProductionDate'])
data.index = data['productionDate']
data.drop(columns='productionDate', inplace=True)
data.drop(columns='ID', inplace=True)
data = data.sort_values('productionDate')

df_article = {}
for x in range(len(articles)):
    df_article[x] = data.loc[data['articleID'] == x+1]
    df_article[x].drop(columns='articleID', inplace=True)
    df_article[x].groupby('productionDate')['quantity'].sum()

    #decomposing sarimax structure
    pd.DataFrame(df_article[x], columns=['productionDate'])
    decompose_data = seasonal_decompose(df_article[x], model="additive", period=15)
    print(decompose_data)
    decompose_data.plot()
    #plt.show()

    seasonality = decompose_data.seasonal
    seasonality.plot(color='green')
    #plt.show()
print(df_article[1].dtypes)

#check if data is stationary based on ADFuller Test (P-Value<0.05 -> stationary, else non-stationary
dftest = adfuller(df_article[0], autolag = 'AIC')
print("1 - AR.py. ADF : ", dftest[0])
print("2. P-Value : ", dftest[1])
print("3. ARMA.py. Num Of Lags : ", dftest[2])
print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
print("5. Critical Values :")
for key, val in dftest[4].items():
    print("\t",key, ": ", val)

df_article[0].index = pd.DatetimeIndex(df_article[0].index)

#SARIMAX Model
model = sm.tsa.statespace.SARIMAX(df_article[0],order=(1,1,1),seasonal_order=(1,1,1,12))
history = model.fit()
print(history.summary())

# Testing the model, prediction
df_article[0]['Forecast'] = model.predict(start=90, end=103, dynamic=True)
df_article[0][['quantity','Forecast']].plot(figsize=(12,8))

print("plot is being created.")
fig, ax = plt.subplots(figsize=(8,6))
#ax = pivot0.plot(secondary_y=['0', '1 - AR.py', '2'])
#data.groupby(data['articleID']).plot()
#print(data.groupby(data['articleID']).head())
#data.groupby(data['articleID']).plot(x='productionDate', y='Quantity')
#data0.plot(ax=ax)
#pivot0.plot(ax=ax)
plt.show()