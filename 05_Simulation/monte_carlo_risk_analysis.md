# 🎲 Monte Carlo Risk Analizi

Monte Carlo simülasyonu, girdilerdeki belirsizliği (olasılık dağılımları) kullanarak çıktıların (kar, maliyet, tamamlanma süresi) olasılıksal dağılımını hesaplamaya yarar.

## 1. Uygulama Alanı: Proje Kar Zarar Analizi
Bir projenin gelirinin $Normal(100, 20)$ ve giderinin $Normal(80, 10)$ olduğu bir durumda, projenin zarar etme olasılığı nedir?

### Algoritma:
1. Girdi değişkenleri için dağılımları tanımla.
2. Rastgele binlerce (n=10,000) örnek çek.
3. Her örnek için sonucu hesapla.
4. Sonuçların histogramını ve güven aralığını analiz et.

```python
import numpy as np

# Simülasyon Sayısı
n = 10000

# Rastgele Girdiler
income = np.random.normal(100, 20, n)
expense = np.random.normal(80, 10, n)

# Sonuç
profit = income - expense

loss_probability = np.mean(profit < 0) * 100
print(f"Zarar Etme Olasılığı: %{loss_probability:.2f}")
```

## 2. Neden Monte Carlo?
- Deterministik modeller tek bir sonuç verirken, Monte Carlo **risk seviyesini** gösterir.
- Karmaşık ve doğrusal olmayan sistemlerin modellenmesini sağlar.

---
*Endüstri Mühendisliği Karar Destek Sistemi — Industrial-Engineering-Hub*
