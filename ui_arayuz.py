# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 525)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 525))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 525))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resimler/icons/iconx.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1061, 750))
        self.frame.setMinimumSize(QtCore.QSize(1000, 750))
        self.frame.setMaximumSize(QtCore.QSize(5000, 3000))
        self.frame.setStyleSheet("QFrame{\n"
"background: #354152;\n"
"}\n"
"\n"
"QLineEdit{\n"
" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    min-width: 6em;\n"
"    font-size:20px;\n"
"    padding-left:15px;\n"
"    height:42px;\n"
"    border-radius:15px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    background: transparent;\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius: 15px;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
"padding: 8px 16px;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: black;\n"
"background: #008bd1\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(460, 10, 531, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 501, 391))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 531, 421))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(270, 190, 191, 221))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/resimler/icons/2613204-200.png"))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 390, 441, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_dosya_sec = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_dosya_sec.setStyleSheet("")
        self.btn_dosya_sec.setObjectName("btn_dosya_sec")
        self.horizontalLayout.addWidget(self.btn_dosya_sec)
        self.btn_pdf_analiz_yap = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_pdf_analiz_yap.setEnabled(False)
        self.btn_pdf_analiz_yap.setStyleSheet("")
        self.btn_pdf_analiz_yap.setObjectName("btn_pdf_analiz_yap")
        self.horizontalLayout.addWidget(self.btn_pdf_analiz_yap)
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 431, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.txt_no_baslangic = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_no_baslangic.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_no_baslangic.setObjectName("txt_no_baslangic")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.txt_no_baslangic)
        self.txt_no_referans = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_no_referans.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_no_referans.setObjectName("txt_no_referans")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_no_referans)
        self.txt_no_tablolar = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_no_tablolar.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_no_tablolar.setObjectName("txt_no_tablolar")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.txt_no_tablolar)
        self.txt_no_denklemler = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_no_denklemler.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_no_denklemler.setObjectName("txt_no_denklemler")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_no_denklemler)
        self.txt_no_giris = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_no_giris.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_no_giris.setObjectName("txt_no_giris")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.txt_no_giris)
        self.txt_no_cizelge = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_no_cizelge.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_no_cizelge.setObjectName("txt_no_cizelge")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_no_cizelge)
        self.txt_no_sekiller = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_no_sekiller.setEnabled(True)
        self.txt_no_sekiller.setObjectName("txt_no_sekiller")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.txt_no_sekiller)
        self.txt_no_baslik = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_no_baslik.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_no_baslik.setObjectName("txt_no_baslik")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_no_baslik)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 260, 431, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_no_icindekiler = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_no_icindekiler.setObjectName("txt_no_icindekiler")
        self.verticalLayout.addWidget(self.txt_no_icindekiler)
        self.txt_dosya_yolu = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_dosya_yolu.setObjectName("txt_dosya_yolu")
        self.verticalLayout.addWidget(self.txt_dosya_yolu)
        self.label.raise_()
        self.tabWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.formLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.menuMen = QtWidgets.QMenu(self.menubar)
        self.menuMen.setObjectName("menuMen")
        self.menuHakkinda = QtWidgets.QMenu(self.menubar)
        self.menuHakkinda.setObjectName("menuHakkinda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_gelistiriciler = QtWidgets.QAction(MainWindow)
        self.action_gelistiriciler.setObjectName("action_gelistiriciler")
        self.action_dosya_sec = QtWidgets.QAction(MainWindow)
        self.action_dosya_sec.setObjectName("action_dosya_sec")
        self.menuMen.addAction(self.action_dosya_sec)
        self.menuHakkinda.addAction(self.action_gelistiriciler)
        self.menubar.addAction(self.menuMen.menuAction())
        self.menubar.addAction(self.menuHakkinda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tez Analiz Programı"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "\n"
"\n"
"Tez Analiz Programına Hoşgeldiniz!!!\n"
"\n"
"Program Kullanma Kılavuzu\n"
"\n"
"Sizden istenilen sayfa numaraları pdf sayfa numarasına eş değerdir.\n"
"\n"
"Dökümanın içindekiler kısmının sayfa numaraları burada kullanılamaz."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Kılavuz"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Analiz"))
        self.btn_dosya_sec.setText(_translate("MainWindow", "Dosya Seç"))
        self.btn_pdf_analiz_yap.setText(_translate("MainWindow", "Analizi Başlat"))
        self.txt_no_baslangic.setPlaceholderText(_translate("MainWindow", "Başlangıç Sayfa No"))
        self.txt_no_referans.setPlaceholderText(_translate("MainWindow", "Referanslar Sayfa No"))
        self.txt_no_tablolar.setPlaceholderText(_translate("MainWindow", "Tablolar Sayfa No"))
        self.txt_no_denklemler.setPlaceholderText(_translate("MainWindow", "Denklemler Sayfa No"))
        self.txt_no_giris.setPlaceholderText(_translate("MainWindow", "Giriş Sayfa No"))
        self.txt_no_cizelge.setPlaceholderText(_translate("MainWindow", "Çizelgeler Sayfa No"))
        self.txt_no_sekiller.setPlaceholderText(_translate("MainWindow", "Şekiller Sayfa No"))
        self.txt_no_baslik.setPlaceholderText(_translate("MainWindow", "Başlık Sayfa No"))
        self.txt_no_icindekiler.setPlaceholderText(_translate("MainWindow", "İçindekiler Sayfa No"))
        self.txt_dosya_yolu.setPlaceholderText(_translate("MainWindow", "Dosya Seçili Değil"))
        self.menuMen.setTitle(_translate("MainWindow", "Menü"))
        self.menuHakkinda.setTitle(_translate("MainWindow", "Hakkında"))
        self.action_gelistiriciler.setText(_translate("MainWindow", "Geliştiriciler"))
        self.action_dosya_sec.setText(_translate("MainWindow", "Dosya Seç"))
import resource_rc