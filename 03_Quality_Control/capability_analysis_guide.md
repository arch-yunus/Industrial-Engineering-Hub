# 🏭 Proses Yetenek Analizi (Capability Analysis)

Bir sürecin, müşteri spektlerine (limitlerine) ne kadar uygun üretim yapabildiğini ölçen istatistiksel bir disiplindir.

## 1. Temel İndisler: $C_p$ ve $C_{pk}$

### $C_p$ (Proses Potansiyeli)
Sürecin değişkenliğinin (yayılım), spekt genişliğine oranını gösterir. Merkeze odaklanmaz.
$$C_p = \frac{USL - LSL}{6\sigma}$$

### $C_{pk}$ (Gerçek Proses Yeteneği)
Sürecin merkeze olan yakınlığını da hesaba katar.
$$C_{pk} = \min \left[ \frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma} \right]$$

## 2. Yorumlama Kriterleri
- **$C_{pk} < 1.0$:** Süreç yetersizdir. Hatalı ürün çıkma olasılığı yüksektir.
- **$1.0 \leq C_{pk} < 1.33$:** Süreç kabul edilebilir ancak risklidir.
- **$C_{pk} \geq 1.33$:** Süreç yeterlidir (Sanayi standardı).
- **$C_{pk} \geq 2.0$:** Altı Sigma seviyesinde mükemmel süreç.

## 3. $C_p$ vs $C_{pk}$ İlişkisi
- Eğer $C_p = C_{pk}$ ise süreç tam merkezdedir.
- Eğer $C_p > C_{pk}$ ise süreçte bir "kayma" (shift) vardır.

---
*Endüstri Mühendisliği Karar Destek Sistemi — Industrial-Engineering-Hub*
