"""
🛠️ Industrial-Engineering-Hub: Reliability Engineering Tool
System Reliability Calculator (Series and Parallel Configurations)
"""

import math

class ReliabilityCalculator:
    @staticmethod
    def series_reliability(reliabilities):
        """
        Rs = R1 * R2 * ... * Rn
        """
        result = 1.0
        for r in reliabilities:
            result *= r
        return result

    @staticmethod
    def parallel_reliability(reliabilities):
        """
        Rp = 1 - [(1 - R1) * (1 - R2) * ... * (1 - Rn)]
        """
        failure_prob = 1.0
        for r in reliabilities:
            failure_prob *= (1 - r)
        return 1 - failure_prob

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: Güvenilirlik Analizi ---")
    
    try:
        print("\n [1] Seri Sistem (En zayıf halka kadar güçlüdür)")
        print(" [2] Paralel Sistem (Yedeklemeli/Redundant)")
        choice = input("Sistem tipini seçin: ")
        
        rels_input = input("Bileşen güvenilirlik olasılıklarını virgülle ayırarak giriniz (0-1 arası): ")
        rels = [float(r.strip()) for r in rels_input.split(',')]
        
        calc = ReliabilityCalculator()
        
        if choice == '1':
            res = calc.series_reliability(rels)
            sys_type = "Seri"
        else:
            res = calc.parallel_reliability(rels)
            sys_type = "Paralel"
            
        print("\n" + "="*50)
        print(f"📊 SİSTEM GÜVENİLİRLİK ANALİZİ ({sys_type}):")
        print(f"🔹 Bileşen Sayısı: {len(rels)}")
        print(f"🔹 Toplam Sistem Güvenilirliği R(s): {res:.4f}")
        print(f"🔹 Sistem Arıza Olasılığı Q(s): {1 - res:.4f}")
        print("="*50)
        
    except ValueError:
        print("🛑 Hata: Lütfen geçerli sayısal değerler giriniz.")

if __name__ == "__main__":
    main()
