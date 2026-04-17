"""
🌀 Industrial-Engineering-Hub: System Dynamics Tool
Bullwhip Effect Simulator (4-tier Supply Chain)
"""

import matplotlib.pyplot as plt
import numpy as np

class BullwhipSimulator:
    def __init__(self, periods=20, base_demand=100, demand_spike=20):
        self.periods = periods
        self.base_demand = base_demand
        self.demand_spike = demand_spike
        self.tiers = ["Müşteri", "Perakendeci", "Toptancı", "Distribütör", "Fabrika"]

    def simulate(self):
        # 0: Customer Demand (Inputs)
        # 1-4: Order amounts from each tier
        orders = np.zeros((len(self.tiers), self.periods))
        
        # Step 1: Customer Demand with a sudden spike at period 5
        orders[0, :] = self.base_demand
        orders[0, 5:] += self.demand_spike
        
        # Step 2: Tier calculations (Orders propagation with delays and magnification)
        for t in range(1, len(self.tiers)):
            lead_time_delay = 1
            amplification_factor = 1.2 # Safety margin causing bullwhip
            
            for p in range(self.periods):
                if p < lead_time_delay:
                    orders[t, p] = self.base_demand
                else:
                    # Orders are based on previous tier's demand with extra safety margin
                    orders[t, p] = orders[t-1, p-lead_time_delay] * amplification_factor
                    
        return orders

    def plot(self, results):
        plt.figure(figsize=(12, 7))
        for i, tier in enumerate(self.tiers):
            plt.plot(results[i], label=f'{tier} Siparişleri', linewidth=2 if i==0 else 1.5)
            
        plt.title('Tedarik Zincirinde Kamçı Etkisi (Bullwhip Effect) Simülasyonu')
        plt.xlabel('Zaman (Hafta)')
        plt.ylabel('Sipariş Miktarı')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.show()

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: Kamçı Etkisi Simülatörü ---")
    
    sim = BullwhipSimulator(periods=25)
    results = sim.simulate()
    
    print("\n📊 SİMÜLASYON VERİLERİ (Örnek Kesitler):")
    print("-" * 50)
    print(f"🔹 Başlangıç Müşteri Talebi: {sim.base_demand}")
    print(f"🔹 Talep Sıçraması (5. Hafta): +{sim.demand_spike}")
    print(f"🔹 Fabrika Siparişindeki Maksimum Dalgalanma: {np.max(results[4]):.2f}")
    print("-" * 50)
    
    sim.plot(results)

if __name__ == "__main__":
    main()
