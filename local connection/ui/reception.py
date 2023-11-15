import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from reception_main_page import ReceptionMainPage
from reception_first import ReceptionFirstBtnService
from reception_second import ReceptionSecondBtnService
from reception_third import ReceptionThirdBtnService



app = QtWidgets.QApplication(sys.argv)


MainWindow = QtWidgets.QMainWindow()
ui = ReceptionMainPage()
ui.setupUi(MainWindow)
MainWindow.show()




def OpenFirstPage():
	global First_Page_Window
	First_Page_Window = QtWidgets.QMainWindow()
	ui = ReceptionFirstBtnService()
	ui.setupUi(First_Page_Window)

	MainWindow.close()
	First_Page_Window.show()

	def ReturnToMainPage1():
		First_Page_Window.close()
		MainWindow.show()

	ui.pushButton_back.clicked.connect(ReturnToMainPage1)

def OpenSecondPage():
	global Second_Page_Window
	Second_Page_Window = QtWidgets.QMainWindow()
	ui = ReceptionSecondBtnService()
	ui.setupUi(Second_Page_Window)
	
	MainWindow.close()
	Second_Page_Window.show()

	def ReturnToMainPage2():
		Second_Page_Window.close()
		MainWindow.show()

	ui.pushButton_back.clicked.connect(ReturnToMainPage2)

def OpenThirdPage():
	global Third_Page_Window
	Third_Page_Window = QtWidgets.QMainWindow()
	ui = ReceptionThirdBtnService()
	ui.setupUi(Third_Page_Window)
	
	MainWindow.close()
	Third_Page_Window.show()

	def ReturnToMainPage3():
		Third_Page_Window.close()
		MainWindow.show()

	ui.pushButton_back.clicked.connect(ReturnToMainPage3)



ui.pushButton.clicked.connect(OpenFirstPage)
ui.pushButton_2.clicked.connect(OpenSecondPage)
ui.pushButton_3.clicked.connect(OpenThirdPage)

sys.exit(app.exec_())
