"""
📦 Industrial-Engineering-Hub: Inventory Management Tool
Economic Order Quantity (EOQ) and Reorder Point (ROP) Calculator
"""

import math

def calculate_eoq(demand, ordering_cost, holding_cost):
    """
    Calculates EOQ: Q* = sqrt((2 * D * S) / H)
    """
    return math.sqrt((2 * demand * ordering_cost) / holding_cost)

def calculate_rop(average_daily_demand, lead_time, safety_stock=0):
    """
    Calculates Reorder Point: ROP = (d * L) + SS
    """
    return (average_daily_demand * lead_time) + safety_stock

def main():
    print("--- 🏭 Endüstri Mühendisliği Karar Destek Sistemi: Stok Optimizasyonu ---")
    
    try:
        # EOQ Inputs
        D = float(input("Yıllık Toplam Talep (birim/yıl): "))
        S = float(input("Sipariş Verme Maliyeti (₺/sipariş): "))
        H = float(input("Birim Elde Tutma Maliyeti (₺/birim/yıl): "))
        
        # ROP Inputs
        L = float(input("Tedarik Süresi (gün): "))
        SS = float(input("Güvenlik Stoğu (birim - opsiyonel, yoksa 0): ") or 0)
        
        # Calculations
        eoq = calculate_eoq(D, S, H)
        daily_demand = D / 365
        rop = calculate_rop(daily_demand, L, SS)
        
        total_holding_cost = (eoq / 2) * H
        total_ordering_cost = (D / eoq) * S
        total_annual_cost = total_holding_cost + total_ordering_cost
        
        # Output
        print("\n" + "="*50)
        print(f"📊 SONUÇLAR:")
        print(f"✅ Ekonomik Sipariş Miktarı (EOQ): {eoq:.2f} birim")
        print(f"✅ Yeniden Sipariş Noktası (ROP): {rop:.2f} birim")
        print(f"✅ Yıllık Toplam Stok Maliyeti: {total_annual_cost:.2f} ₺")
        print(f"✅ Yıllık Sipariş Sayısı: {D/eoq:.2f}")
        print("="*50)
        
    except ValueError:
        print("❌ Hata: Lütfen geçerli sayısal değerler giriniz.")

if __name__ == "__main__":
    main()
