# Industrial-Engineering-Hub 🏭: Endüstriyel Karar Destek ve Optimizasyon Ekosistemi

[![Discipline: Industrial Engineering](https://img.shields.io/badge/Discipline-Industrial%20Engineering-darkred.svg)]()
[![Paradigm: Systems Thinking](https://img.shields.io/badge/Paradigm-Systems%20Thinking-blue.svg)]()
[![Complexity: Advanced](https://img.shields.io/badge/Complexity-Advanced-purple.svg)]()
[![Status: Maintained](https://img.shields.io/badge/Status-Maintained-success.svg)]()

> "Mühendisler bir şeyler yapar; Endüstri Mühendisleri ise o şeyleri **daha iyi** yapar."

## 📜 Manifesto ve Amacımız
**Industrial-Engineering-Hub**, modern sistem tasarımı, optimizasyon ve veri odaklı yönetim prensiplerinin bir araya getirildiği bütünsel bir referans merkezidir. Bu ekosistem, karmaşık endüstriyel problemleri matematiksel modeller, istatistiksel araçlar ve ileri simülasyon teknikleri ile çözmeyi hedefler. Temel felsefemiz: **Sürekli İyileştirme (Kaizen) ve Maksimum Verimlilik.**

---

## 🏛️ Modül Mimarisi ve Külliyat

Bu depo, bir endüstri mühendisinin ihtiyaç duyacağı tüm kritik alanları bir "Masterclass" derinliğinde kapsar:

### 0️⃣ FAZ 0: Yöneylem Araştırması (Foundation)
* **LP ve Simplex:** Kısıtlı optimizasyonun matematiksel temelleri.
* **Ağ Optimizasyonu:** Lojistik ağ tasarımı, en kısa yol ve maksimum akış problemleri.

### 🟢 FAZ 1: İş Etüdü ve Ergonomi
* **Metot Mühendisliği:** Değer katmayan adımların (Muda) yok edilmesi ve standart iş tasarımı.
* **Rating & Allowance:** Performans derecelendirme ve endüstriyel tolerans rehberleri.

### 🔵 FAZ 2: Üretim Planlama ve Kontrol (PPC)
* **Talep Tahmini:** İleri zaman serisi analizleri ve tahmin motoru (Python).
* **EOQ & Stok:** Stok maliyet minimizasyonu ve yeniden sipariş noktası optimizasyonu.

### 🟠 FAZ 3: Kalite Mühendisliği (Six Sigma)
* **SPC & Standartlar:** İstatistiksel süreç kontrol tabloları ve kontrol grafikleri.
* **Proses Yeteneği:** Cp, Cpk analizleri ile süreç olgunluk ölçümü.

### 🚚 FAZ 4: Lojistik ve Tesis Planlama
* **Yer Seçimi:** Ağırlık merkezi ve AHP temelli tesis lokasyon modelleri.
* **Hat Dengeleme:** Montaj hattı optimizasyonu ve çevrim süresi yönetimi.

### 🎲 FAZ 5: Simülasyon ve Risk Analizi
* **DES (SimPy):** Fabrika akış modellerinin dijital ikizi.
* **Monte Carlo:** Kar/zarar ve proje süreleri için olasılıksal risk analizi.

---

## 📂 Depo Hiyerarşisi (Directory Structure)

```text
Industrial-Engineering-Hub/
│
├── 00_Operations_Research/            # Optimizasyon ve Matematiksel Modeller
│   ├── linear_programming_and_simplex.md
│   ├── simplex_solver_utils.py
│   └── network_optimization_models.md
│
├── 01_Work_Study_and_Ergonomics/      # İş Etüdü ve İnsan Faktörleri
│   ├── method_engineering_principles.md
│   └── rating_allowance_reference.md
│
├── 02_Production_Planning/            # Üretim Planlama ve Stok
│   ├── forecasting_engine.py
│   ├── advanced_forecasting_methods.md
│   ├── inventory_eoq_calculator.py
│   └── mrp_logic_explanation.md
│
├── 03_Quality_Control/                # İstatistiksel Kalite ve Altı Sigma
│   ├── spc_statistical_tables.md
│   ├── capability_analysis_guide.md
│   └── six_sigma_dmaic_guide.md
│
├── 04_Facility_and_Supply_Chain/      # Tesis Tasarımı ve Lojistik
│   ├── assembly_line_balancing.py
│   └── facility_location_models.md
│
├── 05_Simulation/                     # Sistem Modelleme ve Risk
│   ├── monte_carlo_risk_analysis.md
│   └── simpy_factory_model.py
│
├── 06_Engineering_Economics/          # Finansal Karar Analizi
│   └── financial_models_guide.md
│
├── 07_Project_Management/             # Planlama ve Ağ Analizi
│   └── cpm_pert_analysis.md
│
├── data/                              # Örnek üretim ve talep veri setleri
├── requirements.txt                   # Python bağımlılıkları
└── README.md
```

---

## 🛠️ Yazılım Stoku
* **Diller:** Python, R.
* **Kütüphaneler:** `SciPy` (Opt), `Pandas` (Data), `SimPy` (Sim), `PuLP` (LP), `Plotly` (Viz).

---

## 🚀 Horizon 2025: Endüstriyel Zekaya Doğru
Gelecek sürümlerde bu HUB; otonom tedarik zinciri ajanları, AI destekli çizelgeleme motorları ve IIoT veri hatlarının simülasyonu ile daha da derinleşecektir.

---
*Mükemmel sistem yoktur, her zaman optimize edilecek bir adım daha vardır.*