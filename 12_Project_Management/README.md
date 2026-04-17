# 🗓️ FAZ 12: Proje Yönetimi ve Ağ Analizi

Hoş geldiniz! Bu modül, endüstri mühendisliğinin temel taşlarından biri olan **Proje Yönetimi** tekniklerine, özellikle de **CPM (Kritik Yol Yöntemi)** ve **PERT (Program Değerlendirme ve Gözden Geçirme Tekniği)** analizlerine odaklanmaktadır.

Proje yönetiminde belirsizliklerin ve karmaşık süreçlerin üstesinden gelmek için analitik ağ modellerini kullanmak, kaynakların verimli tahsis edilmesini ve projenin zamanında teslimini garanti eder. Bu modül, projelerinizi deterministik ve stokastik bakış açılarıyla optimize etmeniz için tasarlanmıştır.

---

## 🎯 Modül Hedefleri

- **Zaman Optimizasyonu:** Bir projenin tamamlanabileceği minimum süreyi (Kritik Yol) algoritmik olarak hesaplamak.
- **Risk ve Belirsizlik Yönetimi:** PERT metodolojisi ile iyimser, olası ve kötümser senaryoları ağırlıklandırarak olasılıksal proje tamamlanma süresi (Expected Time) kestirimi yapmak.
- **Kaynak Dengeleme (Resource Leveling):** Aktivitelerin "bolluk (slack)" veya diğer adıyla "kesinti (float)" sürelerini analiz ederek kritik olmayan düğümlerden (node) kritik düğümlere kaynak kaydırmak.

---

## 🗂️ Mimari İçerik ve Matematiksel Modeller

### 1. Kritik Yol Yöntemi (Critical Path Method - CPM)
CPM, projedeki her bir faaliyet süresinin **deterministik** (kesin olarak bilindiği) varsayımlar altında çalışır. Aktiviteler arasındaki bağımlılık diyagramları üzerinden ileri ve geri besleme (forward/backward pass) algoritmaları kullanılarak hesaplanır.

* Temel Hesaplama Parametreleri:
  - **Erken Başlama (ES - Early Start) & Erken Bitiş (EF - Early Finish):** Başlangıçtan sona doğru ilerleyerek (Forward Pass) projenin teorik erken bitiş zamanlamasını belirler.
  - **Geç Başlama (LS - Late Start) & Geç Bitiş (LF - Late Finish):** Sondan başa doğru geriye giderek (Backward Pass) geciktirilebilecek maksimum tarih aralıklarını haritalar.
  - **Bolluk / Kesinti (Slack / Float):** $Slack = LS - ES = LF - EF$ formülü ile bulunur.

> [!CAUTION]
> **Kritik Yol (Critical Path):** Bolluk değeri sıfır ($Slack = 0$) olan aktivitelerin oluşturduğu yönlü grafik (directed graph) yoludur. Bu rota üzerindeki mili-saniyelik bir gecikme dahi projenin nihai teslim tarihini doğrudan öteler.

* **İlgili Modül:** `cpm_calculator.py`

### 2. Program Değerlendirme ve Gözden Geçirme Tekniği (PERT)
PERT, aktivite sürelerinin kesin olarak bilinemediği, stokastik (olasılıksal ve değişken) koşulların hakim olduğu (örneğin yazılım geliştirme, Ar-Ge, savunma sanayii projeleri) süreçler için tasarlanmıştır.

* Üçlü Tahmin Parametreleri:
  - $a$: İyimser Süre (Her şeyin kusursuz gittiği senaryo)
  - $m$: En Olası Süre (Normal şartlar altındaki beklenti)
  - $b$: Kötümser Süre (Sistematik olmayan tüm gecikmelerin yaşandığı senaryo)

* İstatistiksel Hesaplamalar:
  - **Beklenen Süre ($T_e$):** $\frac{a + 4m + b}{6}$ (Beta Dağılımı Yaklaşımı)
  - **Varyans ($\sigma^2$):** $\left(\frac{b - a}{6}\right)^2$ (Sürenin güven aralığını genişliği ve proje riski)

* **İlgili Modül:** `cpm_pert_calculator.py`

---

## 🚀 Çalıştırma Yönergeleri

Python tabanlı yöneylem araçlarımız CLI (Komut Satırı Arayüzü) üzerinden veya başka bir sisteme modül olarak import edilerek çağrılabilir:

```bash
# Deterministik analiz (CPM) hesabı için
python cpm_calculator.py

# Olasılıksal süreçler için (PERT ve CPM hesaplamaları)
python cpm_pert_calculator.py
```

> [!TIP]
> Çıktılar, projenin darboğazlarını (bottlenecks) belirlemek için loglanabilir veya görselleştirme araçları (Gantt Chart vs.) için bir ön veri olarak (pipeline) kullanılabilir.

---

## 📚 Kapsamlı Dokümantasyon
Analizlerin detaylı matrisleri, ileri istatistiksel standart sapma ($\sigma$) hesaplamaları ve teorik temeller için lütfen [`cpm_pert_analysis.md`](cpm_pert_analysis.md) dosyasını inceleyin.

---
*Endüstri Mühendisliği Karar Destek Sistemi — Industrial-Engineering-Hub*
