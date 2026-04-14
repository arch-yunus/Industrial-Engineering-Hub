# Phase 1: İş Etüdü ve Ergonomi (Micro-Optimization) 🔬

Bu modül, bir sistemdeki en küçük birim olan "insan ve iş" etkileşimini optimize etmeye odaklanır. Verimlilik, sadece hızlı çalışmak değil, en doğru ve en az yorucu yöntemle çalışmaktır.

## 📝 Teorik Temeller

### 1. İş Etüdü (Work Study)
İş etüdü, iki ana teknikten oluşur:
- **Metot Etüdü:** İşi yapma yöntemini daha kolay ve etkili hale getirmek için sistematik olarak kaydetme ve eleştirel inceleme işlemidir. (Amacı: İsrafı yok etmek).
- **İş Ölçümü (Zaman Etüdü):** Kalifiye bir işçinin, belirli bir işi, belirli bir performans seviyesinde yapması için gereken süreyi belirler.

### 2. Standart Zaman Formülü
Bir işin standart zamanı şu şekilde hesaplanır:
$$T_{standart} = T_{gozlem} \times \text{Performans (Rating factor)} \times (1 + \text{Toleranslar})$$

### 3. Ergonomi ve İş Güvenliği
Modern Endüstri Mühendisliği'nde verimlilik kadar çalışanın sağlığı da kritiktir.
- **RULA (Rapid Upper Limb Assessment):** Üst ekstremite yüklenmelerini değerlendirir.
- **REBA (Rapid Entire Body Assessment):** Tüm vücut duruşlarını ve yüklenmelerini analiz eder.
- **Antropometri:** Araç ve gereçlerin insan vücut ölçülerine uygun tasarımı (Yüzde 5-95 kuralı).

## 🛠️ Dahili Araçlar

### [time_study_standardizer.py](time_study_standardizer.py)
Gözlem sürelerinizi, performans değerlendirmelerinizi ve tolerans faktörlerini girerek saniyeler içinde bilimsel bir **Standart Zaman** raporu oluşturmanızı sağlar.

## 📚 Kaynakça
- *ILOE (International Labour Organization):* Introduction to Work Study.
- *F.W. Taylor:* The Principles of Scientific Management.
