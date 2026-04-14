# Phase 3: Kalite Mühendisliği ve Yönetimi 📉

Kalite, bir ürünün müşterinin beklentilerini karşılama (ve aşma) derecesidir. Endüstri Mühendisliği perspektifinde kalite, istatistiksel varyasyonun kontrol altına alınmasıdır.

## 📝 Teorik Temeller

### 1. İstatistiksel Süreç Kontrol (SPC)
Sürecin kararlı olup olmadığını ve sadece rastgele nedenlerden kaynaklanan varyasyon içerip içermediğini denetlemek için kullanılır.
- **Değişken Grafikleri:** $\bar{X}$ (Ortalama), R (Açıklık), S (Standart Sapma).
- **Nitelik Grafikleri:** p (Kusurlu oranı), c (Kusur sayısı), u (Birim başına kusur).

### 2. Süreç Yeteneği (Process Capability)
Bir sürecin, belirlenmiş spesifikasyon limitleri ($LSL, USL$) içerisinde çıktı üretme kabiliyetidir.
- **Cp Index:** Sürecin yayılımını ölçer.
- **Cpk Index:** Sürecin hedefe göre ne kadar merkezlendiğini ölçer.

### 3. Altı Sigma (Six Sigma)
Milyo başına sadece 3.4 hata hedefleyen, kök neden odaklı bir metodolojidir.
- **DMAIC:** Define, Measure, Analyze, Improve, Control.
- **Yalın Altı Sigma (Lean Six Sigma):** Hız (israf azaltma) ile kaliteyi (varyasyon azaltma) birleştirir.

## 🛠️ Dahili Araçlar

### [sqc_control_charts.py](sqc_control_charts.py)
Gözlem verilerinden otomatik olarak Üst Kontrol Limiti (UCL) ve Alt Kontrol Limiti (LCL) hesaplar ve `matplotlib` kullanarak kontrol grafiklerini çizer.

## 📚 Kaynakça
- *Montgomery, D. C.:* Introduction to Statistical Quality Control.
- *Feigenbaum, A. V.:* Total Quality Control.
- *Ishikawa, K.:* Guide to Quality Control.
