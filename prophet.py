# Preprocess dati Prophet
prophet_data = data.rename(columns={'Date': 'ds', 'Sales': 'y'})

# Inizializzare modello 
model = Prophet()
model.add_seasonality(name='monthly', period=30, fourier_order=3)
model.fit(prophet_data)

# Creazione dataframe futuro per la previsione
future = model.make_future_dataframe(periods=1, freq='M') # Predice il mese successivo
forecast = model.predict(future)
