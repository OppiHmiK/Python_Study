from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
import sys

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        btn = QPushButton('Quit', self) # NOTE : 버튼에 Quit이라고 적힌 버튼을 하나 생성함.
        btn.move(200, 150)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit) # NOTE : 버튼이 클릭되었을 때 수행될 작업명시.

        self.setWindowTitle('3rd_GUI_for_Python')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
