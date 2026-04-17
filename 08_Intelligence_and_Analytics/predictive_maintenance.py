import random

def predict_maintenance():
    print("="*60)
    print("🛰️ KESTİRİMCİ BAKIM (PREDICTIVE MAINTENANCE) SİMÜLATÖRÜ")
    print("="*60)
    print("Sensör verilerine dayalı arıza olasılığı (RUL - Remaining Useful Life) algoritması.\n")
    try:
        temp = float(input("Makine Sıcaklığı (°C): "))
        vibration = float(input("Titreşim Seviyesi (mm/s): "))
        operating_hours = float(input("Çalışma Saati (Saat): "))
        
        # Basit bir Risk Skoru hesaplaması
        risk_score = 0
        if temp > 75:
            risk_score += (temp - 75) * 1.5
        if vibration > 4.5:
            risk_score += (vibration - 4.5) * 10
        if operating_hours > 5000:
            risk_score += (operating_hours - 5000) * 0.005
            
        probability_of_failure = min(100, risk_score)
        
        print("\n--- ANALİZ SONUÇLARI ---")
        print(f"Hesaplanan Risk Skoru: {risk_score:.2f}")
        print(f"🔥 Yüksek Arıza Olasılığı: %{probability_of_failure:.2f}")
        
        if probability_of_failure > 70:
            print("🚨 KRİTİK ALARM: Sistemi acilen durdurun ve planlı bakım başlatın!")
            print("Tavsiye: Sensör verileri anomali gösteriyor.")
        elif probability_of_failure > 40:
            print("⚠️ UYARI: Bir sonraki vardiyada önleyici bakım (preventive) ekibini yönlendirin.")
        else:
            print("✅ DURUM NORMAL: Spektrogram ve termal veriler operasyonel sınırlar içerisinde.")
            
    except Exception as e:
        print("Hata:", str(e))

if __name__ == "__main__":
    predict_maintenance()
