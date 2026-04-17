# 🗓️ Proje Yönetimi: Kapsamlı CPM ve PERT Analizi Dokümantasyonu

Projelerin zamanında ve bütçe kısıtları dahilinde tamamlanabilmesi için ağ analizleri (Network Analysis) operasyon yönetiminin en kritik unsurlarındandır. Bu doküman, algoritmaların arka planındaki teorik formülleri ve hesaplama metodolojilerini sistematik olarak açıklar.

---

## 1. Kritik Yol Yöntemi (Critical Path Method - CPM)
Bir projenin, aktiviteler arası bağımlılıkları (Precedence Relationships) ihlal etmeden tamamlanabileceği en kısa süreyi veren ardışık faaliyetler dizisidir.

### Algoritmik Hesaplama Adımları (Network Pass)

CPM, bir ağ grafiğinde ileri ve geri geçiş olmak üzere iki aşamalı bir dizi hesaplama ile gerçekleşir.

*   **İleri Geçiş (Forward Pass):** Projenin erken takvimini hesaplar.
    *   **En Erken Başlama (Early Start - ES):** Bir aktivitenin başlayabileceği en erken an. Öncelikli aktivitelerin en büyük `EF` değerine eşittir.
        $$ ES_j = \max(EF_i) $$ (tüm öncül $i$ aktiviteleri için)
    *   **En Erken Bitiş (Early Finish - EF):** $EF = ES + Süre$.

*   **Geri Geçiş (Backward Pass):** Projenin gecikme töleransını hesaplar.
    *   **En Geç Bitiş (Late Finish - LF):** Projenin bitiş tarihini uzatmadan aktivitenin tamamlanması gereken en geç zaman. Kendinden sonraki (ardıl) aktivitelerin en küçük `LS` değerine eşittir.
        $$ LF_i = \min(LS_j) $$ (tüm ardıl $j$ aktiviteleri için)
    *   **En Geç Başlama (Late Start - LS):** $LS = LF - Süre$.

*   **Boşluk (Slack/Float) Analizi:** Aktivitenin, tüm projeyi geciktirmeden ne kadar süre sarkabileceğini gösterir.
    *   $$ Slack = LS - ES \quad \text{veya} \quad LF - EF $$

> [!IMPORTANT]
> **Kritik Yol Kuralı:** Eğer bir istasyon (node) veya aktivite için $Slack = 0$ ise, o aktivite "Kritiktir" (Kritik Yol üzerindedir). Toplam proje süresi, Kritik Yoldaki tüm aktivitelerin sürelerinin toplamına eşittir.

---

## 2. PERT - Üçlü Zaman Tahmin Yöntemi ve İstatistik
PERT (Program Evaluation and Review Technique), faaliyeti tamamlamak için gereken sürenin önceden kesin olarak bilinemediği projelerde kullanılır. PERT, Beta ve Normal Dağılım olasılık teoremleri üzerine inşa edilmiştir.

### Parametreler (The Three Estimates)
*   $a$: **İyimser Süre (Optimistic Time)**
*   $m$: **En Olası Süre (Most Likely Time)**
*   $b$: **Kötümser Süre (Pessimistic Time)**

### Matematiksel Dağılım Formülleri
PERT metodolojisi süre tahminlerini bir Beta olasılık dağılım eğrisine oturtur. Her bir aktivite için beklenen değer ve varyans aşağıdaki gibi hesaplanır:

*   **Beklenen Proje Süresi (Expected Time - $t_e$):**
    Ağırlıklandırılmış ortalama alınır (En olası senaryoya ağırlık verilir).
    $$ t_e = \frac{a + 4m + b}{6} $$

*   **Varyans ($\sigma^2$) ve Standart Sapma ($\sigma$):**
    Tahminin belirsizlik (Risk) seviyesini ölçer. Genişlik (b-a) ne kadar büyükse, belirsizlik o kadar yüksektir (Tahmin bandının altıda biri temel kabul edilir).
    $$ \text{Varyans} (\sigma^2) = \left(\frac{b - a}{6}\right)^2 $$
    $$ \text{Standart Sapma} (\sigma) = \frac{b - a}{6} $$

> [!TIP]
> **Projenin Toplam Beklenen Süresi ve Varyansı:** \
> $T_{(Proje)} = \sum t_{e} \text{ (Sadece Kritik Yol üzerindeki aktivitelerin)}$ \
> $\sigma^2_{(Proje)} = \sum \sigma^2 \text{ (Sadece Kritik Yol üzerindeki aktivitelerin)}$ \
> Kritik olmayan faaliyetlerin varyansları toplam proje risk hesabına (Standart Normal Dağılım eğrisi tablosundayken) _eklenmez._

---
*Endüstri Mühendisliği Karar Destek Sistemi — Industrial-Engineering-Hub*
