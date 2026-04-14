# Modül 7: Sistem Dinamiği ve Karmaşıklık Yönetimi 🌀

Sistem Dinamiği, doğrusal olmayan karmaşık sistemlerin zaman içindeki davranışını anlamak için kullanılan bir modelleme yaklaşımıdır. "Bütünü görmek" ve geri besleme (feedback) döngülerini analiz etmek temelidir.

## 📝 Teorik Temeller

### 1. Sistem Düşüncesi (Systems Thinking)
Bir olayın tekil nedeninden ziyade, o olayı yaratan yapısal ilişkileri inceler.
- **Causal Loop Diagrams (CLD):** Değişkenler arasındaki neden-sonuç ilişkilerini ve döngülerini görselleştirir.
- **Reinforcing Loop (R):** Değişimi hızlandıran (kartopu etkisi) döngüler.
- **Balancing Loop (B):** Değişimi dengeleyen (hedefe yönlendiren) döngüler.

### 2. Stok ve Akış Modelleri (Stocks & Flows)
Sistemin fiziksel yapısını modeller.
- **Stok (Stock):** Sistemin o andaki durumu (Ör: Depodaki su seviyesi, nakit miktarı).
- **Akış (Flow):** Stoğun zaman içindeki değişim hızı (Ör: Giriş hızı, çıkış hızı).

### 3. Kamçı Etkisi (Bullwhip Effect)
Tedarik zincirinde, son tüketici talebindeki küçük bir dalgalanmanın, üreticiye doğru gidildikçe artarak büyümesi fenomenidir. Bilgi asimetrisi ve gecikmelerden kaynaklanır.

## 🛠️ Dahili Araçlar

### [bullwhip_simulator.py](bullwhip_simulator.py)
Bir perakendeci, toptancı, distribütör ve fabrikadan oluşan 4 katmanlı bir tedarik zincirini simüle ederek bilginin ve stokların zaman içindeki dalgalanmasını görselleştirir.

## 📚 Kaynakça
- *Forrester, J. W.:* Industrial Dynamics.
- *Sterman, J. D.:* Business Dynamics: Systems Thinking and Modeling for a Complex World.
- *Meadows, D. H.:* Thinking in Systems: A Primer.
