# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from calculate import Ui_MainWindow
from PyQt5 import QtWidgets


class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)

    def CalculateClcik(self):
        try:
            self.C.setText(str(int(self.B.text()) + int(self.A.text())))
        except:
            print('请输入正确的整数')
            self.C.setText("")


if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = Mywindow()
  window.show()
  sys.exit(app.exec_())
