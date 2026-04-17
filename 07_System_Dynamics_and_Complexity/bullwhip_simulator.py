import numpy as np

def simulate_bullwhip():
    print("="*50)
    print("🌀 KAMÇI ETKİSİ (BULLWHIP EFFECT) SİMÜLATÖRÜ")
    print("="*50)
    print("Tedarik zincirindeki sipariş varyansının talep varyansına oranını (σ²_sipariş / σ²_talep) hesaplar.\n")
    try:
        demand_str = input("Müşteri Talepleri (virgülle ayrılmış liste, ör: 10,12,11,14,9): ")
        orders_str = input("Üretici Siparişleri (virgülle ayrılmış liste, ör: 15,9,18,5,20): ")
        
        demand = [float(x) for x in demand_str.split(',')]
        orders = [float(x) for x in orders_str.split(',')]
        
        if len(demand) != len(orders):
            print("Hata: Talep ve Sipariş veri sayıları eşit olmalıdır!")
            return
            
        var_demand = np.var(demand, ddof=1)
        var_orders = np.var(orders, ddof=1)
        
        if var_demand == 0:
            print("Hata: Talep varyansı sıfır. Hesaplama yapılamaz.")
            return
            
        bullwhip_measure = var_orders / var_demand
        
        print("\n--- SONUÇLAR ---")
        print(f"Talep Varyansı: {var_demand:.2f}")
        print(f"Sipariş Varyansı: {var_orders:.2f}")
        print(f"🔥 Bullwhip Oranı (Bulwhip Measure): {bullwhip_measure:.2f}")
        
        if bullwhip_measure > 1:
            print("Uyarı: Kamçı Etkisi gözlemleniyor. Bilgi asimetrisi veya uzun tedarik süreleri olabilir.")
        elif bullwhip_measure < 1:
            print("Durum: Tedarik zinciri talebi yastıklıyor (Smoothing).")
        else:
            print("Durum: Stabil bir tedarik zinciri eşleşmesi.")
    except Exception as e:
        print("Hata:", str(e))

if __name__ == "__main__":
    simulate_bullwhip()
