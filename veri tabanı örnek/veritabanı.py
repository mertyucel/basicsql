import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

def tablo_oluştur():
    cursor.execute('''CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)''') # Sorguyu çalıştırıyoruz.
    con.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.

def veri_ekle():
    cursor.execute('INSERT INTO kitaplık VALUES ("Istanbul Hatırası","Ahmet Ümit","Everest Yayıncılık",561)')
    con.commit()

def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute('INSERT INTO kitaplık VALUES(?,?,?,?)',(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

def verileri_al():
    cursor.execute('SELECT * FROM kitaplık')
    liste = cursor.fetchall()
    print("Liste yazdırılıyor...")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute('SELECT İsim,Yazar FROM kitaplık')
    liste = cursor.fetchall()
    print("Liste yazdırılıyor...")
    for i in liste:
        print(i)


def verileri_al3(yayınevi):
    cursor.execute('Select * From kitaplık where Yayınevi = ?',(yayınevi,)) # Sadece yayınevi ,Everest olan kitapları alıyoruz.
    liste = cursor.fetchall()
    print("Liste yazdırılıyor...")
    for i in liste:
        print(i)

def verileri_guncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute('UPDATE kitaplık set Yayınevi = ? where Yayınevi = ?',(yeni_yayınevi,eski_yayınevi,)) 
    con.commit()

def verileri_sil(yazar):
    cursor.execute('DELETE from  kitaplık  where Yazar = ?',(yazar,)) 
    con.commit()


verileri_sil("Hayaller")
verileri_al()
#verileri_guncelle("Everest Yayıncılık","Everest")


# verileri_al3("USA")



#verileri_al2()
#verileri_al()

# isim = input("İsim : ")
# yazar = input("Yazar : ")
# yayınevi = input("Yayınevi : ")
# sayfa_sayısı = int(input("Sayfa Sayısı : "))

#veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı)
#tablo_oluştur()





con.close() # Bağlantıyı koparıyoruz.