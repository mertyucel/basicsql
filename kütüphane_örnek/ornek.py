import sqlite3
import time

class Kitap():
    def __init__(self,isim,yazar,tür,yayınevi,baskı_tarih) -> None:
       
        self.isim = isim
        self.yazar = yazar
        self.tür = tür
        self.yayınevi = yayınevi
        self.baskı_tarih = baskı_tarih

    def __str__(self) -> str:
        return "Kitap ismi : {} \n Yazar ismi : {} \n Tür ismi : {} \n Yayınevi İsmi : {} \n Baskı tarihi : {}".format(self.isim,self.yazar,self.tür,self.yayınevi,self.baskı_tarih)


class Kütüphane():

    def __init__(self) -> None:
        self.baglantı_olustur()

    def baglantı_olustur(self):
        self.baglantı = sqlite3.connect("kütüphane.db")
        self.cursor = self.baglantı.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"

        self.cursor.execute(sorgu)

        self.baglantı.commit()

    def baglantıyı_kes(self):
        self.baglantı.close()

    def kitaplarıgoster(self):
        sorgu = "SELECT * FROM kitaplar"
        self.cursor.execute(sorgu)

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Herhangi bir kitap bulunmuyor...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitapsorgula(self,isim):

        sorgu = "Select * from kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Herhangi bir kitap bulunmuyor..")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)

    def kitapekle(self,kitap):
        sorgu = "Insert into kitaplar VALUES (?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.tür,kitap.yayınevi,kitap.baskı_tarih))
        self.baglantı.commit()

    def kitapsil(self,isim):
        sorgu = "Delete from kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglantı.commit()

    def baskıyukselt(self,isim):
        sorgu = "select * from kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("böyle bir kitap bulunmuyor")
        else:
            baskı = kitaplar[0][4]
            baskı += 1

            sorgu2 = "Update kitaplar set baskı = ? where isim = ?"
            self.cursor.execute(sorgu2,(baskı,isim))

            self.baglantı.commit()
