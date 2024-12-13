# K-t-phane_proje_python

2. Kutuphane Sınıfı
Amacı: Kütüphaneyi yönetir ve kitaplarla ilgili işlemleri gerçekleştirir.

Özellikleri:
kitaplar: Kütüphanedeki kitapları tutan liste.
odunc_alinan_kitaplar: Ödünç alınan kitapların listesini tutar.


Metotlar:
kitap_ekle(self, kitap_adi, yazar_adi)
Yeni bir kitap nesnesi oluşturur ve kitaplar listesine ekler.

kitaplari_listele(self)
Kütüphanedeki kitapları listeler. Eğer kütüphane boşsa, uyarı mesajı gösterir.

odunc_ver(self, kitap_adi)
Belirtilen kitabı ödünç verir. Kitap zaten ödünç alınmışsa ya da kütüphanede yoksa uygun mesaj döner.

geri_al(self, kitap_adi)
Belirtilen kitabı ödünç alınanlar listesinden çıkarır ve durumunu günceller.

odunc_alinanlari_listele(self)
Ödünç alınmış kitapları listeler. Hiç ödünç alınan kitap yoksa uygun mesaj gösterir.
