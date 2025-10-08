forecast['Season'] = forecast['ds'].dt.month.apply(classify_season)
forecast_seasonal = forecast.groupby(['ds', 'Season'])['yhat'].sum().reset_index()