# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports
import sys
from SerialPortTools import Ui_MainWindow
from PyQt5 import QtWidgets
import _thread

Com_Open_Flag = False  # 串口打开标志
COM_Band = {"9600", "115200"}
custom_serial = serial.Serial


# 获取串口列表
def Get_Com_List():
    return list(serial.tools.list_ports.comports())


# 获取串口数据
def Com_Data_Rsv(threadName):
    while True:
        while Com_Open_Flag:
            data = custom_serial.read_all()
            if data == b'':
                continue
            else:
                print("receive : ", data)
                window.Set_Display_Data(data)


# 界面UI按键程序重写
class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        COM_List = Get_Com_List()  # 获取串口列表
        for i in range(0, len(COM_List)):  # 将列表导入到下拉框
            self.Com_Port.addItem(COM_List[i].name)
        self.Com_Band.addItem("9600")
        self.Com_Band.addItem("115200")

    def Open_Com_Click(self):
        global custom_serial  # 全局变量，需要加global
        global Com_Open_Flag
        print("点击了打开串口按钮")
        if self.Open_Com.text() == "打开串口":
            print(self.Com_Port.currentText())
            custom_serial = serial.Serial(self.Com_Port.currentText(), int(self.Com_Band.currentText()), timeout=0.5)
            if custom_serial.isOpen():
                print("open success")
                Com_Open_Flag = True
                self.Open_Com.setText("关闭串口")
                self.Com_Band.setEnabled(False)  # 串口号和波特率变为不可选择
                self.Com_Port.setEnabled(False)
            else:
                print("open failed")
        else:
            Com_Open_Flag = False
            self.Open_Com.setText("打开串口")
            custom_serial.close()
            self.Com_Band.setEnabled(True)  # 串口号和波特率变为可选择
            self.Com_Port.setEnabled(True)

    def Set_Display_Data(self, Data):
        self.Date_Display.insertPlainText(str(Data, encoding="utf-8"))

    def Send_Data_Click(self):
        print("点击了发送数据按钮")
        Data_Need_Send = self.Send_Data_Dsiplay.toPlainText()
        if custom_serial.isOpen():
            custom_serial.write(Data_Need_Send.encode("gbk"))
        else:
            print("请先打开串口")



if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = Mywindow()
  window.show()
  _thread.start_new_thread(Com_Data_Rsv, ("Thread-1",))
  sys.exit(app.exec_())

