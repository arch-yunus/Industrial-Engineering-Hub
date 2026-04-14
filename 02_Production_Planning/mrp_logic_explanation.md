# 🔵 Modül 2: Malzeme İhtiyaç Planlaması (MRP) Mantığı

MRP (Material Requirements Planning), üretim sürecinde hangi parçanın ne zaman ve ne miktarda gerektiğini hesaplayan bilgisayar tabanlı bir stok kontrol ve üretim planlama sistemidir.

## 1. MRP'nin Girdileri
Başarılı bir MRP çalışması için 3 temel veri gereklidir:
1. **Ana Üretim Programı (MPS):** Nihai üründen kaç adet ve ne zaman üretilecek?
2. **Ürün Ağacı (BOM - Bill of Materials):** Ürünü oluşturmak için hangi parçalardan kaçar adet lazım? (Hiyerarşik yapı).
3. **Stok Durum Kayıtları:** Elde ne kadar var? Yolda olan sipariş var mı?

## 2. Temel MRP Denklemi
MRP'nin kalbi "Brüt İhtiyaç" ile "Net İhtiyaç" arasındaki farktır.

$$Net İhtiyaç = Brüt İhtiyaç - (Eldeki Stok + Beklenen Teslimatlar) + Güvenlik Stoğu$$

## 3. Adım Adım MRP Süreci (Explosion)
1. **Netleştirme (Netting):** Brüt ihtiyaçtan eldeki stoğun düşülmesi.
2. **Parti Büyüklüğü Belirleme (Lot Sizing):** Net ihtiyaca göre sipariş miktarının belirlenmesi (LFL, EOQ, POQ vb.).
3. **Zaman Kaydırma (Offsetting):** Üretim veya tedarik süresi kadar (Lead Time) geriye gidilerek sipariş açma zamanının belirlenmesi.
4. **Patlatma (Explosion):** Üst seviye ürünün net ihtiyacının, alt seviye parçaların brüt ihtiyacı olarak tanımlanması.

## 4. MRP'nin Amacı
- Stok maliyetlerini minimize etmek.
- Üretim aksamalarını (parça yokluğu) önlemek.
- Teslimat sürelerine sadık kalmak.

---
*Endüstri Mühendisliği Notları — Industrial-Engineering-Hub*
