import sys
import sqlite3
import time

from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):


    def __init__(self):

        super().__init__()

        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):

        baglanti = sqlite3.connect("kendim.sqlite")

        self.cursor = baglanti.cursor()

        self.cursor.execute("CREATE TABLE  IF NOT EXISTS kitaplar (adi,yazari,yayinevi,adedi,fiyati )")

        baglanti.commit()
    def init_ui(self):

        self.kitap_adi = QtWidgets.QLineEdit()
        self.kitap_yazari = QtWidgets.QLineEdit()
        self.kitap_yayinevi = QtWidgets.QLineEdit()
        self.kitap_adeti = QtWidgets.QLineEdit()
        self.kitap_fiyati = QtWidgets.QLineEdit()

        self.giris = QtWidgets.QPushButton("kayıt et")#parantez içinde butona
        #isim veriyorsun
        self.temizle = QtWidgets.QPushButton("Temizle")

        self.yazi_alani = QtWidgets.QLabel("")
        self.baslik = QtWidgets.QLabel("ASEL KİTAPÇILIK")
        self.adii = QtWidgets.QLabel("Kitap Adı")
        self.yazar = QtWidgets.QLabel("Kitap Yazarı")
        self.yayin = QtWidgets.QLabel("Kitap Yayınevi")
        self.aded = QtWidgets.QLabel("Kitap Adedi")
        self.fiyat = QtWidgets.QLabel("Kitap Fiyatı")


        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.baslik)
        v_box.addWidget(self.adii)
        v_box.addWidget(self.kitap_adi)
        v_box.addWidget(self.yazar)
        v_box.addWidget(self.kitap_yazari)
        v_box.addWidget(self.yayin)
        v_box.addWidget(self.kitap_yayinevi)
        v_box.addWidget(self.aded)
        v_box.addWidget(self.kitap_adeti)
        v_box.addWidget(self.fiyat)
        v_box.addWidget(self.kitap_fiyati)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()#arada boşluk bırakmak için
        v_box.addWidget(self.giris)
        v_box.addWidget(self.temizle)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.setWindowTitle("kitap_kayit")

        self.giris.clicked.connect(self.login)
        self.temizle.clicked.connect(self.temiz)

        self.show()

    def login(self):
        baglanti = sqlite3.connect("kendim.sqlite")
        self.cursor = baglanti.cursor()

        isim = self.kitap_adi.text()
        yazar = self.kitap_yazari.text()
        yayinevi = self.kitap_yayinevi.text()
        adedi = self.kitap_adeti.text()
        fiyati = self.kitap_fiyati.text()

        self.cursor.execute("INSERT INTO kitaplar (adi,yazari,yayinevi,adedi,fiyati) VALUES ('"+isim+"','"+yazar+"','"+yayinevi+"','"+adedi+"','"+fiyati+"')")
        baglanti.commit()
        self.yazi_alani.setText("başayıla kaydedildi")

    def temiz(self):
        baglanti = sqlite3.connect("kendim.sqlite")
        self.cursor = baglanti.cursor()

        self.yazi_alani.clear()
        self.kitap_adi.clear()
        self.kitap_yazari.clear()
        self.kitap_yayinevi.clear()
        self.kitap_adeti.clear()
        self.kitap_fiyati.clear()

        baglanti.commit()

app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())