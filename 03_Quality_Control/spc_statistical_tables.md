# 📊 İstatistiksel Kalite Kontrol Tablo ve Formülleri

SPC (Statistical Process Control) için kullanılan standart katsayılar ve hesaplama yöntemleridir.

## 1. Değişkenler İçin Kontrol Kartı Katsayıları
$X̄$ (Ortalama) ve $R$ (Aralık) kartları için kullanılan sabit değerler:

| Örnek Hacmi (n) | $A_2$ | $D_3$ | $D_4$ | $d_2$ |
|---|---|---|---|---|
| 2 | 1.880 | 0 | 3.267 | 1.128 |
| 3 | 1.023 | 0 | 2.574 | 1.693 |
| 4 | 0.729 | 0 | 2.282 | 2.059 |
| 5 | 0.577 | 0 | 2.114 | 2.326 |
| 6 | 0.483 | 0 | 2.004 | 2.534 |
| 10 | 0.308 | 0.223 | 1.777 | 3.078 |

### Kontrol Limitleri Formülleri:
- **$X̄$ Kartı:** $UCL = X̄̄ + A_2R̄$ ve $LCL = X̄̄ - A_2R̄$
- **$R$ Kartı:** $UCL = D_4R̄$ ve $LCL = D_3R̄$

## 2. Nitelikler İçin Kontrol Kartları
- **p-kartı (Kusurlu Oranı):** $p̄ = \frac{\sum Hatalı}{\sum Muayene}$
- **c-kartı (Hata Sayısı):** $c̄ = \frac{\sum Hatalar}{\text{Örnek Sayısı}}$

---
*Endüstri Mühendisliği Karar Destek Sistemi — Industrial-Engineering-Hub*
