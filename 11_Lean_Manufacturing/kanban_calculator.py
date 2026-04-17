"""
🏮 Industrial-Engineering-Hub: Lean Manufacturing Tool
Kanban Card Count Calculator (JIT Production)
"""

import math

class KanbanCalculator:
    def __init__(self, daily_demand, lead_time, container_size, safety_factor=0.1):
        """
        daily_demand: Average daily demand (units)
        lead_time: Time to replenish (days)
        container_size: Capacity of one container
        safety_factor: Buffer for variability (default 10%)
        """
        self.d = daily_demand
        self.l = lead_time
        self.c = container_size
        self.s = safety_factor

    def calculate_n_cards(self):
        # N = (D * L * (1 + S)) / C
        n = (self.d * self.l * (1 + self.s)) / self.c
        return math.ceil(n)

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: Kanban Hesaplayıcı ---")
    
    try:
        D = float(input("Günlük Ortalama Talep (adet/gün): "))
        L = float(input("Tedarik Süresi / Bekleme Süresi (gün): "))
        C = float(input("Bir Kasa/Konteyner Kapasitesi (adet): "))
        S = float(input("Emniyet Faktörü (Ör: %15 için 0.15): ") or 0.1)
        
        calc = KanbanCalculator(D, L, C, S)
        n_cards = calc.calculate_n_cards()
        
        print("\n" + "="*50)
        print(f"📊 KANBAN ANALİZİ:")
        print(f"🔹 Gereken Toplam Kanban Kartı Sayısı: {n_cards}")
        print(f"🔹 Toplam Boruhattı Envanteri: {n_cards * C} adet")
        print("="*50)
        print("✅ Not: Her kart bir dolu konteyneri temsil eder. Kartların sisteme girmesiyle üretim başlar (Çekme Sistemi).")
        
    except ValueError:
        print("🛑 Hata: Lütfen geçerli sayısal değerler giriniz.")

if __name__ == "__main__":
    main()
