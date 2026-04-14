# 0️⃣ Modül 0: Yöneylem Araştırması ve Lineer Programlama

> "Maksimum çıktı, minimum girdi; kısıtlar altında en iyi çözüm."

Yöneylem Araştırması (Operations Research), karmaşık karar verme problemlerinin matematiksel modellerle çözülmesidir.

## 1. Lineer Programlama (LP) Temelleri
LP, doğrusal bir amaç fonksiyonu ve doğrusal kısıtlar kümesinden oluşur.

**Genel Model Yapısı:**
$$\max/min \quad z = \sum_{j=1}^{n} c_j x_j$$
$$Kısıtlar: \quad \sum_{j=1}^{n} a_{ij} x_j \leq b_i \quad (i=1, \dots, m)$$
$$x_j \geq 0$$

## 2. Simpleks Algoritması
Simpleks, çok boyutlu çözüm uzayında köşe noktalarını (extreme points) gezen iteratif bir algoritmadır.

### Adım Adım İşleyiş:
1. **Standart Forma Dönüştürme:** Eşitsizlikleri "slack" (artık) veya "surplus" (fazla) değişkenler kullanarak eşitliğe dönüştürün.
2. **Başlangıç Tablosunun Hazırlanması:** Temel uygun çözüm (BFS) ile tabloyu kurun.
3. **Optimallik Testi:** Amaç fonksiyonu satırındaki katsayıları inceleyin.
4. **Pivot Seçimi:** Giren değişken (en negatif katsayı) ve Çıkan değişken (en küçük pozitif oran testi) belirlenir.
5. **İterasyon:** Gauss-Jordan eliminasyonu ile yeni tablo oluşturulur.

## 3. Dualite Teorisi
Her LP probleminin (Primal), ona karşılık gelen bir "Dual" problemi vardır.
- Primal $\max$ ise Dual $\min$ olur.
- Primal kısıt değerleri, Dual amaç katsayıları olur.
- **Ekonomik Yorum:** Dual değişkenler, kısıtların "Gölge Fiyatları"nı (Shadow Prices) temsil eder.

---
*Endüstri Mühendisliği Karar Destek Sistemi — Industrial-Engineering-Hub*
