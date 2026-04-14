# Phase 4: Tesis Planlama ve Lojistik Ağ Tasarımı 🚚

Bu modül, bir fabrikanın fiziksel yerleşiminden, ürünlerin son tüketiciye ulaşana kadar katettiği tüm lojistik yolun optimizasyonuna odaklanır.

## 📝 Teorik Temeller

### 1. Tesis Yerleşimi (Facility Layout)
Makinelerin ve departmanların, malzeme akışını minimize edecek şekilde yerleştirilmesidir.
- **SLP (Systematic Layout Planning):** Muther tarafından geliştirilen, niteliksel ve niceliksel verileri harmanlayan yöntem.
- **Hücresel Üretim:** Benzer parçaların bir arada üretilmesini sağlayarak kurulum sürelerini azaltır.

### 2. Montaj Hattı Dengeleme (Line Balancing)
Bir üretim hattındaki işleri istasyonlara, boş zamanı (idle time) minimize edecek şekilde dağıtma işlemidir.
- **Takt Time:** Talebi karşılamak için gereken üretim hızı.

### 3. Lojistik ve Tedarik Zinciri
 Hammaddeden nihai ürüne kadar olan tüm fiziksel akışın yönetimidir.
- **Ulaştırma Modeli:** Kaynaklardan (fabrikalar) hedeflere (depolar) en düşük maliyetle ürün sevkiyatı (Doğrusal Programlama).
- **Cross-Docking:** Depolama maliyetlerini yok etmek için malların depoya girdiği gibi sevk edilmesi.

## 🛠️ Dahili Araçlar

### [assembly_line_balancing.py](assembly_line_balancing.py)
"Largest Candidate Rule" sezgiseli kullanarak, görevleri çevrim süresi kısıtına göre istasyonlara atar ve hat verimliliğini hesaplar.

### [logistics_optimizer.py](logistics_optimizer.py)
`PuLP` kütüphanesi kullanarak, birden fazla kaynak ve varış noktası arasındaki ulaştırma problemini çözen bir doğrusal programlama modelidir.

## 📚 Kaynakça
- *Muther, R.:* Systematic Layout Planning.
- *Ballou, R. H.:* Business Logistics Management.
- *Chopra, S. & Meindl, P.:* Supply Chain Management.
