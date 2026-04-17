import numpy as np

def calculate_reliability():
    print("="*50)
    print("🛠️ SİSTEM GÜVENİLİRLİĞİ (RELIABILITY) HESAPLAYICI")
    print("="*50)
    print("Bileşenlerin güvenilirlik oranlarına (R) göre Seri veya Paralel sistem hesaplaması yapar.\n")
    try:
        sys_type = input("Sistem Tipi (Seri için 'S', Paralel için 'P'): ").strip().upper()
        reliabilities_str = input("Bileşen Güvenilirlik Değerleri (0-1 arası, virgülle ayrılmış, ör: 0.95,0.85,0.90): ")
        
        R_list = [float(x) for x in reliabilities_str.split(',')]
        
        for r in R_list:
            if not (0 <= r <= 1):
                print(f"Hata: Güvenilirlik değeri {r} aralık dışında (0 ile 1 arasında olmalı).")
                return
                
        if sys_type == 'S':
            # Series: R_sys = R1 * R2 * ... * Rn
            R_sys = np.prod(R_list)
            print("\n--- SERİ SİSTEM SONUCU ---")
            print(f"⚙️ Tüm bileşenlerin çalışmasına bağımlı sistem güvenilirliği: {R_sys:.4f} ({R_sys*100:.2f}%)")
        elif sys_type == 'P':
            # Parallel: R_sys = 1 - ((1-R1)*(1-R2)*...*(1-Rn))
            fail_probs = [1 - r for r in R_list]
            R_sys = 1 - np.prod(fail_probs)
            print("\n--- PARALEL SİSTEM SONUCU ---")
            print(f"🛡️ Yedekli sistem (Redundancy) güvenilirliği: {R_sys:.4f} ({R_sys*100:.2f}%)")
        else:
            print("Tanımsız sistem tipi. Lütfen 'S' veya 'P' giriniz.")
    except Exception as e:
        print("Hata:", str(e))

if __name__ == "__main__":
    calculate_reliability()
