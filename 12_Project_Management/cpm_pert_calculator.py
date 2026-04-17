def calculate_cpm_pert():
    print("="*50)
    print("⏱️ CPM/PERT PROJE YÖNETİMİ ANALİZÖRÜ")
    print("="*50)
    print("Ağ analizi ile projelerin beklenen süresi ve varyansını hesaplar.\n")
    try:
        tasks = []
        n = int(input("Kaç adet aktivite gireceksiniz?: "))
        for i in range(n):
            task_name = input(f"\nAktivite {i+1} Adı: ")
            opt = float(input("  İyimser Süre (a): "))
            most = float(input("  Olası Süre (m): "))
            pess = float(input("  Kötümser Süre (b): "))
            
            # PERT Formülleri: TE = (a + 4m + b) / 6, Var = ((b-a)/6)^2
            expected_time = (opt + 4 * most + pess) / 6
            variance = ((pess - opt) / 6) ** 2
            
            tasks.append({
                'name': task_name,
                'TE': expected_time,
                'Var': variance
            })
            
        print("\n--- PERT BEKLENEN SÜRELER ---")
        total_time = 0
        total_var = 0
        for t in tasks:
            print(f"Aktivite {t['name']} -> Beklenen: {t['TE']:.2f} | Varyans: {t['Var']:.2f}")
            # Basit olması adına, hepsinin kritik yolda olduğunu varsayalım (örnek kod)
            total_time += t['TE']
            total_var += t['Var']
            
        print("\n--- (Tüm aktivitelerin seri olduğu varsayımıyla) VARSAYIMSAL PROJE ÖZETİ ---")
        print(f"Proje Beklenen Tamamlanma Süresi (Kritik Yol Toplamı): {total_time:.2f}")
        print(f"Toplam Proje Varyansı: {total_var:.2f}")
        
    except Exception as e:
        print("Hata:", str(e))

if __name__ == "__main__":
    calculate_cpm_pert()
