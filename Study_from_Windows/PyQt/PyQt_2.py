# -*- coding : utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import PyQt5
import sys

cal_ui = 'ui_files/calculator.ui'
class Main_page(QDialog):

    def __init__(self):

        QDialog.__init__(self, None)
        uic.loadUi(cal_ui, self)

        self.btn_1.clicked.connect(self.NumClicked) # NOTE : 버튼을 클릭했을 때 해당함수 실행


    def NumClicked(self):
        print('나 클릭됐다 ~')
app = QApplication(sys.argv)
main = Main_page()
main.show()
app.exec_()