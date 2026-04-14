"""
📦 Industrial-Engineering-Hub: Production Planning Tool
AI-Powered Demand Forecaster (Linear Regression)
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class AIDemandForecaster:
    def __init__(self, historical_data):
        """
        historical_data: List of demand values in chronological order
        """
        self.data = np.array(historical_data).reshape(-1, 1)
        self.periods = np.arange(len(historical_data)).reshape(-1, 1)
        self.model = LinearRegression()

    def train(self):
        self.model.fit(self.periods, self.data)

    def forecast(self, future_periods=5):
        last_period = self.periods[-1][0]
        future_x = np.arange(last_period + 1, last_period + 1 + future_periods).reshape(-1, 1)
        predictions = self.model.predict(future_x)
        return predictions.flatten()

    def plot(self, future_periods=5):
        predictions = self.forecast(future_periods)
        full_x = np.arange(len(self.data) + future_periods)
        
        plt.figure(figsize=(10, 6))
        plt.plot(self.periods, self.data, label='Geçmiş Talep Verisi', marker='o')
        
        future_x = np.arange(len(self.data), len(self.data) + future_periods)
        plt.plot(future_x, predictions, label='AI Tahmini (Projeksiyon)', linestyle='--', marker='s', color='red')
        
        plt.title('Endüstriyel Talep Tahmini: Lineer Regresyon Analizi')
        plt.xlabel('Dönem (Zaman)')
        plt.ylabel('Miktar (Birim)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: AI Talep Tahmini ---")
    
    # Example Historical Data (24 months of demand)
    history = [120, 130, 125, 140, 155, 160, 158, 175, 190, 185, 200, 210,
               205, 220, 235, 230, 245, 260, 255, 270, 285, 280, 295, 310]
    
    forecaster = AIDemandForecaster(history)
    forecaster.train()
    
    forecast_results = forecaster.forecast(5)
    
    print("\n📊 GELECEK DÖNEM TAHMİNLERİ:")
    print("-" * 50)
    for i, val in enumerate(forecast_results):
        print(f"🔹 Dönem {len(history) + i + 1}: {val:.2f} birim")
    print("-" * 50)
    
    print("🛰️ Grafik oluşturuluyor...")
    forecaster.plot(5)

if __name__ == "__main__":
    main()
