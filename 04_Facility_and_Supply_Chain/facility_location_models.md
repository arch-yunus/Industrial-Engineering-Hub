# 🚚 Tesis Yer Seçimi Modelleri (Facility Location)

Tesis yer seçimi, bir işletmenin uzun vadeli stratejik kararlarından biridir. Bu modülde en yaygın iki yöntemi inceleyeceğiz.

## 1. Ağırlık Merkezi Yöntemi (Center of Gravity)
Mevcut talep noktalarının koordinatlarını ve talep miktarlarını kullanarak nakliye maliyetini minimize eden merkezi konumu bulur.

**Formüller:**
$$X^* = \frac{\sum (X_i \times W_i)}{\sum W_i}$$
$$Y^* = \frac{\sum (Y_i \times W_i)}{\sum W_i}$$
- $(X_i, Y_i)$: i. talep noktasının koordinatları.
- $W_i$: i. noktadaki talep miktarı (ağırlık).

```python
# Python implementation
coords = [(10, 20), (30, 40), (50, 60)] # (X, Y)
demands = [1000, 500, 1500]

sum_xw = sum(c[0] * d for c, d in zip(coords, demands))
sum_yw = sum(c[1] * d for c, d in zip(coords, demands))
total_w = sum(demands)

print(f"Optimal Koordinatlar: ({sum_xw/total_w:.2f}, {sum_yw/total_w:.2f})")
```

## 2. Analitik Hiyerarşi Süreci (AHP)
Çok kriterli karar verme yöntemidir. Tesis yer seçimi için hem nitel (yaşam kalitesi, altyapı) hem de nicel (maliyet) faktörleri karşılaştırır.

### AHP Adımları:
1. Problemin hiyerarşik yapısını kur.
2. İkili karşılaştırma matrislerini oluştur (1-9 skalası).
3. Özvektörleri hesaplayarak kriter ağırlıklarını bul.
4. Tutarlılık Oranı (CR) kontrolü yap (CR < 0.1 olmalı).

---
*Endüstri Mühendisliği Karar Destek Sistemi — Industrial-Engineering-Hub*
