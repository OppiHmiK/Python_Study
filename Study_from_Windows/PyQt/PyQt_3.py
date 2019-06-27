# -*- coding : utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import PyQt5
import sys


cal = 'ui_files/calculator.ui'

class Main(QDialog):

    def __init__(self):

        QDialog.__init__(self, None)
        uic.loadUi(cal, self)
        self.btn_1.clicked.connect(self.NumClicked)
        self.btn_2.clicked.connect(self.NumClicked)

    def NumClicked(self):

        exist_text = self.q_text.text()
        now_num_text = self.btn_1.text()
        self.q_text.setText(exist_text + now_num_text) # NOTE : q_text안에 있는 문자열을 초기화 시키고 ()안에 있는 문자열을 입력시킴.

app = QApplication(sys.argv)
main = Main()
main.show()
app.exec_()