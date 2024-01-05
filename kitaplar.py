import sqlite3 as sql 

con = sql.connect("kitaplar.db")
cur = con.cursor()

print("""
(0) Çıkmak İçin
(1) Kitap Eklemek İçin
(2) Kitap Silmek için
(3) Kitapların Hepsini Görmek İçin
""")

while True:

    sor = int(input("Yapmak İstediğiniz İşlemi Seçin: "))

    if sor==0:
        print("Çıkılıyor...")
        break

    elif sor==1:
        kitap_adi = input("Kitap Adı Girin: ")
        yazar_adi = input("Yazar Adı Girin: ")
        kitap_fiyati = int(input("Kitabın Fiyatını Girin: "))
        cur.execute("INSERT INTO kitaplar VALUES(?,?,?) ",(kitap_adi,yazar_adi,kitap_fiyati))

    elif sor==2:
        sil_kitap_adi = input("Silinecek Kitap Adı: ")
        cur.execute("DELETE FROM kitaplar WHERE KitapAdi=?", (sil_kitap_adi,))
        con.commit()
        print("Başarı İle Silindi")

    elif sor == 3:
        cur.execute("SELECT * FROM kitaplar")
        data = cur.fetchall()
        print(data)




con.commit()
con.close()