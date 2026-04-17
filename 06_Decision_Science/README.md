# Modül 6: Karar Bilimi ve Çok Ölçütlü Karar Verme (MCDM) 🧠

Karar Bilimi, belirsizlik ve birden fazla (genellikle çelişen) kriterin olduğu durumlarda rasyonel seçimler yapmayı sağlayan disiplindir. Endüstri Mühendisleri için üst yönetim seviyesinde kritik rol oynar.

## 📝 Teorik Temeller

### 1. Karar Verme Süreci
- **Alternatifler:** Seçilebilecek farklı yollar/çözümler.
- **Kriterler:** Kararı etkileyen faktörler (Maliyet, Kalite, Hız, Güvenilirlik).
- **Ağırlıklar:** Kriterlerin önem derecesi.

### 2. AHP (Analytic Hierarchy Process)
Thomas Saaty tarafından geliştirilen, kriterleri ikili karşılaştırmalar (pairwise comparisons) yaparak ağırlıklandıran bir yöntemdir. Tutarlılık Oranı (Consistency Ratio) ile kararın mantıksal doğruluğu denetlenebilir.

### 3. TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)
Alternatifleri, "İdeal Çözüme" en kısa mesafe ve "Negatif İdeal Çözüme" en uzak mesafe olma kriterine göre sıralar.

## 🛠️ Dahili Araçlar

### [ahp_calculator.py](ahp_calculator.py)
Kriterlerin önem derecelerini girdi olarak alır ve özvektör (eigenvector) metodunu kullanarak kriter ağırlıklarını (weights) hesaplar.

### [topsis_ranker.py](topsis_ranker.py)
Normalizasyon ve ağırlıklandırma işlemlerini yaparak en iyi alternatifi seçen bir sıralama aracıdır.

## 📚 Kaynakça
- *Saaty, T. L.:* The Analytic Hierarchy Process.
- *Hwang, C. L. & Yoon, K.:* Multiple Attribute Decision Making.
