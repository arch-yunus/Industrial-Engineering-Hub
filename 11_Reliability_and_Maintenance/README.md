# Modül 11: Güvenilirlik Mühendisliği ve Bakım Yönetimi 🛠️

Güvenilirlik, "bir sistemin veya parçanın, belirlenmiş çalışma koşulları altında ve belirli bir süre boyunca işlevini hatasız yerine getirme olasılığıdır." Bakım ise bu olasılığı diri tutma eylemidir.

## 📝 Teorik Temeller

### 1. Güvenilirlik Fonksiyonu $R(t)$
Zamanın bir fonksiyonu olarak sistemin çalışmaya devam etme olasılığını ifade eder.
- **MTBF (Mean Time Between Failures):** Arızalar arası ortalama süre (Tamir edilebilir sistemler).
- **MTTF (Mean Time To Failure):** Arızaya kadar geçen ortalama süre (Atılabilir sistemler).

### 2. Sistem Konfigürasyonları
- **Seri Sistemler:** Bir parçanın bozulması tüm sistemi durdurur. $R_{sys} = R_1 \times R_2 \times \dots \times R_n$. En zayıf halka kadar güçlüdür.
- **Paralel Sistemler (Yedekleme):** Bir parçanın çalışması sistemin çalışması için yeterlidir. $R_{sys} = 1 - [(1-R_1) \times (1-R_2) \times \dots \times (1-R_n)]$.

### 3. Bakım Stratejileri
- **Düzeltici Bakım (Corrective):** Arıza olduktan sonra yapılan müdahale (Yangın söndürme).
- **Önleyici Bakım (Preventive):** Arıza olmadan, belirli zaman aralıklarıyla yapılan bakım (TBM - Time Based Maintenance).
- **Kestirimci Bakım (Predictive):** Sensör verilerine göre arıza riskini öngörüp yapılan bakım (CBM - Condition Based Maintenance).

## 🛠️ Dahili Araçlar

### [system_reliability_calc.py](system_reliability_calc.py)
Seri ve paralel bileşenlerden oluşan karmaşık sistemlerin toplam güvenilirlik olasılığını hesaplayan bir mühendislik aracıdır.

## 📚 Kaynakça
- *Ebeling, C. E.:* An Introduction to Reliability and Maintainability Engineering.
- *O'Connor, P.:* Practical Reliability Engineering.
- *Dhillon, B. S.:* Maintainability, Maintenance, and Reliability for Engineers.
