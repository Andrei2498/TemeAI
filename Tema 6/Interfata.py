# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Andrei\Desktop\InterfataAI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator

dictionar_of_lcd_values = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 706)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 561))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 91, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 310, 361, 241))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 30, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(210, 30, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 50, 91, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 201, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 160, 101, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 120, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 180, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 260, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 10, 381, 561))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 310, 361, 241))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 260, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lcd_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_1.setGeometry(QtCore.QRect(140, 190, 101, 16))
        self.lcd_1.setText("")
        self.lcd_1.setObjectName("lcd_1")
        self.lcd_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_3.setGeometry(QtCore.QRect(140, 30, 101, 16))
        self.lcd_3.setText("")
        self.lcd_3.setObjectName("lcd_3")
        self.lcd_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_6.setGeometry(QtCore.QRect(140, 110, 101, 16))
        self.lcd_6.setText("")
        self.lcd_6.setObjectName("lcd_6")
        self.lcd_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_2.setGeometry(QtCore.QRect(120, 120, 16, 70))
        self.lcd_2.setText("")
        self.lcd_2.setObjectName("lcd_2")
        self.lcd_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_4.setGeometry(QtCore.QRect(250, 120, 16, 70))
        self.lcd_4.setText("")
        self.lcd_4.setObjectName("lcd_4")
        self.lcd_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_5.setGeometry(QtCore.QRect(250, 40, 16, 70))
        self.lcd_5.setText("")
        self.lcd_5.setObjectName("lcd_5")
        self.lcd_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.lcd_7.setGeometry(QtCore.QRect(120, 40, 16, 70))
        self.lcd_7.setText("")
        self.lcd_7.setObjectName("lcd_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 600, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 600, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
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

        ## Restrict input to int only

        self.onlyInt = QIntValidator()
        self.lineEdit.setValidator(self.onlyInt)
        self.lineEdit_2.setValidator(self.onlyInt)
        self.lineEdit_3.setValidator(self.onlyInt)
        self.lineEdit_4.setValidator(self.onlyInt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Antrenare"))
        self.label.setText(_translate("MainWindow", "Numar de epoci"))
        self.label_2.setText(_translate("MainWindow", "Eroarea maxima"))
        self.label_3.setText(_translate("MainWindow", "Numar de neuroni in stratul ascuns"))
        self.label_4.setText(_translate("MainWindow", "Rata de invatare"))
        self.pushButton_3.setText(_translate("MainWindow", "Antreneaza"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Testare"))
        self.pushButton_4.setText(_translate("MainWindow", "Recunoaste"))
        self.pushButton.setText(_translate("MainWindow", "Despre"))
        self.pushButton_2.setText(_translate("MainWindow", "Iesire"))

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
