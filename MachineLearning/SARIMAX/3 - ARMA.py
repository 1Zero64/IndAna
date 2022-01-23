# https://www.statsmodels.org/stable/examples/notebooks/generated/tsa_arma_1.html?highlight=arma

import pandas as pd

from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_predict
from statsmodels.tsa.arima.model import ARIMA

data = pd.read_json('../../DataProcessing/Datasets/Sales/sales.json')
dictionary = {}

for i in range(data.shape[0]):
    date = pd.Timestamp(data.iloc[i][0]).date()
    if date not in dictionary:
        dictionary[date] = 0
    for j in range(len(data.iloc[i][1])):
        if data.iloc[i][1][j]["articleId"] == 1:
            dictionary[date] = dictionary[date] + data.iloc[i][1][j]["quantity"]

columns = ["date", "quantity"]
data_items = dictionary.items()
data_list = list(data_items)
salesDF = pd.DataFrame(data_list, columns=columns)
salesDF.date = pd.to_datetime(salesDF.date)

salesDF = salesDF.set_index("date", drop=True, append=False, inplace=False, verify_integrity=False)



sales = salesDF.values
arma_mod = ARIMA(salesDF, order=(2, 0, 2), trend="n")
arma_res = arma_mod.fit()

print(arma_res.summary())


fig, ax = plt.subplots(figsize=(10, 8))
fig = plot_predict(arma_res, start="2016-01-01", end="2021-10-31", ax=ax)
legend = ax.legend(loc="upper left")
plt.show()

plt.figure(figsize=[15, 7.5]); # Set dimensions for figure
plt.plot(sales)
plt.title("Simulated ARMA(1,1) Process")
plt.xlim([0, 200])
plt.show()
