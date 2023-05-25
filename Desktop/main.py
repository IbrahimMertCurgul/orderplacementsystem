import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from MainWindow import Ui_MainWindow
import mysql.connector as mscon

connection = mscon.connect(user='root', password='12345678',host='localhost',database='siparisvt')

cursor = connection.cursor()

class Program(QtWidgets.QMainWindow): 
    def __init__(self):
        super(Program,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionKapat.triggered.connect(sys.exit)

    #############################  BUTONLAR  #########################################################    
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        self.ui.btn_tumkayitlar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_arama.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.btn_siparisgor.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.btn_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_menu2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_menu3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))   
        self.ui.btn_sorgula.clicked.connect(self.sorgula)
        self.ui.btn_sorgulasiparis.clicked.connect(self.siparisara)
        self.ui.btn_sorgulaisletme.clicked.connect(self.musteriara)
        self.ui.btn_sorgulatel.clicked.connect(self.telefonara)
        self.ui.btn_sorgulamail.clicked.connect(self.mailara)
        self.ui.btn_sorgulatarih.clicked.connect(self.tarihara)
        self.ui.btn_gor.clicked.connect(self.siparisgor)
    ###############################################################################################

    ############################# TÜM SİPARİŞLERİ LİSTELE #########################################
    def sorgula(self):
        cursor.execute("SELECT * FROM siparistablosu")
        satir = 0
        for (tarih, siparisno, isletmeismi, telefon, email, siparis) in cursor:
            self.ui.table_sorgu.setItem(int(satir) , 0 , QTableWidgetItem(str(tarih)))
            self.ui.table_sorgu.setItem(int(satir) , 1 , QTableWidgetItem(str(siparisno)))
            self.ui.table_sorgu.setItem(int(satir) , 2 , QTableWidgetItem(str(isletmeismi)))
            self.ui.table_sorgu.setItem(int(satir) , 3 , QTableWidgetItem(str(telefon)))
            self.ui.table_sorgu.setItem(int(satir) , 4 , QTableWidgetItem(str(email)))
            self.ui.table_sorgu.setItem(int(satir) , 5 , QTableWidgetItem(str(siparis)))
            satir+=1
        self.ui.table_sorgu.setRowCount(satir)
    ###############################################################################################
        
    ############################# SİPARİŞ ARAMA KUTUSU ############################################      
    def siparisara(self):
        arama = self.ui.line_siparis.text()
        cursor.execute(f"SELECT * FROM siparistablosu WHERE siparisno = '{arama}'")
        satir = 0
        for (tarih, siparisno, isletmeismi, telefon, email, siparis) in cursor:
            self.ui.table_arama.setItem(int(satir) , 0 , QTableWidgetItem(str(tarih)))
            self.ui.table_arama.setItem(int(satir) , 1 , QTableWidgetItem(str(siparisno)))
            self.ui.table_arama.setItem(int(satir) , 2 , QTableWidgetItem(str(isletmeismi)))
            self.ui.table_arama.setItem(int(satir) , 3 , QTableWidgetItem(str(telefon)))
            self.ui.table_arama.setItem(int(satir) , 4 , QTableWidgetItem(str(email)))
            self.ui.table_arama.setItem(int(satir) , 5 , QTableWidgetItem(str(siparis)))
            satir+=1
        self.ui.table_arama.setRowCount(satir)
    ##############################################################################################

    ############################# İŞLETME ARAMA KUTUSU ###########################################       
    def musteriara(self):
        arama = self.ui.line_musterismi.text()
        cursor.execute(f"SELECT * FROM siparistablosu WHERE isletmeismi = '{arama}'")
        satir = 0
        for (tarih, siparisno, isletmeismi, telefon, email, siparis) in cursor:
            self.ui.table_arama.setItem(int(satir) , 0 , QTableWidgetItem(str(tarih)))
            self.ui.table_arama.setItem(int(satir) , 1 , QTableWidgetItem(str(siparisno)))
            self.ui.table_arama.setItem(int(satir) , 2 , QTableWidgetItem(str(isletmeismi)))
            self.ui.table_arama.setItem(int(satir) , 3 , QTableWidgetItem(str(telefon)))
            self.ui.table_arama.setItem(int(satir) , 4 , QTableWidgetItem(str(email)))
            self.ui.table_arama.setItem(int(satir) , 5 , QTableWidgetItem(str(siparis)))
            satir+=1
        self.ui.table_arama.setRowCount(satir)
    ##############################################################################################

    ############################# TELEFON ARAMA KUTUSU ###########################################       
    def telefonara(self):
        arama = self.ui.line_tel.text()
        cursor.execute(f"SELECT * FROM siparistablosu WHERE telefon = '{arama}'")
        satir = 0
        for (tarih, siparisno, isletmeismi, telefon, email, siparis) in cursor:
            self.ui.table_arama.setItem(int(satir) , 0 , QTableWidgetItem(str(tarih)))
            self.ui.table_arama.setItem(int(satir) , 1 , QTableWidgetItem(str(siparisno)))
            self.ui.table_arama.setItem(int(satir) , 2 , QTableWidgetItem(str(isletmeismi)))
            self.ui.table_arama.setItem(int(satir) , 3 , QTableWidgetItem(str(telefon)))
            self.ui.table_arama.setItem(int(satir) , 4 , QTableWidgetItem(str(email)))
            self.ui.table_arama.setItem(int(satir) , 5 , QTableWidgetItem(str(siparis)))
            satir+=1
        self.ui.table_arama.setRowCount(satir)
    ############################################################################################

    ############################# MAİL ARAMA KUTUSU ############################################      
    def mailara(self):
        arama = self.ui.line_mail.text()
        cursor.execute(f"SELECT * FROM siparistablosu WHERE email = '{arama}'")
        satir = 0
        for (tarih, siparisno, isletmeismi, telefon, email, siparis) in cursor:
            self.ui.table_arama.setItem(int(satir) , 0 , QTableWidgetItem(str(tarih)))
            self.ui.table_arama.setItem(int(satir) , 1 , QTableWidgetItem(str(siparisno)))
            self.ui.table_arama.setItem(int(satir) , 2 , QTableWidgetItem(str(isletmeismi)))
            self.ui.table_arama.setItem(int(satir) , 3 , QTableWidgetItem(str(telefon)))
            self.ui.table_arama.setItem(int(satir) , 4 , QTableWidgetItem(str(email)))
            self.ui.table_arama.setItem(int(satir) , 5 , QTableWidgetItem(str(siparis)))
            satir+=1
        self.ui.table_arama.setRowCount(satir)
    ############################################################################################
    ############################# TARİH ARAMA KUTUSU ############################################      
    def tarihara(self):
        arama = self.ui.line_tarih.text()
        cursor.execute(f"SELECT * FROM siparistablosu WHERE tarih = '{arama}'")
        satir = 0
        for (tarih, siparisno, isletmeismi, telefon, email, siparis) in cursor:
            self.ui.table_arama.setItem(int(satir) , 0 , QTableWidgetItem(str(tarih)))
            self.ui.table_arama.setItem(int(satir) , 1 , QTableWidgetItem(str(siparisno)))
            self.ui.table_arama.setItem(int(satir) , 2 , QTableWidgetItem(str(isletmeismi)))
            self.ui.table_arama.setItem(int(satir) , 3 , QTableWidgetItem(str(telefon)))
            self.ui.table_arama.setItem(int(satir) , 4 , QTableWidgetItem(str(email)))
            self.ui.table_arama.setItem(int(satir) , 5 , QTableWidgetItem(str(siparis)))
            satir+=1
        self.ui.table_arama.setRowCount(satir)
    #############################################################################################
    
    ############################# SİPARİŞ ARAMA KUTUSU ############################################      
    def siparisgor(self):
        arama = self.ui.line_siparisgor.text()
        cursor.execute(f"SELECT * FROM siparistablosu WHERE siparisno = '{arama}'")

        for (tarih, siparisno, isletmeismi, telefon, email, siparis) in cursor:
            self.ui.textEdit_siparis.setText(f"{isletmeismi} firmasına ait {siparisno} numaralı sipariş:\n\n{siparis}\n\n{tarih}\n{telefon}\n{email}")
    ##############################################################################################


def application():
    app = QtWidgets.QApplication(sys.argv)
    win = Program()
    win.show()
    sys.exit(app.exec_())

application()