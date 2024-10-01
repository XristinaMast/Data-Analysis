# Time Series Forecasting: Demand Prediction for Bike Stations

This project demonstrates time series forecasting techniques applied to predict bike station demand. The dataset contains timestamps of when bikes are delivered or taken from a specific station. We use two time series models, **Exponential Smoothing** and **ARIMA**, to forecast the demand, and compare their performance using metrics like MAE (Mean Absolute Error) and RMSE (Root Mean Squared Error).

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Data](#data)
- [Methodology](#methodology)
- [Usage](#usage)
- [Evaluation](#evaluation)
- [Results](#results)
- [Technologies Used](#technologies-used)

## Project Overview
The goal of this project is to predict the demand for bikes at a specific station using a time series analysis of data. The demand is calculated by the difference between the number of bikes delivered and taken from the station. The dataset is divided into training and testing sets, with two models (Exponential Smoothing and ARIMA) used for forecasting. The performance of each model is evaluated and compared.

## Installation
### Prerequisites
To run this project, you will need:
- Python 3.x installed on your system
- The following Python libraries:
  - `pandas`
  - `numpy`
  - `statsmodels`
  - `sklearn`
  - `matplotlib`

### Installation Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/bike-station-demand-forecasting.git
    ```
2. Navigate to the project directory:
    ```bash
    cd bike-station-demand-forecasting
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Data
The data should be provided in a CSV format with the following columns:
- `StartTime`: The start time of a bike trip.
- `EndTime`: The end time of a bike trip.
- `StartStationId`: The ID of the station where the bike trip started.
- `EndStationId`: The ID of the station where the bike trip ended.

The project will group the data into 2-hour intervals and calculate the net demand for bikes at the target station.

### Example of Input Data:
| StartTime            | EndTime              | StartStationId | EndStationId |
|----------------------|----------------------|----------------|--------------|
| 2023-01-01 09:00:00  | 2023-01-01 09:15:00  | 1              | 2            |
| 2023-01-01 09:30:00  | 2023-01-01 10:00:00  | 2              | 1            |
| 2023-01-01 11:00:00  | 2023-01-01 11:30:00  | 1              | 1            |

## Methodology
1. **Data Preprocessing**: We convert the `StartTime` and `EndTime` columns to `datetime` format and round the times to the nearest 2-hour interval (`T = 2`).
2. **Demand Calculation**: The net demand is calculated as the difference between the number of bikes delivered to the station (`EndStationId = 1`) and the bikes taken from the station (`StartStationId = 1`).
3. **Train/Test Split**: The data is split into 70% training and 30% testing.
4. **Forecasting**:
    - **Exponential Smoothing**: A time series forecasting model with additive trend, applied to the training data.
    - **ARIMA**: An ARIMA model is fitted with order `(5, 1, 0)` and used to make predictions on the test data.
5. **Model Evaluation**: The models are evaluated using **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**.
6. **Visualization**: The forecasted values from both models are plotted alongside the actual test data.

## Usage
1. **Run the Script**: To run the forecasting script, provide the name of the CSV file that contains the bike station data. You will be prompted to input the file name.

    Example command:
    ```bash
    python forecasting_script.py
    ```

2. **Output**:
    - The program will output the **MAE** and **RMSE** for both models.
    - A plot will be generated to compare the actual demand with the predicted values from both models.

## Evaluation
To evaluate the models, the following metrics are used:
- **Mean Absolute Error (MAE)**: Measures the average magnitude of the errors in a set of predictions, without considering their direction.
- **Root Mean Squared Error (RMSE)**: Measures the square root of the average squared differences between predicted and actual values.

## Results
The performance of the models is printed in terms of **MAE** and **RMSE**. Additionally, a plot visualizes the predictions of both models alongside the actual demand.

Example output:
```
Exponential Smoothing - MAE: 5.123, RMSE: 6.456 ARIMA - MAE: 4.789, RMSE: 5.987
```

## Technologies Used
- **Python 3.x**
- **Pandas** for data manipulation and analysis
- **NumPy** for numerical computations
- **Statsmodels** for time series modeling
- **Scikit-learn** for evaluation metrics
- **Matplotlib** for data visualization
