from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont, QIcon
import sys

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QPushButton</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(200, 150)
        btn.resize(btn.sizeHint())


        self.setWindowIcon(QIcon('web.png'))
        self.setWindowTitle('4th_GUI_for_python')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())