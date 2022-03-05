
from ornek import *

print("""***********************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil 

5. Baskı Yükselt

Çıkmak için 'q' ya basın.
***********************************""")

kütüphane = Kütüphane()

while True:
    işlem = input("Yapacağınız İşlem:")

    if (işlem == "q"):
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    elif(işlem == "1"):
        kütüphane.kitaplarıgoster()
    elif(işlem == "2"):
        isim = input("Hangi kitabı sorguluyorsunuz? ")
        print("Sorgu yapılıyor...")
        time.sleep(2)
        kütüphane.kitapsorgula(isim)
    elif(işlem == "3"):
        isim = input("Kitap :")
        yazar = input("Yazar :")
        tür = input("Tür :")
        yayınevi = input("Yayınevvi :")
        baskı_tarih = int(input("Baskı Tarihi :"))

        yeni_kitap = Kitap(isim,yazar,tür,yayınevi,baskı_tarih)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kütüphane.kitapekle(yeni_kitap)
        print("Kitap eklendi...")

    elif(işlem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz?")
        cevap = input("Emin misiniz? (E/H)")

        if(cevap == "E"):
            print("Kitap siliniyor..")
            time.sleep(2)
            kütüphane.kitapsil(isim)
            print("Kitap silindi!")
    elif(işlem == "5"):
        isim = input("Hangi kitabı yükseltmek istiyorsunuz?")
        print("Baskı yükseltiliyor..")
        time.sleep(2)
        kütüphane.baskıyukselt(isim)
        print("Baskı yükseltildi!")

    else:
        print("Geçersiz işlem...")



