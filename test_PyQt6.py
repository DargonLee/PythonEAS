# -*- coding: utf-8 -*-

"""
@author: harlan
@software: PyCharm
@file: test_PyQt6.py
@time: 2023/2/16 14:27
"""
import sys
from PyQt6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.setWindowTitle('教务管理系统')
window.resize(550, 500)

button = QtWidgets.QPushButton(window)
button.setText('登录')
button.move(250, 250)
window.show()



sys.exit(app.exec())