# Phase 5: Simülasyon ve Sistem Modelleme 🎲

Simülasyon, "Gerçek hayatta denemesi imkansız veya çok pahalı olan sistemlerin, bilgisayar ortamında taklit edilmesi" sanatıdır. Endüstri Mühendisliği'nde simülasyon, büyük yatırımlardan önce riskleri görmek için kullanılır.

## 📝 Teorik Temeller

### 1. Kesikli Olay Simülasyonu (Discrete Event Simulation - DES)
Sistemin durumunun sadece belirli "olay" anlarında değiştiği modelleme türüdür (Ör: Bir parçanın makineye girişi, bir müşterinin sıradan ayrılışı).
- **Varlıklar (Entities):** Sistemde akan nesneler (Parçalar, Müşteriler).
- **Kaynaklar (Resources):** Sınırlı kapasiteye sahip birimler (Makineler, Kasiyerler).
- **Kuyruklar (Queues):** Kaynak bekleyen varlıkların toplandığı alanlar.

### 2. Monte Carlo Simülasyonu
Deterministik bir modelin, girdi değişkenlerine olasılık dağılımları atanarak binlerce kez çalıştırılmasıdır. Belirsizlik altındaki riskleri analiz etmek için kullanılır.
- **PERT/CPM Risk Analizi:** Bir projenin bitiş süresinin olasılıksal dağılımını bulur.

### 3. Ajan Bazlı Modelleme (Agent-Based Modeling)
Bireylerin (ajanların) birbirleriyle ve çevreleriyle etkileşimlerine odaklanan sistem modelleme yaklaşımıdır.

## 🛠️ Dahili Araçlar

### [simpy_factory_model.py](simpy_factory_model.py)
`SimPy` kütüphanesi kullanarak, bir üretim hattındaki makine ve operatör darboğazlarını analiz eden profesyonel bir DES modelidir.

### [monte_carlo_risk.py](monte_carlo_risk.py)
Proje yönetiminde (PERT) kritik yol sürelerini modelleyerek, projenin zamanında bitme olasılığını hesaplayan Monte Carlo simülasyonudur.

## 📚 Kaynakça
- *Law, A. M.:* Simulation Modeling and Analysis.
- *Kelton, W. D.:* Simulation with Arena.
- *Banks, J.:* Discrete-Event System Simulation.
