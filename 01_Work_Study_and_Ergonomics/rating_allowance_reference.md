# ⏱️ Performans Derecelendirme ve Tolerans Rehberi

İş etüdünde gözlemlenen sürelerin standart süreye dönüştürülmesi için kullanılan kritik tabloları içerir.

## 1. Westinghouse Performans Derecelendirme Sistemi
Operatörün performansını dört ana faktör üzerinden değerlendirir:
1. **Beceri (Skill):** İşi yapma ustalığı.
2. **Çaba (Effort):** İş başındaki isteklilik.
3. **Koşullar (Conditions):** Çalışma ortamının durumu.
4. **Tutarlılık (Consistency):** Döngü süreleri arasındaki fark.

### Puanlama Mantığı:
Puanlar toplanır ve 1.00 (Normal) değerine eklenir/çıkarılır.
- Örnek: Beceri (B1: +0.11), Çaba (A2: +0.12), Koşullar (E: -0.03), Tutarlılık (F: -0.02)
- Toplam Katsayı: $1 + 0.11 + 0.12 - 0.03 - 0.02 = 1.18$

## 2. Standart Tolerans (Allowance) Değerleri
Normal zamana eklenen ek sürelerdir:
- **Kişisel Gereksinimler:** %5 (Sabit)
- **Temel Yorgunluk:** %4 (Sabit)
- **Duruş Toleransı:** Oturma (%0), Eğilme (%2), Ayakta Durma (%2)
- **Çevresel Koşullar:** Gürültü (%0-5), Sıcaklık (%0-10), Işık (%0-5)

### ILO Standartları (Yaklaşık Değerler):
| Kategori | Tolerans (%) |
|---|---|
| Hafif İş (Oturarak) | %11 |
| Orta İş (Ayakta) | %15 |
| Ağır İş | %20+ |

---
*Endüstri Mühendisliği Karar Destek Sistemi — Industrial-Engineering-Hub*
