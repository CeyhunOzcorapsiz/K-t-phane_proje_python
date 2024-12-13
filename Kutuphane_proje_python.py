class Kitap:
    def __init__(self, kitap_adi, yazar_adi):
        self.kitap_adi = kitap_adi
        self.yazar_adi = yazar_adi
        self.odunc_alindi = False

    def __str__(self):
        return f"{self.kitap_adi} - {self.yazar_adi} (Ödünç Alındı: {'Evet' if self.odunc_alindi else 'Hayır'})"

class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.odunc_alinan_kitaplar = []

    def kitap_ekle(self, kitap_adi, yazar_adi):
        yeni_kitap = Kitap(kitap_adi, yazar_adi)
        self.kitaplar.append(yeni_kitap)
        print(f"'{kitap_adi}' kütüphaneye eklendi.")

    def kitaplari_listele(self):
        if not self.kitaplar:
            print("Kütüphane boş.")
        else:
            print("\nKütüphane:\n")
            for kitap in self.kitaplar:
                print(kitap)

    def odunc_ver(self, kitap_adi):
        for kitap in self.kitaplar:
            if kitap.kitap_adi == kitap_adi:
                if kitap.odunc_alindi:
                    print(f"'{kitap_adi}' zaten ödünç alındı.")
                else:
                    kitap.odunc_alindi = True
                    self.odunc_alinan_kitaplar.append(kitap)
                    print(f"'{kitap_adi}' ödünç verildi.")
                return
        print(f"'{kitap_adi}' kütüphanede bulunamadı.")

    def geri_al(self, kitap_adi):
        for kitap in self.odunc_alinan_kitaplar:
            if kitap.kitap_adi == kitap_adi:
                kitap.odunc_alindi = False
                self.odunc_alinan_kitaplar.remove(kitap)
                print(f"'{kitap_adi}' geri alındı.")
                return
        print(f"'{kitap_adi}' ödünç alınan kitaplar listesinde bulunamadı.")

    def odunc_alinanlari_listele(self):
        if not self.odunc_alinan_kitaplar:
            print("Ödünç alınan kitap yok.")
        else:
            print("\nÖdünç Alınan Kitaplar:\n")
            for kitap in self.odunc_alinan_kitaplar:
                print(kitap)

kutuphane = Kutuphane()

kutuphane.kitap_ekle("Simyacı", "Paulo Coelho")
kutuphane.kitap_ekle("1984", "George Orwell")
kutuphane.kitap_ekle("Bir Ömür Nasıl Yaşanır?", "İlber Ortaylı")

kutuphane.kitaplari_listele()

kutuphane.odunc_ver("1984")
kutuphane.odunc_ver("Simyacı")


kutuphane.odunc_alinanlari_listele()


kutuphane.geri_al("1984")


kutuphane.kitaplari_listele()
kutuphane.odunc_alinanlari_listele()