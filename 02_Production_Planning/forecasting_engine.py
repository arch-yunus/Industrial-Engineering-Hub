"""
🔮 Industrial-Engineering-Hub: Forecasting Engine
Basic Time Series Analysis and Error Metrics
"""

import numpy as np
import pandas as pd

def simple_moving_average(data, n):
    """Calculates SMA for a given window n."""
    return data.rolling(window=n).mean()

def exponential_smoothing(data, alpha):
    """Calculates EMA with smoothing factor alpha."""
    result = [data[0]] # first value is same
    for n in range(1, len(data)):
        result.append(alpha * data[n] + (1 - alpha) * result[n-1])
    return result

def calculate_errors(actual, forecast):
    """Calculates MAD and MSE."""
    actual = np.array(actual)
    forecast = np.array(forecast)
    mad = np.mean(np.abs(actual - forecast))
    mse = np.mean((actual - forecast)**2)
    return mad, mse

def main():
    print("--- 🏭 Endüstri Mühendisliği: Talep Tahmin Motoru ---")
    
    # Sample Demand Data (12 months)
    months = np.arange(1, 13)
    demand = [120, 135, 140, 160, 155, 170, 185, 190, 210, 205, 220, 235]
    
    df = pd.DataFrame({'Month': months, 'Demand': demand})
    
    # 3-Month Moving Average
    df['SMA_3'] = simple_moving_average(df['Demand'], 3)
    
    # Exponential Smoothing (alpha = 0.3)
    df['EMA_0.3'] = exponential_smoothing(df['Demand'], 0.3)
    
    print("\n📈 Talep Tahmin Tablosu:")
    print(df.tail(5).to_string(index=False))
    
    # Error comparison (for values where SMA is available)
    valid_df = df.dropna()
    mad_sma, mse_sma = calculate_errors(valid_df['Demand'], valid_df['SMA_3'])
    mad_ema, mse_ema = calculate_errors(valid_df['Demand'], valid_df['EMA_0.3'])
    
    print("\n🔍 Performans Analizi (Hata Payları):")
    print(f"📍 SMA (3-Ay) -> MAD: {mad_sma:.2f}, MSE: {mse_sma:.2f}")
    print(f"📍 EMA (0.3)  -> MAD: {mad_ema:.2f}, MSE: {mse_ema:.2f}")
    
    if mad_ema < mad_sma:
        print("\n💡 Öneri: EMA modeli bu veri seti için daha düşük sapma gösteriyor.")
    else:
        print("\n💡 Öneri: SMA modeli bu veri seti için daha düşük sapma gösteriyor.")

if __name__ == "__main__":
    main()
