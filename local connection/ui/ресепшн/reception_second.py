# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reception_second.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ReceptionSecondBtnService(object):
    def setupUi(self, Second_Page_Window):
        Second_Page_Window.setObjectName("Second_Page_Window")
        Second_Page_Window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Second_Page_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 210, 740, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 120, 740, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 740, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 300, 740, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 390, 740, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(310, 480, 180, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        Second_Page_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Second_Page_Window)
        self.statusbar.setObjectName("statusbar")
        Second_Page_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Second_Page_Window)
        QtCore.QMetaObject.connectSlotsByName(Second_Page_Window)

    def retranslateUi(self, Second_Page_Window):
        _translate = QtCore.QCoreApplication.translate
        Second_Page_Window.setWindowTitle(_translate("Second_Page_Window", "Second_Page_Window"))
        self.pushButton_3.setText(_translate("Second_Page_Window", "Квота,мүгедек және Жастар Практикасы,Тұрақты жұмыс орындары"))
        self.pushButton_2.setText(_translate("Second_Page_Window", "Көші-қон, ақылы қоғамдық жұмыс орындары"))
        self.pushButton.setText(_translate("Second_Page_Window", "Әлеуметтік жұмыс орындары, Тұрақты жұмыс орындары"))
        self.pushButton_4.setText(_translate("Second_Page_Window", "Жаңа жұмыс орындары"))
        self.pushButton_6.setText(_translate("Second_Page_Window", "Бөлім басшысы "))
        self.pushButton_back.setText(_translate("Second_Page_Window", "Артқа"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Second_Page_Window = QtWidgets.QMainWindow()
#     ui = ReceptionSecondBtnService()
#     ui.setupUi(Second_Page_Window)
#     Second_Page_Window.show()
#     sys.exit(app.exec_())
