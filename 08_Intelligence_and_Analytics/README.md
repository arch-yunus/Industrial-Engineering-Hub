# Modül 8: Zeka ve Veri Analitiği (Intelligence & Analytics) 🛰️

Bu modül, Endüstri Mühendisliği ile Veri Bilimi ve Yapay Zeka disiplinlerinin kesişim noktasına odaklanır. Veri artık sadece raporlamak için değil, geleceği tahmin etmek ve otonom sistemler kurmak için kullanılır.

## 📝 Teorik Temeller

### 1. Endüstriyel Veri Bilimi
Klasik istatistiğin (SPC) ötesine geçerek, büyük veri setlerinden anlamlı örüntüler çıkarma sürecidir.
- **Tahminleme (Predictive Analytics):** Makine öğrenmesi modelleri ile talep, fiyat veya arıza tahmini.
- **Tanımlama (Descriptive Analytics):** Mevcut durumun dashboardlar ile görselleştirilmesi.
- **Yönerge Verme (Prescriptive Analytics):** "Ne yapmalıyım?" sorusuna optimizasyon algoritmaları ile cevap verme.

### 2. Kestirimci Bakım (Predictive Maintenance - PdM)
Sensör verilerini kullanarak, bir makinenin ne zaman arızalanacağını tahmin etme ve arıza oluşmadan müdahale etme stratejisidir. Bu, plansız duruş sürelerini (downtime) minimize eder.

### 3. Dijital İkiz (Digital Twin)
Fiziksel bir sistemin (fabrika, depo, makine) dijital ortamdaki canlı kopyasıdır. Simülasyon ve gerçek zamanlı verinin birleşimidir.

## 🛠️ Dahili Araçlar

### [ai_demand_forecaster.py](../02_Production_Planning/ai_demand_forecaster.py)
`scikit-learn` kütüphanesi kullanarak, geçmiş talep verileri üzerinden doğrusal regresyon analizi yapar ve gelecek dönem satış projeksiyonlarını oluşturur.

## 📚 Kaynakça
- *Provost, F. & Fawcett, T.:* Data Science for Business.
- *Goodfellow, I.:* Deep Learning.
- *Endüstri 4.0 ve Akıllı Fabrikalar:* Çeşitli akademik makaleler ve beyaz kağıtlar.
