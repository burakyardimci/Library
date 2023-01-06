from library import *

print(""""***********************************************

Kütüphane programına hoşgeldiniz.

İşlemler:

1. Kitapları göster

2. Kitap sorgula

3. Kitap ekle

4. Kitap sil

5. Baskı yükselt

Çıkmak için 'q' ya basın

**************************************************""")

kütüphane = Kütüphane()

while True:
    islem = input("Yapacağınız İşlem:")
    if islem == "q":
        print("Program sonlandırılıyor...")
        print("Yine bekleriz...")
        break
    elif islem == "1":
        kütüphane.kitapları_goster()
    elif islem == "2":
        isim = input("Hangi kitabı istiyorsunuz?")
        print("Kitap sorgulanıyor...")
        time.sleep(1)
        kütüphane.kitap_sorgula(isim)
    elif islem == "3":
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayınevi = input("Yayınevi:")
        tür = input("Tür:")
        baskı = int(input("Baskı"))
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        print("Kitap ekleniyor...")
        kütüphane.kitap_ekle(yeni_kitap)
        time.sleep(1)
        print("Ekleme başarılı...")
    elif islem == "4":
        isim = input("Hangi kitabı silmek istiyorsunuz?")
        time.sleep(1)
        kütüphane.kitap_sil(isim)
        print("Kitap silme başarılı...")

    elif islem == "5":
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz?")
        kütüphane.baskı_yükselt(isim)
        time.sleep(1)
        print("Baskı yükseltme başarılı...")
    else:
        print("Geçersiz işlem...")
