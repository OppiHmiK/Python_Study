from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
import sys

class Prac_App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn = QPushButton('Quit', self)
        btn.move(400,300)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        btn2 = QPushButton('Cancel', self)
        btn2.move(330, 300)
        btn2.resize(btn.sizeHint())
        btn2.pressed.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('GUI Practice')
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(300, 300, 500, 350)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    prac = Prac_App()
    sys.exit(app.exec_())
