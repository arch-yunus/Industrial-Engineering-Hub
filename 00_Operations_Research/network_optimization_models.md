# 🕸️ Ağ Optimizasyon Modelleri (Network Models)

Ağ modelleri, düğümler (nodes) ve yaylar (arcs) arasındaki ilişkileri optimize etmek için kullanılır. Lojistik ve tedarik zinciri yönetiminin temelidir.

## 📝 Teorik Temeller

### 1. En Kısa Yol Problemi (Shortest Path)
Bir düğümden diğerine en düşük maliyetle (veya zamanla) gitme problemi.
- **Algoritma:** Dijkstra Algoritması.
- **Uygulama:** Google Haritalar, kargo rotalama.

### 2. Minimum Yayılma Ağacı (Minimum Spanning Tree - MST)
Tüm düğümleri, toplam yay uzunluğu minimum olacak şekilde birbirine bağlama problemi.
- **Algoritmalar:** Kruskal ve Prim Algoritmaları.
- **Uygulama:** Elektrik şebekesi döşeme, fiber optik ağ tasarımı.

### 3. Maksimum Akış Problemi (Maximum Flow)
Bir kaynaktan (source) bir hedefe (sink) birim zamanda gönderilebilecek maksimum miktar.
- **Algoritma:** Ford-Fulkerson Algoritması.
- **Uygulama:** Petrol boru hatları, veri trafiği yönetimi.

### 4. Taşıma ve Atama Problemleri
- **Taşıma Problemi:** Arz ve talep noktaları arasındaki toplam taşıma maliyetini minimize etme.
- **Atama Problemi:** n işin n makineye, toplam maliyet minimum olacak şekilde atanması (**Macar Yöntemi**).

---
*Endüstri Mühendisliği Notları — Industrial-Engineering-Hub*
