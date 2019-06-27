from PyQt5.QtWidgets import  QPushButton, QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
import sys

class my_app(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn = QPushButton('Quit', self)
        btn.move(200, 150)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.statusBar().showMessage('Ready')
        self.setGeometry(300,300,300,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = my_app()
    sys.exit(app.exec_())



