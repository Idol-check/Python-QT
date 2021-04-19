# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import HelloWord
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
  app = QApplication(sys.argv)
  myMainWindow = QMainWindow()
  myUi = HelloWord.Ui_MainWindow()
  myUi.setupUi(myMainWindow)
  myMainWindow.show()
  sys.exit(app.exec_())
