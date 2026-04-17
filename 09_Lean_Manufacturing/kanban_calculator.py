import math

def calculate_kanban_cards():
    print("="*50)
    print("🏮 KANBAN HESAPLAYICI (YALIN ÜRETİM)")
    print("="*50)
    try:
        daily_demand = float(input("Günlük Ortalama Talep (Adet): "))
        lead_time = float(input("Tedarik/Üretim Süresi (Gün): "))
        safety_stock_percent = float(input("Güvenlik Stoğu Yüzdesi (Örn: %10 için 10): ")) / 100
        container_capacity = float(input("Bir Kutu/Kasanın Kapasitesi (Adet): "))
        
        # Kanban Formula: K = (D * L * (1 + S)) / C
        numerator = daily_demand * lead_time * (1 + safety_stock_percent)
        kanban_cards = math.ceil(numerator / container_capacity)
        
        print("\n--- SONUÇLAR ---")
        print(f"Toplam Gereken Parça Miktarı Dolaşımda: {numerator:.2f}")
        print(f"📦 Gerekli KANBAN KART (Kutu) Sayısı: {kanban_cards}")
        print("Sistem tavsiyesi: Yalın üretim için kart sayısını minimumda tutmak esastır.")
    except Exception as e:
        print("Hata: Girdiğiniz değerleri kontrol edin.")

if __name__ == "__main__":
    calculate_kanban_cards()
