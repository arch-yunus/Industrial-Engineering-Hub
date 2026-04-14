# 🗓️ Proje Yönetimi: CPM ve PERT Analizi

Projelerin zamanında ve bütçe dahilinde bitirilmesi için ağ analizleri kritik öneme sahiptir.

## 1. Kritik Yol Yöntemi (CPM)
Projenin en kısa sürede bitirilmesini sağlayan, boşluğu (float) olmayan aktiviteler dizisidir.

### Hesaplama Adımları:
- **İleri Geçiş (Forward Pass):** En erken başlama (ES) ve bitiş (EF) süreleri hesaplanır.
- **Geri Geçiş (Backward Pass):** En geç başlama (LS) ve bitiş (LF) süreleri hesaplanır.
- **Boşluk (Slack/Float):** $Slack = LS - ES = LF - EF$.
- **Kritik Yol:** Slack değeri 0 olan aktivitelerdir.

## 2. PERT - Üçlü Tahmin Yöntemi
Belirsizliğin yüksek olduğu durumlarda istatistiksel süre tahmini yapar.
- $a$: İyimser süre
- $m$: En olası süre
- $b$: Kötümser süre

### Formüller:
- **Beklenen Süre:** $t_e = \frac{a + 4m + b}{6}$
- **Varyans:** $\sigma^2 = (\frac{b - a}{6})^2$

---
*Endüstri Mühendisliği Karar Destek Sistemi — Industrial-Engineering-Hub*
