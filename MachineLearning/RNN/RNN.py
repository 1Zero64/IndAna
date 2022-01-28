import DataProcessing.DataPreparation as dp
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from random import seed
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from datetime import timedelta

# set a global pseudo-random generator at a fixed value
seed_value = 42
np.random.seed(seed_value)
seed(seed_value)
tf.random.set_seed(seed_value)

# load prepared weather data from DataProcessing
weather = dp.prepareWeatherData()

# change number indexes to date indexes
weather['date'] = pd.to_datetime(weather['date'])
weather.set_index('date', inplace=True)
weather = weather.resample('D').mean()

# use only column 'tavg'
weather = weather[['tavg']]

# change dataframe format to float for not loosing precision (float = uncountable infinity)
df = weather.copy()
weather = weather.values
weather = weather.astype('float32')

# normalize the dataset: learn the required parameters by having all values in a similar value range
scaler = MinMaxScaler(feature_range=(-1, 1))
sc = scaler.fit_transform(weather)

timestep = 30  # amount of time steps the rnn runs (memory of 30 characters)
# declare X and Y as empty list
X = []
Y = []

for i in range(len(sc) - timestep):
    X.append(sc[i:i + timestep])
    Y.append(sc[i + timestep])

# convert X and Y into numpy array
X = np.asanyarray(X)
Y = np.asanyarray(Y)

# split dataframe into train and test sets to verify accuracy after fitting the model
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
# X_train.shape: [batch_size, timesteps, feature]

# initializing the rnn
model = Sequential()  # plain stack of layers where each layer has exactly one input and one output tensor
# # 1st layer (input)
model.add(LSTM(32, activation='relu', input_shape=(X_train.shape[1:]), return_sequences=True))
model.add(Dropout(0.2))  # ignores a set of neurons (randomly) for preventing the net from overfitting
# # 2rd Layer (hidden)
model.add(LSTM(32, activation='relu', return_sequences=True))
model.add(Dropout(0.2))
# # 3rd Layer (hidden)
model.add(LSTM(32, activation='sigmoid', return_sequences=False))
model.add(Dropout(0.2))
# # 4th Layer (output)
model.add(Dense(1))  # allows neurons of the layer to be connected to every neuron of its preceding layer

model.compile(optimizer='adam', loss='mse', metrics=['acc'])

model.summary()
history = model.fit(X_train, Y_train, epochs=250, validation_data=(X_test, Y_test))

# make predictions
preds = model.predict(X_test)
preds = scaler.inverse_transform(preds)

Y_test = np.asanyarray(Y_test)
Y_test = Y_test.reshape(-1, 1)
Y_test = scaler.inverse_transform(Y_test)

Y_train = np.asanyarray(Y_train)
Y_train = Y_train.reshape(-1, 1)
Y_train = scaler.inverse_transform(Y_train)

print("")
print("Mean-Square Error: ", mean_squared_error(Y_test, preds))
print("Mean-Absolute Error: ", mean_absolute_error(Y_test, preds))

# plot model accuracy
plt.figure(figsize=(8, 5))
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'g')
plt.plot(epochs, val_loss, 'blue')
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Model Loss Curve")
plt.legend(('Training loss', 'Validation loss'))
plt.show()

# plot model results
plt.figure(figsize=(20, 9))
plt.plot(Y_test, 'blue', linewidth=2)
plt.plot(preds, 'r')
plt.legend(('Test', 'Predicted'))
plt.title("Temperature Prediction")
plt.grid(True)
plt.show()

# build dataframe with actual and predicted data
test = pd.DataFrame(Y_test, columns=['Actual'])
pred = pd.DataFrame(preds, columns=['Prediction'])

results = pd.concat([test, pred], axis=1)
results.to_csv('../../DataProcessing/Datasets/Weather/temperaturePrediction.csv')
print("")
print(results.head(20))


def insert_end(x_in, new_input):
    for i in range(timestep - 1):
        x_in[:, i, :] = x_in[:, i + 1, :]
    x_in[:, timestep - 1, :] = new_input
    return x_in


# this section is for unknown future
future = 30  # forecasting the next 30 steps
forcast = []
x_in = X_test[-1:, :, :]
time = []
for i in range(future):
    out = model.predict(x_in, batch_size=1)
    forcast.append(out[0, 0])
    x_in = insert_end(x_in, out[0, 0])
    time.append(pd.to_datetime(df.index[-1]) + timedelta(days=i + 1))

# make predictions
forcasted_output = np.asanyarray(forcast)
forcasted_output = forcasted_output.reshape(-1, 1)
forcasted_output = scaler.inverse_transform(forcasted_output)

# build predicted values dataframe
forcasted_output = pd.DataFrame(forcasted_output)
date = pd.DataFrame(time)
df_result = pd.concat([date, forcasted_output], axis=1)
df_result.columns = "date", "Forecast"

df_result.to_csv('../../DataProcessing/Datasets/Weather/temperatureForecast.csv')

# show model forecast values from dataframe
print("")
print(df_result)

# plot model forecast
plt.figure(figsize=(16, 8))
plt.title('Temperature Forecast')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Temperature', fontsize=18)
plt.plot(df['tavg'][2101:])
plt.plot(df_result.set_index('date')[['Forecast']], "r--")
plt.legend(('Actual', 'Forecast'))
plt.grid(True)
plt.show()
