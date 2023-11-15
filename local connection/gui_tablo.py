import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

class Window(QMainWindow):
	def __init__(self):
		super(Window, self).__init__()

		self.setWindowTitle('Tablo')
		self.setGeometry(300, 50, 350, 200)

		self.new_text = (QtWidgets.QLabel(self))



		self.main_text = QtWidgets.QLabel (self)
		self.main_text.setText("Text")
		self.main_text.move(100, 500)
		self.main_text.adjustSize()


		self.btn = QtWidgets.QPushButton(self)
		self.btn.move(70, 150)
		self.btn.setText("Button")
		self.btn.adjustSize()
		self.btn.clicked.connect(self.add_label)

	def add_label(self):
		self.new_text.setText("New text")
		self.new_text.move(100, 50)
		self.new_text.adjustSize()



def application():
	app = QApplication(sys.argv)
	window = Window()
	



	window.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	application()
