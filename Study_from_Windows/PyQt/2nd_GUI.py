import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png')) # NOTE : web이라는 이미지를 창의 아이콘으로 사용.
        self.setGeometry(300, 300, 300, 200) # NOTE : 창의 위치와 너비, 높이를 결정
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
