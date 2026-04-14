# Phase 2: Üretim Planlama ve Kontrol (PPC) 🏭

Üretim planlama, bir fabrika veya servis sisteminin "beynidir". Talebi tahmin etmekten, hammaddenin ne zaman sipariş edileceğine ve makinelerin hangi sıra ile çalışacağına kadar tüm stratejik kararlar burada alınır.

## 📝 Teorik Temeller

### 1. Talep Tahmini (Demand Forecasting)
Veriye dayalı kararların başlangıç noktasıdır.
- **Zaman Serisi Modelleri:** Basit hareketli ortalama, ağırlıklı hareketli ortalama ve üstel düzeltme (Holt-Winters).
- **Regresyon:** Talep ile dış faktörler (fiyat, hava durumu vb.) arasındaki ilişki.

### 2. Envanter (Stok) Yönetimi
Stok, Endüstri Mühendisi için "durgun para" ve "gizli israf" demektir.
- **EOQ (Economic Order Quantity):** Toplam yıllık sipariş ve elde tutma maliyetlerini minimize eden miktarı bulur.
- **ABC Analizi:** Ürünleri yıllık tüketim değerlerine göre A (yüksek değer), B (orta) ve C (düşük) olarak sınıflandırarak kontrol seviyesini belirler.

### 3. İhtiyaç Planlaması (MRP)
Bir nihai ürünün üretilmesi için gerekli olan tüm alt parçaların ne zaman ve ne kadar gerektiğini hesaplayan sistemdir.
- **BOM (Bill of Materials):** Ürün ağacı.
- **Net İhtiyaç:** Brüt İhtiyaçlar - Eldeki Stok - Gelen Siparişler.

## 🛠️ Dahili Araçlar

### [inventory_eoq_calculator.py](inventory_eoq_calculator.py)
Klasik Harris-Wilson modelini kullanarak optimum sipariş miktarını ve yeniden sipariş noktasını (ROP) hesaplar.

### [mrp_engine.py](mrp_engine.py)
`pandas` kütüphanesini kullanarak, karmaşık ürün ağaçlarını işleyen ve net hammadde ihtiyaçlarını zaman boyutunda dökümleyen gelişmiş bir MRP motorudur.

## 📚 Kaynakça
- *Orlicky, J.:* Material Requirements Planning.
- *Silver, E. A.:* Inventory Management and Production Planning and Scheduling.
