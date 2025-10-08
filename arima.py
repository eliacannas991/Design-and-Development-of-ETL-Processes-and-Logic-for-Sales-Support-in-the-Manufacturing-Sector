data_arima = data.rename(columns={'Date': 'ds', 'Sales': 'y'})
data_arima = data_arima.set_index('ds')['y']
# Definizione modello ARIMA
arima_model = ARIMA(data_arima, order=(10, 0, 2))  
arima_fit = arima_model.fit()

# Previsione mese successivo
forecast_arima = arima_fit.forecast(steps=1)