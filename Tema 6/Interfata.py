import sys
import rn
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIntValidator

dictionar_of_lcd_values = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 706)
        MainWindow.setMaximumSize(821, 706)
        MainWindow.setMinimumSize(821, 706)
        MainWindow.move(1100, 0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 561))
        self.groupBox.setObjectName("groupBox")
        self.numar_epoci = QtWidgets.QLineEdit(self.groupBox)
        self.numar_epoci.setGeometry(QtCore.QRect(50, 50, 91, 22))
        self.numar_epoci.setObjectName("lineEdit")
        self.rn_screen = QtWidgets.QTextBrowser(self.groupBox)
        self.rn_screen.setGeometry(QtCore.QRect(10, 310, 361, 241))
        self.rn_screen.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 30, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(210, 30, 101, 16))
        self.label_2.setObjectName("label_2")
        self.eroarea_maxima = QtWidgets.QLineEdit(self.groupBox)
        self.eroarea_maxima.setGeometry(QtCore.QRect(210, 50, 91, 22))
        self.eroarea_maxima.setObjectName("eroarea_maxima")
        self.neurons = QtWidgets.QLabel(self.groupBox)
        self.neurons.setGeometry(QtCore.QRect(50, 100, 201, 16))
        self.neurons.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 160, 101, 16))
        self.label_4.setObjectName("label_4")
        self.numar_neuroni = QtWidgets.QLineEdit(self.groupBox)
        self.numar_neuroni.setGeometry(QtCore.QRect(50, 120, 113, 22))
        self.numar_neuroni.setObjectName("numar_neuroni")
        self.rata_de_invatare = QtWidgets.QLineEdit(self.groupBox)
        self.rata_de_invatare.setGeometry(QtCore.QRect(50, 180, 113, 22))
        self.rata_de_invatare.setObjectName("rata_de_invatare")
        self.antreneaza = QtWidgets.QPushButton(self.groupBox)
        self.antreneaza.setGeometry(QtCore.QRect(130, 260, 111, 41))
        self.antreneaza.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 10, 381, 561))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 310, 361, 241))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.recunoaste = QtWidgets.QPushButton(self.groupBox_2)
        self.recunoaste.setGeometry(QtCore.QRect(130, 260, 111, 41))
        self.recunoaste.setObjectName("pushButton_4")
        self.lcd_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_7.setGeometry(QtCore.QRect(140, 190, 101, 16))
        self.lcd_7.setText("")
        self.lcd_7.setObjectName("lcd_7")
        self.lcd_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_1.setGeometry(QtCore.QRect(140, 30, 101, 16))
        self.lcd_1.setText("")
        self.lcd_1.setObjectName("lcd_1")
        self.lcd_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_4.setGeometry(QtCore.QRect(140, 110, 101, 16))
        self.lcd_4.setText("")
        self.lcd_4.setObjectName("lcd_4")
        self.lcd_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_5.setGeometry(QtCore.QRect(120, 120, 16, 70))
        self.lcd_5.setText("")
        self.lcd_5.setObjectName("lcd_5")
        self.lcd_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_6.setGeometry(QtCore.QRect(250, 120, 16, 70))
        self.lcd_6.setText("")
        self.lcd_6.setObjectName("lcd_6")
        self.lcd_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_3.setGeometry(QtCore.QRect(250, 40, 16, 70))
        self.lcd_3.setText("")
        self.lcd_3.setObjectName("lcd_3")
        self.lcd_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_2.setGeometry(QtCore.QRect(120, 40, 16, 70))
        self.lcd_2.setText("")
        self.lcd_2.setObjectName("lcd_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 600, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.close_app = QtWidgets.QPushButton(self.centralwidget)
        self.close_app.setGeometry(QtCore.QRect(550, 600, 111, 41))
        self.close_app.setObjectName("close_app")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## On click action

        self.lcd_1.clicked.connect(self.lcd_number_1)
        self.lcd_2.clicked.connect(self.lcd_number_2)
        self.lcd_3.clicked.connect(self.lcd_number_3)
        self.lcd_4.clicked.connect(self.lcd_number_4)
        self.lcd_5.clicked.connect(self.lcd_number_5)
        self.lcd_6.clicked.connect(self.lcd_number_6)
        self.lcd_7.clicked.connect(self.lcd_number_7)
        self.close_app.clicked.connect(self.quit_app)

        ## Restrict input to int only

        self.onlyInt = QIntValidator()
        self.numar_epoci.setValidator(self.onlyInt)
        self.eroarea_maxima.setValidator(self.onlyInt)
        self.numar_neuroni.setValidator(self.onlyInt)
        self.rata_de_invatare.setValidator(self.onlyInt)
        self.recunoaste.clicked.connect(self.recunoaste_cifra)

        self.antreneaza.clicked.connect(self.antreneaza_metoda)

        self.numar_neuroni.setText("10")
        self.eroarea_maxima.setText("0.001")
        self.numar_epoci.setText("1000")
        self.rata_de_invatare.setText("0.5")

    def antreneaza_metoda(self):
        res = rn.antreneaza_reteaua(int(self.numar_neuroni.text()), float(self.rata_de_invatare.text()),
                              float(self.eroarea_maxima.text()), int(self.numar_epoci.text()))
        output = ''
        output += 'MSE= ' + res[1].__str__() + '\n\n'
        for i in res[0]:
            for j in i:
                output += round(j, 2).__str__() + ' '
            output += '\n'
        self.rn_screen.setText(output)
        print(res[0])

    def quit_app(self):
        sys.exit()

    def recunoaste_cifra(self):
        rn.recunoastere_numar(list(dictionar_of_lcd_values.values()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Antrenare"))
        self.label.setText(_translate("MainWindow", "Numar de epoci"))
        self.label_2.setText(_translate("MainWindow", "Eroarea maxima"))
        self.neurons.setText(_translate("MainWindow", "Numar de neuroni in stratul ascuns"))
        self.label_4.setText(_translate("MainWindow", "Rata de invatare"))
        self.antreneaza.setText(_translate("MainWindow", "Antreneaza"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Testare"))
        self.recunoaste.setText(_translate("MainWindow", "Recunoaste"))
        self.pushButton.setText(_translate("MainWindow", "Despre"))
        self.close_app.setText(_translate("MainWindow", "Iesire"))

    def lcd_number_1(self):
        if dictionar_of_lcd_values.get(1) == 0:
            self.lcd_1.setStyleSheet("background-color: red")
            dictionar_of_lcd_values.update({1: 1})
        else:
            self.lcd_1.setStyleSheet("")
            dictionar_of_lcd_values.update({1: 0})

    def lcd_number_2(self):
        if dictionar_of_lcd_values.get(2) == 0:
            self.lcd_2.setStyleSheet("background-color: red")
            dictionar_of_lcd_values.update({2: 1})
        else:
            self.lcd_2.setStyleSheet("")
            dictionar_of_lcd_values.update({2: 0})

    def lcd_number_3(self):
        if dictionar_of_lcd_values.get(3) == 0:
            self.lcd_3.setStyleSheet("background-color: red")
            dictionar_of_lcd_values.update({3: 1})
        else:
            self.lcd_3.setStyleSheet("")
            dictionar_of_lcd_values.update({3: 0})

    def lcd_number_4(self):
        if dictionar_of_lcd_values.get(4) == 0:
            self.lcd_4.setStyleSheet("background-color: red")
            dictionar_of_lcd_values.update({4: 1})
        else:
            self.lcd_4.setStyleSheet("")
            dictionar_of_lcd_values.update({4: 0})

    def lcd_number_5(self):
        if dictionar_of_lcd_values.get(5) == 0:
            self.lcd_5.setStyleSheet("background-color: red")
            dictionar_of_lcd_values.update({5: 1})
        else:
            self.lcd_5.setStyleSheet("")
            dictionar_of_lcd_values.update({5: 0})

    def lcd_number_6(self):
        if dictionar_of_lcd_values.get(6) == 0:
            self.lcd_6.setStyleSheet("background-color: red")
            dictionar_of_lcd_values.update({6: 1})
        else:
            self.lcd_6.setStyleSheet("")
            dictionar_of_lcd_values.update({6: 0})

    def lcd_number_7(self):
        if dictionar_of_lcd_values.get(7) == 0:
            self.lcd_7.setStyleSheet("background-color: red")
            dictionar_of_lcd_values.update({7: 1})
        else:
            self.lcd_7.setStyleSheet("")
            dictionar_of_lcd_values.update({7: 0})


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    mainWin = Ui_MainWindow()
    mainWin.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
