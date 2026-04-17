# Modül 10: Mühendislik Ekonomisi ve Yatırım Analizi 💰

Endüstri Mühendisi, teknik veriyi finansal dile tercüme eden kişidir. Bir projenin mühendislik açısından kusursuz olması yetmez; aynı zamanda kârlı ve sürdürülebilir olması gerekir.

## 📝 Teorik Temeller

### 1. Paranın Zaman Değeri (Time Value of Money)
Bugünkü 1 TL, yarınki 1 TL'den daha değerlidir. Bu kavram, tüm finansal analizlerin temelidir.
- **Bileşik Faiz:** $F = P(1 + i)^n$
- **İndirgeme (Present Value):** Gelecekteki nakit akışlarının bugünkü değerine çekilmesi.

### 2. Yatırım Değerleme Yöntemleri
- **Net Bugünkü Değer (NPV):** Tüm nakit giriş ve çıkışlarının bugünkü değerlerinin toplamıdır. $NPV > 0$ ise proje kabul edilir.
- **İç Verimlilik Oranı (IRR):** NPV'yi sıfır yapan iskonto oranıdır. Şirketin sermaye maliyetinden yüksek olmalıdır.
- **Geri Ödeme Süresi (Payback Period):** Yatırımın kendisini ne kadar sürede amorti ettiği.

### 3. Amortisman ve Vergiler
Varlıkların zamanla değer kaybetmesi ve vergi kalkanı etkisi, net nakit akışlarını doğrudan etkiler.

## 🛠️ Dahili Araçlar

### [investment_appraisal.py](investment_appraisal.py)
Yıllık nakit akışlarını ve başlangıç yatırım tutarını girdi olarak alarak NPV ve Geri Ödeme Süresi gibi metrikleri otomatik hesaplayan finansal analiz aracıdır.

## 📚 Kaynakça
- *Blank, L. & Tarquin, A.:* Engineering Economy.
- *Park, C. S.:* Contemporary Engineering Economics.
- *Newnan, D. G.:* Engineering Economic Analysis.
