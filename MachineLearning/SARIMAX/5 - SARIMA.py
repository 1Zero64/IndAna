# https://towardsdatascience.com/time-series-forecasting-with-sarima-in-python-cda5b793977b

from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_json('../../DataProcessing/Datasets/Sales/sales.json')
dictionary = {}

for i in range(data.shape[0]):
    date = pd.Timestamp(data.iloc[i][0]).date()
    if date not in dictionary:
        dictionary[date] = 0
    for j in range(len(data.iloc[i][1])):
        if data.iloc[i][1][j]["articleId"] == 1:
            dictionary[date] = dictionary[date] + data.iloc[i][1][j]["quantity"]