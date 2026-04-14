# 🔮 İleri Talep Tahmin Yöntemleri

Gelecekteki talebi tahmin etmek, üretim planlama ve stok yönetiminin başlangıç noktasıdır.

## 1. Zaman Serisi Analizi
Talebin geçmiş verilerdeki örüntülerini (trend, mevsimsellik, döngü) kullanarak tahmin yapma.

### Hareketli Ortalamalar (Moving Average)
Son n dönemin ortalaması alınır.
$$t_t = \frac{\sum_{i=i}^{n} D_{t-i}}{n}$$

### Üstel Düzeltme (Exponential Smoothing)
Geçmiş hata payını dikkate alarak güncelleme yapar.
$$t_t = \alpha D_{t-1} + (1 - \alpha) F_{t-1}$$
- $\alpha$: Düzeltme katsayısı (0 ile 1 arası).

## 2. Tahmin Hata Metrikleri
Tahmin modelinin doğruluğunu ölçmek için kullanılır:
- **MAD (Mean Absolute Deviation):** Mutlak hataların ortalaması.
- **MSE (Mean Squared Error):** Hataların karelerinin ortalaması (Büyük hataları cezalandırır).
- **MAPE (Mean Absolute Percentage Error):** Oransal hata.

## 3. Holt-Winters Modeli
Hem trendi hem de mevsimselliği modele katan ileri düzey üstel düzeltme yöntemidir.

---
*Endüstri Mühendisliği Karar Destek Sistemi — Industrial-Engineering-Hub*
