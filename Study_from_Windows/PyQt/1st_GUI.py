import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget): # NOTE : MyApp이라는 클래스가 QWidget으로 부터 상속받음.

    def __init__(self):
         super().__init__() # NOTE : QWidget 클래스의 생성자를 실행하도록 하는 코드.
         self.initUI()

    def initUI(self):

        self.setWindowTitle('First GUI')
        self.move(300, 300) # NOTE : 위젯을 x, y = 300px의 위치로 이동
        self.resize(400, 200) # NOTE : 너비 400px, 높이 200px로 조절
        self.show() # NOTE : 위젯을 보여줌.


if __name__ == '__main__':

    app = QApplication(sys.argv)
    wx = MyApp()
    sys.exit(app.exec_())

