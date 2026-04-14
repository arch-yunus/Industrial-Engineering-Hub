"""
⏱️ Industrial-Engineering-Hub: Work Study Tool
Standard Time Calculator with Performance Rating and Allowances
"""

class TimeStudyStandardizer:
    def __init__(self, observation_times, rating_factor, allowance_percentage):
        """
        observation_times: list of times (e.g. seconds) for each cycle
        rating_factor: percentage (e.g. 1.10 for 10% faster than normal)
        allowance_percentage: percentage (e.g. 0.15 for 15% allowance)
        """
        self.observation_times = observation_times
        self.rating_factor = rating_factor
        self.allowance_percentage = allowance_percentage

    def calculate_average_time(self):
        return sum(self.observation_times) / len(self.observation_times)

    def calculate_normal_time(self):
        return self.calculate_average_time() * self.rating_factor

    def calculate_standard_time(self):
        return self.calculate_normal_time() * (1 + self.allowance_percentage)

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: Zaman Etüdü Standardizasyonu ---")
    
    try:
        times_input = input("Gözlemlenen çevrim sürelerini virgülle ayırarak giriniz (sn): ")
        obs_times = [float(t.strip()) for t in times_input.split(',')]
        
        rating = float(input("Performans Derecesi (Ör: Normal için 1.0, %10 hızlı için 1.1): "))
        allowance = float(input("Tolerans Yüzdesi (Ör: %15 için 0.15): "))
        
        study = TimeStudyStandardizer(obs_times, rating, allowance)
        
        avg_time = study.calculate_average_time()
        normal_time = study.calculate_normal_time()
        standard_time = study.calculate_standard_time()
        
        print("\n" + "="*50)
        print(f"📊 ZAMAN ETÜDÜ RAPORU:")
        print(f"🔹 Gözlem Sayısı: {len(obs_times)}")
        print(f"🔹 Ortalama Gözlem Süresi: {avg_time:.2f} sn")
        print(f"🔹 Normal Zaman (Avg * Rating): {normal_time:.2f} sn")
        print(f"🔹 STANDART ZAMAN (Normal * (1+Allow)): {standard_time:.2f} sn")
        print(f"🔹 Saatlik Standart Üretim Kapasitesi: {3600 / standard_time:.2f} adet/saat")
        print("="*50)
        
    except ValueError:
        print("🛑 Hata: Lütfen geçerli sayısal değerler giriniz.")

if __name__ == "__main__":
    main()
