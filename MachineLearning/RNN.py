#Source: https://medium.com/analytics-vidhya/weather-forecasting-with-recurrent-neural-networks-1eaa057d70c3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Feature Scaling
from sklearn.preprocessing import MinMaxScaler

# RNN model for forecasting weather
import keras.layers as kl
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

# import dataset from weather_012019-102021.csv file
weather_df = pd.read_csv('../DataProcessing/Datasets/Weather/weather_012019-102021.csv')

# only include avg temperature column as to forecast temperature
# drop all the rows that have no values or has a NaN
weather_df = weather_df.dropna(subset=["tavg"])
weather_df = weather_df.reset_index(drop=True)

# create training and test datasets
x_train = []
y_train = []

#############################################################################
weather_df['split'] = np.random.randn(weather_df.shape[0], 1)
msk = np.random.rand(len(weather_df)) <= 0.8

# [':' all rows, '0:2' columns date and tavg]
train = weather_df[msk].iloc[:, 1:2].values
test = weather_df[~msk].iloc[:, 1:2].values
#############################################################################

#print(train)
print(type(train))
# print(test)

# Feature Scaling: normalize temperature in the range 0 to 1
sc = MinMaxScaler(feature_range=(0,1))
train_scaled = sc.fit_transform(train)

# next 4 days temperature forecast
n_future = 4
# past 30 days
n_past = 30

# x_train contains 30 previous temperature inputs before that day
# y_train contains 4 days temperature outputs after that day
for i in range(0, len(train_scaled) - n_past - n_future + 1):
    x_train.append(train_scaled[i : i + n_past, 0])
    y_train.append(train_scaled[i + n_past : i + n_past + n_future, 0])

# converts lists (x_train, y_train) to numpy array for fitting training set to the model
x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))


# defines layers in the RNN
regressor = Sequential()

regressor.add(kl.Bidirectional(LSTM(units = 30, return_sequences = True,
input_shape = (x_train.shape[1], 1) ) ))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 30, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 30, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 30))
regressor.add(Dropout(0.2))
regressor.add(Dense(units = n_future, activation = 'linear'))
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['acc'])
regressor.fit(x_train, y_train, epochs = 500, batch_size = 32 )


# test RNN performance with test dataset
test_scaled = sc.transform(test)
test_scaled = np.array(test_scaled)
test_scaled = np.reshape(test_scaled, (test_scaled.shape[1], test_scaled.shape[0], 1))

print(test_scaled)

# test RNN model with test dataset
predicted_temperature = regressor.predict(test_scaled)
predicted_temperature = sc.inverse_transform(predicted_temperature)
print("predicted_temp")
print(predicted_temperature)
#predicted_temperature = np.reshape(predicted_temperature, (predicted_temperature.shape[1], predicted_temperature[0]))

print(test)

