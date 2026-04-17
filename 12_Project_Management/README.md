# 🗓️ FAZ 12: Proje Yönetimi ve Ağ Analizi

Hoş geldiniz! Bu modül, endüstri mühendisliğinin temel taşlarından biri olan **Proje Yönetimi** tekniklerine, özellikle de **CPM (Kritik Yol Yöntemi)** ve **PERT (Program Değerlendirme ve Gözden Geçirme Tekniği)** analizlerine odaklanmaktadır.

Proje yönetiminde belirsizliklerin ve karmaşık süreçlerin üstesinden gelmek için analitik ağ modellerini kullanmak, kaynakların verimli tahsis edilmesini ve projenin zamanında teslimini garanti eder.

## 🎯 Hedefler

- **Zaman Optimizasyonu:** Bir projenin tamamlanabileceği en kısa süreyi (Kritik Yol) hesaplamak.
- **Risk ve Belirsizlik Yönetimi:** PERT kullanarak, iyimser, en olası ve kötümser süre tahminleriyle olasılıksal süre hesaplamak.
- **Kaynak Yönetimi:** Aktivitelerin "bolluk (slack)" sürelerini analiz ederek, kaynakların kritik olmayan işlerden kritik işlere kaydırılmasını (resource leveling) sağlamak.

## 🗂️ İçerik ve Matematiksel Modeller

### 1. Kritik Yol Yöntemi (CPM)
CPM, faaliyet sürelerinin deterministik (kesin) olduğu varsayımıyla çalışır. Her aktivitenin bir önceliği ve süresi vardır.

Temel Kavramlar:
- **Erken Başlama (ES) ve Erken Bitiş (EF):** İleriye doğru hesaplama.
- **Geç Başlama (LS) ve Geç Bitiş (LF):** Geriye doğru hesaplama.
- **Bolluk / Kesinti (Slack / Float) = LS - ES = LF - EF**

> **🚨 Kritik Yol:** Bolluk değeri sıfır (0) olan aktivitelerin oluşturduğu yoldur. Projede yaşanacak en ufak bir gecikme tüm projenin teslim tarihini etkiler.

*İlgili Kod:* `cpm_calculator.py`

### 2. PERT Analizi
PERT, sürelerin stokastik (olasılıksal) olduğu durumlarda devreye girer (örneğin Ar-Ge projeleri, yeni ürün geliştirmeleri).

Tahmin Parametreleri:
- $a$: İyimser Süre
- $m$: En Olası Süre
- $b$: Kötümser Süre

Hesaplanan Değerler:
- **Beklenen Süre ($T_e$):** $\frac{(a + 4m + b)}{6}$
- **Varyans ($\sigma^2$):** $(\frac{b - a}{6})^2$

*İlgili Kod:* `cpm_pert_calculator.py`

## 🚀 Nasıl Kullanılır?

Python tabanlı araçlar CLI üzerinden veya modül üzerinden çağrılabilir:

```bash
# CPM hesabı için
python cpm_calculator.py

# PERT ve CPM hesaplamaları (Olasılıksal analiz) için
python cpm_pert_calculator.py
```

## 📚 Dokümantasyon
Bu analizlerin teorik temelleri ve formül matrisleri için lütfen [`cpm_pert_analysis.md`](cpm_pert_analysis.md) dosyasını inceleyin.

---
*Endüstri Mühendisliği Karar Destek Sistemi — Industrial-Engineering-Hub*
