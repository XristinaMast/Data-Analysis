import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import csv


def read_data(file_name):
    try:
        data = pd.read_csv(file_name)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None

file_name = input("Enter the name of the CSV file: ")

data = read_data(file_name)
if data is None:
    exit()


data['StartTime'] = pd.to_datetime(data['StartTime'])
data['EndTime'] = pd.to_datetime(data['EndTime'])  

T = 2 
data['StartInterval'] = data['StartTime'].dt.floor(
    f'{T}H')
data['EndInterval'] = data['EndTime'].dt.floor(f'{T}H')

delivered = data[data['EndStationId'] == 1].groupby('EndInterval').size()
taken = data[data['StartStationId'] == 1].groupby('StartInterval').size()

demand = delivered.to_frame(name='delivered').join(taken.to_frame(name='taken'), how='outer').fillna(0)
demand['demand'] = demand['delivered'] - demand['taken']

split_ratio = 0.7
split_index = int(len(demand) * split_ratio)

train_data = demand['demand'][:split_index] 
test_data = demand['demand'][split_index:]


model_es = ExponentialSmoothing(train_data, trend='add', seasonal=None,
                                damped_trend=False).fit() 
es_forecast = model_es.forecast(
    len(test_data)) 

model_arima = ARIMA(train_data, order=(5, 1, 0)).fit()
arima_forecast = model_arima.forecast(
    steps=len(test_data))


def evaluate_forecast(actual, forecast):
    mae = mean_absolute_error(actual, forecast)
    rmse = np.sqrt(mean_squared_error(actual, forecast))
    return mae, rmse


es_mae, es_rmse = evaluate_forecast(test_data, es_forecast)
arima_mae, arima_rmse = evaluate_forecast(test_data, arima_forecast)

print(f'Exponential Smoothing - MAE: {es_mae}, RMSE: {es_rmse}')
print(f'ARIMA - MAE: {arima_mae}, RMSE: {arima_rmse}')

plt.figure(figsize=(12, 6))
plt.plot(train_data.index, train_data, label='Training Data')
plt.plot(test_data.index, test_data, label='Test Data')
plt.plot(test_data.index, es_forecast,
         label='Exponential Smoothing Forecast') 
plt.plot(test_data.index, arima_forecast, label='ARIMA Forecast') 
plt.legend()
plt.show()
