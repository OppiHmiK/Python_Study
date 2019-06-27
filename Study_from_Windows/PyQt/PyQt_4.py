# -*- coding : utf-8 -*-

from PyQt5.QtWidgets import  *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import PyQt5
import sys

cal_ui = 'ui_files/calculator.ui'
class Main(QDialog):

    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(cal_ui, self)

        self.btn_1.clicked.connect(lambda state, button=self.btn_1: self.NumClicked(state, button))

    def NumClicked(self, state, btn):
        print(state)
        exist_text = self.q_text.text()
        num_btn = self.btn.text()
        self.q_text.setText(exist_text + num_btn)



app = QApplication(sys.argv)
main = Main()
main.show()
app.exec_()