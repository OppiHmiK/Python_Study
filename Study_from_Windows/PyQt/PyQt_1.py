# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import PyQt5
import sys

class Main_Page(QDialog):

    def __init__(self):
        QDialog.__init__(self,None)

app = QApplication(sys.argv) # NOTE : 프로그램을 실행시키는 역할
main = Main_Page()
main.show()
app.exec_() # NOTE : 프로그램을 이벤트루프로 진입시키는 메소드
            # NOTE : 이벤트 루프 = 프로그램을 무한루프 안에서 계속 실행시키고,
            #        프로그램에서 벌어지는 이벤트를 받아 처리


