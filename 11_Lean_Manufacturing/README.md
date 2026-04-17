# Modül 9: Yalın Üretim ve Toyota Üretim Sistemi (TPS) 🏮

Yalın Üretim, "değer katmayan her türlü israfı (Muda) yok ederek, en kısa çevrim süresinde en yüksek kaliteyi ve en düşük maliyeti hedefleyen" bir felsefedir.

## 📝 Teorik Temeller

### 1. İsrafın 7 Türü (MUDA)
1. **Aşırı Üretim:** Gereğinden fazla veya erken üretim.
2. **Bekleme:** İşçi veya makinenin boş kalması.
3. **Taşıma:** Gereksiz malzeme hareketi.
4. **Gereksiz İşlem:** Müşterinin para ödemeyeceği ekstra adımlar.
5. **Stok:** İhtiyaç fazlası hammadde veya ürün (sorunları örter).
6. **Hareket:** İşçinin ergonomik olmayan veya gereksiz hareketleri.
7. **Hatalı Üretim:** Hurda ve yeniden işleme maliyetleri.

### 2. Temel Yalın Araçları
- **5S:** Ayıkla, Düzenle, Temizle, Standartlaştır, Disiplin.
- **Kaizen:** Sürekli ama küçük iyileştirmeler.
- **SMED:** Tek haneli dakikalarda kalıp değişimi (Setup süresi azaltma).
- **Poka-Yoke:** Hata önleyici düzenekler.
- **Kanban:** Tam zamanında üretim (JIT) için kartlı sinyal sistemi.

### 3. Değer Akış Şeması (Value Stream Mapping - VSM)
Bir ürünün hammaddeden müşteriye kadar olan tüm akışını, üzerindeki her saniyenin değer katıp katmadığını belirlemek için görselleştirir.

## 🛠️ Dahili Araçlar

### [kanban_calculator.py](kanban_calculator.py)
Günlük talep, tedarik süresi ve emniyet faktörü gibi değişkenleri baz alarak, sistemin akışını sağlayacak optimum **Kanban Kart Sayısını** hesaplar.

## 📚 Kaynakça
- *Ohno, T.:* Toyota Production System: Beyond Large-Scale Production.
- *Womack, J. P. & Jones, D. T.:* Lean Thinking.
- *Rother, M. & Shook, J.:* Learning to See (VSM Guide).
