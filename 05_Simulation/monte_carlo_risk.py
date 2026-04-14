"""
🎲 Industrial-Engineering-Hub: Simulation Tool
Monte Carlo Simulation for Project Risk Analysis (PERT)
"""

import numpy as np
import matplotlib.pyplot as plt

class ProjectRiskSim:
    def __init__(self, activities, iterations=10000):
        """
        activities: dict {name: (optimistic, most_likely, pessimistic)}
        iterations: number of simulation runs
        """
        self.activities = activities
        self.iterations = iterations
        self.results = None

    def simulate(self):
        # Using Triangular distribution for PERT
        simulated_times = np.zeros((self.iterations, len(self.activities)))
        
        for i, (name, (a, m, b)) in enumerate(self.activities.items()):
            simulated_times[:, i] = np.random.triangular(a, m, b, self.iterations)
            
        # Total project time is the sum of activity times (assuming purely serial for this demo)
        self.results = np.sum(simulated_times, axis=1)
        return self.results

    def plot_results(self, target_time):
        if self.results is None:
            self.simulate()
            
        prob_on_time = np.mean(self.results <= target_time) * 100
        
        plt.figure(figsize=(10, 6))
        plt.hist(self.results, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
        plt.axvline(target_time, color='red', linestyle='--', label=f'Hedef: {target_time} Gün')
        plt.title('Monte Carlo Proje Bitiş Süresi Dağılımı')
        plt.xlabel('Toplam Süre (Gün)')
        plt.ylabel('Frekans')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
        
        return prob_on_time

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: Monte Carlo Risk Analizi ---")
    
    # Example Project Activities: (Optimistic, Most Likely, Pessimistic)
    project_plan = {
        'Tasarım': (10, 15, 25),
        'Geliştirme': (20, 30, 50),
        'Test': (5, 10, 15),
        'Dağıtım': (2, 5, 10)
    }
    
    sim = ProjectRiskSim(project_plan)
    results = sim.simulate()
    
    target = 65 # Target days to complete
    prob = sim.plot_results(target)
    
    print(f"\n📊 SİMÜLASYON SONUÇLARI ({sim.iterations} İterasyon):")
    print("-" * 50)
    print(f"🔹 Ortalama Bitiş Süresi: {np.mean(results):.2f} gün")
    print(f"🔹 En Kısa Süre: {np.min(results):.2f} gün")
    print(f"🔹 En Uzun Süre: {np.max(results):.2f} gün")
    print(f"🔹 Hedef Süre ({target} gün) İçinde Bitme Olasılığı: %{prob:.2f}")
    print("-" * 50)

if __name__ == "__main__":
    main()
