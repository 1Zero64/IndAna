from statsmodels.graphics.tsaplots import plot_predict
from statsmodels.tsa.arima.model import ARIMA
from matplotlib import pyplot as plt
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

columns = ["date", "quantity"]
data_items = dictionary.items()
data_list = list(data_items)
salesDF = pd.DataFrame(data_list, columns=columns)
salesDF.date = pd.to_datetime(salesDF.date)

salesDF = salesDF.set_index("date", drop=True, append=False, inplace=False, verify_integrity=False)

# Fit an MA(1) model to the first simulated data
mod = ARIMA(salesDF, order=(2, 0, 2), trend="n")
res = mod.fit()

# Print out summary information on the fit
print(res.summary())

# Print out the estimate for the constant and for theta
print("When the true theta=-0.9, the estimate of theta (and the constant) are:")
print(res.params)

fig, ax = plt.subplots(figsize=(10, 8))
fig = plot_predict(res, start="2020-01-01", end="2021-10-31", ax=ax)
legend = ax.legend(loc="upper left")
plt.show()


salesAppleList = salesDF["quantity"].tolist()

windowSize = 7

# Convert array of integers to pandas series
numbers_series = pd.Series(salesAppleList)

# Get the window of series
# of observations of specified window size
windows = numbers_series.rolling(windowSize)

# Create a series of moving
# averages of each window
moving_averages = windows.mean()

# Convert pandas series back to list
moving_averages_list = moving_averages.tolist()

# Remove null entries from the list
final_list = moving_averages_list[windowSize - 1:]

print(final_list)
plt.plot(final_list)
plt.show()
